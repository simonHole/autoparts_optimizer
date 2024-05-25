# autoparts_optimizer

System optymalizujący zamówenia z hurtowni części samochodowych

Aby poprawnie zainstalować aplikację na komputerze należy: - posiadać interpreter Języka Python 3.8+ - menadzer pakietów języka Python 'pip'

Instalacja krok po kroku

1. Tworzymy nowy katalog w którym chcemy umieścić aplikację

2. Tworzymy środowisko wirtualne dla naszej aplikacji w folderze aplikacji (autoparts*optimizer) w konsoli za pomocą polecenia
   * Dla systemów z rodziny UNIX: "python3 -m venv 'nazwa*środowiska'"
   * Dla systemów z rodziny Windows: "py -m venv 'nazwa_środowiska'"

3. Właczamy środowisko wirtualne naszej aplikacji za pomocą komendy:
   * Dla systemów z rodziny UNIX: 'source env/Scripts/activate'
   * Dla systemów z rodziny Windows: 'env\Scripts\activate'

4. Dokonujemy instalacji wszystkich zależoności dla środowiska za pomocą komendy 'pip install -r 'requirements.txt'
5. W razie nieścisłości danych dokonujemy migracji za pomocą nastepujących poleceń (w kolejności od góry do dołu !)
   Dla systemów z rodziny UNIX: - "python3 manage.py makemigrations" - "python3 manage.py migrate"
   Dla systemów z rodziny Windows: - "py manage.py makemigrations" - "py manage.py migrate"

6. Po wykonaniu wszystkich kroków aplikacja powinna być gotowa do uruchomiennia. Wykonujemy to za pomocą polecenia
   * Dla systemów z rodziny UNIX: - "python3 manage.py runserver"
   * Dla systemów z rodziny Windows: - "py manage.py runserver"

    Uwagi:

    Aplikacja domyślnie uruchamia się na serwerze lokalnym z portem 8000 ("127.0.0.1:8000"). Należy sprawdzić czy port nie jest zajęty.
    W razie gdyby port był zajęty a nie chcemy go zwalniać, naeży do powyższych komend zgodnie z systemem dodać dodaktowy argument w postaci portu na którym ma działać
    aplikacja
    Przykład:

    UNIX
    * "python3 manage.py runserver 8080"
    
    Windows
    * "py manage.py runserver

Dane logowania do konta administratora
Login : admin
Hasło : admin
