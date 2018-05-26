---
title: MaxUsers
description: Number of simultaneous users that can access the Distributed File System resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fb911169-12a4-4b01-940b-8a87804897d3
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MaxUsers Failover Cluster ,for file shares
- MaxUsers Failover Cluster
topic_type:
- apiref
api_name:
- MaxUsers
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MaxUsers

Describes the number of simultaneous users that can access the Distributed File System resource. The following table summarizes the attributes of the **MaxUsers** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 0                                         |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 0xFFFFFFFF                                |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **MaxUsers** can be set with the following example code.


```C++
DWORD          MaxUsersData = 10;
CLUSPROP_DWORD MaxUsersValue;

MaxUsersValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
MaxUsersValue.cbLength  = sizeof(DWORD);
MaxUsersValue.dw        = MaxUsersData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Distributed File System Private Properties](distributed-file-system-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





