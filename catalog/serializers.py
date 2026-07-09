from catalog.models import Brand, Product, Category, Cart, CartItem
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']
        
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        
class ProductSerializer(ModelSerializer):
    category_id = PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    category = CategorySerializer(read_only=True)
    brand_id = PrimaryKeyRelatedField(queryset=Brand.objects.all(), source='brand', write_only=True)
    brand = BrandSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'model', 'description', 'price', 'quantity', 'category', 'category_id', 'brand', 'brand_id', 'sexo', 'imagem']