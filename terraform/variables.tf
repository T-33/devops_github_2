variable "content" {
  type        = string
  description = "The text to write inside the file"
  default     = "Hello from Terraform!"
}

variable "filename" {
  type        = string
  description = "The name of the file to create"
  default     = "hello.txt"
}
