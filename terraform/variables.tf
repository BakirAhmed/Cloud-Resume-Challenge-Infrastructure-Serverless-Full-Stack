variable "aws_region" {
  type    = string
  default = "eu-west-3"
}

variable "project_name" {
  type    = string
  default = "cloud-resume"
}

variable "domain_name" {
  description = "Nom de domaine du CV (laisser vide pour utiliser le domaine CloudFront par défaut)"
  type        = string
  default     = ""
}
