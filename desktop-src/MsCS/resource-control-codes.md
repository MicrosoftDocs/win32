---
title: Resource Control Codes
description: Resource control code usage in the Failover Cluster API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 71ec60fd-67ec-4932-983b-f78c6b552954
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource control codes Failover Cluster
- control codes Failover Cluster ,resource
- resources Failover Cluster ,control codes
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource Control Codes

Resource control codes are used in the following ways:

-   Applications use [*external control codes*](https://www.bing.com/search?q=*external control codes*) as [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) parameters to initiate operations on a [resource](resources.md).
-   Resource DLLs receive both external and [*internal control codes*](https://www.bing.com/search?q=*internal control codes*) as parameters to the [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) entry point function. A resource DLL may implement special procedures in response to a control code, depending on the control code and the needs of the resources it manages.

To support both application and DLL developers, each resource control code presents information on how to use the code in a control code function and how to support it in a resource DLL.

For more information, refer to the following topics:

-   [External Resource Control Codes](external-resource-control-codes.md)
-   [Internal Resource Control Codes](internal-resource-control-codes.md)

Resource control codes use the **CLUS\_OBJECT\_RESOURCE** value of the [**CLUSTER\_CONTROL\_OBJECT**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_control_object) enumeration to indicate that the control code applies to cluster resources. For more information about control codes, see [Control Code Architecture](control-code-architecture.md).

Resource control codes are enumerated by the [**CLUSCTL\_RESOURCE\_CODES**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clusctl_resource_codes) enumeration.

## Related topics

<dl> <dt>

[Control Codes](control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol)
</dt> </dl>

 

 




