
<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1069601291929665566/1212717428300320850/icon.png?ex=65f2da1e&is=65e0651e&hm=d9b1c5639f78c05b96de997f00ae919dc521c1423cbec9078cbd1d2bb4083521&" alt="MediMate" height="50 px">
</p>

# Project Documentation

This project is linked to {link} and was undertaken to gather additional data for the project, specifically in the following areas:

## Data on Allergies

The collection of data on allergies was a crucial aspect of this project. Despite our thorough research and discussions with Mr. Aimé, we found it challenging to freely access relevant information in this field. However, Mr. Aimé recommended a website providing the leaflets for all medications ([https://base-donnees-publique.medicaments.gouv.fr/affichageDoc.php?specid=68721786&typedoc=R](https://base-donnees-publique.medicaments.gouv.fr/affichageDoc.php?specid=68721786&typedoc=R)). We utilized a Python script to extract information between sections 4.3 and 4.4. Using natural language processing techniques, we were able to identify potential allergies and classify medications according to associated allergies in a JSON file.

## Data on Contraindications by User Type

Collecting data on specific contraindications for certain types of users was also a major challenge of the project. Due to the lack of freely accessible information on the Internet, we performed scraping of the same website ([https://base-donnees-publique.medicaments.gouv.fr/affichageDoc.php?specid=68721786&typedoc=R](https://base-donnees-publique.medicaments.gouv.fr/affichageDoc.php?specid=68721786&typedoc=R)). This time, our analysis focused on section 4.4, "Special warnings and precautions for use," of each medical notice. Linguistic analysis of the collected data allowed us to identify relevant information (such as "child," "pregnant," "breastfeeding," "newborn," "infant," "nursed"). This information facilitated the classification of medications, thereby alerting our users to associated risks.

## Data on Contraindications Between Medications

To gather actionable data regarding contraindications between medications, we relied on this PDF: Thesaurus of Drug Interactions - September 2023. The data extraction method is based on the analysis of font sizes used in the document: the names of the active ingredients appear in size 10, while the mentions of active ingredients not to be associated are indicated in size 8. A Python script was developed to read the PDF and extract relevant information based on font size. 

## Copyright Notice

All code developed for this project is the property of the individuals who worked on the project. Unauthorized use, duplication, or distribution of the code without explicit permission from the copyright holders is strictly prohibited. This copyright notice serves to protect the intellectual property of the developers and ensure that their contributions are recognized and respected.

## Authors

- [@Romain GOURAUD](https://github.com/Ziroles)
- [@Nathan FERRY](https://github.com/GSBlackdragon)
- [@Sylvain BAUDOUIN](https://www.github.com/syysy)
- [@Lilian DELHOMMEAU](https://github.com/Redly0n)

