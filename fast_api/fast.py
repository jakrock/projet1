from fastapi import FastAPI,Request
from fastapi.responses import FileResponse
import pymongo

client=pymongo.MongoClient('localhost',27017)
db=client["finale"]
# collection5=db["data supprimer"]
# collection6=db["data supprimer1"]
#collection6=db["pure_valubet"]

app = FastAPI()

@app.get("/indexsurebet")
async def read_root2():
    return FileResponse("/home/romualdjja/projet1/projet1/fast_api/templates/indexsurebet.html")





@app.get("/")
async def read_root():
    return FileResponse("/home/romualdjja/projet1/projet1/fast_api/templates/index.html")


# @app.get("/mini")
# async def read_root1():
#     return FileResponse("/home/romualdjja/projet1/projet1/fast_api/templates/indexmini.html")


@app.get("/item/{item_id}")
async def valueApi(item_id:str):



    db_match_odd=client["finale"]
    collection1=db_match_odd["Match Odds"]
    #data=list(collection1.find({},{"_id":0}))
    collection2=db_match_odd[item_id]
    collection3=db_match_odd[item_id]
    collection4=db_match_odd[item_id]
    result1=list(collection4.find({},{"_id":0}))
    #result2=list(collection5.find({},{"_id":0}))
    #data=filter(lambda x :x["id"] not in [ i["id"] for i in result2],result1)
    return list(collection4.find({},{"_id":0}))

@app.post("/item/retour")
async def create_item(request: Request):
    # Récupérer les données brutes du corps de la requête
    

    db=client["finale"]
    collection5=db["data supprimer"]
    item_data = await request.body()

    import json

    item_data_json = item_data.decode()  # Décodez les données en tant que chaîne JSON
    item_data_dict = json.loads(item_data_json)  # Convertissez la chaîne JSON en un dictionnaire Python

    result = collection5.insert_one(item_data_dict[0])

    # Traiter les données ou effectuer les opérations souhaitées
    # ...

    return {"message": "Item created successfully"}


@app.post("/item/retour/surebet")
async def create_item1(request: Request):
    # Récupérer les données brutes du corps de la requête
    
    db=client["finale"]
    collection6=db["data supprimer1"]
    item_data = await request.body()

    import json

    item_data_json = item_data.decode()  # Décodez les données en tant que chaîne JSON
    item_data_dict = json.loads(item_data_json)  # Convertissez la chaîne JSON en un dictionnaire Python

    result = collection6.insert_one(item_data_dict[0])

    # Traiter les données ou effectuer les opérations souhaitées
    # ...

    return {"message": "Item created successfully"}


# @app.get("/mini")
# async def datapi(item_id1:str):
#     db=client["finale"]
#     collection6=db['valuebet']
#     data=list(collection6.find({},{"_id":0}))
#     newdata=list(filter(lambda x:x["valeur"]<1.89,data))
#     return newdata
   

@app.get("/mini")
async def read_root3():
    return FileResponse("/home/romualdjja/projet1/projet1/fast_api/templates/indexmini.html")


@app.get("/mini1/mini2")
async def datapi():
    db=client["finale"]
    collection6=db['valuebet']
    data=list(collection6.find({},{"_id":0}))
    newdata=list(filter(lambda x:x["valeur"]<2.21,data))
    return newdata
   

@app.get("/pre_match")
async def read_root4():
    return FileResponse("/home/romualdjja/projet1/projet1/fast_api/templates/pre_match.html")






@app.get("pre_match/value")
async def datapi1():
    db=client["finale_pre"]
    collection6=db['valuebet']
    data=list(collection6.find({},{"_id":0}))
    #newdata=list(filter(lambda x:x["valeur"]<2.21,data))
    return data
   



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)
