---
title: OverrideAddressMatch
description: Allows IP address resources to be on any network if set to 1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a2d0fe51-d140-4c0f-b270-25fbfaab50fd
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- OverrideAddressMatch Failover Cluster , for IPv4 Address private properties
- OverrideAddressMatch Failover Cluster
topic_type:
- apiref
api_name:
- OverrideAddressMatch
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OverrideAddressMatch

Allows IP address resources to be on any network if set to 1. The default value (0) only allows IP address resource on a network in the valid subnet range specified by [**SubnetMask**](ip-addresses-subnetmask.md). The following table summarizes the attributes of the **OverrideAddressMatch** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | (0)                                       |
| Maximum   | (1)                                       |
| Default   | (0)                                       |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **OverrideAddressMatch** can be set with the following example code.


```C++
DWORD          OverrideAddressMatchData = 0;
CLUSPROP_DWORD OverrideAddressMatchValue;

OverrideAddressMatchValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
OverrideAddressMatchValue.cbLength  = sizeof(DWORD);
OverrideAddressMatchValue.dw        = OverrideAddressMatchData;
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

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





