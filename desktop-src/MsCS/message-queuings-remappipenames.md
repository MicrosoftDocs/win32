---
title: RemapPipeNames
description: Controls how named pipes are opened on the network managed by the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '10265A34-CA57-4BEC-8593-5F2DB8E0241B'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["RemapPipeNames Failover Cluster ,for message queuings", "RemapPipeNames Failover Cluster"]
topic_type:
- apiref
api_name:
- RemapPipeNames
api_type:
- NA
---

# RemapPipeNames

Controls how named pipes are opened on the [network](networks.md) managed by the resource. The following table summarizes the attributes of the **RemapPipeNames** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | **FALSE**                                 |
| Maximum   | **TRUE**                                  |
| Default   | **FALSE**                                 |



 

## Remarks

If **RemapPipeNames** is set to **TRUE**, named pipes are always opened using local pipe names. For example, when a client opens "Pipe" on "\\\\NodeName" the client will actually open "$$\\NodeName\\Pipe".

By default, **RemapPipeNames** is set to **FALSE**.

## Examples

The property value portion of a [property list](property-lists.md) entry for **RemapPipeNames** can be set with the following example code.


```C++
DWORD RemapPipeNameData            = TRUE;
CLUSPROP_DWORD RemapPipeNameValue;
RemapPipeNameValue.Syntax.dw       = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
RemapPipeNameValue.cbLength        = sizeof(DWORD);
RemapPipeNameValue.dw              = RemapPipeNameData;
```



## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Message Queuing Private Properties](message-queuing-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





