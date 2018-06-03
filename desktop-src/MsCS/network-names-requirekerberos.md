---
title: RequireKerberos
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: da1c3346-2000-46c8-831a-e59d30aa29c1
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RequireKerberos Failover Cluster ,for network names
- RequireKerberos Failover Cluster
topic_type:
- apiref
api_name:
- RequireKerberos
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RequireKerberos

\[This property is available for use only in Windows Server 2003.\]

This property is not supported.

## Examples

The property value portion of a [property list](property-lists.md) entry for **RequireKerberos** can be set with the following example code.


```C++
DWORD          RequireKerberosData = 1;
CLUSPROP_DWORD RequireKerberosValue;

RequireKerberosValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
RequireKerberosValue.cbLength  = sizeof(DWORD);
RequireKerberosValue.dw        = RequireKerberosData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Name Private Properties](network-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





