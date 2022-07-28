resource "aws_key_pair" "k" {
  key_name   = "k"
  public_key = file("./k.pub")
}
