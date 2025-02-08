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

        for c in local_string:
            if c not in valid_local_chars:
                return False

        # Check domain part characters
        for c in domain_string:
            if c not in valid_domain_chars:
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
        # TODO: Implement record transformation
        pass


class DataProcessor:
    """Main class for processing data files."""

    def __init__(self, input_file: str):
        """Initialize processor with input file path."""
        # TODO: Initialize processor
        pass

    def process_file(self) -> None:
        """Process the input file and validate/transform all records."""
        # TODO: Implement file processing
        pass

    def _process_record(self, record: Dict) -> Optional[Dict]:
        """Process a single record with validation and transformation."""
        # TODO: Implement record processing
        pass

    def to_json(self, output_file: str) -> None:
        """Output processed data to JSON file."""
        # TODO: Implement JSON output
        pass

    def to_sql(self, output_file: str) -> None:
        """Output processed data as SQL insert statements."""
        # TODO: Implement SQL output
        pass


if __name__ == "__main__":
    # TODO: Add example usage
    pass
