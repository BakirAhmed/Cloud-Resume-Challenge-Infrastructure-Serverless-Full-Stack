output "cloudfront_domain" {
  value = aws_cloudfront_distribution.site.domain_name
}

output "api_endpoint" {
  value = "${aws_apigatewayv2_api.http_api.api_endpoint}/count"
}

output "s3_bucket_name" {
  value = aws_s3_bucket.site.bucket
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.visitor_counter.name
}
