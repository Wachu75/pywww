import factory
from faker import Factory

faker = Factory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "auth.User"
        django_get_or_create = ('email', )
    email = factory.Sequence(lambda n: f'user-{n}@example.com')
    username = factory.Sequence(lambda n: f'user{n}')
    pasword = "default"


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "post.Post"

    title = factory.Sequence(lambda n: f'post {n}')
    content = factory.Sequence(lambda n: faker.text(200))
    published = factory.Sequence(lambda n: faker.boolean())
    sponsored = factory.Sequence(lambda n: faker.boolean())
    author = factory.SubFactory(UserFactory)
    image = factory.django.FileField(filename="image.jpg")
