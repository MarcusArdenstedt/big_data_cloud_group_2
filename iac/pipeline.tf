#usuccessful creation for container group in Azure

# resource "azurerm_container_group" "acg" {
#   name                = "acg${random_string.suffix.result}"
#   resource_group_name = azurerm_resource_group.rg.name
#   location            = azurerm_resource_group.rg.location
#   ip_address_type     = "Private"
#   os_type             = "Linux"

#   volume {
#     name                 = "data"
#     mount_path           = "/mnt/data/"
#     storage_account_name = azurerm_storage_account.asa.name
#     storage_account_key  = azurerm_storage_account.asa.primary_access_key
#     share_name           = azurerm_storage_share.ass.name
#   }

#   container {
#     name   = "dbt-executor"
#     image  = "myregistry.azurecr.io/dbt-image:latest"
#     cpu    = 2
#     memory = 4

#     # 2. Mount the Volume into the Container
#     volume_mount {
#       name       = "data"
#       mount_path = "/data" # Container path where files are accessible
#       read_only  = true
#     }
#   }
# }
