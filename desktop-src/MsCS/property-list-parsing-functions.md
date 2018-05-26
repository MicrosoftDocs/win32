---
title: Property List Parsing Functions
description: The property list parsing functions are used by applications and resource DLLs to locate specific values or properties in a property list.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b6287135-e9b3-43ab-aaf4-1488dad3e9ed
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- property list parsing functions Failover Cluster
- cluster utility functions Failover Cluster ,property list parsing functions
- property lists Failover Cluster ,parsing functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Property List Parsing Functions

The [property list](property-lists.md) parsing functions are used by applications and [resource DLLs](resource-dlls.md) to locate specific values or properties in a property list.

## In this section

<dl> <dt>

[*ResUtilFindBinaryProperty*](/windows/previous-versions/ResApi/nc-resapi-presutil_find_binary_property?branch=master)
</dt> <dd>

Locates a specified binary property in a [property list](property-lists.md) and can also return the value of the property. The **PRESUTIL\_FIND\_BINARY\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilFindDwordProperty*](/windows/previous-versions/ResApi/nc-resapi-presutil_find_dword_property?branch=master)
</dt> <dd>

Locates an unsigned long property value in a [property list](property-lists.md). The **PRESUTIL\_FIND\_DWORD\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilFindExpandedSzProperty*](/windows/previous-versions/ResApi/nc-resapi-presutil_find_expanded_sz_property?branch=master)
</dt> <dd>

Locates an expanded string property value in a [property list](property-lists.md). The **PRESUTIL\_FIND\_EXPANDED\_SZ\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilFindExpandSzProperty*](/windows/previous-versions/ResApi/nc-resapi-presutil_find_expand_sz_property?branch=master)
</dt> <dd>

Locates an [expandable string](e-gly.md#-wolf-expandable-string-gly) property in a [property list](property-lists.md). The **PRESUTIL\_FIND\_EXPAND\_SZ\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilFindLongProperty*](/windows/previous-versions/ResApi/nc-resapi-presutil_find_long_property?branch=master)
</dt> <dd>

Locates a signed long property value in a [property list](property-lists.md). The **PRESUTIL\_FIND\_LONG\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilFindMultiSzProperty*](/windows/previous-versions/ResApi/nc-resapi-presutil_find_multi_sz_property?branch=master)
</dt> <dd>

Locates a multiple string property in a [property list](property-lists.md). The **PRESUTIL\_FIND\_MULTI\_SZ\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilFindSzProperty*](/windows/previous-versions/ResApi/nc-resapi-presutil_find_sz_property?branch=master)
</dt> <dd>

Locates a string property in a [property list](property-lists.md). The **PRESUTIL\_FIND\_SZ\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilFindULargeIntegerProperty*](/windows/previous-versions/ResApi/nc-resapi-presutil_find_ulargeinteger_property?branch=master)
</dt> <dd>

Gets a large integer property value from a property list. The **PRESUTIL\_FIND\_ULARGEINTEGER\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetBinaryProperty*](/windows/previous-versions/ResApi/nc-resapi-presutil_get_binary_property?branch=master)
</dt> <dd>

Retrieves a binary property from a [property list](property-lists.md) and advances a pointer to the next property in the list. The **PRESUTIL\_GET\_BINARY\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetDwordProperty*](/windows/previous-versions/ResApi/nc-resapi-presutil_get_dword_property?branch=master)
</dt> <dd>

Retrieves a **DWORD** property from a [property list](property-lists.md) and advances a pointer to the next property in the list. The **PRESUTIL\_GET\_DWORD\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetMultiSzProperty*](/windows/previous-versions/ResApi/nc-resapi-presutil_get_multi_sz_property?branch=master)
</dt> <dd>

Retrieves a multiple string property from a [property list](property-lists.md) and advances a pointer to the next property in the list. The **PRESUTIL\_GET\_MULTI\_SZ\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetSzProperty*](/windows/previous-versions/ResApi/nc-resapi-presutil_get_sz_property?branch=master)
</dt> <dd>

Retrieves a string property from a [property list](property-lists.md) and advances a pointer to the next property in the list. The **PRESUTIL\_GET\_SZ\_PROPERTY** type defines a pointer to this function.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Utility Functions](cluster-utility-functions.md)
</dt> </dl>

 

 




