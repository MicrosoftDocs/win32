---
title: ResourceData
description: Stores the virtual computer objects encrypted password.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 932DFE64-BB76-4C55-AF4A-94E77FD5ADCF
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ResourceData Failover Cluster ,for virtual machine replication brokers
- ResourceData Failover Cluster
topic_type:
- apiref
api_name:
- ResourceData
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ResourceData

Stores the virtual computer object's encrypted password. The following table summarizes the attributes of the **ResourceData** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | byte array                                                       |
| Access    | [Read-only](read-only-properties.md)                            |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_BINARY**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_binary?branch=master)                      |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | 0                                                                |



 

## Remarks

Access to **ResourceData** is limited to the local administrator, system, and creator owner.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Virtual Machine Replication Broker Private Properties](virtual-machine-replication-broker-private-properties.md)
</dt> <dt>

[**CreatingDC**](virtual-machine-replication-brokers-creatingdc.md)
</dt> </dl>

 

 





