# Generated by Django 4.2.1 on 2023-05-06 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dh_code', '0017_advantages_time_create_advantages_time_update_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvantagesEN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Установить текст:')),
                ('marketing_column', models.CharField(max_length=256, null=True, verbose_name='Установить заголовок маркетингового столбца:')),
                ('marketing_column_percent', models.IntegerField(null=True, verbose_name='Установить процент столбца маркетинга:')),
                ('experience_column', models.CharField(max_length=256, null=True, verbose_name='Установить заголовок столбца опыта:')),
                ('experience_column_percent', models.IntegerField(null=True, verbose_name='Установить процент столбца опыта:')),
                ('develope_column', models.CharField(max_length=256, null=True, verbose_name='Установить заголовок маркетингового столбца:')),
                ('develope_column_percent', models.IntegerField(null=True, verbose_name='Установить процент столбца разработки:')),
                ('charachters_title', models.CharField(max_length=256, null=True, verbose_name='Установить заголовок персонажа:')),
                ('characters_column_first', models.CharField(max_length=265, null=True, verbose_name='Установить первый заголовок столбца:')),
                ('characters_column_second', models.CharField(max_length=265, null=True, verbose_name='Установить второй заголовок столбца:')),
                ('characters_column_third', models.CharField(max_length=265, null=True, verbose_name='Установить третий заголовок столбца:')),
                ('characters_column_fourth', models.CharField(max_length=265, null=True, verbose_name='Установить четвертый заголовок столбца:')),
                ('characters_column_fiveth', models.CharField(max_length=265, null=True, verbose_name='Установить пятый заголовок столбца:')),
                ('characters_column_sixth', models.CharField(max_length=265, null=True, verbose_name='Установить шестой заголовок столбца:')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания:')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения:')),
            ],
            options={
                'verbose_name': 'Преимущества EN',
                'verbose_name_plural': 'Преимущества EN',
            },
        ),
        migrations.CreateModel(
            name='AdvantagesRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Установить текст:')),
                ('marketing_column', models.CharField(max_length=256, null=True, verbose_name='Установить заголовок маркетингового столбца:')),
                ('marketing_column_percent', models.IntegerField(null=True, verbose_name='Установить процент столбца маркетинга:')),
                ('experience_column', models.CharField(max_length=256, null=True, verbose_name='Установить заголовок столбца опыта:')),
                ('experience_column_percent', models.IntegerField(null=True, verbose_name='Установить процент столбца опыта:')),
                ('develope_column', models.CharField(max_length=256, null=True, verbose_name='Установить заголовок маркетингового столбца:')),
                ('develope_column_percent', models.IntegerField(null=True, verbose_name='Установить процент столбца разработки:')),
                ('charachters_title', models.CharField(max_length=256, null=True, verbose_name='Установить заголовок персонажа:')),
                ('characters_column_first', models.CharField(max_length=265, null=True, verbose_name='Установить первый заголовок столбца:')),
                ('characters_column_second', models.CharField(max_length=265, null=True, verbose_name='Установить второй заголовок столбца:')),
                ('characters_column_third', models.CharField(max_length=265, null=True, verbose_name='Установить третий заголовок столбца:')),
                ('characters_column_fourth', models.CharField(max_length=265, null=True, verbose_name='Установить четвертый заголовок столбца:')),
                ('characters_column_fiveth', models.CharField(max_length=265, null=True, verbose_name='Установить пятый заголовок столбца:')),
                ('characters_column_sixth', models.CharField(max_length=265, null=True, verbose_name='Установить шестой заголовок столбца:')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания:')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения:')),
            ],
            options={
                'verbose_name': 'Преимущества RU',
                'verbose_name_plural': 'Преимущества RU',
            },
        ),
        migrations.CreateModel(
            name='BasicEN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(null=True, upload_to='media/%Y/%m/%d', verbose_name='Загрузить логотип:')),
                ('title', models.CharField(max_length=256, verbose_name='Установить заголовок:')),
                ('description', models.TextField(verbose_name='Описание:')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания:')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения:')),
            ],
            options={
                'verbose_name': 'Управление страницей EN',
                'verbose_name_plural': 'Управление страницей EN',
            },
        ),
        migrations.CreateModel(
            name='BasicRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(null=True, upload_to='media/%Y/%m/%d', verbose_name='Загрузить логотип:')),
                ('title', models.CharField(max_length=256, verbose_name='Установить заголовок:')),
                ('description', models.TextField(verbose_name='Описание:')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания:')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения:')),
            ],
            options={
                'verbose_name': 'Управление страницей RU',
                'verbose_name_plural': 'Управление страницей RU',
            },
        ),
        migrations.CreateModel(
            name='EtapsEN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=256, verbose_name='Установить заголовок страницы:')),
                ('title', models.CharField(max_length=256, verbose_name='Установить заголовок:')),
                ('description', models.TextField(verbose_name='Установить текст:')),
                ('actions_title', models.CharField(max_length=256, verbose_name='Установить название действия:')),
                ('action_first_title', models.CharField(max_length=256, verbose_name='Установить действие первым заголовком:')),
                ('action_second_title', models.CharField(max_length=256, verbose_name='Установить второй заголовок действия:')),
                ('action_third_title', models.CharField(max_length=256, verbose_name='Установить третье название действия:')),
                ('action_fourth_title', models.CharField(max_length=256, verbose_name='Установить четвертое название действия:')),
                ('action_fiveth_title', models.CharField(max_length=256, verbose_name='Установить пятое название действия:')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания:')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения:')),
            ],
            options={
                'verbose_name': 'Этапы EN',
                'verbose_name_plural': 'Этапы EN',
            },
        ),
        migrations.CreateModel(
            name='EtapsRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=256, verbose_name='Установить заголовок страницы:')),
                ('title', models.CharField(max_length=256, verbose_name='Установить заголовок:')),
                ('description', models.TextField(verbose_name='Установить текст:')),
                ('actions_title', models.CharField(max_length=256, verbose_name='Установить название действия:')),
                ('action_first_title', models.CharField(max_length=256, verbose_name='Установить действие первым заголовком:')),
                ('action_second_title', models.CharField(max_length=256, verbose_name='Установить второй заголовок действия:')),
                ('action_third_title', models.CharField(max_length=256, verbose_name='Установить третье название действия:')),
                ('action_fourth_title', models.CharField(max_length=256, verbose_name='Установить четвертое название действия:')),
                ('action_fiveth_title', models.CharField(max_length=256, verbose_name='Установить пятое название действия:')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания:')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения:')),
            ],
            options={
                'verbose_name': 'Этапы',
                'verbose_name_plural': 'Этапы RU',
            },
        ),
        migrations.CreateModel(
            name='ReviewsEN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userIcon', models.ImageField(null=True, upload_to='media/%Y/%m/%d', verbose_name='Загрузить значок:')),
                ('userName', models.CharField(max_length=256, verbose_name='Заголовок отзыва:')),
                ('href', models.URLField(null=True, verbose_name='Установить ссылку')),
                ('body', models.TextField(verbose_name='Текст отзыва')),
                ('img_f', models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Сначала просмотрите изображение')),
                ('img_s', models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Второе изображение обзора')),
                ('img_t', models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Изображение обзора третье')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания:')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения:')),
            ],
            options={
                'verbose_name': 'Отзывы EN',
                'verbose_name_plural': 'Отзывы EN',
            },
        ),
        migrations.CreateModel(
            name='ReviewsRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userIcon', models.ImageField(null=True, upload_to='media/%Y/%m/%d', verbose_name='Загрузить значок:')),
                ('userName', models.CharField(max_length=256, verbose_name='Заголовок отзыва:')),
                ('href', models.URLField(null=True, verbose_name='Установить ссылку')),
                ('body', models.TextField(verbose_name='Текст отзыва')),
                ('img_f', models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Сначала просмотрите изображение')),
                ('img_s', models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Второе изображение обзора')),
                ('img_t', models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Изображение обзора третье')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания:')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения:')),
            ],
            options={
                'verbose_name': 'Отзывы RU',
                'verbose_name_plural': 'Отзывы RU',
            },
        ),
        migrations.CreateModel(
            name='ServicesEN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Установить заголовок:')),
                ('description', models.TextField(verbose_name='Установить текст:')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания:')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения:')),
            ],
            options={
                'verbose_name': 'Портфолио EN',
                'verbose_name_plural': 'Портфолио EN',
            },
        ),
        migrations.CreateModel(
            name='ServicesRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Установить заголовок:')),
                ('description', models.TextField(verbose_name='Установить текст:')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания:')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения:')),
            ],
            options={
                'verbose_name': 'Портфолио RU',
                'verbose_name_plural': 'Портфолио RU',
            },
        ),
        migrations.DeleteModel(
            name='Advantages',
        ),
        migrations.DeleteModel(
            name='Basic',
        ),
        migrations.DeleteModel(
            name='Etaps',
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакты', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщения', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={},
        ),
        migrations.AlterField(
            model_name='contact',
            name='fl_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Установить имя FL'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='gmail',
            field=models.EmailField(max_length=254, verbose_name='Установить адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=50, verbose_name='Установить номер телефона'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='telegram',
            field=models.CharField(max_length=50, verbose_name='Установить номер телеграммы'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания:'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='time_update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения:'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='whatsapp',
            field=models.CharField(max_length=50, verbose_name='Установить номер WhatsApp'),
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.CharField(max_length=256, verbose_name='Электронная почта отправителя:'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=256, verbose_name='Сообщение отправителя:'),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Имя отправителя:'),
        ),
        migrations.AlterField(
            model_name='message',
            name='phone',
            field=models.CharField(max_length=256, verbose_name='Телефон отправителя:'),
        ),
        migrations.AlterField(
            model_name='message',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания:'),
        ),
        migrations.AlterField(
            model_name='message',
            name='time_update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения:'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='img',
            field=models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Загрузить изображение портфолио'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания:'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='time_update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения:'),
        ),
    ]
