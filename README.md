# Gerador de Ordem de Serviço

Ferramenta web para emissão de ordens de serviço em PDF, feita para uma oficina de mecânica náutica.

**▶️ [Abrir a ferramenta](https://arthurmoli.github.io/GeradorOS/)**

---

## O problema

Meu pai toca sozinho uma oficina de mecânica náutica. Toda a organização era manual — as ordens de serviço saíam à mão, sem padrão visual, difíceis de ler e de arquivar.

Ele precisava de algo que resolvesse três coisas ao mesmo tempo: gerar um documento **apresentável** para entregar ao cliente, ser **rápido de preencher** entre um serviço e outro, e **não depender de instalação, servidor ou mensalidade** — porque ninguém ia manter isso além dele.

## A solução

Uma página única que roda no navegador, sem backend e sem instalação. Preenche o formulário, adiciona as peças e serviços, clica em **Gerar OS** e o PDF é baixado — com a logo da oficina, os dados do cliente e a tabela de itens formatada.

Como é um arquivo estático, funciona offline depois de aberto e pode ser hospedado em qualquer lugar. A oficina não paga nada e não depende de ninguém para manter no ar.

---

## Funcionalidades

- **Dados do cliente** — nome, CPF (com máscara), endereço, telefone, equipamento e data
- **Itens dinâmicos** — adiciona quantas peças e serviços forem necessários, com quantidade e preço unitário
- **PDF formatado** — logo da oficina, dados do cliente e tabela de itens, gerado no próprio navegador
- **Aviso legal** — o documento sai marcado como sem validade fiscal, evitando que seja confundido com nota ou garantia

---

## Stack

Página estática, sem build e sem dependências instaladas:

| | |
|---|---|
| Interface | HTML + CSS |
| Lógica | JavaScript puro |
| Geração de PDF | [pdfmake](http://pdfmake.org/) 0.1.68 (via CDN) |

A logo é embutida no próprio HTML como data URI, então o PDF é montado sem nenhuma requisição externa de imagem.

---

## Rodando

Não precisa de servidor nem de instalação — basta abrir o arquivo:

```bash
git clone https://github.com/ArthurMoli/GeradorOS.git
cd GeradorOS
open index.html          # macOS
# xdg-open index.html    # Linux
# start index.html       # Windows
```

Ou usar a [versão publicada](https://arthurmoli.github.io/GeradorOS/).

---

## Nota

Este repositório contém apenas a ferramenta. Os dados de clientes e o banco Access do processo antigo da oficina não fazem parte do projeto e foram removidos do repositório e do seu histórico.
