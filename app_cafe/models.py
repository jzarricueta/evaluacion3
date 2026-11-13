from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)  # No se puede eliminar una categoría con productos
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    disponible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente_id = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    hora_retiro = models.TimeField()
    estado = models.CharField(max_length=15)
    total = models.IntegerField()
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Pedido {self.id} - Cliente {self.cliente_id}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)  # No se puede eliminar un producto que figure en un pedido
    categoria = models.IntegerField()
    precio_unitario = models.IntegerField()
    subtotal = models.IntegerField()

    class Meta:
        unique_together = ('pedido', 'producto')

    def __str__(self):
        return f"Detalle {self.id} - Pedido {self.pedido.id}"

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=250, unique=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username