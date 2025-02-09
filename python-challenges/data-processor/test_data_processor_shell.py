import unittest
from data_processor_shell import DataValidator, DataTransformer, DataProcessor


class TestDataValidator(unittest.TestCase):
    def setUp(self):
        self.validator = DataValidator()


    def test_validate_email(self):
        """Test email validation logic"""
        #testing a valid email address
        self.assertTrue(DataValidator.validate_email("samuellewis92@icloud.com"))

        #testing an invalid email (missing '@')
        self.assertFalse(DataValidator.validate_email("samuellewis92icloud.com"))

        #testing an invalid email (extra '@')
        self.assertFalse(DataValidator.validate_email("samuellewis92@icloud@com"))

        #testing an invalid email (local part too long)
        long_local = "a" * 65  # local part has 65 characters
        self.assertFalse(DataValidator.validate_email(f"{long_local}@icloud.com"))

        #testing an invalid email (domain part too long)
        long_domain = "a" * 250 + ".com"  # domain part has more than 253 characters
        self.assertFalse(DataValidator.validate_email(f"samuellewis92@{long_domain}"))

        #testing an invalid email (local part starts with a period)
        self.assertFalse(DataValidator.validate_email(".samuellewis92@icloud.com"))

        #testing an invalid email (local part ends with a period)
        self.assertFalse(DataValidator.validate_email("samuellewis92.@icloud.com"))

        #testing an invalid email (double period in local part)
        self.assertFalse(DataValidator.validate_email("samuellewis92..lewis@icloud.com"))

        #testing an invalid email (domain part starts with a hyphen)
        self.assertFalse(DataValidator.validate_email("samuellewis92@-icloud.com"))

        #testing an invalid email (no period in domain part)
        self.assertFalse(DataValidator.validate_email("samuellewis92@icloudcom"))

        #testing an invalid email (domain part ends with a hyphen)
        self.assertFalse(DataValidator.validate_email("samuellewis92@icloud-.com"))


    def test_validate_age(self):
        """Test age validation logic"""
        #testing for a valid positive integer for age
        self.assertTrue(DataValidator.validate_age(21))

        #testing for an age of 0
        self.assertFalse(DataValidator.validate_age(0))

        #testing for a negative age
        self.assertFalse(DataValidator.validate_age(-7))

        #testing for a float (should be invalid)
        self.assertFalse(DataValidator.validate_age(21.5))

        #testing for a string input (should be invalid)
        self.assertFalse(DataValidator.validate_age("21"))

        #testing for `None` as input
        self.assertFalse(DataValidator.validate_age(None))

        #testing for age as a negative float
        self.assertFalse(DataValidator.validate_age(-21.5))


    def test_validate_date(self):
        """Test date validation logic"""
        #testing for a valid date
        self.assertTrue(DataValidator.validate_date("2004-01-02"))

        #testing for incorrect seperator
        self.assertFalse(DataValidator.validate_date("2023/03/15"))

        #non-existent day
        self.assertFalse(DataValidator.validate_date("2023-02-30"))

        #invalid month
        self.assertFalse(DataValidator.validate_date("2023-13-01"))

        #testing for leap year
        self.assertTrue(DataValidator.validate_date("2020-02-29"))

        #testing for non-leap year
        self.assertFalse(DataValidator.validate_date("2019-02-29"))

        #testing for empty input string
        self.assertFalse(DataValidator.validate_date(""))

        #testing for None as input
        self.assertFalse(DataValidator.validate_date(None))

        #testing for a date with invalid characters
        self.assertFalse(DataValidator.validate_date("202a-03-15"))

        #testing for date with too many characters
        self.assertFalse(DataValidator.validate_date("2023-03-150"))


class TestDataTransformer(unittest.TestCase):
    def setUp(self):
        self.transformer = DataTransformer()

    def test_transform_record(self):
        """Test record transformation logic"""
        # TODO: Implement record transformation tests
        pass

    def test_transform_invalid_record(self):
        """Test handling of invalid records"""
        # TODO: Implement invalid record tests
        pass


class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        """Set up test data and processor"""
        # TODO: Implement test setup
        pass

    def test_process_file(self):
        """Test file processing functionality"""
        # TODO: Implement file processing tests
        pass

    def test_json_output(self):
        """Test JSON output functionality"""
        # TODO: Implement JSON output tests
        pass

    def test_sql_output(self):
        """Test SQL output functionality"""
        # TODO: Implement SQL output tests
        pass


if __name__ == "__main__":
    unittest.main()
