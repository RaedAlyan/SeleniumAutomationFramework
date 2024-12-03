from faker import Faker


class RandomDataGenerator:

    def __init__(self):
        self.faker = Faker()

    def get_random_name(self):
        return self.faker.name()

    def get_random_email(self):
        return self.faker.email()

    def get_random_phone_number(self):
        return self.faker.phone_number()

