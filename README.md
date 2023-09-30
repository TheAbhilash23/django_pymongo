<h1> Welcome to django_pymongo project</h1>

<h3> The project aims to create a django application with the use of PyMongo library which is the official library for synchronous MongoDB operations</h3>

<br>
This project is intended to create a simple absctraction over PyMongo APIs to create an Object Docmument Mapping,
for a better developer experience for someone coming from SQL based ORM based development background.

<h4>
With this project you will learn

</h4>

<br>
<table>
    <th>Sr. No.</th> <th>Phase</th> <th>Details</th> <th>Status</th>
    <tr> <td>1</td> <td>0.0.1</td> <td>Generic Field Type: MongoField, Taking any number of kwargs but only the ones mentioned in the "$jsonSchema" documentation. If collection is not created it will create collection with schema validation as defined in models.py, If it is already present then it will call 'collMod' command to modify the collection validator.</td> <td> DONE</td></tr>
    <tr> <td>2</td> <td>0.0.2</td> <td>Create nested fields and apply validations their validations.</td><td>Active</td></tr>
    <tr> <td>3</td> <td>0.0.3</td> <td>Create Migration model in django sqlite3 database and track the changes. </td> <td>Not Started Yet</td></tr>
</table>

<h2> PS:: Djongo is not used in this project.</h2>
