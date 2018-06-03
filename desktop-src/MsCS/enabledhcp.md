---
title: EnableDhcp
description: Enables DHCP on the IP Address \ 32;resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d330bffd-9b9e-47c1-a5c1-2aa364c7c543
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- EnableDhcp Failover Cluster , for IPv4 Address private properties
- EnableDhcp Failover Cluster
topic_type:
- apiref
api_name:
- EnableDhcp
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EnableDhcp

Enables DHCP on the [IP Address](ip-address.md) [resource](resources.md). The following table summarizes the attributes of the **EnableDhcp** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Required                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | **FALSE** (0) - disable DHCP              |
| Maximum   | **TRUE** (1) - enable DHCP                |
| Default   | **FALSE** (0)                             |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **EnableDhcp** can be set with the following example code.


```C++
DWORD          EnableDhcpData = TRUE;
CLUSPROP_DWORD EnableDhcpValue;

EnableDhcpValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
EnableDhcpValue.cbLength  = sizeof(DWORD);
EnableDhcpValue.dw        = EnableDhcpData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[IP Address Private Properties](ip-address-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





