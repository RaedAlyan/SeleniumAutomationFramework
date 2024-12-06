from faker import Faker


class RandomDataGenerator:

    def __init__(self, locale: str = 'en_US'):
        self.faker = Faker(locale)

    def generate_random_first_name(self) -> str:
        """Generates a random first name."""
        return self.faker.first_name()

    def generate_random_last_name(self) -> str:
        """Generates a random last name."""
        return self.faker.last_name()

    def generate_random_full_name(self) -> str:
        """Generates a random full name."""
        return self.faker.name()

    def generate_random_email(self) -> str:
        """Generates a random email address."""
        return self.faker.email()

    def generate_random_phone_number(self) -> str:
        """Generates a random phone number."""
        return self.faker.phone_number()

    def generate_random_password(self, length: int = 12, special_chars: bool = True, upper_case: bool = True,
                                 digits: bool = True) -> str:
        """
        Generates a random password with customizable complexity.

        :param length: Length of the password (default is 12).
        :param special_chars: Whether to include special characters (default is True).
        :param upper_case: Whether to include uppercase letters (default is True).
        :param digits: Whether to include digits (default is True).
        :return: A randomly generated password.
        """
        return self.faker.password(length=length, special_chars=special_chars, upper_case=upper_case, digits=digits)
