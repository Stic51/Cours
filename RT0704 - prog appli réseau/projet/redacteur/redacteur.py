# -*- coding: utf8 -*-


# Fonction de creation d'un qcm  #
def creation_qcm(nom):
    from lxml import etree
    
    idqcm = input("Entrez l'id du qcm:")
    formation = input("Entrez le nom de la formation:")
    matiere = input("Entrez le nom de la matiere:")

    verif = input("Voulez-vous entrez une question? (0: oui, 1: non):")
    #while (verif == 0):
    question = etree.Element('question')
    inti = input("Entrez l'intitulé de votre question :")
    intitule = etree.SubElement(question,inti)
    #i = input("Entrez le nombre de réponse possible (min 2)")

    #while(i<2):
    #    i = input("Entrez le nombre de réponse possible (min 2)")
    #for j in range(1,i) :
    #    rep[j] = input("Entrez votre reponse n°"+j+":")


    try:
        #On ouvre (ou crée) le fichier xml pour travailler avec
        with open(nom,'w') as fichier:
                #En-tête du fichier xml
                fichier.write('<?xml version="1.0" encoding="UTF_8"?>\n')
                fichier.write('<qcm xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="qcmSchema.xsd" id="'+ idqcm +'" formation="'+ formation +'" matiere="'+ matiere +'">\n')
                #On écrit tous les éléments précédemment déclarer
                fichier.write(etree.tostring(question,pretty_print=True).decode('utf-8'))
    except IOError:
        print('Problème rencontré lors de l\'écriture ...')
        exit(1)




# Programme principal #
nom= input("entrez le nom de votre xml:")
creation_qcm(nom+".xml")
