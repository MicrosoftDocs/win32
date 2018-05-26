---
title: LeaseObtainedTime
description: Contains the time that the current DHCP lease was obtained.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 71a3fae2-8c93-4a11-af07-0a2043c34106
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- LeaseObtainedsTime Failover Cluster , for IPv4 Address private properties
- LeaseObtainedTime Failover Cluster
topic_type:
- apiref
api_name:
- LeaseObtainedTime
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LeaseObtainedTime

Contains the time that the current DHCP lease was obtained. The following table summarizes the attributes of the **LeaseObtainedTime** property.



| Attribute | Value                                           |
|-----------|-------------------------------------------------|
| Data type | [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284)               |
| Access    | [Read-only](read-only-properties.md)           |
| Status    | Optional                                        |
| Structure | [**CLUSPROP\_FILETIME**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_filetime?branch=master) |
| Minimum   | 0                                               |
| Maximum   | 0                                               |
| Default   | {{ 0, 0 },{ 0, 0 },{ 0xFFFFFFFF, 0xFFFFFFFF },} |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_IPADDR\_LEASE\_OBTAINED\_TIME**.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[IP Address Private Properties](ip-address-private-properties.md)
</dt> <dt>

[**CLUSPROP\_FILETIME**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_filetime?branch=master)
</dt> <dt>

[**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284)
</dt> </dl>

 

 





