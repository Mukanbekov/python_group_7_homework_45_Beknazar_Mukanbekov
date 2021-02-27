from django.db import models

status_choices = (
    ('new', 'Новый'),
    ('progress', 'В процессе'),
    ('done', 'Сделано')
)


class List(models.Model):
    list = models.CharField(max_length=200, null=False, blank=False, verbose_name='Текст')
    status = models.TextField(max_length=30, null=False, blank=False, choices=status_choices, default='new', verbose_name='Статус')
    created_at = models.DateField(verbose_name='Время создания', blank=True, null=True)

    class Meta:
        db_table = 'lists'
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'

    def __str__(self):
        return "{}. {}".format(self.id, self.list, self.status)




