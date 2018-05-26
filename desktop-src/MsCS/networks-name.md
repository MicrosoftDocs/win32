---
title: Name
description: Provides the name of the network. The following table summarizes the attributes of the Name property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f494788e-4581-4a1a-8b10-24b8715f5fce
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Name Failover Cluster ,for networks
- Name Failover Cluster
topic_type:
- apiref
api_name:
- Name
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Name

Provides the name of the [network](networks.md). The following table summarizes the attributes of the **Name** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

Because the **Name** property is read-only, it cannot be changed using the [CLUSCTL\_NETWORK\_SET\_COMMON\_PROPERTIES](clusctl-network-set-common-properties.md) control code. Applications can change a network's name only by calling [**SetClusterNetworkName**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_network_name?branch=master), which is one of the [network management functions](network-management-functions.md).

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[CLUSCTL\_NETWORK\_SET\_COMMON\_PROPERTIES](clusctl-network-set-common-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**SetClusterNetworkName**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_network_name?branch=master)
</dt> </dl>

 

 





