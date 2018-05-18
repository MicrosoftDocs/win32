---
title: PublishPTRRecords
description: Determines whether PTR resource records, apart from A or AAAA, are published for the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '101006B0-FE50-4C51-8FA0-FD273A92F1B1'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["PublishPTRRecords Failover Cluster , for message queuings", "PublishPTRRecords Failover Cluster"]
topic_type:
- apiref
api_name:
- PublishPTRRecords
api_type:
- NA
---

# PublishPTRRecords

Determines whether PTR resource records, apart from A or AAAA, are published for the resource. The following table summarizes the attributes of the **PublishPTRRecords** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0                                         |
| Maximum   | 1                                         |
| Default   | 0                                         |



 

## Remarks

Setting this private property to 0, the default value, ensures that the PTR resource records are not published.

This constant for this property is **CLUSREG\_NAME\_NETNAME\_PUBLISH\_PTR**.

## Examples

The property value portion of a [property list](property-lists.md) entry for **PublishPTRRecords** can be set with the following example code.


```C++
DWORD          PublishPTRRecordsData = 0;
CLUSPROP_DWORD PublishPTRRecordsValue;

PublishPTRRecordsValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
PublishPTRRecordsValue.cbLength  = sizeof(DWORD);
PublishPTRRecordsValue.dw        = PublishPTRRecordsData;
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

 

 





