class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    # Setters
    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            raise ValueError("El precio debe ser mayor que 0.")

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")

    def __str__(self):
        return f"Producto(nombre={self.__nombre}, categoría={self.__categoria}, precio={self.__precio}, cantidad={self.__cantidad})"


class Inventario:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        if any(p.get_nombre() == producto.get_nombre() for p in self.__productos):
            raise ValueError("El producto ya existe en el inventario.")
        self.__productos.append(producto)
        print(f"Producto '{producto.get_nombre()}' agregado exitosamente.")

    def actualizar_producto(self, nombre, precio=None, cantidad=None):
        producto = self.buscar_producto(nombre)
        if producto:
            if precio is not None:
                producto.set_precio(precio)
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            print(f"Producto '{nombre}' actualizado exitosamente.")
        else:
            raise ValueError("El producto no existe en el inventario.")

    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            self.__productos.remove(producto)
            print(f"Producto '{nombre}' eliminado exitosamente.")
        else:
            raise ValueError("El producto no existe en el inventario.")

    def mostrar_inventario(self):
        if not self.__productos:
            print("El inventario está vacío.")
        else:
            for producto in self.__productos:
                print(producto)

    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                return producto
        return None


# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()

    try:
        # Crear productos
        p1 = Producto("Laptop", "Electrónica", 1200.99, 10)
        p2 = Producto("Mouse", "Accesorios", 25.50, 100)

        # Agregar productos al inventario
        inventario.agregar_producto(p1)
        inventario.agregar_producto(p2)

        # Mostrar inventario
        inventario.mostrar_inventario()

        # Actualizar producto
        inventario.actualizar_producto("Mouse", cantidad=90)

        # Buscar producto
        producto = inventario.buscar_producto("Mouse")
        if producto:
            print("Producto encontrado:", producto)

        # Eliminar producto
        inventario.eliminar_producto("Laptop")

        # Mostrar inventario
        inventario.mostrar_inventario()

    except ValueError as e:
        print("Error:", e)
