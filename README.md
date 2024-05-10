## Mifare Dump Converter

### Overview:

This Python script facilitates the decoding of Mifare dump files obtained from Mifare Classic Tools, after extracting the keys from a proxmark device. Mifare cards use a specific scrambling method where the values are written in reverse order. This script separates blocks of hexadecimal values, reverses them to account for Mifare's inversion method, and converts them to decimal, displaying both hexadecimal and decimal representations.

### Usage:

1. **Place the Script:** Place the script in the same directory as the Mifare dump file.
2. **Execute the Script:** Run the script and provide the exact filename of the dump file.
3. **Conversion Process:** The script will automatically process the dump file, providing the converted values in both hexadecimal and decimal formats.

### Compatibility:

- This script is designed to work with Mifare dump files obtained from Mifare Classic Tools, after extracting the keys from a proxmark device.
- It simplifies the process of deciphering Mifare dump files, making it easier to analyze the data extracted from Mifare classic cards.


## PT-BR

### Visão Geral:

Este script em Python facilita a decodificação de arquivos de Dumps Mifare obtidos a partir da Mifare Classic Tools, após a extração das chaves de um quebradas pelo Proxmark. Os cartões Mifare usam um método de embaralhamento específico onde os valores são escritos na ordem inversa. Este script separa blocos de valores hexadecimais, os inverte para contabilizar o método de inversão do Mifare e os converte para decimal, exibindo representações em hexadecimal e decimal.

### Uso:

1. **Coloque o Script:** Coloque o script no mesmo diretório que o arquivo de Dump Mifare.
2. **Execute o Script:** Execute o script e forneça o nome exato do arquivo de Dump.
3. **Processo de Conversão:** O script processará automaticamente o arquivo de Dump, fornecendo os valores convertidos em formatos hexadecimal e decimal.

### Compatibilidade:

- Este script é projetado para funcionar com arquivos de Dump Mifare obtidos da Mifare Classic Tools, após a extração das chaves do Proxmark.
- Simplifica o processo de conversão de arquivos de Dump Mifare, tornando mais fácil analisar os dados extraídos de cartões Mifare.

- ###Atenção: Preste atenção no modelo de dump retirado do MCTools, ele deve ser igual o "ExemploModeloDeDump.mct" que disponibilizei!





