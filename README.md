-- # AWS Cloud Cost Optimization - Identifying Stale Resources
Identifying Stale EBS Snapshots
In this example, we'll create a Lambda function that identifies EBS snapshots that are no longer associated with any active EC2 instance and deletes them to save on storage costs.

Description:
The Lambda function fetches all EBS snapshots owned by the same account ('self') and also retrieves a list of active EC2 instances (running and stopped). For each snapshot, it checks if the associated volume (if exists) is not associated with any active instance. If it finds a stale snapshot, it deletes it, effectively optimizing storage costs.


-- ## Auto Convert EBS Volume Type Lambda Function
This Lambda function automatically converts the volume type from gp2 to gp3 when a new volume is created in AWS EC2. It utilizes Python and the boto3 SDK to interact with AWS services.

## Overview
When a new volume is created in AWS EC2, this Lambda function is triggered by an EventBridge rule listening for the `CreateVolume` event. Upon invocation, the function checks if the volume type is gp2. If it is, the function modifies the volume type to gp3.

## Setup
1. **Deployment**: Deploy the Lambda function in your AWS account using the provided script or manually through the AWS Management Console.

2. **IAM Permissions**: Ensure that the Lambda function has the necessary IAM permissions to describe volumes and modify their types.

3. **EventBridge Rule**: Configure an EventBridge rule to trigger the Lambda function on the `CreateVolume` event.
   
## Usage
1. Create a new volume in AWS EC2 with the desired size and availability zone.
2. Monitor the CloudWatch Logs associated with the Lambda function to view the execution logs and confirm successful volume type conversion.
   
## Limitations
- Currently, the function only supports converting the volume type from gp2 to gp3. Additional logic can be added to support other volume types as needed.
