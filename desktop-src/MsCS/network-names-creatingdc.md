---
title: CreatingDC
description: Stores the name of the domain controller that was used by the Cluster service to obtain the VirtualServer Computer object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1c2c3440-9e34-484d-9820-406c2cb57e32
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CreatingDC Failover Cluster ,for network names
- CreatingDC Failover Cluster
topic_type:
- apiref
api_name:
- CreatingDC
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreatingDC

Stores the name of the domain controller that was used by the [Cluster service](cluster-service.md) to obtain the **VirtualServer** Computer object if the [**RequireKerberos**](network-names-requirekerberos.md)[Network Name](network-name.md) property is set to 1. The following table summarizes the attributes of the **CreatingDC** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

If [**RequireKerberos**](network-names-requirekerberos.md) is set to 0, the **CreatingDC** property is automatically set to **NULL**.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Name Private Properties](network-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**RequireDNS**](network-names-requiredns.md)
</dt> <dt>

[**RequireKerberos**](network-names-requirekerberos.md)
</dt> <dt>

[**ResourceData**](network-names-resourcedata.md)
</dt> </dl>

 

 





