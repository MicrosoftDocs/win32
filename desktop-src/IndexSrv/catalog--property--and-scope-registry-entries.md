---
title: Catalog, Property, and Scope Registry Entries
description: Catalog, Property, and Scope Registry Entries
ms.assetid: 8453a660-c93a-4986-8c1b-0b359925ff47
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Catalog, Property, and Scope Registry Entries

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Catalogs on the system are included as subkeys of the key

**HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\ContentIndex\\Catalogs**.

The subkey for each catalog contains the following entries.



| Registry Name                              | Description                                                                                                                                                                      |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CatalogInactive**](cataloginactive.md) | Controls whether a catalog is active.                                                                                                                                            |
| [**Location**](location.md)               | Path to the catalog directory.                                                                                                                                                   |
| [**Properties**](properties.md)           | Subkey that contains a list of entries that are combinations of property set identifiers and property names or identifiers, each specifying information for a property to cache. |
| [**Scopes**](scopes.md)                   | Subkey that contains a list of strings, each containing one scope definition for the catalog.                                                                                    |



 

Each catalog subkey can include an alternative entry with a name identical to many in the [Main Registry Entries](main-registry-entries.md). When an alternative entry occurs in a catalog subkey, the value of that entry takes precedence over the value of the global, main registry entry.

 

 




