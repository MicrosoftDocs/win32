---
title: Resource DLL Structures
description: The resource DLL structures contain information for resource DLL operations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9ab4b974-28b5-4f33-a7c4-b9b2472059aa'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource DLL structures Failover Cluster", "structures Failover Cluster ,resource DLL", "resource DLLs Failover Cluster ,structures"]
---

# Resource DLL Structures

The resource DLL structures contain information for resource DLL operations.

## In this section

<dl> <dt>

[**CLRES\_CALLBACK\_FUNCTION\_TABLE**](clres-callback-function-table.md)
</dt> <dd>

Represents a function table for the [*StartupEx*](startupex.md) callback function.

</dd> <dt>

[**CLRES\_FUNCTION\_TABLE**](clres-function-table.md)
</dt> <dd>

Describes a function table for any version of the [Resource API](resource-api.md).

</dd> <dt>

[**CLRES\_V1\_FUNCTIONS**](clres-v1-functions.md)
</dt> <dd>

Contains pointers to all [Resource API](resource-api.md) version 1.0 entry points except [**Startup**](startup.md).

</dd> <dt>

[**CLRES\_V2\_FUNCTIONS**](clres-v2-functions.md)
</dt> <dd>

Contains pointers to all [Resource API](resource-api.md) version 2.0 entry points except [*StartupEx*](startupex.md).

</dd> <dt>

[**CLRES\_V3\_FUNCTIONS**](clres-v3-functions.md)
</dt> <dd>

Contains pointers to all [Resource API](resource-api.md) version 3.0 entry points, except [*StartupEx*](startupex.md).

</dd> <dt>

[**CLRES\_V4\_FUNCTIONS**](clres-v4-functions.md)
</dt> <dd>

Contains pointers to all [Resource API](resource-api.md) version 4.0 entry points, except [*StartupEx*](startupex.md).

</dd> <dt>

[**GET\_OPERATION\_CONTEXT\_PARAMS**](get-operation-context-params.md)
</dt> <dd>

Represents context parameters that are used as input for the [CLUSCTL\_RESOURCE\_GET\_OPERATION\_CONTEXT](clusctl-resource-get-operation-context.md) control code.

</dd> <dt>

[**HCLUSCRYPTPROVIDER**](hcluscryptprovider.md)
</dt> <dd>

Represents a handle to a Cryptographic Service Provider that is used for [Checkpointing](checkpointing.md).

</dd> <dt>

[**MONITOR\_STATE**](monitor-state.md)
</dt> <dd>

TBD

</dd> <dt>

[**PaxosTagCStruct**](paxostagcstruct.md)
</dt> <dd>

Contains the Paxos tag values of a cluster node, which stores information about the cluster configuration version of the node when the cluster uses a File Share witness.

</dd> <dt>

[**POST\_UPGRADE\_VERSION\_INFO**](post-upgrade-version-info.md)
</dt> <dd>

Represents post-upgrade state information for the cluster service.

</dd> <dt>

[**RESOURCE\_STATUS**](resource-status.md)
</dt> <dd>

Contains information about a [resource](resources.md) that is being brought online or taken offline. This structure is used as a parameter to the callback function [**SetResourceStatus**](setresourcestatus.md).

</dd> <dt>

[**RESOURCE\_STATUS\_EX**](resource-status-ex.md)
</dt> <dd>

Contains information about a [resource](resources.md) that is being brought online or taken offline. This structure is used as a parameter to the callback function [*SetResourceStatusEx*](setresourcestatusex.md).

</dd> <dt>

[**WitnessTagHelper**](witnesstaghelper.md)
</dt> <dd>

Contains information used to validate a [**PaxosTagCStruct**](paxostagcstruct.md) structure.

</dd> <dt>

[**WitnessTagUpdateHelper**](witnesstagupdatehelper.md)
</dt> <dd>

Contains information used to update and validate a [**PaxosTagCStruct**](paxostagcstruct.md) structure.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Structures](cluster-structures.md)
</dt> </dl>

 

 




