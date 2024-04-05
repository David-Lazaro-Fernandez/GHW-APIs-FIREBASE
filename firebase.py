import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("authkey.json")
firebase_admin.initialize_app(cred)

# Create a new document in Firestore
def create_document(collection : str, document_data: dict):
    db = firestore.client()
    doc_ref = db.collection(collection).document()
    doc_ref.set(document_data)
    print('Document created with ID:', doc_ref.id)

# Usage example
create_document('users', {'name': 'John Doe', 'email': 'johndoe@example.com'})

