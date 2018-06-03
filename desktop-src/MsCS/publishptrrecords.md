---
title: PublishPTRRecords
description: Determines if PTR resource records, apart from A or AAAA, are published for the Cluster Name.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4bc191f4-0d4d-479f-8e09-eb8a75f93ca7
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PublishPTRRecords Failover Cluster , for Network Name properties
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

Determines if PTR resource records, apart from A or AAAA, are published for the Cluster Name. The following table summarizes the attributes of the **PublishPTRRecords** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 1                                         |
| Default   | 0                                         |



 

## Remarks

Setting this private property to 0, the default value, ensures that the PTR resource records are not published.

The constant for this property is **CLUSREG\_NAME\_NETNAME\_PUBLISH\_PTR**.

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



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Name Private Properties](network-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





