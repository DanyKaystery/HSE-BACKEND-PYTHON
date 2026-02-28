from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_mock_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Post = apps.get_model('core', 'Post')
    Comment = apps.get_model('core', 'Comment')

    if not User.objects.filter(username='admin').exists():
        user = User.objects.create(
            username='admin',
            email='admin@example.com',
            password=make_password('admin123'),
            is_staff=True,
            is_superuser=True
        )
    else:
        user = User.objects.get(username='admin')

    post1 = Post.objects.create(title='Первый пост', content='Контент первого поста', author=user)
    post2 = Post.objects.create(title='Второй пост', content='DRF это круто', author=user)

    Comment.objects.create(content='Классный пост!', author=user, post=post1)
    Comment.objects.create(content='Согласен с автором.', author=user, post=post1)
    Comment.objects.create(content='Жду продолжения!', author=user, post=post2)

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_mock_data),
    ]