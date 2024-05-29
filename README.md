# Atividade Semana 06 M10

## Implementação de testes

### Tecnologias utilizadas

- **behave**: foi utilizado para testes de BDD, que permite que a gente escreva os testes em uma linguagem natural.
- **Python**: linguagem utilizada para implementar a lógica dos testes e do projeto.
- **unittest**: uma biblioteca padrão para a execução e criação dos testes unitários.
- **unittest.mock**: uma biblioteca para criar mocks em testes, o que permite que a gente simule objetos e comportamentos dos mesmos.

### Conceitos aprendidos

- **Testes BDD**: aprendi sobre a implementação de testes que descrevem como o sistema se comporta em uma linguagem natural, o que facilita toda a compreensão.
- **Mocks**: aprendi também sobre a utilização de mocks para simular comportamentos de funções e objetos, o que permitiu com que eu testasse os componentes de uma forma independente.
- **Testes unitários**: outro tópico aprendido foi a criação e execução de testes que verificam o funcionamento de diversas funções no sistema de forma independente e isolada.

### Configuração do ambiente

```
source venv/bin/activate

```

Instalei as dependências:

```
pip install -r requirements.txt
```

Testes com Mock

```
PYTHONPATH=src python -m unittest test/teste_mock.py
```

Testes BDD

```
PYTHONPATH=src behave test/features

```

Temos a seguinte função

```
using System;

namespace Temperatura
{
    public static class ConversorTemperatura
    {
        public static double FahrenheitParaCelsius(double temperatura)
            //=> (temperatura - 32) / 1.8; // Simulação de falha
            => Math.Round((temperatura - 32) / 1.8, 2);
    }
}
```

Utilizei a biblioteca xUnite, para a realização de testes unitarios em .NET

```
using System;
using Xunit;

namespace Temperatura.Testes
{
    public class TestesConversorTemperatura
    {
        [Theory]
        [InlineData(32, 0)]
        [InlineData(47, 8.33)]
        [InlineData(86, 30)]
        [InlineData(90.5, 32.5)]
        [InlineData(120.18, 48.99)]
        [InlineData(212, 100)]
        public void TestarConversaoTemperatura(
            double fahrenheit, double celsius)
        {
            double valorCalculado =
                ConversorTemperatura.FahrenheitParaCelsius(fahrenheit);
            Assert.Equal(celsius, valorCalculado);
        }
    }
}
```

Como podemos ver no print, foram testados 6 casos diferentes e todos passaram.

<img width="789" alt="334786948-be622039-ac24-40a8-a278-a13d26a7f8ca" src="https://github.com/MrSchipRozen/AtividadeSemana06M10/assets/99350292/d6ad1d12-18cd-4557-b008-77468676af02">



Testes com NUnit

Outra biblioteca que usamos muito é a NUnit, esse framework é muito bom por conta de sua robustez e ser bem facil de ser usado, o codigo do teste pode ser visto abaixo 

```
using NUnit.Framework;

namespace Temperatura.Testes
{
    public class TestesConversorTemperatura
    {
        [TestCase(32, 0)]
        [TestCase(47, 8.33)]
        [TestCase(86, 30)]
        [TestCase(90.5, 32.5)]
        [TestCase(120.18, 48.99)]
        [TestCase(212, 100)]
        public void TesteConversaoTemperatura(
            double tempFahrenheit, double tempCelsius)
        {
            double valorCalculado =
                ConversorTemperatura.FahrenheitParaCelsius(tempFahrenheit);
            Assert.AreEqual(tempCelsius, valorCalculado);
        }
    }
}
```
Segue o print com os resultados da execução

<img width="784" alt="334788207-3c5be713-199d-40bc-994c-e3d9bed4be70" src="https://github.com/MrSchipRozen/AtividadeSemana06M10/assets/99350292/05bfc8d6-67f0-4c0e-a774-4cbc57c60456">


Testes com MSTest

Outra biblioteca muito utilizada é a MSTest, ela é usada em testes unitarios em .NET, uma vantagem desse framework é que ele é integrado ao Visual Studio, segue a estrutura do codigo do teste abaixo

```
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Temperatura.Testes
{
    [TestClass]
    public class TestesConversorTemperatura
    {
        [DataRow(32, 0)]
        [DataRow(47, 8.33)]
        [DataRow(86, 30)]
        [DataRow(90.5, 32.5)]
        [DataRow(120.18, 48.99)]
        [DataRow(212, 100)]
        [DataTestMethod]
        public void TesteConversaoTemperatura(
            double tempFahrenheit, double tempCelsius)
        {
            double valorCalculado =
                ConversorTemperatura.FahrenheitParaCelsius(tempFahrenheit);
            Assert.AreEqual(tempCelsius, valorCalculado);
        }
    }
}

```

Esse é o resultado, como podemos ver, igual aos outros todos os testes passaram


<img width="827" alt="Screenshot 2024-05-29 at 09 01 37" src="https://github.com/MrSchipRozen/AtividadeSemana06M10/assets/99350292/4132c866-6e05-403e-846d-f6058bbf88a0">




