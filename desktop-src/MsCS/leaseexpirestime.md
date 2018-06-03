---
title: LeaseExpiresTime
description: Contains the time that the DHCP lease will expire.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f6d298e7-afce-4fa3-9560-22b47e4d29ec
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- LeaseExpiresTime Failover Cluster , for IPv4 Address private properties
- LeaseExpiresTime Failover Cluster
topic_type:
- apiref
api_name:
- LeaseExpiresTime
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LeaseExpiresTime

Contains the time that the DHCP lease will expire. The following table summarizes the attributes of the **LeaseExpiresTime** property.



| Attribute | Value                                           |
|-----------|-------------------------------------------------|
| Data type | [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284)               |
| Access    | [Read-only](read-only-properties.md)           |
| Status    | Optional                                        |
| Structure | [**CLUSPROP\_FILETIME**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_filetime) |
| Minimum   | 0                                               |
| Maximum   | 0                                               |
| Default   | {{ 0, 0 },{ 0, 0 },{ 0xFFFFFFFF, 0xFFFFFFFF },} |



 

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[IP Address Private Properties](ip-address-private-properties.md)
</dt> <dt>

[**CLUSPROP\_FILETIME**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_filetime)
</dt> <dt>

[**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284)
</dt> </dl>

 

 





