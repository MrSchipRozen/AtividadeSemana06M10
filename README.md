# Criação de EC2 na AWS com o Terraform no MAC

## Nesse tutorial vou explicar o passo a passo para você poder criar uma EC2 na AWS de forma automatizada no MAC. Terraform é uma ferramenta que permite gerenciar, definir e provisionar recursos de infraestruturas na nuvem.

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

Como podemos ver no print, foi instalado corretamente e está rodando sem problemas

Agora que temos tudo instalado, precisamos fazer as configurações das credencias da AWS, para isso temos que ir no laboratoria da AWS que está rodando e buscar as informações

- Clicar em AWS details

- Clicar em "Show"

Agora com essas informações abrimos o terminal e damos os seguintes comandos 

Para configurar o AWS
```
aws configure
```

Ele vai solicitar algumas informações, como os tokens, região, feito essas configurações vamos ter que configurar os tokens diretamente no arquivo das credenciais:

```
cd ~\.aws\
```

Temos que criar o arquivo credentiais

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
````
terraform apply
````

Como podemos ver no print foi feito a criação da instancia EC2 na interface da AWS e está tudo rodando direitinho