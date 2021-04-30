---
description: During a Windows Installer installation, the installer can search for a registry entry and create a property holding the value of the registry.
ms.assetid: 3a663fc7-cdcf-4ac3-8251-836ba0d3cc11
title: Searching for a Registry Entry and Creating a Property Holding the Value of the Registry
ms.topic: article
ms.date: 05/31/2018
---

# Searching for a Registry Entry and Creating a Property Holding the Value of the Registry

**To search for a registry entry and create a property holding the value of that file**

1.  Do not add the signature to the [Signature Table](signature-table.md) or the [CompLocator Table](complocator-table.md). If a file signature is listed in the [AppSearch Table](appsearch-table.md) and is not listed in the Signature or CompLocator tables, the Installer looks in the [RegLocator Table](reglocator-table.md).

2.  Specify the registry entry to be searched for in the [RegLocator Table](reglocator-table.md). If the signature is absent from the [Signature Table](signature-table.md) and the value of the Type column is **msidbLocatorTypeRawValue**, then the search is assumed to be for the specific registry key name pointed to by the RegLocator Table.

    [RegLocator Table](reglocator-table.md) (partial)

    

    | Signature\_         | Root         | Key                                                           | Name                  | Type                                    |
    |---------------------|--------------|---------------------------------------------------------------|-----------------------|-----------------------------------------|
    | AppValue<br/> | 2<br/> | **SOFTWARE**\\**Microsoft**\\**MyApp**<br/> <br/> | **Myname**<br/> | **msidbLocatorTypeRawValue**<br/> |

    

     

3.  Finally, populate the [AppSearch Table](appsearch-table.md) so that the [AppSearch Action](appsearch-action.md) returns the value of AppValue. After the Installer executes the AppSearch Action, the value of MYREGVAL is the value of AppValue.

    [AppSearch Table](appsearch-table.md) (partial)

    

    | Property            | Signature           |
    |---------------------|---------------------|
    | MYREGVAL<br/> | AppValue<br/> |

    

     

 

 




