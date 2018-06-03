---
title: PublishPTRRecords
description: Determines if PTR resource records, apart from A or AAAA, are published for the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: EB0CA473-B1C8-49AB-893F-E854C80F539B
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PublishPTRRecords Failover Cluster , for virtual machine replication brokers
- PublishPTRRecords Failover Cluster
topic_type:
- apiref
api_name:
- PublishPTRRecords
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PublishPTRRecords

Determines if PTR resource records, apart from A or AAAA, are published for the resource. The following table summarizes the attributes of the **PublishPTRRecords** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 1                                         |
| Default   | 0                                         |



 

## Remarks

Setting this private property to 0, the default value, ensures that the PTR resource records are not published.

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
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Virtual Machine Replication Broker Private Properties](virtual-machine-replication-broker-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





