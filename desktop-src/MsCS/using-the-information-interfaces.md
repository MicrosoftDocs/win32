---
title: Using the Information Interfaces
description: Your implementations of the Failover Cluster Administrator extension interfaces can use the Failover Cluster Administrator information interfaces to gather information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9057081e-3e3f-49c4-a0fc-006608cedfe2'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Failover Cluster Administrator Failover Cluster ,Failover Cluster Administrator Extension API,information interfaces,using"]
---

# Using the Information Interfaces

\[Support for Failover Cluster Administrator extension DLLs was removed in Windows Server 2008.\]

Your implementations of the [Failover Cluster Administrator extension interfaces](cluster-administrator-extension-interfaces.md) can use the [Failover Cluster Administrator information interfaces](cluster-administrator-information-interfaces.md) to gather information. Note the following restrictions:

-   [**IGetClusterUIInfo**](igetclusteruiinfo.md), [**IGetClusterObjectInfo**](igetclusterobjectinfo.md), and [**IGetClusterDataInfo**](igetclusterdatainfo.md) can be called by any extension DLL.
-   [**IGetClusterGroupInfo**](igetclustergroupinfo.md) should be called only by extension DLLs that are extending [groups](groups.md).
-   [**IGetClusterNetworkInfo**](igetclusternetworkinfo.md) should be called only by extension DLLs that are extending [networks](networks.md).
-   [**IGetClusterNetInterfaceInfo**](igetclusternetinterfaceinfo.md) should be called only by extension DLLs that are extending [network interfaces](network-interfaces.md).
-   [**IGetClusterNodeInfo**](igetclusternodeinfo.md) should be called only by extension DLLs that are extending [nodes](nodes.md).
-   [**IGetClusterResourceInfo**](igetclusterresourceinfo.md) should be called only by extension DLLs that are extending [resources](resources.md).

 

 




