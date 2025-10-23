#storage account
resource "azurerm_storage_account" "asa" {
  name                     = "asa${random_string.suffix.result}"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

# #storgae container - skipping this as it does not seem to be needed for us
# resource "azurerm_storage_container" "sc" {
#   name                  = "sc${random_string.suffix.result}"
#   storage_account_id    = azurerm_storage_account.asa.id
#   container_access_type = "private"
# }

#create file share
resource "azurerm_storage_share" "ass" {
  name                 = "data"
  storage_account_id = azurerm_storage_account.asa.id
  quota                = 50
}

resource "azurerm_storage_share_file" "asf" {
  name             = "profiles.yml"
  storage_share_id = azurerm_storage_share.ass.url
  source           = "profiles.yml"
}