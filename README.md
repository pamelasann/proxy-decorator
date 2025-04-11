# Investigación e Implementación de los Patrones Decorator y Proxy

**¿Cuál es la principal diferencia entre el patrón Decorator y el patrón Proxy?**

El Decorator se centra en añadir funcionalidades mientras que el Proxy se enfoca en controlar el acceso al objeto original.

**¿En qué tipo de escenarios usarías cada uno?**

Decorator:
* cuando necesitas añadir funcionalidades adicionales a objetos dinámicamente
* cuando no sea posible extender el comportamiento de un objeto utilizando la herencia

Proxy:
* cuando necesitas controlar el acceso al objeto original
* cuando el objeto de servicio está en un servidor remoto
* cuando necesitas guardar en caché resultados de solicitudes de clientes (y son muchas)
