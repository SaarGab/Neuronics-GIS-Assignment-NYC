# Neuronics-GIS-Assignment-NYC

Important: Before running the code, please do the following:
1. Open a new ArcGIS Pro project by clicking the "Map" template when the initial screen of the program opens.
2. In the code, change the value of the variable 'project_path' to the path of the .aprx file inside your new project (the .aprx file is created automatically upon the creation of your new project).
3. In the code, change the value of the variable 'gdb_path' to the path of the gdb file inside your new project (the gdb file is created automatically upon the creation of your new project).
4. Before running the code, change your python interpreter's path to the path where you downloaded ArcGIS Pro, and then to \bin\Python\envs\arcgispro-py3\python.exe (This interpreter comes with the ArcGIS Pro program).

I used the environment ArcGIS Pro with the ArcPy Python library for this project.

The code in this project does the following:

A. Loads and displays an orthophoto layer of New York City to the project's map. Source of the orthophoto layer used: https://maps.nyc.gov/xyz/1.0.0/photo/2018/{z}/{x}/{y}.png8

Note: The url does not work on the web, but it does show the orthophoto on the map.

Before and after images:

<img width="1047" height="728" alt="image" src="https://github.com/user-attachments/assets/ced4e71b-8e23-4444-a169-138c1412c755" />

<img width="1097" height="730" alt="image" src="https://github.com/user-attachments/assets/51e05327-28ef-42be-ac01-83a311f082fc" />

A zoom-in for pixel detail:

<img width="1610" height="730" alt="image" src="https://github.com/user-attachments/assets/255470b9-0a06-4c83-99b3-6cbfc3fa2b97" />

<img width="1615" height="730" alt="image" src="https://github.com/user-attachments/assets/57080b58-3cae-4d40-97e1-4c9ee1301e60" />

B. Adds the following vector layers on top of the orthophoto:

A polygon layer called "Buildings_NYC" of all the buildings in New York City, source: https://services2.arcgis.com/IsDCghZ73NgoYoz5/ArcGIS/rest/services/NYC_Building_Footprint/FeatureServer 

<img width="1616" height="731" alt="image" src="https://github.com/user-attachments/assets/83ca5555-f2d1-41f2-bf15-b09cb283c03b" />

A line layer called "Roads_NYC" of all the roads (streets, bridges, etc.) in New York City, source: https://services5.arcgis.com/GfwWNkhOj9bNBqoJ/ArcGIS/rest/services/DCM_Street_Center_Line/FeatureServer
<img width="1617" height="730" alt="image" src="https://github.com/user-attachments/assets/43db108e-4a7f-4b32-adce-fc5319abbb58" />

C. Defines the following queries:

A query for the "Buildings_NYC" polygon layer: "HEIGHTROOF is greater than 500".

A query for the "Roads_NYC" line layer: "Borough is equal to Manhattan".

D. Identify-On-Click: Already an add-in of the application:

<img width="1082" height="718" alt="image" src="https://github.com/user-attachments/assets/a9f692c7-8054-4c9f-b83a-5c9a5fcd2e79" />

E. Exports the filtered features from section C:

Exports the first query in section C to a new polygon layer called "Tallest_Buildings_In_NYC":
<img width="1905" height="730" alt="image" src="https://github.com/user-attachments/assets/ca014245-4f8b-4cb1-afbd-536ba4c71f60" />

Exports the second query in section C to a new line layer called "Roads_In_Manhattan":

<img width="1461" height="727" alt="image" src="https://github.com/user-attachments/assets/88835ef7-a6a4-40c0-a04d-40696791d8b4" />

The total time the assignemnt took me was 2 hours. I completed all of the tasks (both the required task and the optional tasks).
