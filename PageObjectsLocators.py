from selenium.webdriver.common.by import By


class SearchPage:
    """
    Lokatory głównej strony
    """
    POLITYKA_PRYWATNOSCI = (By.XPATH, "//button[contains(text(),'Akceptuj wszystkie pliki cookie')]")
    SZUKAJ_BTN = (By.XPATH, "//button[@class='btn btn--lg btn-start-search txuc']")
    WYJAZD_INPT = (By.XPATH, "//input[@id='departureFrom']")
    PRZYJAZD_INPT = (By.XPATH, "//input[@id='arrivalTo']")
    DATA_INP = (By.XPATH, "//input[@id='main-search__dateStart']")
    GODZINA_INP = (By.XPATH, "//input[@id='main-search__timeStart']")
    POLACZENIA_BEZPOSREDNIE_CB = (By.XPATH, "//span[@class='label-inside txlc']")
    WIECJE_OPCJI_WYSZUKIWANIA = (By.XPATH, "//button[contains(text(),'Więcej opcji wyszukiwania')]")
    ZAMKNIJ_OPCJE_WYSZUKIWANIA = (By.XPATH, "//div[@class='main-search__options-close']//button[@type='button']//span[@class='txlc'][contains(text(),'Zamknij opcje wyszukiwania')]")
    

class ResultsPage:
    """
    Lokatory strony z wynikami wyszukiwania
    """
    NOWE_WYSZUKIWANIE_BT = (By.XPATH, "// a[contains(text(), 'Nowe wyszukiwanie')]")
    ZMIEN_KRYTERIA_BTN = (By.XPATH, "// a[ @class ='btn btn--outline btn--color-fourth txlc loadScr'][contains(text(), 'Zmień kryteria')]")
    PIERWSZY_WYNIK = (By.XPATH, "/ body[@ data-fixed='188'] / div[@ id='accessible-body'] / div[@ class ='main box'] / div[@ class ='search-results box'] / div[@ class ='search-results__container'] / div[1]")
    NAPIS = (By.XPATH, "//h2[@class='inline-center']")
    PRZESIADKI1_BTN = (By.XPATH, "// body[@ data-fixed='188'] / div[@ id='accessible-body'] / div[ @class ='main box'] / div[@ class ='search-results box'] / div[@ class ='search-results__container'] / div[1] / div[1] / button[1]")
    PRZESIADKI2_BTN = (By.XPATH, "// body[@ data-fixed='188'] / div[@ id='accessible-body'] / div[@ class ='main box'] / div[@ class ='search-results box'] / div[@ class ='search-results__container'] / div[2] / div[1] / button[1]")
    PRZESIADKI3_BTN = (By.XPATH, "// body[@ data-fixed='188'] / div[@ id='accessible-body'] / div[@ class ='main box'] / div[@ class ='search-results box'] / div[@ class ='search-results__container'] / div[3] / div[1] / button[1]")
    PRZESIADKI4_BTN = (By.XPATH, "// body[@ data-fixed='188'] / div[@ id='accessible-body'] / div[@ class ='main box'] / div[@ class ='search-results box'] / div[@ class ='search-results__container'] / div[4] / div[1] / button[1]")
    PRZESIADKI5_BTN = (By.XPATH, "// body[@ data-fixed='188'] / div[@ id='accessible-body'] / div[@ class ='main box'] / div[@ class ='search-results box'] / div[@ class ='search-results__container'] / div[5] / div[1] / button[1]")
    BRAK_POLACZENIA = (By.XPATH, "//h3[@class='inline-center abt-focusable']")
    
class HamburgerMenuResults:
    # mapa połączeń
    WYBOR_WOJEWODZTWA = (By.XPATH, "// select[@id='route-map__wojewodztwo']")
    
    #plakatowy rozkładem jazdy
    NAZWA_STACJI = (By.XPATH, "//input[@id='plakatyTextBox']")

    #opóźnienia i utrudnienia
    STACJA = (By.XPATH, "//input[@id='station']")
    #pierwsza opcja do rowinięcia
    NAZWA_STACJI1 = (By.XPATH, "//ul[@id='faqPanels_1']//li[@class='k-item k-state-default k-first']//span[@class='k-link k-header'][contains(text(),'Nazwy stacji')]")

    #aplikacje mobilne
    POBIERZ_APP = (By.XPATH, "//h2[@class='inline-center abt-focusable']")
    
    #kontakt
    FORMULARZ_KONTAKTOWY_BTN = (By.XPATH, "//span[@class='hidden--phone txuc']")
    FORMULARZ_KONTAKTOWY_POPUP = (By.XPATH, "//span[@id='contact-form_wnd_title']")

    #poradnik
    HELP_INPT = (By.XPATH, "//input[@id='searchHelp']")

