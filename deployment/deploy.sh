#!/bin/bash
HSTNM='pool_connection'
aws ec2 run-instances \
    --image-id ami-0b60e7d34d8ba6db4 \
    --count 1 --instance-type t2.micro  \
    --region sa-east-1 \
    --security-group-ids 'sg-63fe031a' \
    --subnet-id 'subnet-36ecf651' \
    --monitoring Enabled=true \
    --key-name $PRIVATE_KEY \
    --user-data file://user_data.txt \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$HSTNM}]"

