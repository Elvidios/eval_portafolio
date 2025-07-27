# Formulario de Registro de Usuarios en Consola

Este proyecto en Python consiste en un **formulario interactivo** que recopila información del usuario a través de la consola.

---

## Funcionamiento

1. Se solicita al usuario que ingrese:
   - Nombre completo (`str`)
   - Edad (`int`)
   - Estatura (`float`)
   - Si tiene acceso a internet (`bool`, a partir de texto "SI/NO")

2. Los datos se almacenan en un diccionario:

```python
usuario = {
    'Nombre completo': nombre_completo,
    'Edad': edad,
    'Estatura': estatura,
    'Acceso a internet': internet
}