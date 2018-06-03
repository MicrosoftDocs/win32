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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get Property Utility Functions

The get property utility functions obtain properties directly from the [cluster database](cluster-database.md) and return them in the form of a [property list](property-lists.md), a [parameter block](parameter-blocks.md), or a [property table](property-tables.md).



| Function                                                                             | Description                                                                                                           |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**ResUtilAddUnknownProperties**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_add_unknown_properties)                   | Retrieves [unknown properties](unknown-properties.md) from the cluster database and appends them to a property list. |
| [**ResUtilEnumPrivateProperties**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_enum_private_properties)                 | Enumerates the names of an object's [private properties](private-properties.md).                                     |
| [**ResUtilEnumProperties**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_enum_properties)                               | Enumerates the names of an object's [common properties](common-properties.md).                                       |
| [**ResUtilGetAllProperties**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_all_properties)                           | Returns all of the default and unknown properties for an object in a property list.                                   |
| [**ResUtilGetPrivateProperties**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_private_properties)                   | Returns the private properties of a [cluster object](cluster-objects.md) in a property list. .                       |
| [**ResUtilGetProperties**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_properties)                                 | Returns specified properties for an object in a property list.                                                        |
| [**ResUtilGetPropertiesToParameterBlock**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_properties_to_parameter_block) | Returns specified properties for an object in a parameter block.                                                      |
| [**ResUtilGetProperty**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_property)                                     | Returns a single property.                                                                                            |
| [**ResUtilGetPropertySize**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_property_size)                             | Returns the byte size of a specified property.                                                                        |



 

 

 




