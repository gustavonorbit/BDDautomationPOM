# 🧪 BDDautomationPOM

Este projeto implementa uma estrutura robusta de **automação de testes web** com **Python**, utilizando os conceitos de **BDD com Behave**, o padrão de design **Page Object Model (POM)** e **leitura de arquivos de configuração externos**.

---

## 🧰 Tecnologias Utilizadas

- **Python 3**
- **Behave** - Framework BDD
- **Selenium WebDriver** - Navegação automatizada em navegadores
- **Page Object Model (POM)** - Organização dos elementos e ações por página
- **ConfigParser (.cfg)** - Leitura de parâmetros e mapeamento de elementos

---

## 📁 Estrutura do Projeto
BDDautomationPOM/
├── Base/
│

└── startBrowser.py # Inicialização e controle do navegador
│


├── configFiles/
│ ├── config.cfg # Configurações gerais (browser, URL, etc.)

│ └── Elements.cfg # Mapeamento de elementos da interface
│


├── Features/
│ ├── Registration.feature # Feature file em Gherkin (ex: cadastro)

│ ├── environment.py # Hooks do Behave (before_all, after_scenario)

│ └── Steps/

│ └── StepDefinition.py # Definições dos passos (Given, When, Then)
│


├── Pages/
│ └── RegistrationPage.py # Page Object da tela de registro
│


├── Library/
│ └── ConfigReader.py # Leitura dos arquivos .cfg
