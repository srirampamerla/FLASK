### put and delete -HTTP verbs
### Working with API's--JSON

from flask import Flask,jsonify,request

app=Flask(__name__)

##Intial Data in my to do lisst

items=[
    {"id":1,"name":"Item 1","description":"This is item 1"},
    {"id":2,"name":"Item 2","description":"This is item 2"}
]

@app.route('/')
def home():
    return "Welcome to the sample to DO List APP"

##GET : Retrieve all the items

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

## Get : Reterieve a specific item by id

@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

## Post: create the new task

@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    new_item={
        "id":items[-1]["id"] + 1 if items else 1,
        "name":request.json['name'],
        "description":request.json["description"]
    }
    items.append(nw_item)
    return jsonify(new_item)

# put: Update the existing item

@app.route('/items<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])
    return jsonify(item)

#Delete Item
@app.route('/items<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    item=[item for item in items if item["id"]!=item_id]
    return jsonify({"result":"Item deleted"})



if __name__=="__main__":  # Execution basically starts from Here
    app.run(host="0.0.0.0",debug=True,port=5002) # It will run with this