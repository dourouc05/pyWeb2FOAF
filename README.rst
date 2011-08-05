pyWeb2FOAF
==========

This project is architectured as follows: 
 - A Vocabularies folder, to hold all vocabularies you can dream of; each of them will be able to output its content as RDF triples. E.g. the FOAF vocabulary will have many options to store what the FOAF vocabulary can (name, title, but also geographic informations based on other vocabularies). 
 - An Output folder, to hold all the output engines you can imagine; they'll take the RDF triples from the vocabularies to what they're up to. 