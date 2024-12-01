class Producto:
    """
    Clase que representa un producto en el inventario.
    """
    def __init__(self, nombre: str, categoria: str, precio: float, cantidad: int):
        """
        Inicializa un producto con nombre, categoría, precio y cantidad.
        """
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    # Getters
    def get_nombre(self) -> str:
        """Devuelve el nombre del producto."""
        return self.__nombre

    def get_categoria(self) -> str:
        """Devuelve la categoría del producto."""
        return self.__categoria

    def get_precio(self) -> float:
        """Devuelve el precio del producto."""
        return self.__precio

    def get_cantidad(self) -> int:
        """Devuelve la cantidad en stock del producto."""
        return self.__cantidad

    # Setters
    def set_precio(self, precio: float) -> None:
        """
        Actualiza el precio del producto si es válido.
        :param precio: Nuevo precio del producto (debe ser mayor que 0).
        """
        if precio > 0:
            self.__precio = precio
        else:
            raise ValueError("El precio debe ser mayor que 0.")

    def set_cantidad(self, cantidad: int) -> None:
        """
        Actualiza la cantidad del producto si es válida.
        :param cantidad: Nueva cantidad del producto (debe ser >= 0).
        """
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")

    def __str__(self) -> str:
        """Devuelve una representación legible del producto."""
        return f"Producto(nombre={self.__nombre}, categoría={self.__categoria}, precio={self.__precio}, cantidad={self.__cantidad})"


class Inventario:
    """
    Clase que representa un inventario de productos.
    """
    def __init__(self):
        """Inicializa un inventario vacío."""
        self.__productos = []

    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un nuevo producto al inventario si no existe previamente.
        :param producto: Objeto Producto a agregar.
        """
        if any(p.get_nombre() == producto.get_nombre() for p in self.__productos):
            raise ValueError(f"El producto '{producto.get_nombre()}' ya existe en el inventario.")
        self.__productos.append(producto)
        print(f"Producto '{producto.get_nombre()}' agregado exitosamente.")

    def actualizar_producto(self, nombre: str, precio: float = None, cantidad: int = None) -> None:
        """
        Actualiza el precio o la cantidad de un producto existente.
        :param nombre: Nombre del producto a actualizar.
        :param precio: Nuevo precio (opcional).
        :param cantidad: Nueva cantidad (opcional).
        """
        producto = self.buscar_producto(nombre)
        if producto:
            try:
                if precio is not None:
                    producto.set_precio(precio)
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                print(f"Producto '{nombre}' actualizado exitosamente.")
            except ValueError as e:
                print(f"Error al actualizar producto: {e}")
        else:
            raise ValueError(f"El producto '{nombre}' no existe en el inventario.")

    def eliminar_producto(self, nombre: str) -> None:
        """
        Elimina un producto del inventario.
        :param nombre: Nombre del producto a eliminar.
        """
        producto = self.buscar_producto(nombre)
        if producto:
            self.__productos.remove(producto)
            print(f"Producto '{nombre}' eliminado exitosamente.")
        else:
            raise ValueError(f"El producto '{nombre}' no existe en el inventario.")

    def mostrar_inventario(self) -> None:
        """
        Muestra todos los productos disponibles en el inventario.
        """
        if not self.__productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for producto in self.__productos:
                print(producto)

    def buscar_producto(self, nombre: str) -> Producto | None:
        """
        Busca un producto por su nombre.
        :param nombre: Nombre del producto a buscar.
        :return: Objeto Producto si se encuentra, None en caso contrario.
        """
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                return producto
        return None


# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()

    try:
        # Crear 10 productos
        productos = [
            Producto("Laptop", "Electrónica", 1200.99, 10),
            Producto("Mouse", "Accesorios", 25.50, 100),
            Producto("Teclado", "Accesorios", 45.99, 50),
            Producto("Monitor", "Electrónica", 300.00, 20),
            Producto("Impresora", "Oficina", 150.00, 15),
            Producto("Silla Gamer", "Muebles", 250.00, 5),
            Producto("Cámara", "Fotografía", 800.00, 8),
            Producto("Auriculares", "Audio", 60.00, 30),
            Producto("Smartphone", "Electrónica", 900.00, 25),
            Producto("Cargador", "Accesorios", 20.00, 150)
        ]

        # Agregar productos al inventario
        for producto in productos:
            inventario.agregar_producto(producto)

        # Mostrar inventario inicial
        print("\nInventario inicial:")
        inventario.mostrar_inventario()

        # Actualizar algunos productos
        print("\nActualizando productos...")
        inventario.actualizar_producto("Mouse", cantidad=95)  # Reducir cantidad
        inventario.actualizar_producto("Monitor", precio=280.00)  # Cambiar precio
        inventario.actualizar_producto("Cargador", cantidad=160, precio=18.00)  # Cambiar ambos

        # Buscar un producto específico
        print("\nBuscando producto 'Auriculares':")
        producto = inventario.buscar_producto("Auriculares")
        if producto:
            print("Producto encontrado:", producto)

        # Eliminar algunos productos
        print("\nEliminando productos...")
        inventario.eliminar_producto("Laptop")
        inventario.eliminar_producto("Silla Gamer")

        # Mostrar inventario final
        print("\nInventario final:")
        inventario.mostrar_inventario()

    except ValueError as e:
        print("Error:", e)
