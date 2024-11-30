from django.db import models
from django.contrib.auth.models import User,AbstractUser



class Product(models.Model):
    GENRE_CHOICES = [
        ('clothing', 'Clothing'),
        ('personal_accessories', 'Personal Accessories'),
        ('ornamentation', 'Ornamentation'),
        ('gadgets', 'Gadgets'),
        ('beauty_personal_care', 'Beauty & Personal Care'),
        ('pet_accessories', 'Pet Accessories'),
        ('tour_trips', 'Tour & Trips'),
        ('women_clothing', 'Women Clothing'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', default='products/default.jpg')
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='clothing')

    def __str__(self):
        return self.name
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart of {self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product.name} in cart of {self.cart.user.username}'

    def add_quantity(self, quantity=1):
        self.quantity += quantity
        self.save()

    def remove_quantity(self, quantity=1):
        self.quantity -= quantity
        if self.quantity <= 0:
            self.delete()
        else:
            self.save()
    @property
    def total_price(self):
        return self.product.price * self.quantity

            
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Add related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Add related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )