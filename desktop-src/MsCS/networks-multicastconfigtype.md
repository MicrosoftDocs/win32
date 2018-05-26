---
title: MulticastConfigType
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 338796e4-b7eb-4def-9c48-c405c3a8ab02
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MulticastConfigType Failover Cluster , for networks
- MulticastConfigType Failover Cluster
topic_type:
- apiref
api_name:
- MulticastConfigType
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MulticastConfigType

\[The **MulticastConfigType** property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2003:  **

Specifies whether a [network's](networks.md) [*heartbeat*](h-gly.md#-wolf-heartbeat-gly) multicast address was set manually, obtained from Multicast Address Dynamic Client Allocation Protocol (MADCAP), or chosen by the [*cluster*](c-gly.md#-wolf-cluster-gly). The following table summarizes the attributes of the **MulticastConfigType** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | Required                                  |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 0                                         |
| Maximum   | 2                                         |
| Default   | 0                                         |



 

## Remarks

**MulticastConfigType** can have one of the following values.



| MulticastConfigType value | MulticastAddress configuration |
|---------------------------|--------------------------------|
| 0                         | manual                         |
| 1                         | MADCAP                         |
| 2                         | cluster                        |



 

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[**MulticastAddress**](networks-multicastaddress.md)
</dt> <dt>

[**MulticastAddressRangeLower**](networks-multicastaddressrangelower.md)
</dt> <dt>

[**MulticastAddressRangeUpper**](networks-multicastaddressrangeupper.md)
</dt> <dt>

[**MulticastDisabled**](networks-multicastdisabled.md)
</dt> </dl>

 

 





