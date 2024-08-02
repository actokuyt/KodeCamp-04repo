variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type = string
  default = "ami-0932dacac40965a65"
}

variable "instance_type" {
  description = "Instance type for the EC2 instance"
  type = string
  default = "t2.micro"
}

variable "key_name" {
  description = "ssh key pair name"
  type = string
  default = "awsec2"
}

variable "private_sg_id" {
  description = "value of private security group"
  type = string
}

variable "public_sg_id" {
  description = "value of public security group"
  type = string
}

variable "public_subnet_id" {
  description = "Subnet ID for the public subnet"
  type = string
}

variable "private_subnet_id" {
  description = "Subnet ID for the private subnet"
  type = string
}
