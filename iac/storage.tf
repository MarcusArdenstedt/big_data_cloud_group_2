#storage account
resource "azurerm_storage_account" "asa" {
  name                     = "asa${random_string.suffix.result}"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}



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

resource "azurerm_storage_container" "asc" {
  name = "group2${random_string.suffix.result}"
  storage_account_id = azurerm_storage_account.asa.id
  container_access_type = "blob"
}

resource "azurerm_storage_blob" "asb" {
  name = "geojson_data"
  storage_account_name = azurerm_storage_account.asa.name
  storage_container_name = azurerm_storage_container.asc.name
  type = "Block"
  source = "../data/swedish_regions.geojson"
}