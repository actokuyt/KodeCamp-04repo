terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.57.0"
    }
  }
}

provider "aws" {
  region = "eu-west-1"
}


module "vpc" {
  source = "./vpc"

  cidr_block = "10.0.0.0/16"
  vpc_name = "KCVPC"
}

module "subnet" {
  source = "./subnet"

  vpc_id = module.vpc.vpc_id
}

module "igw" {
  source = "./igw"

  vpc_id = module.vpc.vpc_id
}

module "rt" {
  source = "./rt"

  vpc_id            = module.vpc.vpc_id
  gateway_id        = module.igw.gateway_id
  private_subnet_id = module.subnet.private_subnet_id
  public_subnet_id  = module.subnet.public_subnet_id
}

module "eip" {
  source = "./eip"
}

module "nat" {
  source = "./nat"

  eip_id = module.eip.eip_id
  subnet_id = module.subnet.public_subnet_id
}

module "sg" {
  source = "./sg"

  vpc_id = module.vpc.vpc_id
}

module "nacl" {
  source = "./nacl"

  vpc_id = module.vpc.vpc_id
}

module "ec2" {
  source = "./ec2"

  ami_id = "ami-0932dacac40965a65"
  instance_type = "t2.micro"
  key_name = "awsec2"
  public_subnet_id = module.subnet.public_subnet_id
  public_sg_id  = module.sg.public_sg_id
  private_subnet_id = module.subnet.private_subnet_id
  private_sg_id = module.sg.private_sg_id
}