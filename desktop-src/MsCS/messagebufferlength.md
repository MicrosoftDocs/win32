---
title: MessageBufferLength
description: Specifies the number of characters in a message buffer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0BED9E8D-5C71-40C3-82F8-D48BA4991D13'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["MessageBufferLength Failover Cluster"]
topic_type:
- apiref
api_name:
- MessageBufferLength
api_type:
- NA
---

# MessageBufferLength

Specifies the number of characters in a message buffer.



| Attribute            | Value                                     |
|----------------------|-------------------------------------------|
| Data type<br/> | **DWORD**                                 |
| Access<br/>    | [Read/write](read-write-properties.md)   |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum<br/>   | 1<br/>                              |
| Maximum<br/>   | 1000<br/>                           |
| Default<br/>   | 50<br/>                             |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_MESSAGE\_BUFFER\_LENGTH**.

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | None supported<br/>         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





