aws_region: us-east-1

# Ubuntu 14.04 64-bit
ami_id: ami-09d069a04349dc3cb

# Instance type
instance_type: t2.micro

# Key pair name
key_name: key_aws

# Tags
tags_used: aws-docker-ansible 

# CIDR Range
cidr_range: */32

# VPC Information
vpc_name: aws-ansible-docker
vpc_cidr_block: 10.0.0.0/16

# For Security Group Rule
my_ip_range: */32

# Subnets
public_subnet_1_cidr:  10.0.0.0/20

# VPC Id
vpc_id: vpc-*
vpc_subnet_id: subnet-*
