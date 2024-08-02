resource "aws_instance" "public_instance" {
  ami             = var.ami_id
  instance_type   = var.instance_type
  subnet_id       = var.public_subnet_id
  security_groups = [var.public_sg_id]
  key_name        = var.key_name

  associate_public_ip_address = true

  user_data = file("${path.module}/../scripts/main.sh")

  tags = {
    Name = "PublicInstance"
  }
}

resource "aws_instance" "private_instance" {
  ami             = var.ami_id
  instance_type   = var.instance_type
  subnet_id       = var.private_subnet_id
  security_groups = [var.private_sg_id]
  key_name        = var.key_name

  tags = {
    Name = "PrivateInstance"
  }
}

