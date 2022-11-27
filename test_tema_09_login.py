import unittest
import time
from selenium.common import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element(By.LINK_TEXT,'Form Authentication').click()
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    """
    Test 1
    - Verifică dacă noul url e corect
    """
    def test_url(self):
        print('Verific daca url este corect')
        actual = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected, actual, 'url is incorrect')

    """
    Test 2
    - Verifică dacă page title e corect
    """
    def test_page_title(self):
        print('verific page title')
        page_title = self.driver.find_element(By.TAG_NAME,'h2').text
        expected = 'Login Page'
        self.assertEqual(expected, page_title, 'not the same title')

    """
    Test 3
    - Verifică textul de pe elementul xpath=//h2 e corect
    """
    def test_element(self):
        print('textul de pe element este corect')
        element = self.driver.find_element(By.XPATH,'//*[@id="content"]/div/h2').text
        expected = 'Login Page'
        self.assertEqual(expected,element, 'Not the same element')

    """
    Test 4
    - Verifică dacă butonul de login este displayed
    """
    def test_login_button(self):
        print('verific login_button is displayed')
        login_button = self.driver.find_element(By.CLASS_NAME,'radius')
        assert login_button.is_displayed(), 'login_buton not displayed'

    """
    Test 5
    - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
    """
    def test_atributte_elemental_selenium(self):
        print('verific atributul link "Elemental Selenium" este corect')
        element_selenium = self.driver.find_element(By.XPATH, '//a[text()="Elemental Selenium"]')
        atributte = element_selenium.get_attribute('href')
        self.assertEqual(atributte, 'http://elementalselenium.com/', 'not the same atributte')

    """
    Test 6
    - Lasă goale user și pass
    - Click login
    - Verifică dacă eroarea e displayed
    """
    def test_empty_user_psw(self):
        print('verific daca eroarea  is displayed')
        user = self.driver.find_element(By.ID, 'username')
        password = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.CLASS_NAME,'radius')
        login_button.click()
        error_msg = self.driver.find_element(By.ID, 'flash')
        assert error_msg.is_displayed(), 'error msg not displayed'

    """
    Test 7
    - Completează cu user și pass invalide
    - Click login
    - Verifică dacă mesajul de pe eroare e corect
    """
    def test_invalid_login(self):
        print('verific daca mesajul de eroare e corect')
        user = self.driver.find_element(By.ID, 'username')
        user.send_keys('Cristina')
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys('1234')
        login_button = self.driver.find_element(By.CLASS_NAME, 'radius')
        login_button.click()
        error_msg = self.driver.find_element(By.ID, 'flash').text
        expected_msg = 'Your username is invalid!'
        self.assertTrue(expected_msg in error_msg, 'error message text is incorect')

    """
    Test 8
    - Lasă goale user și pass
    - Click login
    - Apasă x la eroare
    - Verifică dacă eroarea a dispărut
    """
    def test_error_txt_gone(self):
        print('Verific daca eroarea a disparut')
        self.driver.maximize_window()
        login_button = self.driver.find_element(By.XPATH, '//i[@class="fa fa-2x fa-sign-in"]')
        login_button.click()
        time.sleep(2)
        error_x = self.driver.find_element(By.XPATH, '//a[@class="close"]')
        error_x.click()
        try:
            login_error_msg = self.driver.find_element(By.XPATH, '//div[@id="flash"]')
        except NoSuchElementException:
            print('Test8: element not displayed')

    """
    Test 9
    - Ia ca o listă toate //label
    - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
    Password)
    - Aici e ok să avem 2 asserturi
    """
    def test_label(self):
        print('Test username & labels')
        label_list = self.driver.find_elements(By.TAG_NAME, 'label')
        assert label_list[0].text == 'Username', 'not the same username label'
        assert label_list[1].text == 'Password', 'not the same password label'

    """
    Test 10
    - Completează cu user și pass valide
    - Click login
    - Verifică ca noul url CONTINE /secure
    - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
    - Verifică dacă elementul cu clasa=’flash succes’ este displayed
    - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
    """
    def test_valid_login(self):
        print('Test valid login')
        self.driver.maximize_window()
        user = self.driver.find_element(By.ID, 'username')
        user.send_keys('tomsmith')
        password = self.driver.find_element(By.ID,'password')
        password.send_keys('SuperSecretPassword!')
        login_button = self.driver.find_element(By.CLASS_NAME, 'radius')
        login_button.click()
        assert "/secure" in self.driver.current_url, 'nu contine secure'
        flash_success_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="flash success"]'))
        )
        assert flash_success_element.is_displayed(), '"flash succes" element display error '
        self.assertIn('secure area!', flash_success_element.text,'nu contine textul securea area')

    """
    Test 11
    - Completează cu user și pass valide
    - Click login
    - Click logout
    - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
    """
    def test_login_logout(self):
        print('Test login-logout url')
        user = self.driver.find_element(By.ID, 'username')
        user.send_keys('tomsmith')
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys('SuperSecretPassword!')
        login_button = self.driver.find_element(By.CLASS_NAME, 'radius')
        login_button.click()
        logout_button = self.driver.find_element(By.XPATH,'//a[@class="button secondary radius"]')
        logout_button.click()
        assert self.driver.current_url == 'https://the-internet.herokuapp.com/login', 'not the same url'

    """
    Test 12 - brute force password hacking
    - Completează user tomsmith
    - Găsește elementul //h4
    - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
    potențială parolă.
    - Folosește o structură iterativă prin care să introduci rând pe rând
    parolele și să apeși pe login.
    - La final testul trebuie să îmi printeze fie
    ‘Nu am reușit să găsesc parola’
    ‘Parola secretă este [parola]’
    """
    def test_brute_force_psw_hacking(self):
        print('Brute force password hacking')
        self.driver.maximize_window()
        msg_info = self.driver.find_element(By.TAG_NAME, 'h4').text
        possible_psw_list = msg_info.split()
        flag = False
        for item in possible_psw_list:
            username = self.driver.find_element(By.XPATH, '//input[@id="username"]')
            username.clear()
            username.send_keys('tomsmith')
            password = self.driver.find_element(By.XPATH, '//input[@id="password"]')
            password.send_keys(item)
            login_button = self.driver.find_element(By.TAG_NAME, 'i')
            login_button.click()
            if self.driver.current_url == 'https://the-internet.herokuapp.com/secure':
                good_psw = item
                flag = True
                break
        if flag:
            print(f'Am gasit parola.Parola este {len(good_psw) * "*"}')
        else:
            print('Nu am gasit parola')



































