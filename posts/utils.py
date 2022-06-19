'''
 w terminalu uruchamiamy:
 $pyton manage.py shell_plus
In[1] from posts.utils import created_post
In[2] created_posts(20)
In[3] from postsmodels import Post
In[4] Post.models.all()
powienien wyświetlić nowe wygenerowane posty
'''

from .models import Post
from faker import Faker
from random import randint
# from datetime import datetime

def created_posts(n=10):
    fake = Faker('pl_PL')
    for _ in range(n):
        created = fake.date_time()
        post = Post(
            title=fake.text(randint(10,30)),
            content=fake.text(randint(100,300)),
            created=created,
            modified=created + fake.time_delta(10),
            published=fake.boolean(),
            sponsored=fake.boolean(),
            author_id=1
        )

        post.save()
