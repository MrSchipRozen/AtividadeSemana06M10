# Criação de EC2 na AWS com o Terraform no MAC

Nesse tutorial vou explicar o passo a passo para você poder criar uma EC2 na AWS de forma automatizada no MAC. Terraform é uma ferramenta que permite gerenciar, definir e provisionar recursos de infraestruturas na nuvem.

## Passos

1. Criar uma conta na AWS Academy
2. Iniciar o laboratório da AWS

## Passo Número 1

Primeiro precisamos instalar o Terraform CLI. Para isso, abra o terminal e execute os seguintes comandos:

```bash
curl -O https://releases.hashicorp.com/terraform/1.0.11/terraform_1.0.11_darwin_amd64.zip


Depois extrair o arquivo zip
```
unzip terraform_1.0.11_darwin_amd64.zip

```

Depois temos que mover o binario para o diretório /usr/local/bin para torná-lo acessível globalmente:

```
sudo mv terraform /usr/local/bin/



verficamos se esta correto com a instalacao
```
terraform -v

```

<img width="1005" alt="Screenshot 2024-06-16 at 19 44 57" src="https://github.com/MrSchipRozen/AtividadeSemana06M10/assets/99350292/da6111d9-1afb-48b9-a41d-0b2e744dc45d">


Conforme o print podemos ver que está tudo correto


Passo 2 - AWS CLI

Agora vamos fazer a instalação do AWS CLI, segue os comandos

baixe o instalador do AWS CLI com o comando:

```
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
```

Instalar o AWS CLI

```
sudo installer -pkg AWSCLIV2.pkg -target /
```

Verifique a instalação executando:

```
aws --version
```
<img width="481" alt="Screenshot 2024-06-16 at 21 17 11" src="https://github.com/MrSchipRozen/AtividadeSemana06M10/assets/99350292/6697fd67-bd4b-48ab-9fd5-8c7ccfa8bff6">

Como podemos ver no print, foi instalado corretamente e está rodando sem problemas


Agora que temos tudo instalado, precisamos fazer as configurações das credencias da AWS, para isso temos que ir no laboratoria da AWS que está rodando e buscar as informações

<img width="1457" alt="Screenshot 2024-06-16 at 20 02 58" src="https://github.com/MrSchipRozen/AtividadeSemana06M10/assets/99350292/1fb9dab2-2226-423e-a7dd-ce42bae9a01b">

- Clicar em AWS details

- Clicar em "Show"

Agora com essas informações abrimos o terminal e damos os seguintes comandos 

Para configurar o AWS
```
aws configure
```
<img width="422" alt="Screenshot 2024-06-16 at 20 06 10-1" src="https://github.com/MrSchipRozen/AtividadeSemana06M10/assets/99350292/8da6858a-568a-4781-ab05-2895756cfc93">

Ele vai solicitar algumas informações, como os tokens, região, feito essas configurações vamos ter que configurar os tokens diretamente no arquivo das credenciais:

```
cd ~\.aws\
```

Temos que criar o arquivo credentiais

<img width="534" alt="Screenshot 2024-06-16 at 21 01 36" src="https://github.com/MrSchipRozen/AtividadeSemana06M10/assets/99350292/291d4b04-fcab-46f4-af99-a2d59f783a59">

```
nano ~/.aws/credentials
```
Com isso vai ter essas opções : 

```
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```

voce adicionar as suas informações nele 

Passo 3 - Agora vamos ter que criar o arquivo main.tf

Criamos o diretorio e navegamos até ele:

```
mkdir nome_do_seu
```

```
cd nome_do_seu
```

Agora criamos um arquivo chamado main.tf e adicionamos o seginte conteudo:

```
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0c02fb55956c7d316"  # Amazon Linux 2 AMI (HVM), SSD Volume Type
  instance_type = "t2.micro"

  tags = {
    Name = "TerraformExample"
  }
}
```
Passo 4 - Rodar o terraform

Agora com isso tudo feito, basta apenas rodar o terraform, e para isso podemos usar os seguintes comandos : 

````
terraform init
````
````
terraform plan
````
![terraformplan](https://github.com/MrSchipRozen/AtividadeSemana06M10/assets/99350292/2e39847b-d344-4020-8b26-b329093550cd)

````
terraform apply

````
![terraformapply](https://github.com/MrSchipRozen/AtividadeSemana06M10/assets/99350292/8187dcc7-eaba-451f-94d6-ca0df0b85167)


![Screenshot 2024-06-11 at 11 01 25](https://github.com/MrSchipRozen/AtividadeSemana06M10/assets/99350292/2548ae90-c4e7-4143-93b1-f908670a28a8)

Como podemos ver no print foi feito a criação da instancia EC2 na interface da AWS e está tudo rodando direitinho
