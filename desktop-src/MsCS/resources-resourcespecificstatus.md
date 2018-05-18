---
title: ResourceSpecificStatus
description: Provides a resource-specific status message of the resource. The following table summarizes the attributes of the ResourceSpecificStatus property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6ba9765c-f32d-40f1-a8cf-8c465ad4176c'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ResourceSpecificStatus Failover Cluster ,for resources", "ResourceSpecificStatus Failover Cluster"]
topic_type:
- apiref
api_name:
- ResourceSpecificStatus
api_type:
- NA
---

# ResourceSpecificStatus

Provides a resource-specific status message of the [resource](resources.md). The following table summarizes the attributes of the **ResourceSpecificStatus** property.



| Attribute            | Value                                                                     |
|----------------------|---------------------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>                        |
| Structure<br/> | [**CLUSPROP\_SZ**](clusprop-sz.md)<br/>                            |
| Minimum<br/>   | **NULL**<br/>                                                       |
| Maximum<br/>   | None (but see [Maximum String Size](maximum-string-size.md)).<br/> |
| Default<br/>   | **NULL**<br/>                                                       |



 

## Remarks

The **ResourceSpecificStatus** property can be changed using the [CLUSCTL\_RESOURCE\_SET\_COMMON\_PROPERTIES](clusctl-resource-set-common-properties.md) control code.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Resource Common Properties](resource-common-properties.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_SET\_COMMON\_PROPERTIES](clusctl-resource-set-common-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> </dl>

 

 





