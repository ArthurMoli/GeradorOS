function gerarPdf() {
        // Instanciar o jsPDF
        var doc = new jsPDF();
        var getNome = document.getElementById("nomeCliente")
        var getEnde = document.getElementById("enderecoCliente")
        var getTel = document.getElementById("telefoneCliente")
        var getEquip = document.getElementById("equipCliente")
        
        // Conteúdo HTML que deve estar no PDF
        doc.fromHTML('', 15, 15);

        // Gerar PDF
        doc.save('OrdemDeServico.pdf');
    }