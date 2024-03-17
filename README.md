Project Management API Documentation
Base URL: https://benmore-project.onrender.com



Authentication:
The API does not require authentication for accessing endpoints.



Projects Endpoints:
List Projects

Endpoint: GET /projects/

Description: Retrieves a list of all projects.
Request Body: None
[ { "id": 1, "name": "Project 1", "description": "Description of Project 1", "due_in": "2 days", "tasks_total": 10, "tasks_completed": 5, "members": [1, 2] }, { "id": 2, "name": "Project 2", "description": "Description of Project 2", "due_in": "1 day", "tasks_total": 8, "tasks_completed": 3, "members": [2, 3] }, ...]
Frontend Integration: Use this endpoint to fetch the list of projects to display on the frontend dashboard.


Create Project

Endpoint: POST /projects/

Description: Creates a new project.
{ "name": "New Project", "description": "Description of the new project", "due_in": "3 days", "tasks_total": 15, "members": [1, 3]}
{ "id": 3, "name": "New Project", "description": "Description of the new project", "due_in": "3 days", "tasks_total": 15, "tasks_completed": 0, "members": [1, 3]}
Frontend Integration: Use this endpoint to allow users to create new projects via a form in the frontend.

Retrieve Project

Endpoint: GET /projects/{project_id}/

Description: Retrieves details of a specific project.
Request Body: None
{ "id": 1, "name": "Project 1", "description": "Description of Project 1", "due_in": "2 days", "tasks_total": 10, "tasks_completed": 5, "members": [1, 2]}
Frontend Integration: Use this endpoint to fetch detailed information about a specific project for viewing/editing purposes.


Update Project

Endpoint: PUT /projects/{project_id}/

Description: Updates details of a specific project.
{ "name": "Updated Project 1", "description": "Updated description of Project 1", "due_in": "5 days", "tasks_total": 12, "members": [1, 3]}
{ "id": 1, "name": "Updated Project 1", "description": "Updated description of Project 1", "due_in": "5 days", "tasks_total": 12, "tasks_completed": 5, "members": [1, 3]}
Frontend Integration: Use this endpoint to allow users to update project details via a form in the frontend.

Delete Project

Endpoint: DELETE /projects/{project_id}/

Description: Deletes a specific project.
Request Body: None
Response Body: None
Frontend Integration: Use this endpoint to allow users to delete a project from the frontend.




Tasks Endpoints:
(Endpoints follow a similar structure to Projects endpoints)



Members Endpoints:
(Endpoints follow a similar structure to Projects endpoints)


