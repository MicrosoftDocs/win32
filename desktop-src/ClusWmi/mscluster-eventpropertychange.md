---
title: MSCluster\_EventPropertyChange class
description: A WMI class that represents a property change event. A property change event is generated when a cluster object property is changed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1f52cce9-3637-47b3-84b8-efb0600337c8
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_EventPropertyChange class
- MSCluster_EventPropertyChange class, described
topic_type:
- apiref
api_name:
- MSCluster_EventPropertyChange
- MSCluster_EventPropertyChange.SECURITY_DESCRIPTOR
- MSCluster_EventPropertyChange.TIME_CREATED
- MSCluster_EventPropertyChange.EventTypeMajor
- MSCluster_EventPropertyChange.EventTypeMinor
- MSCluster_EventPropertyChange.EventObjectName
- MSCluster_EventPropertyChange.EventObjectType
- MSCluster_EventPropertyChange.EventObjectPath
- MSCluster_EventPropertyChange.EventProperty
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSCluster\_EventPropertyChange class

A [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a property change event. A property change event is generated when a cluster object property is changed.

The following syntax is simplified from MOF code, and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{4CB6135C-E55D-46fe-8AE4-51E24AF901BD}"), AMENDMENT]
class MSCluster_EventPropertyChange : MSCluster_Event
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  uint32 EventTypeMajor;
  uint32 EventTypeMinor;
  string EventObjectName;
  uint32 EventObjectType;
  string EventObjectPath;
  string EventProperty;
};
```

## Members

The **MSCluster\_EventPropertyChange** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_EventPropertyChange** class has these properties.

<dl> <dt>

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

**EventProperty**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for future use. XML-encoded property names and values for added or changed properties.

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

The **MSCluster\_EventPropertyChange** class is derived from the [**MSCluster\_Event**](mscluster-event.md) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



 

 





