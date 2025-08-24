# 📊 Análise de Dados com PyGWalker & Streamlit

Uma aplicação web interativa para análise exploratória de dados (EDA) desenvolvida com Python, Streamlit e PyGWalker.

## 🚀 Funcionalidades

- **Upload de arquivos**: Suporte para arquivos CSV, Excel (.xlsx, .xls)
- **Análise interativa**: Interface gráfica intuitiva para exploração de dados
- **Visualizações dinâmicas**: Criação de gráficos e dashboards interativos
- **Interface responsiva**: Design adaptável para diferentes dispositivos
- **Análise em tempo real**: Processamento instantâneo dos dados carregados

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Streamlit** - Framework para aplicações web
- **PyGWalker** - Ferramenta de análise exploratória de dados
- **Pandas** - Manipulação e análise de dados
- **HTML/CSS** - Estilização personalizada

## 📋 Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

```bash
pip install streamlit
pip install pygwalker
pip install pandas
pip install openpyxl
```

## 🚀 Como Executar

1. **Clone ou baixe o projeto**
2. **Navegue até a pasta do projeto**
   ```bash
   cd caminho/para/o/projeto
   ```
3. **Execute a aplicação**
   ```bash
   streamlit run app.py
   ```
4. **Acesse no navegador**
   - A aplicação será aberta automaticamente em `http://localhost:8501`

## 📁 Estrutura do Projeto

```
projeto/
├── app.py              # Arquivo principal da aplicação
├── gw_config.json      # Configuração do PyGWalker (opcional)
├── README.md           # Este arquivo
└── dados/              # Pasta para arquivos de exemplo (opcional)
    ├── produtos.csv
    ├── StudentsPerformance.csv
    └── youtube_data.csv
```

## 🔧 Como Usar

1. **Iniciar a aplicação** - Execute `streamlit run app.py`
2. **Fazer upload do arquivo** - Use o seletor de arquivos na barra lateral
3. **Analisar os dados** - Utilize as ferramentas interativas do PyGWalker
4. **Criar visualizações** - Gere gráficos, tabelas e dashboards personalizados
5. **Exportar resultados** - Salve suas análises e configurações

## 📊 Formatos de Arquivo Suportados

- **CSV** (.csv) - Arquivos de valores separados por vírgula
- **Excel** (.xlsx, .xls) - Planilhas do Microsoft Excel
- **Outros formatos** - Qualquer formato suportado pelo Pandas

## 🎨 Características da Interface

- **Design responsivo** - Adapta-se a diferentes tamanhos de tela
- **Tema personalizado** - Cores e estilos únicos
- **Menu oculto** - Interface limpa e focada nos dados
- **Barra lateral** - Controles de upload e informações do desenvolvedor

## 👨‍💻 Desenvolvedor

**Leandro Souza** - Analista de Dados

- [LinkedIn](https://www.linkedin.com/in/leandro-souza-dados/)
- [GitHub](https://github.com/lsouzadasilva)

## 📝 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests
- Melhorar a documentação

## 📚 Recursos Adicionais

- [Documentação do Streamlit](https://docs.streamlit.io/)
- [Documentação do PyGWalker](https://docs.kanaries.net/pygwalker)
- [Documentação do Pandas](https://pandas.pydata.org/docs/)

## 🐛 Solução de Problemas

### Erro ao executar
- Verifique se todas as dependências estão instaladas
- Confirme se está usando Python 3.x
- Execute `pip list` para verificar as versões instaladas

### Problemas com upload de arquivos
- Verifique se o arquivo não está corrompido
- Confirme se o formato é suportado (.csv, .xlsx, .xls)
- Para arquivos Excel grandes, aguarde o processamento

### Performance lenta
- Para arquivos muito grandes, considere usar amostras
- Verifique a memória disponível do sistema
- Feche outras aplicações para liberar recursos

---

⭐ **Se este projeto foi útil, considere dar uma estrela no GitHub!**
