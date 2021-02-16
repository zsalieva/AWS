
import boto3, json
session = boto3.Session(profile_name='development')
#global variables for region_name
east = 'us-east-1'
west = 'us-west-2'
# declaring ec2East variable to use ec2 session.client
ec2East = session.client('ec2', region_name = east)
ec2West = session.client('ec2', region_name = west)

def getEC2withTags():
    ec2IDs = []
    response = ec2East.describe_instances(
        Filters=[
            {
                'Name': 'tag:TechnicalTeam',
                'Values': ['DevOps',]

            },
            {
                'Name': 'instance-state-name',
                'Values': ['running',]
                
            }
        ],
    )


    a = response['Reservations']
    for i in a:
        #print(i['Instances'])
          for j in i['Instances']: 
            ec2IDs.append(j['InstanceId'])

    return  ec2IDs

onlyRunning=getEC2withTags()
def shutdown(onlyRunning):
    for  k in onlyRunning:

        responce=ec2East.stop_instances(InstanceIds=[k,], DryRun=False)
        print(responce)


shutdown(onlyRunning)      
          

           