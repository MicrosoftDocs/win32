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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Resource DLL Structures

The resource DLL structures contain information for resource DLL operations.

## In this section

<dl> <dt>

[**CLRES\_CALLBACK\_FUNCTION\_TABLE**](/windows/previous-versions/ResApi/ns-resapi-clres_callback_function_table?branch=master)
</dt> <dd>

Represents a function table for the [*StartupEx*](/windows/previous-versions/ResApi/nc-resapi-pstartup_ex_routine?branch=master) callback function.

</dd> <dt>

[**CLRES\_FUNCTION\_TABLE**](/windows/previous-versions/ResApi/ns-resapi-clres_function_table?branch=master)
</dt> <dd>

Describes a function table for any version of the [Resource API](resource-api.md).

</dd> <dt>

[**CLRES\_V1\_FUNCTIONS**](/windows/previous-versions/ResApi/ns-resapi-clres_v1_functions?branch=master)
</dt> <dd>

Contains pointers to all [Resource API](resource-api.md) version 1.0 entry points except [**Startup**](/windows/previous-versions/ResApi/nc-resapi-pstartup_routine?branch=master).

</dd> <dt>

[**CLRES\_V2\_FUNCTIONS**](/windows/previous-versions/ResApi/ns-resapi-clres_v2_functions?branch=master)
</dt> <dd>

Contains pointers to all [Resource API](resource-api.md) version 2.0 entry points except [*StartupEx*](/windows/previous-versions/ResApi/nc-resapi-pstartup_ex_routine?branch=master).

</dd> <dt>

[**CLRES\_V3\_FUNCTIONS**](/windows/previous-versions/ResApi/ns-resapi-clres_v3_functions?branch=master)
</dt> <dd>

Contains pointers to all [Resource API](resource-api.md) version 3.0 entry points, except [*StartupEx*](/windows/previous-versions/ResApi/nc-resapi-pstartup_ex_routine?branch=master).

</dd> <dt>

[**CLRES\_V4\_FUNCTIONS**](/windows/previous-versions/ResApi/ns-resapi-clres_v4_functions?branch=master)
</dt> <dd>

Contains pointers to all [Resource API](resource-api.md) version 4.0 entry points, except [*StartupEx*](/windows/previous-versions/ResApi/nc-resapi-pstartup_ex_routine?branch=master).

</dd> <dt>

[**GET\_OPERATION\_CONTEXT\_PARAMS**](/windows/previous-versions/ResApi/ns-resapi-get_operation_context_params?branch=master)
</dt> <dd>

Represents context parameters that are used as input for the [CLUSCTL\_RESOURCE\_GET\_OPERATION\_CONTEXT](clusctl-resource-get-operation-context.md) control code.

</dd> <dt>

[**HCLUSCRYPTPROVIDER**](/windows/previous-versions/ResApi/?branch=master)
</dt> <dd>

Represents a handle to a Cryptographic Service Provider that is used for [Checkpointing](checkpointing.md).

</dd> <dt>

[**MONITOR\_STATE**](/windows/previous-versions/ResApi/ns-resapi-monitor_state?branch=master)
</dt> <dd>

TBD

</dd> <dt>

[**PaxosTagCStruct**](/windows/previous-versions/ResApi/ns-resapi-_paxostagcstruct?branch=master)
</dt> <dd>

Contains the Paxos tag values of a cluster node, which stores information about the cluster configuration version of the node when the cluster uses a File Share witness.

</dd> <dt>

[**POST\_UPGRADE\_VERSION\_INFO**](/windows/previous-versions/ResApi/ns-resapi-post_upgrade_version_info?branch=master)
</dt> <dd>

Represents post-upgrade state information for the cluster service.

</dd> <dt>

[**RESOURCE\_STATUS**](/windows/previous-versions/ResApi/ns-resapi-resource_status?branch=master)
</dt> <dd>

Contains information about a [resource](resources.md) that is being brought online or taken offline. This structure is used as a parameter to the callback function [**SetResourceStatus**](/windows/previous-versions/ResApi/nc-resapi-pset_resource_status_routine?branch=master).

</dd> <dt>

[**RESOURCE\_STATUS\_EX**](/windows/previous-versions/ResApi/ns-resapi-resource_status_ex?branch=master)
</dt> <dd>

Contains information about a [resource](resources.md) that is being brought online or taken offline. This structure is used as a parameter to the callback function [*SetResourceStatusEx*](/windows/previous-versions/ResApi/nc-resapi-pset_resource_status_routine_ex?branch=master).

</dd> <dt>

[**WitnessTagHelper**](/windows/previous-versions/ResApi/ns-resapi-_witnesstaghelper?branch=master)
</dt> <dd>

Contains information used to validate a [**PaxosTagCStruct**](/windows/previous-versions/ResApi/ns-resapi-_paxostagcstruct?branch=master) structure.

</dd> <dt>

[**WitnessTagUpdateHelper**](/windows/previous-versions/ResApi/ns-resapi-_witnesstagupdatehelper?branch=master)
</dt> <dd>

Contains information used to update and validate a [**PaxosTagCStruct**](/windows/previous-versions/ResApi/ns-resapi-_paxostagcstruct?branch=master) structure.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Structures](cluster-structures.md)
</dt> </dl>

 

 




