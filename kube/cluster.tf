resource "aws_eks_cluster" "cluster" {
  name     = "Lessons"
  role_arn = aws_iam_role.eks_role.arn

  vpc_config {
    endpoint_public_access = true
    public_access_cidrs    = ["0.0.0.0/0"]
    subnet_ids             = aws_subnet.subnets.*.id
    security_group_ids     = ["${aws_security_group.worker_sgp.id}"]
  }

  kubernetes_network_config {
    ip_family         = "ipv4"
    service_ipv4_cidr = "172.16.0.0/12"
  }
}

resource "aws_eks_node_group" "node" {
  cluster_name  = aws_eks_cluster.cluster.name
  node_role_arn = aws_iam_role.node_role.arn

  scaling_config {
    desired_size = 1
    max_size     = 2
    min_size     = 1
  }

  subnet_ids      = aws_subnet.subnets[*].id
  capacity_type   = "ON_DEMAND"
  instance_types  = ["t2.medium"]
  node_group_name = "testing_nodes"

  remote_access {
    ec2_ssh_key               = aws_key_pair.k.key_name
    source_security_group_ids = ["${aws_security_group.worker_sgp.id}"]
  }

  update_config {
    max_unavailable_percentage = 25
  }
}