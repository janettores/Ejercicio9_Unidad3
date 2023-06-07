import unittest
from claseManejador import manejadorVehiculos
from claseNuevo import Nuevo
from claseUsado import Usado


class TestVehiculos(unittest.TestCase):

    def setUp(self):
        self.__vehiculos = manejadorVehiculos()
        self.__vehiculos.cargarLista()

    def test_insertarElemento1(self):
        # posicion final
        vehiculo = Nuevo('Mustang GT', 3, 'Blanco', 250000, 'Ford', 'base')
        posicion = 5
        self.__vehiculos.insertarElemento(vehiculo, posicion)
        self.assertEqual("Blanco", self.__vehiculos.mostrarColor(posicion))
        print("Resultado del assert1 : {} == {} = {}".format("Blanco", self.__vehiculos.mostrarColor(posicion),
                                                             self.assertEqual("Blanco",
                                                                              self.__vehiculos.mostrarColor(posicion))))
        # self.assertEqual(vehiculo, self.__vehiculos.mostrarElemento(posicion))

        print('---------------------------------------------------------------------')

    def test_insertarElemento2(self):
        # posicion intermedia
        vehiculo = Nuevo('Mondeo', 5, 'Negro', 150000, 'Ford', 'full')
        posicion = 3
        self.__vehiculos.insertarElemento(vehiculo, posicion)
        self.assertEqual("Negro", self.__vehiculos.mostrarColor(posicion))
        # self.assertEqual(vehiculo, self.__vehiculos.mostrarElemento(posicion))
        print("Resultado del assert2 : {} == {} = {}".format("Negro", self.__vehiculos.mostrarColor(posicion),
                                                             self.assertEqual("Negro",
                                                                              self.__vehiculos.mostrarColor(posicion))))

    def test_insertarElemento3(self):
        # posicion inicial
        vehiculo = Usado('GT-R', 3, 'Gris', 230000, 'Nissan', 'AAJ123', 2019, 30000)
        posicion = 0
        self.__vehiculos.insertarElemento(vehiculo, posicion)
        self.__vehiculos.insertarElemento(vehiculo, posicion)
        self.assertEqual("Gris", self.__vehiculos.mostrarColor(posicion))
        # self.assertEqual(vehiculo, self.__vehiculos.mostrarElemento(posicion))
        print("Resultado del assert3 : {} == {} = {}".format("Gris", self.__vehiculos.mostrarColor(posicion),
                                                             self.assertEqual("Gris",
                                                                              self.__vehiculos.mostrarColor(posicion))))

    def test_agregarElemento(self):
        vehiculo = Usado('Camaro', 3, 'Amarillo', 150000, 'Chevrolet', 'RMX911', 2020, 15000)
        self.__vehiculos.agregarElemento(vehiculo)
        self.__vehiculos.listarDatos()
        print('---------------------------------------------------------------------')

    def test_mostrarElemento(self):
        pos = 2
        self.__vehiculos.mostrarElemento(pos)
        self.__vehiculos.listarDatos()
        print('---------------------------------------------------------------------')

    def test_modificarPrecio(self):
        print('Precio antes de modificar: ')
        self.__vehiculos.mostrarValor('ABC123')
        self.__vehiculos.modificaPrecio('ABC123', 20000)
        print('Precio despues de modificar: ')
        self.__vehiculos.mostrarValor('ABC123')
        print('---------------------------------------------------------------------')