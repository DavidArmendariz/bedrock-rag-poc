resource "aws_s3_bucket" "knowledgebase_bucket" {
  bucket        = "${var.bucket_name}-${local.account_id}"
  force_destroy = true

  tags = {
    Name = var.bucket_name
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "knowledgebase_bucket" {
  bucket = aws_s3_bucket.knowledgebase_bucket.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket" "knowledgebase_bucket_outputs" {
  bucket        = "${var.bucket_name}-outputs-${local.account_id}"
  force_destroy = true

  tags = {
    Name = var.bucket_name
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "knowledgebase_bucket_output" {
  bucket = aws_s3_bucket.knowledgebase_bucket_outputs.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

