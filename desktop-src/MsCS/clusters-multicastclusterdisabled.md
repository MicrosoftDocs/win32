---
title: MulticastClusterDisabled
description: Enables or disables heartbeat multicasting for all networks in a cluster (subject to override by individual networks). The following table summarizes the attributes of the MulticastClusterDisabled property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 19db732a-630c-4265-b11a-3720eaf18242
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MulticastClusterDisabled Failover Cluster ,for clusters
- MulticastClusterDisabled Failover Cluster
topic_type:
- apiref
api_name:
- MulticastClusterDisabled
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MulticastClusterDisabled

\[The **MulticastClusterDisabled** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Enables or disables [*heartbeat*](https://www.bing.com/search?q=*heartbeat*) multicasting for all networks in a [*cluster*](https://www.bing.com/search?q=*cluster*) (subject to override by individual networks). The following table summarizes the attributes of the **MulticastClusterDisabled** property.



| Attribute | Value                                          |
|-----------|------------------------------------------------|
| Data type | **DWORD**                                      |
| Access    | [Read/write](read-write-properties.md)        |
| Status    | Optional                                       |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)      |
| Minimum   | 0 (multicast enabled)                          |
| Maximum   | any nonzero to 0xFFFFFFFF (multicast disabled) |
| Default   | 0 (multicast enabled)                          |



 

## Remarks

A network's [**MulticastDisabled**](networks-multicastdisabled.md) property overrides the cluster's **MulticastClusterDisabled** property for that particular network.

## Examples

The property value portion of a [property list](property-lists.md) entry for **MulticastClusterDisabled** can be set with the following example code.


```C++
DWORD          MulticastClusterDisabledData = 0;
CLUSPROP_DWORD MulticastClusterDisabledValue;

MulticastClusterDisabledValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
MulticastClusterDisabledValue.cbLength  = sizeof(DWORD);
MulticastClusterDisabledValue.dw        = MulticastClusterDisabledData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Private Properties](cluster-private-properties.md)
</dt> <dt>

[**MulticastAddress**](networks-multicastaddress.md)
</dt> <dt>

[**MulticastAddressRangeLower**](networks-multicastaddressrangelower.md)
</dt> <dt>

[**MulticastAddressRangeUpper**](networks-multicastaddressrangeupper.md)
</dt> <dt>

[**MulticastConfigType**](networks-multicastconfigtype.md)
</dt> <dt>

[**MulticastDisabled**](networks-multicastdisabled.md)
</dt> </dl>

 

 





