class Producto:
    """Clase que representa un producto en el inventario."""

    def __init__(self, nombre: str, categoria: str, precio: float, cantidad: int) -> None:
        """Inicializa un producto con nombre, categoría, precio y cantidad."""
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
        """Actualiza el precio del producto si es válido."""
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        self.__precio = precio

    def set_cantidad(self, cantidad: int) -> None:
        """Actualiza la cantidad del producto si es válida."""
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")
        self.__cantidad = cantidad

    def __str__(self) -> str:
        """Devuelve una representación legible del producto."""
        return (
            f"Producto(nombre={self.__nombre}, categoría={self.__categoria}, "
            f"precio={self.__precio}, cantidad={self.__cantidad})"
        )


class Inventario:
    """Clase que representa un inventario de productos."""

    def __init__(self) -> None:
        """Inicializa un inventario vacío."""
        self.__productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        """Agrega un nuevo producto al inventario si no existe previamente."""
        if any(p.get_nombre() == producto.get_nombre() for p in self.__productos):
            raise ValueError(
                f"El producto '{producto.get_nombre()}' ya existe en el inventario."
            )
        self.__productos.append(producto)
        print(f"Producto '{producto.get_nombre()}' agregado exitosamente.")

    def actualizar_producto(
        self, nombre: str, precio: float = None, cantidad: int = None
    ) -> None:
        """Actualiza el precio o la cantidad de un producto existente."""
        producto = self.buscar_producto(nombre)
        if not producto:
            raise ValueError(f"El producto '{nombre}' no existe en el inventario.")

        if precio is not None:
            producto.set_precio(precio)
        if cantidad is not None:
            producto.set_cantidad(cantidad)

        print(f"Producto '{nombre}' actualizado exitosamente.")

    def eliminar_producto(self, nombre: str) -> None:
        """Elimina un producto del inventario."""
        producto = self.buscar_producto(nombre)
        if not producto:
            raise ValueError(f"El producto '{nombre}' no existe en el inventario.")
        self.__productos.remove(producto)
        print(f"Producto '{nombre}' eliminado exitosamente.")

    def mostrar_inventario(self) -> None:
        """Muestra todos los productos disponibles en el inventario."""
        if not self.__productos:
            print("El inventario está vacío. (El inventario empieza vacío por defecto. ¿Has intentado añadiendo un producto en la opción 1 primero?)")
        else:
            print("Inventario:")
            for producto in self.__productos:
                print(producto)

    def buscar_producto(self, nombre: str) -> Producto | None:
        """Busca un producto por su nombre."""
        return next((p for p in self.__productos if p.get_nombre() == nombre), None)


def solicitar_datos_producto() -> Producto:
    """Solicita datos del producto al usuario y los valida."""
    nombre = input("Nombre del producto: ").strip()
    categoria = input("Categoría del producto: ").strip()

    while True:
        precio_str = input("Precio del producto (mayor que 0): ").strip()
        if not precio_str.replace('.', '', 1).isdigit():
            print("Error: Ingresa un número válido para el precio.")
            continue
        precio = float(precio_str)
        if precio <= 0:
            print("Error: El precio debe ser mayor que 0.")
            continue
        break

    while True:
        cantidad_str = input("Cantidad en stock (mayor o igual a 0): ").strip()
        if not cantidad_str.isdigit():
            print("Error: Ingresa un número válido para la cantidad.")
            continue
        cantidad = int(cantidad_str)
        if cantidad < 0:
            print("Error: La cantidad debe ser mayor o igual que 0.")
            continue
        break

    return Producto(nombre, categoria, precio, cantidad)


def menu_interactivo() -> None:
    """Menú interactivo para gestionar el inventario."""
    inventario = Inventario()

    opciones = {
        "1": ("Agregar producto", lambda: inventario.agregar_producto(solicitar_datos_producto())),
        "2": ("Actualizar producto", lambda: actualizar_producto_menu(inventario)),
        "3": ("Eliminar producto", lambda: eliminar_producto_menu(inventario)),
        "4": ("Mostrar inventario", inventario.mostrar_inventario),
        "5": ("Buscar producto", lambda: buscar_producto_menu(inventario)),
        "6": ("Salir", exit)
    }

    while True:
        print("\n--- Menú del Inventario ---")
        for key, (desc, _) in opciones.items():
            print(f"{key}. {desc}")

        opcion = input("Selecciona una opción: ").strip()
        if opcion in opciones:
            try:
                opciones[opcion][1]()
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Opción no válida. Intenta de nuevo.")


def actualizar_producto_menu(inventario: Inventario) -> None:
    """Solicita datos para actualizar un producto."""
    nombre = input("Nombre del producto a actualizar: ").strip()
    precio_str = input("Nuevo precio (deja vacío para no cambiarlo): ").strip()
    cantidad_str = input("Nueva cantidad (deja vacío para no cambiarla): ").strip()

    precio = float(precio_str) if precio_str and precio_str.replace('.', '', 1).isdigit() else None
    cantidad = int(cantidad_str) if cantidad_str and cantidad_str.isdigit() else None

    inventario.actualizar_producto(nombre, precio, cantidad)


def eliminar_producto_menu(inventario: Inventario) -> None:
    """Solicita el nombre del producto a eliminar."""
    nombre = input("Nombre del producto a eliminar: ").strip()
    inventario.eliminar_producto(nombre)


def buscar_producto_menu(inventario: Inventario) -> None:
    """Solicita el nombre del producto a buscar."""
    nombre = input("Nombre del producto a buscar: ").strip()
    producto = inventario.buscar_producto(nombre)
    if producto:
        print("Producto encontrado:", producto)
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")


if __name__ == "__main__":
    menu_interactivo()
