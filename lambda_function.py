import boto3
def lambda_handler(event, context):
    type = event['type'];
    id =event['id'];
    # this will create dynamodb resource object and
    # here dynamodb is resource name
    client = boto3.resource('dynamodb')
    
    # this will search for dynamoDB table 
    # your table name may be different
    table = client.Table("votting_table")
    
    if type=="get":
        db_value=table.get_item(Key={'id': id})['Item']['Count']
        resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": {
            "Count": db_value
        }
        }
    else:
    
        db_value=table.get_item(Key={'id': id})['Item']['Count']
        table.put_item(Item= {'id': id,'Count':  db_value+1})
        new_value=table.get_item(Key={'id': id})['Item']['Count']
                    
        resp = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
            },
            "body": {
                "Count": new_value
            }
        }
    return resp

    


