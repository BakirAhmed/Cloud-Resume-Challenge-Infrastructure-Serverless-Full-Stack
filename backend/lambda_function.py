"""
Lambda - Compteur de visiteurs du Cloud Resume Challenge.
Incrémente et retourne le nombre de visites stockées dans DynamoDB.
"""
import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Content-Type": "application/json",
}


def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={"id": "visitor_count"},
            UpdateExpression="ADD visits :inc",
            ExpressionAttributeValues={":inc": 1},
            ReturnValues="UPDATED_NEW",
        )
        count = int(response["Attributes"]["visits"])

        return {
            "statusCode": 200,
            "headers": HEADERS,
            "body": json.dumps({"visits": count}),
        }
    except Exception as exc:  # pragma: no cover
        return {
            "statusCode": 500,
            "headers": HEADERS,
            "body": json.dumps({"error": str(exc)}),
        }
