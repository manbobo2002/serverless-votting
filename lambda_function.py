def lambda_handler(event, context):
   number = event['value'];
   count = int (number) + 1;
   resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": {
            "Count": count
        }
    }
   return resp