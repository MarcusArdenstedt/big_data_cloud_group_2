variable "location" {
  description = "location to be used for resources"
  default     = "swedencentral"
}

# resource group
resource "azurerm_resource_group" "rg" {
  name     = "rg-group-2"
  location = var.location
}