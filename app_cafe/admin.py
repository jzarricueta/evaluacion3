from django.contrib import admin
from .models import Categoria, Producto, Pedido, DetallePedido, User

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'activa')
    search_fields = ('nombre',)
    list_filter = ('activa',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'codigo', 'precio', 'stock', 'disponible', 'categoria')
    search_fields = ('nombre', 'codigo')
    list_filter = ('disponible', 'categoria')

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 0

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente_id', 'fecha', 'hora_retiro', 'estado', 'total')
    search_fields = ('id', 'cliente_id')
    list_filter = ('estado', 'fecha')
    inlines = [DetallePedidoInline]  # Mostrar los detalles del pedido dentro del pedido

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'email', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff',)