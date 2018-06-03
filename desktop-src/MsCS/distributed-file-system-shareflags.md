---
title: ShareFlags
description: Share flags of a Distributed File System resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 81ca801c-647f-4a72-8cfa-36d85e1ccbab
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ShareFlags Failover Cluster , for Distributed File System private properties
- ShareFlags Failover Cluster
topic_type:
- apiref
api_name:
- ShareFlags
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ShareFlags

Stores the share flags of a Distributed File System resource. The following table summarizes the attributes of the **ShareFlags** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 0xF30                                     |
| Default   | 0                                         |



 

## Remarks

See the definition of the **SHI1005\_VALID\_FLAGS\_SET** value defined in LMShare.h and the descriptions of the values allowed for the **shi1005\_flags** member of the [**SHARE\_INFO\_1005**](https://msdn.microsoft.com/library/windows/desktop/bb525404) structure for more information on the meaning of the individual flags.

## Examples

The property value portion of a [property list](property-lists.md) entry for **ShareFlags** can be set with the following example code.


```C++
DWORD          ShareFlagsData = TRUE;
CLUSPROP_DWORD ShareFlagsValue;

ShareFlagsValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
ShareFlagsValue.cbLength  = sizeof(DWORD);
ShareFlagsValue.dw        = ShareFlagsData;
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

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





