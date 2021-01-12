import boto3
import paramiko
import datetime
from botocore.exceptions import ClientError
ses=boto3.Session(profile_name="abc", region_name="us-east-2")
client=ses.client(service_name="ec2")
snapshots=client.describe_snapshots(OwnerIds=['123456789123'])
count=1
for snapshot in snapshots['Snapshots']:
	a=snapshot['StartTime']
	b=a.date()
	c=datetime.datetime.now().date()
	d=c-b
	try:
		if(d.days>30):
			id=str(snapshot['SnapshotId'])
			client.delete_snapshot(SnapshotId=id)
			print("Deleted "+id+" snapshot and the count is : "+str(count))
			count+=1
		except ClientError as e:
			if('InvalidSnapshot.InUse' in e.response['Error']['Code']):
				print("Skipping this snapshot")
				continue
print("Total Deleted Snapshots which are more than 30 Days Old are : "+str(count-1))
