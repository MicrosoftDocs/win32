---
title: Resource DLL Structures
description: The resource DLL structures contain information for resource DLL operations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9ab4b974-28b5-4f33-a7c4-b9b2472059aa
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource DLL structures Failover Cluster
- structures Failover Cluster ,resource DLL
- resource DLLs Failover Cluster ,structures
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource DLL Structures

The resource DLL structures contain information for resource DLL operations.

## In this section

<dl> <dt>

[**CLRES\_CALLBACK\_FUNCTION\_TABLE**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-clres_callback_function_table)
</dt> <dd>

Represents a function table for the [*StartupEx*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pstartup_ex_routine) callback function.

</dd> <dt>

[**CLRES\_FUNCTION\_TABLE**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-clres_function_table)
</dt> <dd>

Describes a function table for any version of the [Resource API](resource-api.md).

</dd> <dt>

[**CLRES\_V1\_FUNCTIONS**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-clres_v1_functions)
</dt> <dd>

Contains pointers to all [Resource API](resource-api.md) version 1.0 entry points except [**Startup**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pstartup_routine).

</dd> <dt>

[**CLRES\_V2\_FUNCTIONS**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-clres_v2_functions)
</dt> <dd>

Contains pointers to all [Resource API](resource-api.md) version 2.0 entry points except [*StartupEx*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pstartup_ex_routine).

</dd> <dt>

[**CLRES\_V3\_FUNCTIONS**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-clres_v3_functions)
</dt> <dd>

Contains pointers to all [Resource API](resource-api.md) version 3.0 entry points, except [*StartupEx*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pstartup_ex_routine).

</dd> <dt>

[**CLRES\_V4\_FUNCTIONS**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-clres_v4_functions)
</dt> <dd>

Contains pointers to all [Resource API](resource-api.md) version 4.0 entry points, except [*StartupEx*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pstartup_ex_routine).

</dd> <dt>

[**GET\_OPERATION\_CONTEXT\_PARAMS**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-get_operation_context_params)
</dt> <dd>

Represents context parameters that are used as input for the [CLUSCTL\_RESOURCE\_GET\_OPERATION\_CONTEXT](clusctl-resource-get-operation-context.md) control code.

</dd> <dt>

[**HCLUSCRYPTPROVIDER**](/previous-versions/windows/desktop/api/ResApi/)
</dt> <dd>

Represents a handle to a Cryptographic Service Provider that is used for [Checkpointing](checkpointing.md).

</dd> <dt>

[**MONITOR\_STATE**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-monitor_state)
</dt> <dd>

TBD

</dd> <dt>

[**PaxosTagCStruct**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-_paxostagcstruct)
</dt> <dd>

Contains the Paxos tag values of a cluster node, which stores information about the cluster configuration version of the node when the cluster uses a File Share witness.

</dd> <dt>

[**POST\_UPGRADE\_VERSION\_INFO**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-post_upgrade_version_info)
</dt> <dd>

Represents post-upgrade state information for the cluster service.

</dd> <dt>

[**RESOURCE\_STATUS**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-resource_status)
</dt> <dd>

Contains information about a [resource](resources.md) that is being brought online or taken offline. This structure is used as a parameter to the callback function [**SetResourceStatus**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pset_resource_status_routine).

</dd> <dt>

[**RESOURCE\_STATUS\_EX**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-resource_status_ex)
</dt> <dd>

Contains information about a [resource](resources.md) that is being brought online or taken offline. This structure is used as a parameter to the callback function [*SetResourceStatusEx*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pset_resource_status_routine_ex).

</dd> <dt>

[**WitnessTagHelper**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-_witnesstaghelper)
</dt> <dd>

Contains information used to validate a [**PaxosTagCStruct**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-_paxostagcstruct) structure.

</dd> <dt>

[**WitnessTagUpdateHelper**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-_witnesstagupdatehelper)
</dt> <dd>

Contains information used to update and validate a [**PaxosTagCStruct**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-_paxostagcstruct) structure.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Structures](cluster-structures.md)
</dt> </dl>

 

 




