---
title: MSCluster\_EventGroupStateChange class
description: Represents a group state change event.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 41001fb6-3b22-4195-a580-69e6defbd5e2
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_EventGroupStateChange class
- MSCluster_EventGroupStateChange class, described
topic_type:
- apiref
api_name:
- MSCluster_EventGroupStateChange
- MSCluster_EventGroupStateChange.SECURITY_DESCRIPTOR
- MSCluster_EventGroupStateChange.TIME_CREATED
- MSCluster_EventGroupStateChange.EventTypeMajor
- MSCluster_EventGroupStateChange.EventTypeMinor
- MSCluster_EventGroupStateChange.EventObjectName
- MSCluster_EventGroupStateChange.EventObjectType
- MSCluster_EventGroupStateChange.EventObjectPath
- MSCluster_EventGroupStateChange.EventNewState
- MSCluster_EventGroupStateChange.EventNode
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSCluster\_EventGroupStateChange class

Represents a [group](https://msdn.microsoft.com/library/aa369645) state change event.

The following syntax is simplified from MOF code, and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{D264369A-3133-45eb-AE1D-65B1B641AEAF}"), AMENDMENT]
class MSCluster_EventGroupStateChange : MSCluster_EventStateChange
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  uint32 EventTypeMajor;
  uint32 EventTypeMinor;
  string EventObjectName;
  uint32 EventObjectType;
  string EventObjectPath;
  uint32 EventNewState;
  string EventNode;
};
```

## Members

The **MSCluster\_EventGroupStateChange** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_EventGroupStateChange** class has these properties.

<dl> <dt>

**EventNewState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

Current state of the object that is reporting a state change.



| **EventObjectType** value               | Enumeration                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------|
| 2 (Node Object)<br/>              | [**CLUSTER\_NODE\_STATE**](https://msdn.microsoft.com/library/bb309157)<br/>                 |
| 3 (Group object)<br/>             | [**CLUSTER\_GROUP\_STATE**](https://msdn.microsoft.com/library/bb309150)<br/>               |
| 4 (Resource Object)<br/>          | [**CLUSTER\_RESOURCE\_STATE**](https://msdn.microsoft.com/library/bb309168)<br/>         |
| 6 (Network Object)<br/>           | [**CLUSTER\_NETWORK\_STATE**](https://msdn.microsoft.com/library/bb309155)<br/>           |
| 7 (Network Interface Object)<br/> | [**CLUSTER\_NETINTERFACE\_STATE**](https://msdn.microsoft.com/library/bb309152)<br/> |



 

This property is inherited from [**MSCluster\_EventStateChange**](mscluster-eventstatechange.md).

</dd> <dt>

**EventNode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current node that is hosting this group.

</dd> <dt>

**EventObjectName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

Provides the name of the object to which this event applies.

This property is inherited from [**MSCluster\_Event**](mscluster-event.md).

</dd> <dt>

**EventObjectPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

Provides the WMI path of the object to which this event applies.

This property is inherited from [**MSCluster\_Event**](mscluster-event.md).

</dd> <dt>

**EventObjectType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
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
</dt> <dt>

Qualifiers: 
</dt> </dl>

Provides the major event category. A value of 0 indicates an event returned by [**GetClusterNotify**](https://msdn.microsoft.com/library/aa369623).

This property is inherited from [**MSCluster\_Event**](mscluster-event.md).

</dd> <dt>

**EventTypeMinor**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
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

The **MSCluster\_EventGroupStateChange** class is derived from the [**MSCluster\_EventStateChange**](mscluster-eventstatechange.md) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



 

 





