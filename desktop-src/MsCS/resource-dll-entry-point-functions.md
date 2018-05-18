---
title: Resource DLL Entry-Point Functions
description: The resource DLL entry point functions are used by the Cluster service to indirectly initiate operations on cluster resources. These functions are implemented in resource DLLs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '933d7b97-b5be-4c84-a983-41d1fd935c19'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource DLL functions Failover Cluster ,entry point functions", "resource DLL functions Failover Cluster ,entry point functions,(See also entry point functions.)", "entry point functions Failover Cluster", "resource DLLs Failover Cluster ,implementing,(See also entry point functions)"]
---

# Resource DLL Entry-Point Functions

The resource DLL entry point functions are used by the [Cluster service](cluster-service.md) to indirectly initiate operations on cluster [resources](resources.md). These functions are implemented in resource DLLs.

For information about create resource DLLs, see [Creating Resource Types](creating-resource-types.md).

## In this section

<dl> <dt>

[*Arbitrate*](arbitrate.md)
</dt> <dd>

Allows a [node](nodes.md) to attempt to regain ownership of a [quorum resource](quorum-resource.md).

</dd> <dt>

[*BeginResourceControl*](beginresourcecontrol.md)
</dt> <dd>

Starts a call to a resource control code. The **PBEGIN\_RESCALL\_ROUTINE** type defines a pointer to this callback function.

</dd> <dt>

[*BeginResourceControlAsUser*](beginresourcecontrolasuser.md)
</dt> <dd>

The **PBEGIN\_RESCALL\_AS\_USER\_ROUTINE** type defines a pointer to this callback function.

</dd> <dt>

[*BeginResourceTypeControl*](beginresourcetypecontrol.md)
</dt> <dd>

Starts a call to a resource control code. The **PBEGIN\_RESTYPECALL\_ROUTINE** type defines a pointer to this callback function.

</dd> <dt>

[*BeginResourceTypeControlAsUser*](beginresourcetypecontrolasuser.md)
</dt> <dd>

The **PBEGIN\_RESTYPECALL\_AS\_USER\_ROUTINE** type defines a pointer to this callback function.

</dd> <dt>

[*Cancel*](cancel.md)
</dt> <dd>

Cancels an operation on a resource.

</dd> <dt>

[*PCLOSE\_ROUTINE*](close.md)
</dt> <dd>

Closes a [resource](resources.md).

</dd> <dt>

[*IsAlive*](isalive.md)
</dt> <dd>

Determines whether a [resource](resources.md) is available for use.

</dd> <dt>

[*LooksAlive*](looksalive.md)
</dt> <dd>

Determines whether a [resource](resources.md) appears to be available for use.

</dd> <dt>

[*Offline*](offline.md)
</dt> <dd>

Marks a [resource](resources.md) as unavailable for use after cleanup processing is complete.

</dd> <dt>

[*OfflineV2*](offlinev2.md)
</dt> <dd>

Marks a [resource](resources.md) as unavailable for use after cleanup processing is complete.

</dd> <dt>

[*Online*](online.md)
</dt> <dd>

Marks a [resource](resources.md) as available for use.

</dd> <dt>

[*OnlineV2*](onlinev2.md)
</dt> <dd>

Marks a [resource](resources.md) as available for use.

</dd> <dt>

[*Open*](open.md)
</dt> <dd>

Opens a [resource](resources.md).

</dd> <dt>

[*OpenV2*](openv2.md)
</dt> <dd>

Opens a [resource](resources.md).

</dd> <dt>

[*PRELEASE\_ROUTINE*](release.md)
</dt> <dd>

Releases the [quorum resource](quorum-resource.md) from arbitration.

</dd> <dt>

[*ResourceControl*](resourcecontrol.md)
</dt> <dd>

Performs an operation that applies to a [resource](resources.md).

</dd> <dt>

[*ResourceTypeControl*](resourcetypecontrol.md)
</dt> <dd>

Performs an operation that applies to a [resource type](resource-types.md).

</dd> <dt>

[*Startup*](startup.md)
</dt> <dd>

Loads a [resource DLL](resource-dlls.md), returning a structure containing a function table and a version number.

</dd> <dt>

[*StartupEx*](startupex.md)
</dt> <dd>

Loads a [resource DLL](resource-dlls.md), returning a structure that contains a function table and a version number.

</dd> <dt>

[*Terminate*](terminate.md)
</dt> <dd>

Immediately marks a [resource](resources.md) as unavailable for use without waiting for cleanup processing to be completed.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Functions](failover-cluster-functions.md)
</dt> </dl>

 

 




