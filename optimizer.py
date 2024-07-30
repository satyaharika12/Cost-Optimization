import boto3

def lambda_handler(event, context):
    # Check if the event is for creating a new volume
    if event['detail']['eventName'] == 'CreateVolume':
        ec2 = boto3.client('ec2')
        volume_id = event['detail']['responseElements']['volumeId']
        
        response = ec2.describe_volumes(
            VolumeIds=[volume_id]
        )
        
        # Extract the volume type
        volume_type = response['Volumes'][0]['VolumeType']
        
        # Check if the volume type is gp2
        if volume_type == 'gp2':
            print("Volume type is gp2. Converting to gp3...")
            
            # Modify the volume to gp3
            response = ec2.modify_volume(
                VolumeId=volume_id,
                VolumeType='gp3',
            )
            
            print("Volume converted to gp3 successfully.")
        else:
            print("Volume type is not gp2. No action needed.")
