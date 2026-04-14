OAuth-2.0 : -
<img width="400" height="500" alt="image" src="https://github.com/user-attachments/assets/cf5bf7cc-66e4-4ad0-a6ad-6f5770bac17e" />


🧠 Key learnings: 
Registered an OAuth client
*How to use Postman to test the complete OAuth 2.0 Authorization Code Flow
How to call a protected API using the Access Token
Exchanged a code for an access token
Client ID / Secret usage
Token-based authentication
Testing secured APIs using Postman

POSTMAN LINK: https://ankitkumar-2356106.postman.co/workspace/PYATB5X~6c73ff5a-90de-444d-a0c7-b5326cebbe4c/collection/44694445-2c780b0b-89ec-45f8-aba6-07f7dc7fc609?action=share&source=copy-link&creator=44694445

🧠 Key Testing Learnings
Concept	What to Test
Token Validity	Tokens expire; check expiry time
Scope Behavior	Try using token with less/more scopes
Unauthorized Access	Try API without token → should get 401 Unauthorized
Token Reuse	Use the same token again → should still work until expired

JSON Schema : -

Key Learnings :
What JSON Schema is
Step-by-step guide in Postman
How to test schema validation

Step	Task	Description
1	Create API request - Use https://reqres.in/api/users/2
2	Write Schema - Define expected structure
3	Add in Tests tab - Use pm.response.to.have.jsonSchema(schema)
4	Run test - Validate schema
