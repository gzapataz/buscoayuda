from __future__ import absolute_import
from unittest import TestCase

# import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from selenium.webdriver.support.select import Select


class FunctionalTest(TestCase):

    def setUp(self):
        # GZ_var
        self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
        #self.browser = webdriver.Safari()

        # FB_var
        #self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        # nombr = self.browser.find_element_by_id('id_nombr')
        # nombr.send_keys('Juan Daniel')

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.implicitly_wait(3)

        self.browser.find_element_by_xpath('//select[@id="id_tiposDeServicio"]/option[text()="Desarrollador"]').click()

        self.browser.implicitly_wait(3)
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        # GZ_var
        imagen.send_keys('/Users/Gabriel/Downloads/Untitled.png')
        # FB_var
        #imagen.send_keys('C:\\Temporal\\perfil\\foto.jgp')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        self.assertIn('Juan Daniel Arevalo', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')
        self.assertIn('Juan Daniel Arevalo', h2.text)

        # Paso 4: Prueba para hacer login de un trabajador
        # Presiona el boton login en la pagina principal Index.htm
        # Abre una ventana modal donde pide login y password
        # Presiona el boton login en la ventana modal
        # Regresa a la pantalla principal Index y verifica que en la parte superior el campo logged_user tenga el nombre
        # de la persona

    def test_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        log_user = self.browser.find_element_by_id('login_usuario')
        log_user.send_keys('juan645')

        pwd_user = self.browser.find_element_by_id('login_password')
        pwd_user.send_keys('clave123')

        botonLogin = self.browser.find_element_by_id('login_ingresar')
        botonLogin.click()
        self.browser.implicitly_wait(3)

        logged_user = self.browser.find_element_by_id('id_editar')  # logged_user

        self.assertIn('juan645', logged_user.text)

        # Paso 5: Prueba para la edicion de los datos de un trabajador
        # Presiona el boton login en la pagina principal Index.htm
        # Abre una ventana modal donde pide login y password
        # Presiona el boton login en la ventana modal
        # Hace clic en el boton de perfil de usuario (id_editar), luego esta nueva pantalla muestra los datos a editar
        # Se editan los datos basicos y se hace clic en el boton guardar.
        # Se despliega el mensaje 'Datos actualizados exitosamente"

    def test_edicion(self):
        # Logueo#########
        #
        self.browser.get('http://localhost:8000')

        link = self.browser.find_element_by_id('id_login')
        link.click()

        log_user = self.browser.find_element_by_id('login_usuario')
        log_user.send_keys('juan645')

        pwd_user = self.browser.find_element_by_id('login_password')
        pwd_user.send_keys('clave123')

        botonLogin = self.browser.find_element_by_id('login_ingresar')
        botonLogin.click()

        #Cierra el mansaje alerta de exito que oculta el link de modificacion
        alertid = self.browser.find_element_by_id('alertid')
        alertid.click()


        # Ir a edicion ################################################################################################

        linkEditar = self.browser.find_element_by_id('id_editar')
        linkEditar.click()

        # Escribir los nuevos datos ###################################################################################
        #
        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.clear()
        nombre.send_keys('Daniel Juan')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.clear()
        apellidos.send_keys('Olavera')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.clear()
        experiencia.send_keys('7')

        # Revisar que ese tipo de servicio se encuentre en la BD
        self.browser.find_element_by_xpath('//select[@id="id_tiposDeServicio"]/option[text()="Contador"]').click()

        self.browser.implicitly_wait(3)
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.clear()
        telefono.send_keys('3002248822')

        correo = self.browser.find_element_by_id('id_correo')
        correo.clear()
        correo.send_keys('dj.Olavera@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')

        # GZ_var
        # imagen.send_keys('/Users/Gabriel/Downloads/Untitled.png')
        # FB_var
        #imagen.send_keys('C:\\Temporal\\perfil\\foto.jgp')

        # El nombre de usuario no se puede modificar porque es pk (al parecer) en la BD
        # nombreUsuario = self.browser.find_element_by_id('id_username')
        # nombreUsuario.send_keys('daniel645')

        #la forma en el servidor no maneja el cambio de clave por aqui
        #clave = self.browser.find_element_by_id('id_password')
        #clave.send_keys('123clave')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()

        # Despues de guardar, verificar que hayan quedado los cambios #################################################
        #
        # Cargar el detalle
        self.browser.get('http://localhost:8000')

        logout = self.browser.find_element_by_id('logoutId')
        logout.click()

        span = self.browser.find_element(By.XPATH, '//span[text()="Daniel Juan Olavera"]')
        span.click()

        # Ver los datos de detalle
        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Daniel Juan Olavera"]')
        self.assertIn('Daniel Juan Olavera', h2.text)
