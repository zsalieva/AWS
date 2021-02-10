import boto3, json
session = boto3.Session(profile_name='development')
east = 'us-east-1'
west = 'us-west-2'
ec2East = session.client('ec2', region_name = east)
elbEast= session.client('elb',region_name=east)

responseEC2 = ec2East.describe_security_groups(
    Filters=[
        {
            'Name': 'ip-permission.cidr',
            'Values': [
                '0.0.0.0/0',
            ]
        },
        
    ],
)
sgs = responseEC2['SecurityGroups']
sgsWithOpenPorts = []
for i in sgs:

    sgsWithOpenPorts.append(i['GroupName'])
print(sgsWithOpenPorts)


for sg in sgsWithOpenPorts:
    ports=[80,22,443]
    for k in ports:
        responseEC2 = ec2East.revoke_security_group_ingress(
        CidrIp='0.0.0.0/0',
        FromPort=k,
        GroupName= sg,
        IpProtocol='tcp',
        ToPort=k,
    )