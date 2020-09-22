# NucMatDatafication

Welcome!

Here you can find the publicly available python codes created for the master's thesis "Datafication of material mechanisms in nuclear applications". The three Excel files are eiter the output of the python functions or manually gathered SS316 database. 
* collect_articles.py contains the functions to download scientific publications of interest as XML files,
* classify_files.py extracts the DOI-number of files depending on a query, e.g. REGEX of metallic alloys (output: Files_classifications.xlsx),
* records_tables.py counts the appearences of REGEX entities in the classified XML-files (output: Entities_in_tables.xlsx),
* SS316_database.xlsx is the resulting collection of material data of the austenitic stainless steel SS316,
* material_mechanism_map.py plots the derived material mechanisms map of SS316 based on the collected database before. 


## Datafication of material mechanisms in nuclear applications

### Abstract
Material selection relies on the information of feasible materials, especially in nuclear applications, where material tests are complex and require special attention to safety. A more profound material selection decision one can make with the increasing availability of the information. Peer-reviewed scientific articles present a vital source with high quality. 

This thesis studies the possibilities of information extraction and information summarization of the properties of metallic alloys. The following challenges for this purpose were identified: Fully automated information extraction by machine learning algorithms will become possible with the creation of material science related corpus for natural language processing. Also, an automated plot digitizer would excavate enormous amounts of material data. With the increasing size of the database, its clarity decreases. So, the contained information should be summarized comprehensibly. The approach presented in this thesis is a material mechanism map. Based on the idea of Ashby maps, material mechanism maps visualize areas of material property changes under specific environmental conditions. As an example, a material mechanism map for the austenitic steel SS316, serving as nuclear fuel-cladding material, was computed. The map contains information about material hardening, recovery, irradiation embrittlement, swelling, creep, and precipitation formation depending on the irradiation dose and the homologous temperature.

