# -*- coding: utf8 -*-


''' 
        Fonction de creation d'un qcm 
        prend en paramettre un string : le nom du fichier que l'on souhaite créer
'''
def creation_qcm(nom):
    from lxml import etree
    try:
        #On ouvre (ou crée) le fichier xml pour travailler avec
        with open(nom,'w') as fichier:
                
                idqcm = input("Entrez l'id du qcm:")
                formation = input("Entrez le nom de la formation:")
                matiere = input("Entrez le nom de la matiere:")

                #En-tête du fichier xml
                fichier.write('<?xml version="1.0" encoding="UTF_8"?>\n')
                fichier.write('<qcm xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="qcmSchema.xsd" idqcm="'+ idqcm +'" formation="'+ formation +'" matiere="'+ matiere +'">\n')
                q_num = 1 #numero de question init a 1
                q_verif = '0'
                #creation de plusieurs questions
                while q_verif == '0':
                        #creation de la balise question
                        question = etree.Element('question')
                        #initialisation de l'attribut 'num' de question
                        question.set("num",str(q_num))
                        #creation d'une sous-balise 'intitule'
                        intitule = etree.SubElement(question,'intitule')
                        #ajoute la question
                        intitule.text = input("Entrez l'intitulé de votre question :")
                        r_num = 1 #numero de reponse init a 1
                        r_verif = '0'
                        #creation de plusieurs réponses
                        while r_verif == '0':
                                #creation d'une balise 'reponse'
                                reponse = etree.SubElement(question,'reponse')
                                #initialisation de l'attribut 'numRep' de reponse
                                reponse.set("numRep", str(r_num))
                                #ajout de la reponse
                                reponse.text = input("Entrez votre reponse: ")
                                r_num += 1 #numero de reponse +1
                                r_verif = input("Voulez-vous entrez une autre réponse? (0: oui, 1: non):")
                        q_verif = input("Voulez-vous entrez une autre question? (0: oui, 1: non):")
                        #On écrit tous les éléments précédemment déclarer dan un fichier
                        fichier.write(etree.tostring(question,pretty_print=True).decode('utf-8'))
                        #numero de question +1
                        q_num = q_num+1
     
                fichier.write('</qcm>\n') #fermeture de la balise qcm
    except IOError:
        print('Problème rencontré lors de l\'écriture ...')
        exit(1)



# Programme principal #
#nom= input("entrez le nom de votre xml:")
#creation_qcm(str(nom)+".xml")
creation_qcm("qcm1.xml")
