{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled4.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMeK1XXokHsyak0tFcBIOmr",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JorgeTricarico/Py-Procesamiento-y-exploracion-de-datos/blob/main/Statistics.%20Calculo%20de%20Media%20y%20Mediana.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N4nrFK_VGY6M",
        "outputId": "817b3035-2e46-4062-ad7f-017d84637eea"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Lista desordenada: [0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 3, 3, 3, 4, 4]\n",
            "\n",
            "Lista ordenada: [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4]\n",
            "\n",
            "Media de lista: 1.7\n",
            "Mediana de lista: 2.0\n"
          ]
        }
      ],
      "source": [
        "import statistics as st\n",
        "\n",
        "#Funcion para lista con elementos repetidos\n",
        "def nuevaLista(listaResumida):\n",
        "  lista = []\n",
        "  for a in listaResumida:\n",
        "    for i in range(a[1]):\n",
        "      lista.append(a[0])\n",
        "  return lista\n",
        "\n",
        "#Lista resumida [(valor, frecuencia), (valor, frecuencia)]\n",
        "\n",
        "listaResumida = [(0,4),(2,6),(1,5),(3,3),(4,2)]\n",
        "\n",
        "#Convertir a lista normal\n",
        "lista = (nuevaLista(listaResumida))\n",
        "\n",
        "print(\"Lista desordenada: \" + str(lista) + \"\\n\")\n",
        "\n",
        "#Ordenar lista\n",
        "lista.sort()\n",
        "print(\"Lista ordenada: \" + str(lista) + \"\\n\")\n",
        "\n",
        "#Calculo de Media y Mediana\n",
        "print(\"Media de lista: \" + str(st.mean(lista)))\n",
        "print(\"Mediana de lista: \" + str(st.median(lista)))"
      ]
    }
  ]
}