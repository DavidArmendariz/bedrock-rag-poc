variable "bucket_name" {
  description = "The name of the S3 bucket for storing PDFs"
  type        = string
  default     = "knowledgebase"
}

variable "region" {
  description = "The AWS region where the S3 bucket will be created"
  type        = string
  default     = "us-east-1"
}
