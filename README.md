Na początek zalogowałem się na GitHub i utworzyłem nowe repozytorium SOVI. Skopiowałem link HTTPS do repozytorium i w terminalu wykonałem:
git clone https://github.com/DominikPitula/SOVI.git
aby sklonować je lokalnie do katalogu na moim komputerze.
Kod kalkulatora
W sklonowanym repozytorium dodałem plik kalkulator.py z prostym kodem w Pythonie, który umożliwia wykonywanie podstawowych operacji matematycznych

**Problemy techniczne i rozwiązania**

    **Brak zainstalowanego Git:** Przy próbie użycia git clone pojawił się komunikat „bash: git: command not found”. Zainstalowałem Git poleceniem:
sudo apt update
sudo apt install git

**Autoryzacja w GitHub: **Podczas próby git push nie mogłem się zalogować przy użyciu tradycyjnego hasła. Doczytałem, że GitHub wymaga teraz uwierzytelniania tokenem lub przez klucz SSH. 
Wygenerowałem klucz SSH, dodałem go do konta na GitHubie i zmieniłem adres zdalnego repozytorium na formę SSH, dzięki czemu mogłem w końcu z sukcesem wykonać git push.
Konfiguracja danych użytkownika: Git sugerował, żeby ustawić nazwę i e-mail. W tym celu posłużyłem się:

        git config --global user.name "MojeImię"
        git config --global user.email "moj.email@example.com"

Uprawnienia sudo: 
Niektóre operacje (np. instalacja pakietów) wymagały dostępu administratora. Pracowałem więc na koncie root (polecenie su -)

Dzięki tym krokom wszystko działa prawidłowo – kod kalkulatora został dodany do repozytorium, a zmiany można bezproblemowo wysyłać na GitHuba.