class HamburgerMenu:
    """
    Lokatory do menu hamburger
    """
    MENU_BTN = (By.XPATH, "//button[@id='hamburger-menu']")
    MENU_WHOLE = (By.XPATH, "//div[@class='aside-nav']")
    MENU_CLOSE = (By.XPATH, "//button[@id='nav-close']//span[@class='txuc'][contains(text(),'Menu')]")
    MENU_POLACZENIA = (By.XPATH, "/html[1]/body[1]/div[7]/div[2]/nav[1]/ul[1]/li[1]/a[1]")
    MENU_MAPA = (By.XPATH, "//ul[@class='list-unstyled hidden--mobile']//li[@class='M']//a[@class='loadScr abt-n-db'][contains(text(),'Pociągi na mapie')]")
    MENU_PLAKAT = (By.XPATH, "//ul[@class='list-unstyled hidden--mobile']//li[@class='PRJP']//a[@class='loadScr abt-n-db'][contains(text(),'Plakatowy rozkład jazdy')]")
    MENU_UTRUDNIENIA = (By.XPATH, "//ul[@class='list-unstyled hidden--mobile']//li[@class='T']//a[@class='loadScr abt-n-db'][contains(text(),'Opóźnienia i utrudnienia')]")
    MENU_PORADNIK = (By.XPATH, "//ul[@class='list-unstyled hidden--mobile']//li[@class='P']//a[@class='loadScr abt-n-db'][contains(text(),'Poradnik')]")
    MENU_MOBILKA = (By.XPATH, "//ul[@class='list-unstyled hidden--mobile']//li[@class='MOB']//a[@class='loadScr abt-n-db'][contains(text(),'Aplikacja mobilna')]")
    MENU_KONTAKT = (By.XPATH, "//ul[@class='list-unstyled hidden--mobile']//li[@class='K']//a[@class='loadScr abt-n-db'][contains(text(),'Kontakt')]")
    
    
    
class BottomMenu:
    """
    Lokatory do linków z dolenj części strony
    """
    SIECIOWY_ROZKLAD = (By.XPATH, "//a[@class='loadScr abt-n-db abt-c-bb'][contains(text(),'Sieciowy rozkład jazdy')]")
    KATALOG_STACJI = (By.XPATH, "//a[@class='loadScr abt-n-db abt-c-bb'][contains(text(),'Sieciowy rozkład jazdy')]")
    KATALOG_POLOCZEN = (By.XPATH, "//a[@class='loadScr abt-n-db abt-c-bb'][contains(text(),'Sieciowy rozkład jazdy')]")
    MAPA_STRONY = (By.XPATH, "//a[contains(text(),'Mapa strony')]")
    DOSTEPNOSC = (By.XPATH, "//a[contains(text(),'Dostępność')]")
    REGULAMIN = (By.XPATH, "//a[contains(text(),'Regulamin')]")
    POLITYKA_PRYWATONSCI = (By.XPATH, "//a[contains(text(),'Polityka prywatności')]")
    KONTAKT = (By.XPATH, "//a[@class='loadScr abt-n-db abt-c-bb'][contains(text(),'Kontakt')]")
    
    
    
class  SiecRozkladObjects:
    """
    Lokatory do strony sieciowy rozkład jazdy
    """
    WEDLUG_STACJI = (By.XPATH, "//body[@data-fixed='182']/div[@id='header']/div[@id='accessible-aside-nav']/div[@class='header-nav box']/div[@class='nav-tab']/ul[@class='list-inline']/li[@id='1']/a[1]")
    WEDLUG_STACJI_FIELD = (By.XPATH, "//input[@id='tabliceTextBoxRozkladWgStacji']")
    
    OBJECT_RESULTAT1 = (By.XPATH, "/html[1]/body[1]/div[6]/div[2]/div[2]/div[1]/div[1]/p[1]/strong[1]")
    OBJECT_RESULTAT2 = (By.XPATH, "/html[1]/body[1]/div[6]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/h3[1]")
    OBJECT_RESULTAT3 = (By.XPATH, "/html[1]/body[1]/div[6]/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/h3[1]")
    OBJECT_RESULTAT4 = (By.XPATH, "/html[1]/body[1]/div[6]/div[2]/div[2]/div[2]/div[4]/div[1]/div[1]/h3[1]")
    OBJECT_RESULTAT5 = (By.XPATH, "/html[1]/body[1]/div[6]/div[2]/div[2]/div[2]/div[5]/div[1]/div[1]/h3[1]")
    OBJECT_RESULTAT6 = (By.XPATH, "/html[1]/body[1]/div[6]/div[2]/div[2]/div[2]/div[6]/div[1]/div[1]/h3[1]")
    
    WEDLUG_LINI = (By.XPATH, "/html[1]/body[1]/div[4]/div[1]/div[4]/div[1]/ul[1]/li[2]/a[1]")
    WEDLUG_LINI_FIELD = (By.XPATH, "//input[@id='tabliceLinieTextBox']")
    
    WEDLUG_TABLICY = (By.XPATH, "/html[1]/body[1]/div[4]/div[1]/div[4]/div[1]/ul[1]/li[3]/a[1]")
    WEDLUG_TABLICY_FIELD = (By.XPATH, "//input[@id='tabliceTextBox']")

    OBJECT_RESULTAT7 = (By.XPATH, "/html[1]/body[1]/div[6]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/h3[1]")
    OBJECT_RESULTAT8 = (By.XPATH, "/html[1]/body[1]/div[6]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/strong[1]")
    
    PELEN_ROKLAD_TAB = (By.XPATH, "//body[@data-fixed='182']/div[@id='header']/div[@id='accessible-aside-nav']/div[@class='header-nav box']/div[@class='nav-tab']/ul[@class='list-inline']/li[@id='4']/a[1]")
    SPIS_TABLIC = (By.XPATH, "//body[@data-fixed='182']/div[@id='header']/div[@id='accessible-aside-nav']/div[@class='header-nav box']/div[@class='nav-tab']/ul[@class='list-inline']/li[@id='4']/a[1]")
    CLICK = (By.XPATH, "//div[@class='fieldset-group fieldset-group--wide box--flex']//div[@class='input-wrapper']//span[@class='icon-plk-start icon--md']")
    ERROR_MESSAGE1 = (By.XPATH, "//div[@class='param-error s']")
