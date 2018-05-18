---
title: Adapter
description: Provides the name that is used to uniquely identify the network interface in the cluster. The following table summarizes the attributes of the Adapter property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ae43648b-2d35-4775-9604-ec2f9b707f32'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Adapter Failover Cluster ,for network interfaces", "Adapter Failover Cluster"]
topic_type:
- apiref
api_name:
- Adapter
api_type:
- NA
---

# Adapter

Provides the name that is used to uniquely identify the [network interface](network-interfaces.md) in the [*cluster*](c-gly.md#-wolf-cluster-gly). The following table summarizes the attributes of the **Adapter** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

Because the **Adapter** property is read-only, it cannot be changed using the [CLUSCTL\_NETINTERFACE\_SET\_COMMON\_PROPERTIES](clusctl-netinterface-set-common-properties.md) control code.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[CLUSCTL\_NETINTERFACE\_SET\_COMMON\_PROPERTIES](clusctl-netinterface-set-common-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> </dl>

 

 





