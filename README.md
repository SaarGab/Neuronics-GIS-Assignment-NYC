# Neuronics-GIS-Assignment-NYC

Important: Before running the code, please do the following:
1. Open a new ArcGIS Pro project by clicking the "Map" template when the initial screen of the program opens.
2. In the code, change the value of the variable 'project_path' to the path of the .aprx file inside your new project (the .aprx file is created automatically upon the creation of your new project).
3. In the code, change the value of the variable 'gdb_path' to the path of the gdb file inside your new project (the gdb file is created automatically upon the creation of your new project).
4. Before running the code, change your python interpreter's path to the path where you downloaded ArcGIS Pro, and then to \bin\Python\envs\arcgispro-py3\python.exe (This interpreter comes with the ArcGIS Pro program).

I used the environment ArcGIS Pro with the ArcPy Python library for this project.

The code in this project does the following:

A. Loads and displays an orthophoto layer of New York City to the project's map. Source of the orthophoto layer used: https://tiles.arcgis.com/tiles/yG5s3afENB5iO9fj/arcgis/rest/services/NYC_Orthos_2024/MapServer

Before and after images:

<img width="385" height="387" alt="image" src="https://github.com/user-attachments/assets/ade078aa-e4a3-4ca1-a6b8-035e6edf924e" />

<img width="391" height="365" alt="image" src="https://github.com/user-attachments/assets/e01e246e-5fd6-4a3b-aa29-257756a15373" />

Zoom in for pixel detail:

<img width="1103" height="750" alt="image" src="https://github.com/user-attachments/assets/b0eaf748-6185-4f0f-8197-c0b94ecf2dab" />

<img width="1137" height="738" alt="image" src="https://github.com/user-attachments/assets/7c60c21c-a50a-497d-beb4-2e061e39c439" />

B. Adds the following vector layers on top of the orthophoto:

A polygon layer called "Buildings_NYC" of all the buildings in New York City, source: https://services2.arcgis.com/IsDCghZ73NgoYoz5/ArcGIS/rest/services/NYC_Building_Footprint/FeatureServer 

<img width="1897" height="730" alt="image" src="https://github.com/user-attachments/assets/93e6d7a7-5f72-458b-9353-9ead8037912d" />

A line layer called "Roads_NYC" of all the roads (streets, bridges, etc.) in New York City, source: https://services5.arcgis.com/GfwWNkhOj9bNBqoJ/ArcGIS/rest/services/DCM_Street_Center_Line/FeatureServer

<img width="1102" height="752" alt="image" src="https://github.com/user-attachments/assets/0a57df3c-550c-4e23-931e-b0a18bd9815c" />

C. Defines the following queries:

A query for the "Buildings_NYC" polygon layer: "HEIGHTROOF is greater than 500".

A query for the "Roads_NYC" line layer: "Borough is equal to Manhattan".

D. Identify-On-Click: Already an add-in of the application:

<img width="985" height="707" alt="image" src="https://github.com/user-attachments/assets/c0b85189-e817-411d-9b5f-61e81bae3ac1" />

E. Exports the filtered features from section C:

Exports the first query in section C to a new polygon layer called "Tallest_Buildings_In_NYC":

<img width="1898" height="730" alt="image" src="https://github.com/user-attachments/assets/4d0bdb44-cc1b-4d0e-aea5-be3a8b21fed1" />

Exports the second query in section C to a new line layer called "Roads_In_Manhattan":

<img width="1422" height="727" alt="image" src="https://github.com/user-attachments/assets/c620e99f-2681-40ec-9f4d-a7d542b5585d" />

The total time the assignemnt took me was 2 hours. I completed all of the tasks (both the required task and the optional tasks).
