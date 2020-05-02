# ProjectUG3
Code from 3rd year project

In this project we used a set of taxi mobility traces from San Francisco and created a new set of busstops through K-Means Clustering in QGIS.

The steps were:
  - PreProcess data to gain list of PD Points
  - Perform Clustering with QGIS
  - Use the clustered data from QGIS for evaluation
  
The PreProcessing was as Follows:
  - cabspottingdata/ contains the set of cabs and their mobility traces
    - We executed PDDataClean.py to obtain the PD Points
    - We executed PDAreaDataClean.py to remove Points not in the designated Geo area
    - We executed OutlierReduction.py to remove outlying points
  - PDAreaCabDataOutlierFree.csv now contains all valid points
    - We executed UrbanRuralPDAreaDataClean.py to split into our designated Urban and Rural areas
  - Urban.csv and Rural.csv are now the two datasets to perform clustering on
  
The datasets were then clustered in QGIS for varying levels of K(For purpose of saving space only the final choices have been uploaded)

In BusStops/:
  - The Clusters folder held the output files from QGIS holding each point
    - We executed URBusStopCreator.py to create our new set of Bus stops
    - We executed URBusStopErrorAnalysis.py to analyze our stops sets error and
    - We executed BusStopDistanceAnalysis.py to analyze our interstop distance on distance matrix from QGIS

We had now decided on our final stop set 
    - We executed RouteEvaluation.py to find the uncovered points
  - finalChoiceCorrected.csv displays the points ot covered by our stops
