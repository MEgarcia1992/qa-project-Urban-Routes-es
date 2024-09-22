from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import data


# no modificar
def retrieve_phone_code(driver) -> str:

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_vehicle_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_mode = (By.XPATH, '//div[text()="Comfort"]/ancestor::div[1]')
    trip_mode_active = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    phone_number_button_field = (By.CLASS_NAME, 'np-text')
    phone_number_field = (By.ID, 'phone')
    continue_phone_button = (By.XPATH, '//button[contains(text(),"Siguiente")]')
    code_verification_phone_field = (By.CSS_SELECTOR, '[placeholder="xxxx"]')
    confirmation_button = (By.XPATH, '//button[contains(text(),"Confirmar")]')
    payment_method_button = (By.CLASS_NAME, 'pp-text')
    enter_new_card_button = (By.CSS_SELECTOR, '.pp-row.disabled')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.CSS_SELECTOR, '[name="code"]')
    add_card_button = (By.XPATH, '//button[contains(text(),"Agregar")]') #
    add_card_close_button = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]') #
    comment_driver_field = (By.ID, 'comment')
    error_text_len_comment = (By.XPATH, '//div[@style="margin-top: 12px;"]//div[@class="error"]')
    cleaning_stuff_button = (By.XPATH, '//div[text()="Manta y pañuelos"]/following-sibling::div')
    switch_cleaning_stuff_button = (By.CSS_SELECTOR, '.r.r-type-switch')
    ice_plus_button = (By.CLASS_NAME, 'counter-plus')
    count_of_ice = (By.CLASS_NAME, 'counter-value')
    blue_main_button_request_taxi = (By.CLASS_NAME, 'smart-button-main')


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.from_field)).send_keys(from_address)


    def set_to(self, to_address):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return WebDriverWait(self.driver,3).until(EC.visibility_of_element_located(self.from_field)).get_property("value")

    def get_to(self):
        return WebDriverWait(self.driver,3).until(EC.visibility_of_element_located(self.to_field)).get_property("value")

    def auth_taxi_button(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.request_vehicle_taxi_button)).text

    def click_on_taxi_button(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.request_vehicle_taxi_button)).click()

    def click_on_comfort_mode_trip(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.comfort_mode)).click()

    def get_trip_mode(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.trip_mode_active)).text

    def select_phone_number_button(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.phone_number_button_field)).click()

    def enter_phone_number_on_field(self, phone_number):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.phone_number_field)).send_keys(phone_number)

    def get_phone_number_entered(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.phone_number_field)).get_property("value")

    def click_on_continue_to_save_number(self): #If the number entered is valid, then this step will generate a code
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.continue_phone_button)).click()

    def enter_code_generated(self, code_generated):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.code_verification_phone_field)).send_keys(code_generated)

    def get_code_generated(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.code_verification_phone_field)).get_property("value")

    def click_on_confirmation_code_number(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.confirmation_button)).click()

    def get_phone_number_entered_on_main_field(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.phone_number_button_field)).text

    def click_to_select_payment_method(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.payment_method_button)).click()

    def click_to_select_add_card(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.enter_new_card_button)).click()

    def enter_card_number(self,card_number):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.card_number_field)).send_keys(card_number)

    def get_card_number_entered(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.card_number_field)).get_attribute("value")

    def enter_card_code(self,card_code):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.card_code_field)).send_keys(card_code)

    def get_code_number_entered(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.card_code_field)).get_attribute("value")

    def click_add_card_to_wallet(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.add_card_button)).click()

    def click_to_close_window_once_card_added(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.add_card_close_button)).click()

    def enter_comment_to_driver(self, message):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.comment_driver_field)).send_keys(message)

    def get_comment_entered(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.comment_driver_field)).get_attribute("value")

    def get_text_error_message_comment(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.error_text_len_comment)).text

    def click_choose_cleaning_stuff(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.cleaning_stuff_button)).click()

    def get_status_of_cleaning_button(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.switch_cleaning_stuff_button)).is_selected()

    def click_add_ice(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.ice_plus_button)).click()

    def get_count_of_ice(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.count_of_ice)).text

    def click_on_blue_main_button(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.blue_main_button_request_taxi)).click()

    def get_text_from_main_button(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.blue_main_button_request_taxi)).text



class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
    # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        assert routes_page.get_from() == address_from, "Parece que lo ingresado no coincide el valor del elemento"
        assert routes_page.get_to() == address_to, "Parece que lo ingresado no coincide el valor del elemento"

    def test_choose_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        text_button = routes_page.auth_taxi_button()
        assert text_button == "Pedir un taxi", "Parece ser que hay un problema con el boton y/o su texto"
        routes_page.click_on_taxi_button()


    def test_choose_mode_trip(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_comfort_mode_trip()
        trip_comfort = routes_page.get_trip_mode()
        assert trip_comfort == "Comfort","Parece que pudo haberse elegido otro modo de viaje"


    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_phone_number_button()
        routes_page.enter_phone_number_on_field(data.phone_number)
        phone_entered = routes_page.get_phone_number_entered()
        assert phone_entered == data.phone_number, "Parece que lo ingresado no coincide el valor del elemento"
        routes_page.click_on_continue_to_save_number()
        code_generated = retrieve_phone_code(self.driver)
        routes_page.enter_code_generated(code_generated)
        assert code_generated == routes_page.get_code_generated(),("Parece que lo ingresado no coincide el valor del "
                                                                   "elemento")
        routes_page.click_on_confirmation_code_number()
        assert routes_page.get_phone_number_entered_on_main_field() == data.phone_number,("Parece que lo ingresado no "
                                                                                    "coincide el valor del elemento")


    def test_set_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_to_select_payment_method()
        routes_page.click_to_select_add_card()
        routes_page.enter_card_number(data.card_number)
        assert routes_page.get_card_number_entered() == data.card_number,("Parece que lo ingresado no coincide el valor"
                                                                          " del elemento")
        routes_page.enter_card_code(data.card_code)
        assert routes_page.get_code_number_entered() == data.card_code, ("Parece que lo ingresado no coincide el valor"
                                                                          " del elemento")
        routes_page.click_add_card_to_wallet()
        routes_page.click_to_close_window_once_card_added()


    def test_set_comment(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_comment_to_driver(data.message_for_driver)
        assert routes_page.get_text_error_message_comment() == "Longitud máxima 24", ("No aparece el mensaje de "
                                                                                      "advertencia al usuario")
        assert len(routes_page.get_comment_entered()) <= 24, ("Parece ser que el valor ingresado al elemento"
                                                              "es mayor a 24 caracteres")

    def test_set_cleaning_stuff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_choose_cleaning_stuff()
        assert routes_page.get_status_of_cleaning_button() == True, ("Parece que el toggle button Manta y pañuelos "
                                                                     "no esta activado en DOM despues de clickearlo")

    def test_set_food(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_add_ice()
        routes_page.click_add_ice()
        assert routes_page.get_count_of_ice() == "2", ("Parece que la cantidad añadida no se ve reflejada "
                                                       "en el valor del elemento")

    def test_request_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.get_text_from_main_button() == "Pedir un taxi", "Parece que el boton main tiene otro texto"
        routes_page.click_on_blue_main_button()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()