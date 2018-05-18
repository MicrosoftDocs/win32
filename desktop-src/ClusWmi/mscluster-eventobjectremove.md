---
title: MSCluster\_EventObjectRemove class
description: The MSCluster\_EventObjectRemove class is a WMI class that represents a remove object event. A remove object event is generated when a cluster object is removed from a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c1e90009-cd2d-47ec-9056-6001c882f0dd'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_EventObjectRemove class", "MSCluster_EventObjectRemove class, described"]
topic_type:
- apiref
api_name:
- MSCluster_EventObjectRemove
- MSCluster_EventObjectRemove.SECURITY_DESCRIPTOR
- MSCluster_EventObjectRemove.TIME_CREATED
- MSCluster_EventObjectRemove.EventTypeMajor
- MSCluster_EventObjectRemove.EventTypeMinor
- MSCluster_EventObjectRemove.EventObjectName
- MSCluster_EventObjectRemove.EventObjectType
- MSCluster_EventObjectRemove.EventObjectPath
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_EventObjectRemove class

The **MSCluster\_EventObjectRemove** class is a [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a remove object event. A remove object event is generated when a cluster object is removed from a [*cluster*](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly).

The following syntax is simplified from MOF code, and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{F12EA54A-75FE-43c9-ACE4-5745D1CA0552}")]
class MSCluster_EventObjectRemove : MSCluster_Event
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  uint32 EventTypeMajor;
  uint32 EventTypeMinor;
  string EventObjectName;
  uint32 EventObjectType;
  string EventObjectPath;
};
```

## Members

The **MSCluster\_EventObjectRemove** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_EventObjectRemove** class has these properties.

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

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634). For more information about constants used to set this security descriptor, see [WMI Security Constants](https://msdn.microsoft.com/library/aa394576).

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

The **MSCluster\_EventObjectRemove** class is derived from the [**MSCluster\_Event**](mscluster-event.md) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



 

 





