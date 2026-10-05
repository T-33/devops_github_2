terraform {
  required_version = ">= 1.0.0"
}

resource "local_file" "example" {
  content  = var.content
  filename = "${path.module}/${var.filename}"
}

output "file_created" {
  value = local_file.example.filename
}
