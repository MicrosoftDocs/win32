---
title: Set Property Utility Functions
description: The set property utility functions use the contents of a property list, parameter block, or property table to change one or more properties in the cluster database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 88c198e5-a819-486c-a459-749f805196db
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set Property Utility Functions

The set property utility functions use the contents of a [property list](property-lists.md), [parameter block](parameter-blocks.md), or [property table](property-tables.md) to change one or more properties in the cluster database.



| Function                                                                         | Description                                                                                                                                   |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**ResUtilSetPrivatePropertyList**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_private_property_list?branch=master)           | Writes [private properties](private-properties.md) to the [cluster database](cluster-database.md) based on the contents of a property list. |
| [**ResUtilSetPropertyParameterBlock**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_property_parameter_block?branch=master)     | Conditionally writes properties to the cluster database based on the contents of a parameter block.                                           |
| [**ResUtilSetPropertyParameterBlockEx**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_property_parameter_block_ex?branch=master) | Force writes properties to the cluster database based on the contents of a parameter block.                                                   |
| [**ResUtilSetPropertyTable**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_property_table?branch=master)                       | Conditionally writes properties to the cluster database based on the contents of a property table.                                            |
| [**ResUtilSetPropertyTableEx**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_property_table_ex?branch=master)                   | Force writes properties to the cluster database based on the contents of a property table.                                                    |
| [**ResUtilSetUnknownProperties**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_unknown_properties?branch=master)               | Sets [unknown properties](unknown-properties.md) based on the contents of a property table.                                                  |



 

 

 




