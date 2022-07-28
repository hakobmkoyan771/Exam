resource "aws_route_table" "route_table" {
  vpc_id = aws_vpc.vpc.id

  route {
    gateway_id = aws_internet_gateway.igw.id
    cidr_block = "0.0.0.0/0"
  }
}

resource "aws_route_table_association" "route_table_association" {
  count          = length(aws_subnet.subnets.*.id)
  route_table_id = aws_route_table.route_table.id
  subnet_id      = aws_subnet.subnets[count.index].id
}