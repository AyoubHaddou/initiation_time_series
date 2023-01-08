# Time-Series: objets perdus SNCF

## Contexte du projet: 
Vous avez été embauché comme data-scientist à la SNCF.

Votre manager vous demande de travailler sur un sujet crucial au niveau de la satisfaction client, la gestion des objets trouvés. C'est forcément un point positif pour le groupe de proposer une pretation de qualité sur ce service mais cela a également un cout. Il faut donc s'assurer de prévoir au mieux le volume d'objets trouvés pour faire correspondre exactement les ressources humaines qui seront chargées de les traiter.

​

Votre Manager vous demande donc de faire un POC, pour voir ce qu'il est possible de faire sur le sujet. Pour le moment vous ne devrez pas fournir d'applications ni d'interfaces graphiques mais simplement des modèles prédictifs. De plus, vous ne travaillerez dans un premier temps que sur les gares lilloises.

****************************************************************

* Api: https://ressources.data.sncf.com/explore/dataset/objets-trouves-restitution/table/?sort=date&refine.gc_obo_gare_origine_r_name=Lille+Europe&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJiYXIiLCJmdW5jIjoiQ09VTlQiLCJjb2xvciI6InJhbmdlLWN1c3RvbSIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlfV0sInhBeGlzIjoiZGF0ZSIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6InllYXIiLCJzb3J0IjoiIiwic2VyaWVzQnJlYWtkb3duIjoiZ2Nfb2JvX3R5cGVfYyIsInNlcmllc0JyZWFrZG93blRpbWVzY2FsZSI6Im1vbnRoIiwic3RhY2tlZCI6Im5vcm1hbCIsImNvbmZpZyI6eyJkYXRhc2V0Ijoib2JqZXRzLXRyb3V2ZXMtcmVzdGl0dXRpb24iLCJvcHRpb25zIjp7InNvcnQiOiJkYXRlIiwicmVmaW5lLmdjX29ib19nYXJlX29yaWdpbmVfcl9uYW1lIjoiTGlsbGUgRXVyb3BlIn19fV0sInRpbWVzY2FsZSI6IiIsImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9
* Import des données de cet API pour la gare Lille Europe 2016-2023 sur le fichier models_lille_europe.py (Base de donnée SQLlite)
* Visualisation et création de modele de time series sur le notebook (.ipynb)

****************************************************************