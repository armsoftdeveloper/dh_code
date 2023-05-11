from django.db import models

#Models RU

class BasicRU(models.Model):
    title = models.CharField(("Установить заголовок:"), max_length=256)
    description = models.TextField(("Описание:"))
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания:" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения:" , null = True)

    def __str__(self):
        return "Главная Страница"

    class Meta:
        ordering = ["id"]
        verbose_name = "Главная Страница RU"
        verbose_name_plural = "Главная Страница RU"

class EtapsRU(models.Model):
    title = models.CharField(("Установить заголовок:"), max_length=256)
    description = models.TextField(("Установить текст:"))
    actions_title = models.CharField(("Установить название Набор действий:"), max_length=256)
    action_first_title = models.CharField(("Установить первым заголовок действия:"), max_length=256)
    action_second_title = models.CharField(("Установить второй заголовок действия:"), max_length=256)
    action_third_title = models.CharField(("Установить третье название действия:"), max_length=256)
    action_fourth_title = models.CharField(("Установить четвертое название действия:"), max_length=256)
    action_fiveth_title = models.CharField(("Установить пятое название действия:"), max_length=256)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания:" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения:" , null = True)

    def __str__(self):
        return "Этапы RU"
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Этапы"
        verbose_name_plural = "Этапы RU"


class ServicesRU(models.Model):
    title = models.CharField(("Установить заголовок:"), max_length=256)
    description = models.TextField(("Установить текст:"))
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания:" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения:" , null = True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Услуги RU"
        verbose_name_plural = "Услуги RU"


class AdvantagesRU(models.Model):
    description = models.TextField(("Установить текст:"))
    marketing_column = models.CharField(("Установить заголовок маркетингового столбца:"), max_length=256 , null = True)
    marketing_column_percent = models.IntegerField(("Установить процент столбца маркетинга:") , null = True)
    experience_column = models.CharField(("Установить заголовок столбца опыта:"), max_length=256 , null = True)
    experience_column_percent = models.IntegerField(("Установить процент столбца опыта:") , null = True)
    develope_column = models.CharField(("Установить заголовок маркетингового столбца:"), max_length=256 , null = True)
    develope_column_percent = models.IntegerField(("Установить процент столбца разработки:") , null = True)
    charachters_title = models.CharField(("Установить заголовок персонажа:"), max_length=256 , null = True)
    characters_column_first = models.CharField(("Установить первый заголовок столбца:"), max_length=265 , null = True)
    characters_column_second = models.CharField(("Установить второй заголовок столбца:"), max_length=265 , null = True)
    characters_column_third = models.CharField(("Установить третий заголовок столбца:"), max_length=265 , null = True)
    characters_column_fourth = models.CharField(("Установить четвертый заголовок столбца:"), max_length=265 , null = True)
    characters_column_fiveth = models.CharField(("Установить пятый заголовок столбца:"), max_length=265 , null = True)
    characters_column_sixth = models.CharField(("Установить шестой заголовок столбца:"), max_length=265 , null = True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания:" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения:" , null = True)

    def __str__(self):
        return "Преимущества"
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Преимущества RU"
        verbose_name_plural = "Преимущества RU"


class ReviewsRU(models.Model):
    userIcon = models.ImageField(("Загрузить значок:"), upload_to="media/%Y/%m/%d" , null = True)
    userName = models.CharField(("Заголовок отзыва:"), max_length=256)
    href = models.URLField(("Установить ссылку"), max_length=200 , null = True)
    body = models.TextField(("Текст отзыва"))
    img_f = models.ImageField(("Сначала просмотрите изображение"), upload_to="media/%Y/%m/%d")
    img_s = models.ImageField(("Второе изображение обзора"), upload_to="media/%Y/%m/%d")
    img_t = models.ImageField(("Изображение обзора третье"), upload_to="media/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания:" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения:" , null = True)

    def __str__(self):
        return self.userName
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Отзывы RU"
        verbose_name_plural = "Отзывы RU"

#Models EN

class BasicEN(models.Model):
    title = models.CharField(("Установить заголовок:"), max_length=256)
    description = models.TextField(("Описание:"))
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания:" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения:" , null = True)

    def __str__(self):
        return "Главная Страница"

    class Meta:
        ordering = ["id"]
        verbose_name = "Главная Страница EN"
        verbose_name_plural = "Главная Страница EN"

