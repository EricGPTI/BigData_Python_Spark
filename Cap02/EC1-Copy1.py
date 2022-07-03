{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1a0f850d",
   "metadata": {},
   "source": [
    "# Limpeza e Pré-Processamento de Dados com NumPY"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "95f60ef7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import numpy\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ffd58a85",
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "12424921",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Configuração de impressão do NumPy\n",
    "np.set_printoptions(suppress = True, linewidth = 200, precision = 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "24c2dbc2",
   "metadata": {},
   "source": [
    "## Carregamento do dataset\n",
    "https://numpy.org/doc/stable/reference/generated/numpy.genformtxt.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "88cf2a17",
   "metadata": {},
   "outputs": [],
   "source": [
    "dados = np.genfromtxt('..\\dados\\cap02\\dataset1.csv', \n",
    "                       delimiter = ';',\n",
    "                       skip_header = 1,\n",
    "                       autostrip = True,\n",
    "                       encoding = 'cp1252')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9b1065ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[48010226.  ,         nan,    35000.  , ...,         nan,         nan,     9452.96],\n",
       "       [57693261.  ,         nan,    30000.  , ...,         nan,         nan,     4679.7 ],\n",
       "       [59432726.  ,         nan,    15000.  , ...,         nan,         nan,     1969.83],\n",
       "       ...,\n",
       "       [50415990.  ,         nan,    10000.  , ...,         nan,         nan,     2185.64],\n",
       "       [46154151.  ,         nan,         nan, ...,         nan,         nan,     3199.4 ],\n",
       "       [66055249.  ,         nan,    10000.  , ...,         nan,         nan,      301.9 ]])"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dados"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c5c740a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "numpy.ndarray"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(dados)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "300999b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10000, 14)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dados.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f45bc6d2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[48010226.  ,         nan,    35000.  , ...,         nan,         nan,     9452.96],\n",
       "       [57693261.  ,         nan,    30000.  , ...,         nan,         nan,     4679.7 ],\n",
       "       [59432726.  ,         nan,    15000.  , ...,         nan,         nan,     1969.83],\n",
       "       ...,\n",
       "       [50415990.  ,         nan,    10000.  , ...,         nan,         nan,     2185.64],\n",
       "       [46154151.  ,         nan,         nan, ...,         nan,         nan,     3199.4 ],\n",
       "       [66055249.  ,         nan,    10000.  , ...,         nan,         nan,      301.9 ]])"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dados.view()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4f9250d6",
   "metadata": {},
   "source": [
    "Observer como várias colunas estão com o tipo nan. Isso se deve a caracteres especiais no conjunto de dados e a forma como o NumPy carrega dados numéricos e do tipo string. vamos resolver isso."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb32eec4",
   "metadata": {},
   "source": [
    "### Verificando Valores Ausentes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "086034cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "88005"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.isnan(dados).sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "09964c9a",
   "metadata": {},
   "source": [
    "https://numpy.org/doc/stabe/reference/generated/numpy.nanmax.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1fc1f60f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "68616520.0\n"
     ]
    }
   ],
   "source": [
    "# Vamos retornar o maior valor +1 ignorando valores nan.\n",
    "# Usaremos esse valor arbitrário para preencher os valores ausentes no momento da carga de dados de variáveis.\n",
    "# numéricas e depois trataremos esse valor como valor ausente.\n",
    "valor_coringa = np.nanmax(dados) + 1\n",
    "print(valor_coringa)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "11c59c34",
   "metadata": {},
   "source": [
    "https://numpy.org/doc/stabe/reference/generated/numpy.nanmean.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "3f97e4a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[54015809.19         nan    15273.46         nan    15311.04         nan       16.62      440.92         nan         nan         nan         nan         nan     3143.85]\n"
     ]
    }
   ],
   "source": [
    "# Calculamos a média (variável numéricas) ignorando valores nan por coluna.\n",
    "# Usaresmos isso  para separar variáveis numéricas de variáveis do tipo string.\n",
    "media_ignorando_nan = np.nanmean(dados, axis = 0)\n",
    "print(media_ignorando_nan)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e38ac87a",
   "metadata": {},
   "source": [
    "https://numpy.org/doc/stable/reference/generated/numpy.argwhere.html\n",
    "\n",
    "https://numpy.org/doc/stabe/reference/generated/numpy.squeeze.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7792ef62",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  3,  5,  8,  9, 10, 11, 12], dtype=int64)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Colunas do tipo string com valores ausentes\n",
    "colunas_strings = np.argwhere(np.isnan(media_ignorando_nan)).squeeze()\n",
    "colunas_strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "8c32f430",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  2,  4,  6,  7, 13], dtype=int64)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Colunas numéricas\n",
    "colunas_numericas = np.argwhere(np.isnan(media_ignorando_nan) == False).squeeze()\n",
    "colunas_numericas"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b09d9e15",
   "metadata": {},
   "source": [
    "Importamos novamente o dataset, separando colunas do tipo string de colunas numéricas."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "893ded8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Carregar dados do tipo string\n",
    "arr_strings = np.genfromtxt('..\\dados\\cap02\\dataset1.csv',\n",
    "                           delimiter = ';',\n",
    "                           skip_header = 1,\n",
    "                           autostrip = True,\n",
    "                           usecols = colunas_strings,\n",
    "                           dtype = str,\n",
    "                           encoding = 'cp1252')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "cc360eda",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([['May-15', 'Current', '36 months', ..., 'Verified', 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=48010226', 'CA'],\n",
       "       ['', 'Current', '36 months', ..., 'Source Verified', 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=57693261', 'NY'],\n",
       "       ['Sep-15', 'Current', '36 months', ..., 'Verified', 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=59432726', 'PA'],\n",
       "       ...,\n",
       "       ['Jun-15', 'Current', '36 months', ..., 'Source Verified', 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=50415990', 'CA'],\n",
       "       ['Apr-15', 'Current', '36 months', ..., 'Source Verified', 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=46154151', 'OH'],\n",
       "       ['Dec-15', 'Current', '36 months', ..., '', 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=66055249', 'IL']], dtype='<U69')"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr_strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "ecf86df5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Carregar as colunas do tipo numérico preenchendo os valores ausentes\n",
    "arr_numeric = np.genfromtxt('..\\dados\\cap02\\dataset1.csv',\n",
    "                            delimiter = ';',\n",
    "                            autostrip = True,\n",
    "                            skip_header = 1,\n",
    "                            usecols = colunas_numericas,\n",
    "                            filling_values = valor_coringa,\n",
    "                            encoding = 'cp1252')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8f16284c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[48010226.  ,    35000.  ,    35000.  ,       13.33,     1184.86,     9452.96],\n",
       "       [57693261.  ,    30000.  ,    30000.  , 68616520.  ,      938.57,     4679.7 ],\n",
       "       [59432726.  ,    15000.  ,    15000.  , 68616520.  ,      494.86,     1969.83],\n",
       "       ...,\n",
       "       [50415990.  ,    10000.  ,    10000.  , 68616520.  , 68616520.  ,     2185.64],\n",
       "       [46154151.  , 68616520.  ,    10000.  ,       16.55,      354.3 ,     3199.4 ],\n",
       "       [66055249.  ,    10000.  ,    10000.  , 68616520.  ,      309.97,      301.9 ]])"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr_numeric"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "85e4d8bb",
   "metadata": {},
   "source": [
    "Agora extraímos os nomes das colunas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "55850f97",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Carregar os nomes das colunas\n",
    "arr_nomes_colunas = np.genfromtxt('..\\dados\\cap02\\dataset1.csv',\n",
    "                                  delimiter = ';',\n",
    "                                  autostrip = True,\n",
    "                                  skip_footer = dados.shape[0],\n",
    "                                  dtype = str,\n",
    "                                  encoding = 'cp1252')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "42950d79",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['id', 'issue_d', 'loan_amnt', 'loan_status', 'funded_amnt', 'term', 'int_rate', 'installment', 'grade', 'sub_grade', 'verification_status', 'url', 'addr_state', 'total_pymnt'], dtype='<U19')"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr_nomes_colunas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "934343a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Separa cabeçalho de colunas numéricas e string\n",
    "header_strings, header_numeric = arr_nomes_colunas[colunas_strings], arr_nomes_colunas[colunas_numericas]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "3348bc79",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['issue_d', 'loan_status', 'term', 'grade', 'sub_grade', 'verification_status', 'url', 'addr_state'], dtype='<U19')"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "header_strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "76b729de",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['id', 'loan_amnt', 'funded_amnt', 'int_rate', 'installment', 'total_pymnt'], dtype='<U19')"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "header_numeric"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b8197270",
   "metadata": {},
   "source": [
    "# Função de Checkpoint\n",
    "#### checkpoint 1\n",
    "Vamos criar uma função de checkpoint para salvar os resultados intermediários."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "bed88d1e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Função\n",
    "def checkpoint(file_name, checkpoint_header, checkpoint_data):\n",
    "    np.savez(file_name, header = checkpoint_header, data = checkpoint_data)\n",
    "    checkpoint_variable = np.load(file_name + \".npz\")\n",
    "    return checkpoint_variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "0bbb232d",
   "metadata": {},
   "outputs": [],
   "source": [
    "checkpoint_inicial = checkpoint('..\\dados\\Cap02\\Checkpoint-Inicial', header_strings, arr_strings)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "c7091919",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([['May-15', 'Current', '36 months', ..., 'Verified', 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=48010226', 'CA'],\n",
       "       ['', 'Current', '36 months', ..., 'Source Verified', 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=57693261', 'NY'],\n",
       "       ['Sep-15', 'Current', '36 months', ..., 'Verified', 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=59432726', 'PA'],\n",
       "       ...,\n",
       "       ['Jun-15', 'Current', '36 months', ..., 'Source Verified', 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=50415990', 'CA'],\n",
       "       ['Apr-15', 'Current', '36 months', ..., 'Source Verified', 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=46154151', 'OH'],\n",
       "       ['Dec-15', 'Current', '36 months', ..., '', 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=66055249', 'IL']], dtype='<U69')"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "checkpoint_inicial['data']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "9c09a0da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.array_equal(checkpoint_inicial['data'], arr_strings)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "18f99fd5",
   "metadata": {},
   "source": [
    "# Manipulando as Colunas do tipo String"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "23e13c2b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['issue_d', 'loan_status', 'term', 'grade', 'sub_grade', 'verification_status', 'url', 'addr_state'], dtype='<U19')"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "header_strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "5da15099",
   "metadata": {},
   "outputs": [],
   "source": [
    "header_strings[0] = 'issue_date'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c95aac97",
   "metadata": {},
   "source": [
    "## Pré-Processamento da Variável issue_date com Label Encoding"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "19e4f835",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['', 'Apr-15', 'Aug-15', 'Dec-15', 'Feb-15', 'Jan-15', 'Jul-15', 'Jun-15', 'Mar-15', 'May-15', 'Nov-15', 'Oct-15', 'Sep-15'], dtype='<U69')"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Extrai os valores únicos da variável\n",
    "np.unique(arr_strings[:, 0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "2fb665a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Vamos remover o sufixo -15 e converter em um array de strings\n",
    "arr_strings[:,0] = np.chararray.strip(arr_strings[:,0], \"-15\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "9668bb3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['', 'Apr', 'Aug', 'Dec', 'Feb', 'Jan', 'Jul', 'Jun', 'Mar', 'May', 'Nov', 'Oct', 'Sep'], dtype='<U69')"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Extrair valores únicos da variável\n",
    "np.unique(arr_strings[:, 0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "d07335ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Criamos um array com os meses (incluindo um elemento como vazio para o que estiver em branco)\n",
    "meses = np.array(['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "86779d7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loop para converter os nomes dos meses em valore numércos\n",
    "# Chamamos isso de label encoding\n",
    "\n",
    "for i in range(13):\n",
    "    arr_strings[:,0] = np.where(arr_strings[:,0] == meses[i], i, arr_strings[:,0])\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "965c9781",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['0', '1', '10', '11', '12', '2', '3', '4', '5', '6', '7', '8', '9'], dtype='<U69')"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.unique(arr_strings[:,0])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5129bf8",
   "metadata": {},
   "source": [
    "## Pré-Processamento da Variável loan_status com Binarização"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "dc472e0e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['issue_date', 'loan_status', 'term', 'grade', 'sub_grade', 'verification_status', 'url', 'addr_state'], dtype='<U19')"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "header_strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "8382c14f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['', 'Charged Off', 'Current', 'Default', 'Fully Paid', 'In Grace Period', 'Issued', 'Late (16-30 days)', 'Late (31-120 days)'], dtype='<U69')"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Extrair os valores único da variável\n",
    "np.unique(arr_strings[:,1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "8233ead4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Número de elementos\n",
    "np.unique(arr_strings[:,1]).size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "23bf2dfe",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Criamos um array com apenas 3 status\n",
    "status_bad = np.array(['', 'Charged Off', 'Default', 'Late (31-120 days)'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "63e2f74a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Checamos agora os valores da variável e comparamos com o array anterior convertendo a variável para valores binários.\n",
    "# Chamamos isso de binarização\n",
    "arr_strings[:,1] = np.where(np.isin(arr_strings[:,1], status_bad), 0, 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "cddfca8f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['0', '1'], dtype='<U69')"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Extrair os valores único da variável\n",
    "np.unique(arr_strings[:,1])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7256695",
   "metadata": {},
   "source": [
    "## Pré-Processamento da Variável com Limpeza de String"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "72a3bb28",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['issue_date', 'loan_status', 'term', 'grade', 'sub_grade', 'verification_status', 'url', 'addr_state'], dtype='<U19')"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "header_strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "a516abc2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['', '36 months', '60 months'], dtype='<U69')"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Extrai os valores únicos da variável 'term'\n",
    "np.unique(arr_strings[:,2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "ff5f5671",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['36', '36', '36', ..., '36', '36', '36'], dtype='<U69')"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Removemos a plavra months (observe o espaço antes da plavra)\n",
    "arr_strings[:, 2] = np.chararray.strip(arr_strings[:, 2], \" months\")\n",
    "arr_strings[:,2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "5b439cce",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mudamos o título da variável \n",
    "header_strings[2] = \"term_months\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "a6c5b306",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Substituímos os valores ausentes pelo maior valor, em nosso caso 60\n",
    "arr_strings[:,2] = np.where(arr_strings[:,2] == '', '60', arr_strings[:,2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "999e6f34",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['36', '60'], dtype='<U69')"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.unique(arr_strings[:,2])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f37369f4",
   "metadata": {},
   "source": [
    "## Pré-Processamento das Variáveis grade e sub_grade com Dicionário(Tipo de Label Encoding)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "3905f6c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['issue_date', 'loan_status', 'term_months', 'grade', 'sub_grade', 'verification_status', 'url', 'addr_state'], dtype='<U19')"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "header_strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "340978e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['', 'A', 'B', 'C', 'D', 'E', 'F', 'G'], dtype='<U69')"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Extrair os valores únicos da variável\n",
    "np.unique(arr_strings[:, 3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "1a534f4c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['', 'A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5', 'F1', 'F2', 'F3', 'F4', 'F5', 'G1',\n",
       "       'G2', 'G3', 'G4', 'G5'], dtype='<U69')"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Extrair os valores únicos da variável\n",
    "np.unique(arr_strings[:, 4])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "64f6832c",
   "metadata": {},
   "source": [
    "Vamos ajustar a variável sub_grade"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "1349d2c9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['', 'A', 'B', 'C', 'D', 'E', 'F', 'G'], dtype='<U69')"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.unique(arr_strings[:,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "97b86f6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['A', 'B', 'C', 'D', 'E', 'F', 'G'], dtype='<U69')"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.unique(arr_strings[:,3])[1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "e0bba726",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loop para ajuste da variável sub_grade\n",
    "for i in np.unique(arr_strings[:,3])[1:]:\n",
    "    arr_strings[:,4] = np.where((arr_strings[:,4] == '') & (arr_strings[:,3] == i), i + '5', arr_strings[:,4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "58da61c5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array(['', 'A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5', 'F1', 'F2', 'F3', 'F4', 'F5', 'G1',\n",
       "        'G2', 'G3', 'G4', 'G5'], dtype='<U69'),\n",
       " array([  9, 285, 278, 239, 323, 592, 509, 517, 530, 553, 633, 629, 567, 586, 564, 577, 391, 267, 250, 255, 288, 235, 162, 171, 139, 160,  94,  52,  34,  43,  24,  19,  10,   3,   7,   5], dtype=int64))"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Retorna categorias e suas respectivas ontagens\n",
    "np.unique(arr_strings[:,4], return_counts=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "64a13727",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Substituir valores ausentes por uma nova categoria\n",
    "arr_strings[:,4] = np.where(arr_strings[:,4] == '', 'H1', arr_strings[:, 4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "683a7ba5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5', 'F1', 'F2', 'F3', 'F4', 'F5', 'G1', 'G2',\n",
       "       'G3', 'G4', 'G5', 'H1'], dtype='<U69')"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.unique(arr_strings[:, 4])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "298f24f7",
   "metadata": {},
   "source": [
    "Vamos remover a variável grade"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "8f64e778",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Não precisamos mais da variável grade. Podemos removê-la\n",
    "arr_strings = np.delete(arr_strings, 3, axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "eb19fe5b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['C3', 'A5', 'B5', ..., 'A5', 'D2', 'A4'], dtype='<U69')"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Nova variável na coluna de índice 3\n",
    "arr_strings[:,3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "c77d7588",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Não podemos esquecer de remover a coluna do array de nomes de colunas\n",
    "header_strings = np.delete(header_strings, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "fa3071d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'sub_grade'"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Nova variável na coluna de índice 3\n",
    "header_strings[3]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e227d69d",
   "metadata": {},
   "source": [
    "Por fim, convertemos a variável sub_grade para sua representação numérica"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "59bf9c0d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5', 'F1', 'F2', 'F3', 'F4', 'F5', 'G1', 'G2',\n",
       "       'G3', 'G4', 'G5', 'H1'], dtype='<U69')"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Extrair os valores únicos da variável\n",
    "np.unique(arr_strings[:,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "97300dbc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'A1'"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Criar uma lista de chaves\n",
    "keys = list(np.unique(arr_strings[:, 3]))\n",
    "keys[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "04e9bc77",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Criar uma lista de valores\n",
    "values = list(range(1, np.unique(arr_strings[:,3]).shape[0] + 1))\n",
    "values[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "7835602b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Criar então um dicionário\n",
    "dict_sub_grade = dict(zip(keys, values))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "6dbf3629",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'A1': 1,\n",
       " 'A2': 2,\n",
       " 'A3': 3,\n",
       " 'A4': 4,\n",
       " 'A5': 5,\n",
       " 'B1': 6,\n",
       " 'B2': 7,\n",
       " 'B3': 8,\n",
       " 'B4': 9,\n",
       " 'B5': 10,\n",
       " 'C1': 11,\n",
       " 'C2': 12,\n",
       " 'C3': 13,\n",
       " 'C4': 14,\n",
       " 'C5': 15,\n",
       " 'D1': 16,\n",
       " 'D2': 17,\n",
       " 'D3': 18,\n",
       " 'D4': 19,\n",
       " 'D5': 20,\n",
       " 'E1': 21,\n",
       " 'E2': 22,\n",
       " 'E3': 23,\n",
       " 'E4': 24,\n",
       " 'E5': 25,\n",
       " 'F1': 26,\n",
       " 'F2': 27,\n",
       " 'F3': 28,\n",
       " 'F4': 29,\n",
       " 'F5': 30,\n",
       " 'G1': 31,\n",
       " 'G2': 32,\n",
       " 'G3': 33,\n",
       " 'G4': 34,\n",
       " 'G5': 35,\n",
       " 'H1': 36}"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict_sub_grade"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "5d9f692e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loop para substituir a string com as categorias pela representação numérica (frequência)\n",
    "for i in np.unique(arr_strings[:,3]):\n",
    "    arr_strings[:,3] = np.where(arr_strings[:,3] == i, dict_sub_grade[i], arr_strings[:,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "6991c2af",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '4', '5', '6',\n",
       "       '7', '8', '9'], dtype='<U69')"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.unique(arr_strings[:,3])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ed1a6884",
   "metadata": {},
   "source": [
    "## Pré-Processamento da Variável verification status com Binarização"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "478c1be7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['issue_date', 'loan_status', 'term_months', 'sub_grade', 'verification_status', 'url', 'addr_state'], dtype='<U19')"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Lista com os nomes das variáveis\n",
    "header_strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "2aece435",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['', 'Not Verified', 'Source Verified', 'Verified'], dtype='<U69')"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Extrair os valores únicos da variável\n",
    "np.unique(arr_strings[:,4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "fc23abb3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Usamos a binarização nesta variável\n",
    "arr_strings[:,4] = np.where((arr_strings[:,4] == '') | (arr_strings[:,4] == 'Not Verified'),0 ,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "71d612ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['0', '1'], dtype='<U69')"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Extrai os valores únicos da variável\n",
    "np.unique(arr_strings[:, 4])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "252be953",
   "metadata": {},
   "source": [
    "## Pré-Processamento da Variável url com Extração de ID"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "1360fbf7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['https://www.lendingclub.com/browse/loanDetail.action?loan_id=48010226', 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=57693261',\n",
       "       'https://www.lendingclub.com/browse/loanDetail.action?loan_id=59432726', ..., 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=50415990',\n",
       "       'https://www.lendingclub.com/browse/loanDetail.action?loan_id=46154151', 'https://www.lendingclub.com/browse/loanDetail.action?loan_id=66055249'], dtype='<U69')"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visualizar amostras dos dados\n",
    "arr_strings[:,5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "879da39e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "chararray(['48010226', '57693261', '59432726', ..., '50415990', '46154151', '66055249'], dtype='<U69')"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Extrair o id ao final de cada url\n",
    "np.chararray.strip(arr_strings[:,5], \n",
    "                   \"https://www.lendingclub.com/browse/loanDetail.action?loan_id=\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "091b6a91",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr_strings[:,5] = np.chararray.strip(arr_strings[:,5], \n",
    "                   \"https://www.lendingclub.com/browse/loanDetail.action?loan_id=\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "d1efd5e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([48010226, 57693261, 59432726, ..., 50415990, 46154151, 66055249])"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# converter o tipo para int32\n",
    "arr_strings[:, 5].astype(dtype = np.int32)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "949110f1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([48010226, 57693261, 59432726, ..., 50415990, 46154151, 66055249])"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Prece que esse id está presente na primeira coluna do conjunto de dados.\n",
    "# Vamos converter para int 32 e coparar\n",
    "arr_numeric[:, 0].astype(dtype = np.int32)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "45483ebe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.array_equal(arr_numeric[:,0].astype(dtype=np.int32), arr_strings[:,5].astype(dtype = np.int32))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "51072c95",
   "metadata": {},
   "source": [
    "Sim, é a mesma informação. Vamos então remover uma das colunas.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "1da4323a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Remover coluna 5 do array de dados.\n",
    "arr_strings = np.delete(arr_strings, 5, axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "2a23c7df",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Remover do array de nome de coluna\n",
    "header_strings = np.delete(header_strings, 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "aff9047f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['CA', 'NY', 'PA', ..., 'CA', 'OH', 'IL'], dtype='<U69')"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Nova coluna do índice 5\n",
    "arr_strings[:,5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "9cf3da43",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['issue_date', 'loan_status', 'term_months', 'sub_grade', 'verification_status', 'addr_state'], dtype='<U19')"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Nova lista de colunas\n",
    "header_strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "77b1c08e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([48010226., 57693261., 59432726., ..., 50415990., 46154151., 66055249.])"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Coluna id numérico\n",
    "arr_numeric[:, 0]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2f1ba14a",
   "metadata": {},
   "source": [
    "## Pré-Processamento da Variável address com Categorização"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "ae0e83e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['issue_date', 'loan_status', 'term_months', 'sub_grade', 'verification_status', 'addr_state'], dtype='<U19')"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "header_strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "4fcff4e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Vamos ajustar o nome das colunas\n",
    "header_strings[5] = \"state_address\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "34366298",
   "metadata": {},
   "source": [
    "https://numpy.org/doc/stabe/reference/generated/numpy.argsort.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "ba7807cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Extrai nomes e contagens\n",
    "states_names, states_count = np.unique(arr_strings[:, 5], return_counts = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "ebf68368",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Ordenaem ordem decrescente\n",
    "states_count_sorted = np.argsort(-states_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "0e994057",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array(['CA', 'NY', 'TX', 'FL', '', 'IL', 'NJ', 'GA', 'PA', 'OH', 'MI', 'NC', 'VA', 'MD', 'AZ', 'WA', 'MA', 'CO', 'MO', 'MN', 'IN', 'WI', 'CT', 'TN', 'NV', 'AL', 'LA', 'OR', 'SC', 'KY', 'KS', 'OK',\n",
       "        'UT', 'AR', 'MS', 'NH', 'NM', 'WV', 'HI', 'RI', 'MT', 'DE', 'DC', 'WY', 'AK', 'NE', 'SD', 'VT', 'ND', 'ME'], dtype='<U69'),\n",
       " array([1336,  777,  758,  690,  500,  389,  341,  321,  320,  312,  267,  261,  242,  222,  220,  216,  210,  201,  160,  156,  152,  148,  143,  143,  130,  119,  116,  108,  107,   84,   84,   83,\n",
       "          74,   74,   61,   58,   57,   49,   44,   40,   28,   27,   27,   27,   26,   25,   24,   17,   16,   10], dtype=int64))"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Imprime o resultado\n",
    "states_names[states_count_sorted], states_count[states_count_sorted]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "e09f8491",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Substituir valores ausentes por zero\n",
    "arr_strings[:,5] = np.where(arr_strings[:,5] == '', 0, arr_strings[:,5])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7ead53ee",
   "metadata": {},
   "source": [
    "Vamos separar os estados por regiões. Referência: https://www2.census.gov/geo/pdfs/maps-data/maps/references/us_regdiv.pdf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "df56320a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Separar os estados por regiões\n",
    "states_west = np.array (['WA', 'OR', 'CA' 'NV', 'ID', 'MT', 'WY', 'UT', 'CO', 'AZ', 'NM', 'HI', 'AK'])\n",
    "states_south = np.array(['TX', 'OK', 'AR', 'LA', 'MS', 'AL', 'TN', 'KY', 'FL', 'GA', 'SC', 'NC', 'VA', 'WV', 'MD', 'DE', 'DC'])\n",
    "states_midwest = np.array(['ND', 'SD', 'NE', 'KS', 'MN', 'IA', 'MO', 'WI', 'IL', 'IN', 'MI', 'OH'])\n",
    "states_east = np.array(['PA', 'NY', 'NJ', 'MA', 'VT', 'NH', 'ME', 'RI'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "e35f853e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Agora substituímos cada estado pelo id da sua região\n",
    "arr_strings[:,5] = np.where(np.isin(arr_strings[:,5], states_west), 1, arr_strings[:,5])\n",
    "arr_strings[:,5] = np.where(np.isin(arr_strings[:,5], states_south), 2, arr_strings[:,5])\n",
    "arr_strings[:,5] = np.where(np.isin(arr_strings[:,5], states_midwest), 3, arr_strings[:,5])\n",
    "arr_strings[:,5] = np.where(np.isin(arr_strings[:,5], states_east), 4, arr_strings[:,5])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "b1c155e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['0', '1', '2', '3', '4', 'CA', 'CT', 'NV'], dtype='<U69')"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Extrari os valores únicos\n",
    "np.unique(arr_strings[:, 5])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6669ed4d",
   "metadata": {},
   "source": [
    "## Convertendo o Array\n",
    "Nosso array de strings agora é um array numérico. Vamos ajustar o tipo de dados."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78c36927",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
