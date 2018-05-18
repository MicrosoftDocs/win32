---
title: Name
description: Provides the name of the network being managed by a message queuing resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '458816BC-0229-4E96-9BA5-758007526D7D'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Name Failover Cluster ,for message queuings", "Name Failover Cluster"]
topic_type:
- apiref
api_name:
- Name
api_type:
- NA
---

# Name

Provides the name of the [network](networks.md) being managed by a [message queuing](message-queuing-private-properties.md) resource. The following table summarizes the attributes of the **Name** property.



| Attribute            | Value                                                         |
|----------------------|---------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string<br/>                     |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>            |
| Status<br/>    | Required<br/>                                           |
| Structure<br/> | [**CLUSPROP\_SZ**](clusprop-sz.md)<br/>                |
| Minimum<br/>   | **NULL**<br/>                                           |
| Maximum<br/>   | see [Maximum String Size](maximum-string-size.md)<br/> |
| Default<br/>   | **NULL**<br/>                                           |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md) macro creates a [**CLUSPROP\_SZ**](clusprop-sz.md) structure with an array of the correct size.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Message Queuing Private Properties](message-queuing-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md)
</dt> </dl>

 

 





