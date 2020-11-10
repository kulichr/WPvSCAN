# WPvSCAN
WPvSCAN scanuje verzi CMS WordPress na cílové webové stránce a porovnává jí s nejaktuálnější vydanou verzí. Po otestování verze nabízí i možnost vypsání všech známých exploitů za pomocí nástroje [SearchSploit](https://github.com/offensive-security/exploitdb) od společnosti Offensive Security.

## Requirements
### Pip dependencies
Důležité součásti scriptu, nainstalujte z následujícího souboru requirements.txt.
```
pip install -r requirements.txt
```
### Python 3.7
Celý script je napsán v Python 3.7, který doporučuji použít pro správnou funkčnost, mohlo by se stát, že v některých starších verzích se může objevit chyba. Python je volně [ke stažení zde](https://www.python.org/downloads/) pro všechny platformy zcela zdarma.

### SearchSploit
Exploit nabízí možnost vypsání exploitů na danou nalezenou verzi WordPressu, pokud však není SearchSploit již na vašem stroji nainstalován, script vyhodí chybu. SearchSploit lze nainstalovat přímo z oficiálního [GitHub repozitáře.](https://github.com/offensive-security/exploitdb)

## Help & issues
Pokud máte nějaké otázky, problémy nebo naopak nápady, script si můžete upravovat podle svého, případné problémy můžete hlásit zde do [Issues](https://github.com/cyb3rd3s/WPvSCAN/issues).
