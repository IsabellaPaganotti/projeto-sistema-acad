from faker import Faker
fake = Faker()
matricula = fake.bothify(text='??###')
print(matricula)