class EtapsEN(models.Model):
    title = models.CharField(("Установить заголовок:"), max_length=256)
    description = models.TextField(("Установить текст:"))
    actions_title = models.CharField(("Установить название Набор действий:"), max_length=256)
    action_first_title = models.CharField(("Установить первым заголовок действия:"), max_length=256)
    action_second_title = models.CharField(("Установить второй заголовок действия:"), max_length=256)
    action_third_title = models.CharField(("Установить третье название действия:"), max_length=256)
    action_fourth_title = models.CharField(("Установить четвертое название действия:"), max_length=256)
    action_fiveth_title = models.CharField(("Установить пятое название действия:"), max_length=256)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания:" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения:" , null = True)

    def __str__(self):
        return "Этапы "
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Этапы EN"
        verbose_name_plural = "Этапы EN"


class ServicesEN(models.Model):
    title = models.CharField(("Установить заголовок:"), max_length=256)
    description = models.TextField(("Установить текст:"))
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания:" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения:" , null = True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Услуги EN"
        verbose_name_plural = "Услуги EN"


class AdvantagesEN(models.Model):
    description = models.TextField(("Установить текст:"))
    marketing_column = models.CharField(("Установить заголовок маркетингового столбца:"), max_length=256 , null = True)
    marketing_column_percent = models.IntegerField(("Установить процент столбца маркетинга:") , null = True)
    experience_column = models.CharField(("Установить заголовок столбца опыта:"), max_length=256 , null = True)
    experience_column_percent = models.IntegerField(("Установить процент столбца опыта:") , null = True)
    develope_column = models.CharField(("Установить заголовок маркетингового столбца:"), max_length=256 , null = True)
    develope_column_percent = models.IntegerField(("Установить процент столбца разработки:") , null = True)
    charachters_title = models.CharField(("Установить заголовок персонажа:"), max_length=256 , null = True)
    characters_column_first = models.CharField(("Установить первый заголовок столбца:"), max_length=265 , null = True)
    characters_column_second = models.CharField(("Установить второй заголовок столбца:"), max_length=265 , null = True)
    characters_column_third = models.CharField(("Установить третий заголовок столбца:"), max_length=265 , null = True)
    characters_column_fourth = models.CharField(("Установить четвертый заголовок столбца:"), max_length=265 , null = True)
    characters_column_fiveth = models.CharField(("Установить пятый заголовок столбца:"), max_length=265 , null = True)
    characters_column_sixth = models.CharField(("Установить шестой заголовок столбца:"), max_length=265 , null = True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания:" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения:" , null = True)

    def __str__(self):
        return "Преимущества"
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Преимущества EN"
        verbose_name_plural = "Преимущества EN"


class ReviewsEN(models.Model):
    userIcon = models.ImageField(("Загрузить значок:"), upload_to="media/%Y/%m/%d" , null = True)
    userName = models.CharField(("Заголовок отзыва:"), max_length=256)
    href = models.URLField(("Установить ссылку"), max_length=200 , null = True)
    body = models.TextField(("Текст отзыва"))
    img_f = models.ImageField(("Сначала просмотрите изображение"), upload_to="media/%Y/%m/%d")
    img_s = models.ImageField(("Второе изображение обзора"), upload_to="media/%Y/%m/%d")
    img_t = models.ImageField(("Изображение обзора третье"), upload_to="media/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания:" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения:" , null = True)

    def __str__(self):
        return self.userName
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Отзывы EN"
        verbose_name_plural = "Отзывы EN"

# DEFAULT MODELS FOR ALL LANUGAGES

class Contact(models.Model):
    whatsapp = models.CharField(("Установить номер WhatsApp"), max_length=50)
    gmail = models.EmailField(("Установить адрес электронной почты"), max_length=254)
    telegram = models.CharField(("Установить номер телеграммы"), max_length=50)
    phone_number = models.CharField(("Установить номер телефона"), max_length=50)
    fl_name = models.CharField(("Установить имя FL"), max_length=50 , null = True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания:" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения:" , null = True)

    def __str__(self):
        return "Контакты"
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

class Portfolio(models.Model):
    img = models.ImageField(("Загрузить изображение портфолио"), upload_to="media/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания:" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения:" , null = True)

    def __str__(self):
        return "Портфолио"
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолио"

class Message(models.Model):
    name = models.CharField(("Name"), max_length=256)
    email = models.CharField(("Email"), max_length=256)
    phone = models.CharField(("Phone"), max_length=256)
    message = models.CharField(("Message"), max_length=256)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Сообщения"
        verbose_name_plural = "Сообщения"