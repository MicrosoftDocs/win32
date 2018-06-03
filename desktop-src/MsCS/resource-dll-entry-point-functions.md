---
title: Resource DLL Entry-Point Functions
description: The resource DLL entry point functions are used by the Cluster service to indirectly initiate operations on cluster resources. These functions are implemented in resource DLLs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 933d7b97-b5be-4c84-a983-41d1fd935c19
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource DLL functions Failover Cluster ,entry point functions
- resource DLL functions Failover Cluster ,entry point functions,(See also entry point functions.)
- entry point functions Failover Cluster
- resource DLLs Failover Cluster ,implementing,(See also entry point functions)
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource DLL Entry-Point Functions

The resource DLL entry point functions are used by the [Cluster service](cluster-service.md) to indirectly initiate operations on cluster [resources](resources.md). These functions are implemented in resource DLLs.

For information about create resource DLLs, see [Creating Resource Types](creating-resource-types.md).

## In this section

<dl> <dt>

[*Arbitrate*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-parbitrate_routine)
</dt> <dd>

Allows a [node](nodes.md) to attempt to regain ownership of a [quorum resource](quorum-resource.md).

</dd> <dt>

[*BeginResourceControl*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pbegin_rescall_routine)
</dt> <dd>

Starts a call to a resource control code. The **PBEGIN\_RESCALL\_ROUTINE** type defines a pointer to this callback function.

</dd> <dt>

[*BeginResourceControlAsUser*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pbegin_rescall_as_user_routine)
</dt> <dd>

The **PBEGIN\_RESCALL\_AS\_USER\_ROUTINE** type defines a pointer to this callback function.

</dd> <dt>

[*BeginResourceTypeControl*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pbegin_restypecall_routine)
</dt> <dd>

Starts a call to a resource control code. The **PBEGIN\_RESTYPECALL\_ROUTINE** type defines a pointer to this callback function.

</dd> <dt>

[*BeginResourceTypeControlAsUser*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pbegin_restypecall_as_user_routine)
</dt> <dd>

The **PBEGIN\_RESTYPECALL\_AS\_USER\_ROUTINE** type defines a pointer to this callback function.

</dd> <dt>

[*Cancel*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pcancel_routine)
</dt> <dd>

Cancels an operation on a resource.

</dd> <dt>

[*PCLOSE\_ROUTINE*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pclose_routine)
</dt> <dd>

Closes a [resource](resources.md).

</dd> <dt>

[*IsAlive*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pis_alive_routine)
</dt> <dd>

Determines whether a [resource](resources.md) is available for use.

</dd> <dt>

[*LooksAlive*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-plooks_alive_routine)
</dt> <dd>

Determines whether a [resource](resources.md) appears to be available for use.

</dd> <dt>

[*Offline*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-poffline_routine)
</dt> <dd>

Marks a [resource](resources.md) as unavailable for use after cleanup processing is complete.

</dd> <dt>

[*OfflineV2*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-poffline_v2_routine)
</dt> <dd>

Marks a [resource](resources.md) as unavailable for use after cleanup processing is complete.

</dd> <dt>

[*Online*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-ponline_routine)
</dt> <dd>

Marks a [resource](resources.md) as available for use.

</dd> <dt>

[*OnlineV2*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-ponline_v2_routine)
</dt> <dd>

Marks a [resource](resources.md) as available for use.

</dd> <dt>

[*Open*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-popen_routine)
</dt> <dd>

Opens a [resource](resources.md).

</dd> <dt>

[*OpenV2*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-popen_v2_routine)
</dt> <dd>

Opens a [resource](resources.md).

</dd> <dt>

[*PRELEASE\_ROUTINE*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-prelease_routine)
</dt> <dd>

Releases the [quorum resource](quorum-resource.md) from arbitration.

</dd> <dt>

[*ResourceControl*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine)
</dt> <dd>

Performs an operation that applies to a [resource](resources.md).

</dd> <dt>

[*ResourceTypeControl*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine)
</dt> <dd>

Performs an operation that applies to a [resource type](resource-types.md).

</dd> <dt>

[*Startup*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pstartup_routine)
</dt> <dd>

Loads a [resource DLL](resource-dlls.md), returning a structure containing a function table and a version number.

</dd> <dt>

[*StartupEx*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pstartup_ex_routine)
</dt> <dd>

Loads a [resource DLL](resource-dlls.md), returning a structure that contains a function table and a version number.

</dd> <dt>

[*Terminate*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pterminate_routine)
</dt> <dd>

Immediately marks a [resource](resources.md) as unavailable for use without waiting for cleanup processing to be completed.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Functions](failover-cluster-functions.md)
</dt> </dl>

 

 




