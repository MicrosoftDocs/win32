---
title: Name
description: Provides the cluster-generated name for the network interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3bf22101-a59a-4b6d-b1dd-a39810650e08
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Name Failover Cluster ,for network interfaces
- Name Failover Cluster
topic_type:
- apiref
api_name:
- Name
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Name

Provides the cluster-generated name for the [network interface](network-interfaces.md). This name appears on the network interface's property sheets in [Cluster Administrator](cluster-administrator.md) and is the name passed to the [**OpenClusterNetInterface**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_net_interface) function. The following table summarizes the attributes of the **Name** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

Because the **Name** property is read-only, it cannot be changed using the [CLUSCTL\_NETINTERFACE\_SET\_COMMON\_PROPERTIES](clusctl-netinterface-set-common-properties.md) control code.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[CLUSCTL\_NETINTERFACE\_SET\_COMMON\_PROPERTIES](clusctl-netinterface-set-common-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**OpenClusterNetInterface**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_net_interface)
</dt> </dl>

 

 





