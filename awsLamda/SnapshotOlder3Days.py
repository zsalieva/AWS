import boto 
import datetime
import dateutil
from dateutil import parser
from boto import ec2
connection=ec2.connect_to_region("us-east-1")
ebsAllSnapshots=connection.get_all_snapshots(owner='16-DIGIT-AWS-ACCOUNT-NUMBER')
#Get the 30 days old date
timeLimit=datetime.datetime.now() - datetime.timedelta(days=3)  
for snapshot in ebsAllSnapshots:
    if parser.parse(snapshot.start_time).date() <= timeLimit.date():
        print " Deleting Snapshot %s  %s "  %(snapshot.id,snapshot.tags)
        connection.delete_snapshot(snapshot.id) 
    else:
        # this section will have all snapshots which is created before 3 days
        print "Only Deleting Snapshots which is 3 days old"