---
title: StatusInformation
description: Provides information about the status of a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3C3873C0-E3F6-47AE-B6A0-8F9A3E3509D1
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- StatusInformation Failover Cluster
topic_type:
- apiref
api_name:
- StatusInformation
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StatusInformation

Provides information about the status of a [node](nodes.md).



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | (0x1 \| 0x2 \| 0x10).                     |
| Default   | 0                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NODE\_STATUS\_INFO**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Node Common Properties](node-common-properties.md)
</dt> </dl>

 

 





