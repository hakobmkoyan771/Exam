resource "aws_subnet" "subnets" {
  count                   = length(data.aws_availability_zones.availability_zones.names)
  vpc_id                  = aws_vpc.vpc.id
  cidr_block              = "192.168.${count.index}.0/24"
  availability_zone       = data.aws_availability_zones.availability_zones.names[count.index]
  map_public_ip_on_launch = true
}
