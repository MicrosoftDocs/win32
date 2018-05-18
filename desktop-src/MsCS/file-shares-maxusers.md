---
title: MaxUsers
description: Describes the number of simultaneous users that can access the file share.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f40f3646-305b-43fc-abf3-e08d229ae604'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["MaxUsers Failover Cluster ,for file shares", "MaxUsers Failover Cluster"]
topic_type:
- apiref
api_name:
- MaxUsers
api_type:
- NA
---

# MaxUsers

\[The **MaxUsers** property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2003:  **

Describes the number of simultaneous users that can access the [file share](file-share.md). The following table summarizes the attributes of the **MaxUsers** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
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
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[File Share Private Properties](file-share-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





