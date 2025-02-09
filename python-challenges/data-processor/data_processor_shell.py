from datetime import datetime
import csv
import json
from typing import Dict, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataValidator:
    """Validates input data according to specified rules."""

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format."""
        #checking for the existance of exactly ONE "@" symbol
        if email.count('@') != 1:
            return False
        
        #splitting the email into the local (pre @) and domain (post @) parts
        local_string, domain_string = email.split('@')

        #making sure that the local_string and the domain_string are not empty
        if not local_string or not domain_string:
            return False
        
        #making sure that the local_string is within the 64 character length limit
        if len(local_string) > 64:
            return False
        
        #making sure that the domain_string is within the 253 character length limit
        if len(domain_string) > 253:
            return False
        
        #makeing sure that the local_string does not start or end with a period
        if local_string[0] == '.' or local_string[-1] == '.':
            return False
        
        #making sure that the local_string doesn't contain '..'
        if '..' in local_string:
            return False
        
        #making sure the domain_string does not start or end with a hyphen
        if domain_string[0] == '.' or domain_string[-1] == '-':
            return False
        
        #making sure the domain_string contains a period seperating the domain and TLD
        if '.' not in domain_string:
            return False
        
        #splitting the domain_string into the domain and the TLD
        domain_parts = domain_string.split('.')

        #making sure the TLD is at least 2 characters long
        if len(domain_parts[-1]) < 2:
            return False
        
        #making sure the domain does not contain double periods
        if '..' in domain_string:
            return False
        
        #checking if the local_string and domain_string contain only valid characters
        valid_local_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._%+-"
        valid_domain_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.-"

        for character in local_string:
            if character not in valid_local_chars:
                return False

        # Check domain part characters
        for character in domain_string:
            if character not in valid_domain_chars:
                return False
        
        #if the email passes all of these tests then it is a valid email
        return True


    @staticmethod
    def validate_age(age: int) -> bool:
        """Validate age is positive integer."""
        if isinstance(age, int) and age > 0:
            return True
        return False

    @staticmethod
    def validate_date(date_str: str) -> bool:
        """Validate date string format."""
        # Ensure the string matches the exact format of YYYY-MM-DD
        if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
            return False
        #use datetime to check the date
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

class DataTransformer:
    """Transforms input data into standardized format."""

    @staticmethod
    def transform_record(record: Dict) -> Optional[Dict]:
        """
        Transform a single record according to business rules.

        Rules:
        - Capitalize names
        - Lowercase emails
        - Convert age to integer
        - Standardize dates to YYYY-MM-DD
        """
        #capitalize names if they are in the record dict
        if "name" in record:
            record["name"] = record["name"].title()

        #make sure the emails are all lowercase if they are in the record dict
        if "email" in record:
            if DataValidator.validate_email(record["email"]):  # Validate email format
                record["email"] = record["email"].lower()
            else:
                record["email"] = None

        #converting the age to an integer if possible
        if "age" in record:
            if DataValidator.validate_age(record["age"]):  # Validate age format
                record["age"] = int(record["age"])
            else:
                record["age"] = None

        # Standardize dates to YYYY-MM-DD format if date exists and is valid
        if "date" in record:
            if DataValidator.validate_date(record["date"]):  #validate date format first
                date_obj = datetime.strptime(record["date"], "%Y-%m-%d")  #parse date
                record["date"] = date_obj.strftime("%Y-%m-%d")  #reformat to YYYY-MM-DD
            else:
                record["date"] = None
        return record

class DataProcessor:
    """Main class for processing data files."""

    def __init__(self, input_file: str):
        """Initialize processor with input file path."""
        self.input_file = input_file
        self.records = []

    def process_file(self) -> None:
        """Process the input file and validate/transform all records."""
        try:
            with open(self.input_file, newline='', encoding='utf-8') as csvfile:
                csvreader = csv.DictReader(csvfile)
                for row in csvreader:
                    transformed_record = self._process_record(row)
                    if transformed_record:
                        self.records.append(transformed_record)
            if not self.records:
                logger.warning("No records were processed.")
        except FileNotFoundError:
            logger.error(f"File not found: {self.input_file}")
        except Exception as e:
            logger.error(f"An error occurred while processing the file: {e}")

    def _process_record(self, record: Dict) -> Optional[Dict]:
        """Process a single record with validation and transformation."""
        #apply validation and transformation, even if some fields are invalid
        if "email" in record and not DataValidator.validate_email(record.get("email", "")):
            record["email"] = None
        if "age" in record and not DataValidator.validate_age(record.get("age", 0)):
            record["age"] = None
        if "date" in record and not DataValidator.validate_date(record.get("date", "")):
            record["date"] = None

        #transform the record and return it
        return DataTransformer.transform_record(record)

    def to_json(self, output_file: str) -> None:
        """Output processed data to JSON file."""
        if not self.records:
            logger.warning("No records to write to JSON.")
        else:
            try:
                with open(output_file, 'w', encoding='utf-8') as jsonfile:
                    json.dump(self.records, jsonfile, indent=4)
                logger.info(f"Data successfully written to {output_file}")
            except Exception as e:
                logger.error(f"An error occurred while writing to the file: {e}")

    def to_sql(self, output_file: str) -> None:
        """Output processed data as SQL insert statements."""
        if not self.records:
            logger.warning("No records to write to SQL.")
        else:
            try:
                with open(output_file, 'w', encoding='utf-8') as sqlfile:
                    for record in self.records:
                        sql = f"INSERT INTO table_name ({', '.join(record.keys())}) VALUES ({', '.join([str(v) for v in record.values()])});\n"
                        sqlfile.write(sql)
                logger.info(f"SQL data successfully written to {output_file}")
            except Exception as e:
                logger.error(f"An error occurred while writing to the SQL file: {e}")


if __name__ == "__main__":
    #example usage

    #path to the sample CSV file
    input_file = "data.csv"
    
    #path to output JSON and SQL files
    output_json_file = "output.json"
    output_sql_file = "output.sql"

    #initialize the processor with the input file
    processor = DataProcessor(input_file)

    #process the file
    processor.process_file()

    #output processed data to JSON
    processor.to_json(output_json_file)

    #output processed data to SQL
    processor.to_sql(output_sql_file)

    #completion message
    logger.info("Processing complete. Data has been written to:")
    logger.info(f"JSON file: {output_json_file}")
    logger.info(f"SQL file: {output_sql_file}")