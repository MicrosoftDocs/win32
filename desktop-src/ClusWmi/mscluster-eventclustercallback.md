---
title: MSCluster\_EventClusterCallback class
description: TBD
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f6ff92b7-608f-423c-9977-364a8eb44cec'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_EventClusterCallback class", "MSCluster_EventClusterCallback class, described"]
topic_type:
- apiref
api_name:
- MSCluster_EventClusterCallback
- MSCluster_EventClusterCallback.SECURITY_DESCRIPTOR
- MSCluster_EventClusterCallback.TIME_CREATED
- MSCluster_EventClusterCallback.EventTypeMajor
- MSCluster_EventClusterCallback.EventTypeMinor
- MSCluster_EventClusterCallback.EventObjectName
- MSCluster_EventClusterCallback.EventObjectType
- MSCluster_EventClusterCallback.EventObjectPath
- MSCluster_EventClusterCallback.SetupPhase
- MSCluster_EventClusterCallback.PhaseType
- MSCluster_EventClusterCallback.PhaseSeverity
- MSCluster_EventClusterCallback.PercentComplete
- MSCluster_EventClusterCallback.ObjectName
- MSCluster_EventClusterCallback.Status
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_EventClusterCallback class

TBD

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{5F9229F6-DF68-4115-818A-315A8AF93AA7}"), AMENDMENT]
class MSCluster_EventClusterCallback : MSCluster_Event
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  uint32 EventTypeMajor;
  uint32 EventTypeMinor;
  string EventObjectName;
  uint32 EventObjectType;
  string EventObjectPath;
  sint32 SetupPhase;
  sint32 PhaseType;
  sint32 PhaseSeverity;
  sint32 PercentComplete;
  string ObjectName;
  sint32 Status;
};
```

## Members

The **MSCluster\_EventClusterCallback** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_EventClusterCallback** class has these properties.

<dl> <dt>

**EventObjectName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the name of the object to which this event applies.

This property is inherited from [**MSCluster\_Event**](mscluster-event.md).

</dd> <dt>

**EventObjectPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the WMI path of the object to which this event applies.

This property is inherited from [**MSCluster\_Event**](mscluster-event.md).

</dd> <dt>

**EventObjectType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

<dt>

0
</dt> <dd>

Handle

</dd> <dt>

1
</dt> <dd>

Cluster

</dd> <dt>

2
</dt> <dd>

Node

</dd> <dt>

3
</dt> <dd>

Group

</dd> <dt>

4
</dt> <dd>

Resources

</dd> <dt>

5
</dt> <dd>

Resource type

</dd> <dt>

6
</dt> <dd>

Network

</dd> <dt>

7
</dt> <dd>

Network interface

</dd> <dt>

8
</dt> <dd>

Registry

</dd> <dt>

9
</dt> <dd>

Quorum

</dd> </dl>

Provides the type of object to which this event applies.

This property is inherited from [**MSCluster\_Event**](mscluster-event.md).

</dd> <dt>

**EventTypeMajor**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the major event category. A value of 0 indicates an event returned by [**GetClusterNotify**](https://msdn.microsoft.com/library/aa369623).

This property is inherited from [**MSCluster\_Event**](mscluster-event.md).

</dd> <dt>

**EventTypeMinor**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the subtype within the major category. When the **EventTypeMajor** property is 0, this subtype contains the cluster event value that [**GetClusterNotify**](https://msdn.microsoft.com/library/aa369623) returns.

This property is inherited from [**MSCluster\_Event**](mscluster-event.md).

</dd> <dt>

**ObjectName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the name of the object.

</dd> <dt>

**PercentComplete**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the amount as a percent complete.

Range: 0–100

</dd> <dt>

**PhaseSeverity**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the current phase severity using a value from the [**CLUSTER\_SETUP\_PHASE\_SEVERITY**](https://msdn.microsoft.com/library/bb309174) enumeration.

<dt>

1
</dt> <dd>

Indicates that this phase of the cluster setup can complete successfully.

</dd> <dt>

2
</dt> <dd>

Indicates that this phase of the cluster setup can complete, with a warning.

</dd> <dt>

3
</dt> <dd>

Indicates that this phase of the cluster setup process cannot complete successfully.

</dd> </dl>

</dd> <dt>

**PhaseType**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the current phase type using a value from the [**CLUSTER\_SETUP\_PHASE\_TYPE**](https://msdn.microsoft.com/library/bb309175) enumeration.

<dt>

1
</dt> <dd>

Indicates the start of a new setup phase as provided by the **SetupPhase** property.

</dd> <dt>

2
</dt> <dd>

Indicates the continuation of a setup phase as provided by the **SetupPhase** property.

</dd> <dt>

3
</dt> <dd>

Called once at the end of every setup phase as provided by the **SetupPhase** property.

</dd> </dl>

</dd> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634). For more information about constants used to set this security descriptor, see [WMI Security Constants](https://msdn.microsoft.com/library/aa394576).

</dd> <dt>

**SetupPhase**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the current setup phase using a value enumerated from the [**CLUSTER\_SETUP\_PHASE**](https://msdn.microsoft.com/library/bb309173) enumeration.

<dt>

1
</dt> <dd>

Initialize cluster setup.

</dd> <dt>

100
</dt> <dd>

Validate cluster nodes.

</dd> <dt>

102
</dt> <dd>

Validate cluster networks.

</dd> <dt>

103
</dt> <dd>

Validate cluster disks.

</dd> <dt>

104
</dt> <dd>

Configure cluster service.

</dd> <dt>

105
</dt> <dd>

Start cluster service.

</dd> <dt>

106
</dt> <dd>

Query cluster name.

</dd> <dt>

107
</dt> <dd>

Validate cluster name.

</dd> <dt>

108
</dt> <dd>

Create cluster account.

</dd> <dt>

109
</dt> <dd>

Configure cluster account.

</dd> <dt>

200
</dt> <dd>

Form the cluster.

</dd> <dt>

201
</dt> <dd>

Add properties to cluster.

</dd> <dt>

202
</dt> <dd>

Create resource types.

</dd> <dt>

203
</dt> <dd>

Create resource groups.

</dd> <dt>

204
</dt> <dd>

Create IP address resources.

</dd> <dt>

205
</dt> <dd>

Create network name.

</dd> <dt>

206
</dt> <dd>

Bring cluster groups online.

</dd> <dt>

300
</dt> <dd>

Get current cluster membership.

</dd> <dt>

301
</dt> <dd>

Add node to cluster membership.

</dd> <dt>

302
</dt> <dd>

Start node.

</dd> <dt>

400
</dt> <dd>

Move group to another node.

</dd> <dt>

401
</dt> <dd>

Delete group from cluster.

</dd> <dt>

402
</dt> <dd>

Clean up offline group.

</dd> <dt>

403
</dt> <dd>

Move group offline.

</dd> <dt>

404
</dt> <dd>

Remove a node from the cluster.

</dd> <dt>

405
</dt> <dd>

Return node to pre-clustered state.

</dd> <dt>

406
</dt> <dd>

Return core resource group to pre-clustered state.

</dd> <dt>

999
</dt> <dd>

Return failed resource to pre-clustered state.

</dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the status.

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Times (UTC) format. This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> </dl>

## Remarks

The **MSCluster\_EventClusterCallback** class is derived from the [**MSCluster\_Event**](mscluster-event.md) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> <dt>

[**MSCluster\_Event**](mscluster-event.md)
</dt> <dt>

[**CLUSTER\_SETUP\_PHASE**](https://msdn.microsoft.com/library/bb309173)
</dt> <dt>

[**CLUSTER\_SETUP\_PHASE\_TYPE**](https://msdn.microsoft.com/library/bb309175)
</dt> <dt>

[**CLUSTER\_SETUP\_PHASE\_SEVERITY**](https://msdn.microsoft.com/library/bb309174)
</dt> <dt>

[*ClusterSetupProgressCallback*](https://msdn.microsoft.com/library/bb394687)
</dt> </dl>

 

 





