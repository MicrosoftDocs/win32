---
title: Get Property Utility Functions
description: The get property utility functions obtain properties directly from the cluster database and return them in the form of a property list, a parameter block, or a property table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9a079afe-9e19-4bc1-bc58-d9d02aa7290c
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get Property Utility Functions

The get property utility functions obtain properties directly from the [cluster database](cluster-database.md) and return them in the form of a [property list](property-lists.md), a [parameter block](parameter-blocks.md), or a [property table](property-tables.md).



| Function                                                                             | Description                                                                                                           |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**ResUtilAddUnknownProperties**](/windows/previous-versions/ResApi/nc-resapi-presutil_add_unknown_properties?branch=master)                   | Retrieves [unknown properties](unknown-properties.md) from the cluster database and appends them to a property list. |
| [**ResUtilEnumPrivateProperties**](/windows/previous-versions/ResApi/nc-resapi-presutil_enum_private_properties?branch=master)                 | Enumerates the names of an object's [private properties](private-properties.md).                                     |
| [**ResUtilEnumProperties**](/windows/previous-versions/ResApi/nc-resapi-presutil_enum_properties?branch=master)                               | Enumerates the names of an object's [common properties](common-properties.md).                                       |
| [**ResUtilGetAllProperties**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_all_properties?branch=master)                           | Returns all of the default and unknown properties for an object in a property list.                                   |
| [**ResUtilGetPrivateProperties**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_private_properties?branch=master)                   | Returns the private properties of a [cluster object](cluster-objects.md) in a property list. .                       |
| [**ResUtilGetProperties**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_properties?branch=master)                                 | Returns specified properties for an object in a property list.                                                        |
| [**ResUtilGetPropertiesToParameterBlock**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_properties_to_parameter_block?branch=master) | Returns specified properties for an object in a parameter block.                                                      |
| [**ResUtilGetProperty**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_property?branch=master)                                     | Returns a single property.                                                                                            |
| [**ResUtilGetPropertySize**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_property_size?branch=master)                             | Returns the byte size of a specified property.                                                                        |



 

 

 




