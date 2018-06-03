---
title: Using the Information Interfaces
description: Your implementations of the Failover Cluster Administrator extension interfaces can use the Failover Cluster Administrator information interfaces to gather information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9057081e-3e3f-49c4-a0fc-006608cedfe2
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Failover Cluster Administrator Failover Cluster ,Failover Cluster Administrator Extension API,information interfaces,using
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using the Information Interfaces

\[Support for Failover Cluster Administrator extension DLLs was removed in Windows Server 2008.\]

Your implementations of the [Failover Cluster Administrator extension interfaces](cluster-administrator-extension-interfaces.md) can use the [Failover Cluster Administrator information interfaces](cluster-administrator-information-interfaces.md) to gather information. Note the following restrictions:

-   [**IGetClusterUIInfo**](/previous-versions/windows/desktop/api/cluadmex/nn-cluadmex-igetclusteruiinfo), [**IGetClusterObjectInfo**](/previous-versions/windows/desktop/api/cluadmex/nn-cluadmex-igetclusterobjectinfo), and [**IGetClusterDataInfo**](/previous-versions/windows/desktop/api/cluadmex/nn-cluadmex-igetclusterdatainfo) can be called by any extension DLL.
-   [**IGetClusterGroupInfo**](/previous-versions/windows/desktop/api/cluadmex/nn-cluadmex-igetclustergroupinfo) should be called only by extension DLLs that are extending [groups](groups.md).
-   [**IGetClusterNetworkInfo**](/previous-versions/windows/desktop/api/cluadmex/nn-cluadmex-igetclusternetworkinfo) should be called only by extension DLLs that are extending [networks](networks.md).
-   [**IGetClusterNetInterfaceInfo**](/previous-versions/windows/desktop/api/cluadmex/nn-cluadmex-igetclusternetinterfaceinfo) should be called only by extension DLLs that are extending [network interfaces](network-interfaces.md).
-   [**IGetClusterNodeInfo**](/previous-versions/windows/desktop/api/cluadmex/nn-cluadmex-igetclusternodeinfo) should be called only by extension DLLs that are extending [nodes](nodes.md).
-   [**IGetClusterResourceInfo**](/previous-versions/windows/desktop/api/cluadmex/nn-cluadmex-igetclusterresourceinfo) should be called only by extension DLLs that are extending [resources](resources.md).

 

 




