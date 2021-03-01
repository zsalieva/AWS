import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = "basicSongsTable"

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name="us-east-1")

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)
# Use the DynamoDB client get item method to get a single item
# response = table.get_item(
#     TableName=TABLE_NAME,
#     Key={
#         'artist': 'Arturus Ardvarkian',
#         'song': 'Carrot Eton'
#     }
# )
#print(response['Item'])

# The client's response looks like this:
# {
#  'artist': {'S': 'Arturus Ardvarkian'},
#  'id': {'S': 'dbea9bd8-fe1f-478a-a98a-5b46d481cf57'},
#  'priceUsdCents': {'S': '161'},
#  'publisher': {'S': 'MUSICMAN INC'},
#  'song': {'S': 'Carrot Eton'}
# }

# Use the DynamoDB client to query for all songs by artist Arturus Ardvarkian
# response = dynamodb_client.query(
#     TableName=TABLE_NAME,
#     KeyConditionExpression='artist = :artist',
#     ExpressionAttributeValues={
#         ':artist': {'S': 'Arturus Ardvarkian'}
#     }
# )
# print(response['Items'])
# Use the Table resource to query for all songs by artist Arturus Ardvarkian
# response = table.query(
#   KeyConditionExpression=Key('artist').eq('Arturus Ardvarkian')
# )
# print(response['Items'])
# Use the DynamoDB client query method to get songs by artist Arturus Ardvarkian
# that start with "C"
# response = dynamodb_client.query(
#     TableName=TABLE_NAME,
#     KeyConditionExpression='artist = :artist AND begins_with ( song , :song )',
#     ExpressionAttributeValues={
#         ':artist': {'S': 'Arturus Ardvarkian'},
#         ':song': {'S': 'B'}
#     }
# )
# print(response['Items'])
# response = table.query(
#   KeyConditionExpression=Key('artist').eq('Arturus Ardvarkian') & Key('song').begins_with('B')
# )
# print(response['Items'])

# Use the DynamoDB client query method to get songs by artist Arturus Ardvarkian
# that have a song attribute value BETWEEN 'D' and 'Bz'
response = dynamodb_client.query(
    TableName=TABLE_NAME,
    KeyConditionExpression='artist = :artist AND song BETWEEN :songval1 AND :songval2',
    ExpressionAttributeValues={
        ':artist': {'S': 'Arturus Ardvarkian'},
        ':songval1': {'S': 'Bz'},
        ':songval2': {'S': 'D'}
    }
)
print(response['Items'])