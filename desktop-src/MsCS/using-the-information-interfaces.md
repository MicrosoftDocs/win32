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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using the Information Interfaces

\[Support for Failover Cluster Administrator extension DLLs was removed in Windows Server 2008.\]

Your implementations of the [Failover Cluster Administrator extension interfaces](cluster-administrator-extension-interfaces.md) can use the [Failover Cluster Administrator information interfaces](cluster-administrator-information-interfaces.md) to gather information. Note the following restrictions:

-   [**IGetClusterUIInfo**](/windows/previous-versions/cluadmex/nn-cluadmex-igetclusteruiinfo?branch=master), [**IGetClusterObjectInfo**](/windows/previous-versions/cluadmex/nn-cluadmex-igetclusterobjectinfo?branch=master), and [**IGetClusterDataInfo**](/windows/previous-versions/cluadmex/nn-cluadmex-igetclusterdatainfo?branch=master) can be called by any extension DLL.
-   [**IGetClusterGroupInfo**](/windows/previous-versions/cluadmex/nn-cluadmex-igetclustergroupinfo?branch=master) should be called only by extension DLLs that are extending [groups](groups.md).
-   [**IGetClusterNetworkInfo**](/windows/previous-versions/cluadmex/nn-cluadmex-igetclusternetworkinfo?branch=master) should be called only by extension DLLs that are extending [networks](networks.md).
-   [**IGetClusterNetInterfaceInfo**](/windows/previous-versions/cluadmex/nn-cluadmex-igetclusternetinterfaceinfo?branch=master) should be called only by extension DLLs that are extending [network interfaces](network-interfaces.md).
-   [**IGetClusterNodeInfo**](/windows/previous-versions/cluadmex/nn-cluadmex-igetclusternodeinfo?branch=master) should be called only by extension DLLs that are extending [nodes](nodes.md).
-   [**IGetClusterResourceInfo**](/windows/previous-versions/cluadmex/nn-cluadmex-igetclusterresourceinfo?branch=master) should be called only by extension DLLs that are extending [resources](resources.md).

 

 




