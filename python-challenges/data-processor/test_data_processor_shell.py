import json
import unittest
from datetime import datetime
from data_processor_shell import DataValidator, DataTransformer, DataProcessor


class TestDataValidator(unittest.TestCase):
    def setUp(self):
        self.validator = DataValidator()

    def test_validate_email_valid(self):
        """Test valid email addresses"""
        self.assertTrue(self.validator.validate_email("test@example.com"))
        self.assertTrue(self.validator.validate_email("user.name+tag@domain.co.uk"))
        
    def test_validate_email_invalid(self):
        """Test invalid email addresses"""
        self.assertFalse(self.validator.validate_email("test@com"))
        self.assertFalse(self.validator.validate_email("test@example"))
        self.assertFalse(self.validator.validate_email("test@.com"))
        self.assertFalse(self.validator.validate_email("test@domain..com"))
        self.assertFalse(self.validator.validate_email("test@domain#com"))
        self.assertFalse(self.validator.validate_email("test@domain,com"))
        self.assertFalse(self.validator.validate_email("test@domain.com."))
        self.assertFalse(self.validator.validate_email("test..example@domain.com"))
        self.assertFalse(self.validator.validate_email("test@domain@domain.com"))
        self.assertFalse(self.validator.validate_email(""))

    def test_validate_age_valid(self):
        """Test valid age"""
        self.assertTrue(self.validator.validate_age(25))
        self.assertTrue(self.validator.validate_age(1))

    def test_validate_age_invalid(self):
        """Test invalid age"""
        self.assertFalse(self.validator.validate_age(0))
        self.assertFalse(self.validator.validate_age(-1))
        self.assertFalse(self.validator.validate_age("twenty"))
        self.assertFalse(self.validator.validate_age(None))

    def test_validate_date_valid(self):
        """Test valid date formats"""
        self.assertTrue(self.validator.validate_date("2025-02-09"))
        self.assertTrue(self.validator.validate_date("1999-12-31"))
        
    def test_validate_date_invalid(self):
        """Test invalid date formats"""
        self.assertFalse(self.validator.validate_date("2025-02-30"))
        self.assertFalse(self.validator.validate_date("2025-02-9"))
        self.assertFalse(self.validator.validate_date("2025/02/09"))
        self.assertFalse(self.validator.validate_date("February 9, 2025"))
        self.assertFalse(self.validator.validate_date(""))

        
class TestDataTransformer(unittest.TestCase):
    def setUp(self):
        self.transformer = DataTransformer()

    def test_transform_record_valid(self):
        """Test valid record transformation"""
        record = {
            "name": "john doe",
            "email": "John.Doe@Example.com",
            "age": "25",
            "date": "2025-02-09"
        }
        transformed = self.transformer.transform_record(record)
        self.assertEqual(transformed["name"], "John Doe")
        self.assertEqual(transformed["email"], "john.doe@example.com")
        self.assertEqual(transformed["age"], 25)
        self.assertEqual(transformed["date"], "2025-02-09")

    def test_transform_record_invalid(self):
        """Test handling of invalid records"""
        record = {
            "name": "john doe",
            "email": "invalid-email",
            "age": "invalid-age",
            "date": "2025-02-30"  #invalid date
        }
        transformed = self.transformer.transform_record(record)
        self.assertEqual(transformed["name"], "John Doe")
        self.assertIsNone(transformed["email"])
        self.assertIsNone(transformed["age"])
        self.assertIsNone(transformed["date"])


class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        """Set up test data and processor"""
        self.processor = DataProcessor("test_data.csv")
        self.processor.records = [
            {"name": "john doe", "email": "john.doe@example.com", "age": "25", "date": "2025-02-09"},
            {"name": "alice smith", "email": "alice.smith@example.com", "age": "30", "date": "2025-02-10"},
            {"name": "bob", "email": "bob@bob.com", "age": "40", "date": "2025-02-11"}
        ]

    def test_process_file(self):
        """Test file processing functionality"""
        self.processor.process_file()
        self.assertGreater(len(self.processor.records), 0)  #ensure records are processed
        
    def test_json_output(self):
        """Test JSON output functionality"""
        self.processor.to_json("output_test.json")
        #check if the file exists and is not empty
        with open("output_test.json", "r") as file:
            data = json.load(file)
            self.assertGreater(len(data), 0)

    def test_sql_output(self):
        """Test SQL output functionality"""
        self.processor.to_sql("output_test.sql")
        #check if the file exists and contains valid SQL statements
        with open("output_test.sql", "r") as file:
            content = file.read()
            self.assertIn("INSERT INTO table_name", content)
            self.assertGreater(len(content), 0)

    def test_process_invalid_file(self):
        """Test invalid file handling"""
        invalid_processor = DataProcessor("invalid_file.csv")
        invalid_processor.process_file()
        self.assertEqual(len(invalid_processor.records), 0)


if __name__ == "__main__":
    unittest.main()
