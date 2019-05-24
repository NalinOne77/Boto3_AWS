#Before run the script make sure you've configured AWS credentials properly
import boto3
from boto3.session import Session

# Initialize Session
s = Session()
 #Get ec2 available regions
ec2_regions = s.get_available_regions('ec2')

#Loop through region
for region in ec2_regions:
    client = boto3.client('autoscaling', region_name=region)
    response = client.describe_auto_scaling_groups()
    
    print("=========================> REGION: %s <=========================")%(region)
    #Get each autoscaling group info from one region and display
    for asg in response['AutoScalingGroups']:
        print(asg['AutoScalingGroupName'])
