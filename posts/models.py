from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name="Название сообщества")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Адрес")
    description = models.TextField(null=True, blank=True,
                                   verbose_name="Описание")

    class Meta:
        ordering = ['title']
        verbose_name = 'Группу'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    group = models.ForeignKey(Group, null=True, blank=True,
                              verbose_name="Сообщество",
                              related_name="posts",
                              on_delete=models.SET_NULL)
    text = models.TextField(verbose_name="Текст поста")
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name="Дата публикации")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    image = models.ImageField(upload_to='posts/', blank=True, null=True,
                              verbose_name="Изображение")

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='Пост')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='Автор')
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата комментария')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
