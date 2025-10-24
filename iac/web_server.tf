resource "azurerm_service_plan" "asp" {
  name                = "aspgroup-2"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "S1"
}

resource "azurerm_linux_web_app" "app" {
  name                = "app-group${random_string.suffix.result}-2"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  service_plan_id     = azurerm_service_plan.asp.id
  

  site_config {
    application_stack {
      docker_image_name   = "${azurerm_container_registry.acr.login_server}/dashboard:latest"
      docker_registry_url = "https://${azurerm_container_registry.acr.login_server}"
    }
  }
}