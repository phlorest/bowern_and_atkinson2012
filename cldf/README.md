<a name="ds-genericmetadatajson"> </a>

# Generic Generic

**CLDF Metadata**: [Generic-metadata.json](./Generic-metadata.json)

**Sources**: [sources.bib](./sources.bib)

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Bowern C & Atkinson QD. 2012. Computational phylogenetics and the internal structure of Pama-Nyungan. Language, 88(4), 817-845.
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Generic](http://cldf.clld.org/v1.0/terms.rdf#Generic)
[dc:identifier](http://purl.org/dc/terms/identifier) | https://doi.org/10.1353/lan.2012.0081
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/D-PLACE/dplace-tree-bowern_and_atkinson2012
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/D-PLACE/dplace-tree-bowern_and_atkinson2012/tree/30aec94">D-PLACE/dplace-tree-bowern_and_atkinson2012 30aec94</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v4.4">Glottolog v4.4</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.8.10</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | bowern_and_atkinson2012
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

The LanguageTable lists the taxa, i.e. the leafs of the phylogeny, mapped to languoids.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 194


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 
`Glottolog_Name` | `string` | 

## <a name="table-treescsv"></a>Table [trees.csv](./trees.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 1


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Nexus_File](http://purl.org/dc/terms/relation) | `string` | The newick representation of the tree, labeled with identifiers as described in LanguageTable, is stored in the TREES block of the Nexus file specified here. (See https://en.wikipedia.org/wiki/Nexus_file)
`rooted` | `boolean` | Whether the tree is rooted (true) or unrooted (false) (or no info is available (null))
`type` | `string` | Whether the tree is a summary (or consensus) tree, i.e. can be analysed in isolation, or whether it is a sample, resulting from a method that creates multiple trees
`method` | `string` | Specifies the method that was used to create the tree
`scaling` | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)

