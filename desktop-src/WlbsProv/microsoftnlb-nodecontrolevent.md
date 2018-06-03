---
title: MicrosoftNLB\_NodeControlEvent class
description: The MicrosoftNLB\_NodeControlEvent class is a WMI class that represents a Network Load Balancing (NLB) node control event.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b13f2978-5cec-4d29-9edf-54b60af47cd4
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MicrosoftNLB_NodeControlEvent class
- MicrosoftNLB_NodeControlEvent class, described
topic_type:
- apiref
api_name:
- MicrosoftNLB_NodeControlEvent
- MicrosoftNLB_NodeControlEvent.SECURITY_DESCRIPTOR
- MicrosoftNLB_NodeControlEvent.TIME_CREATED
- MicrosoftNLB_NodeControlEvent.InstanceName
- MicrosoftNLB_NodeControlEvent.Active
- MicrosoftNLB_NodeControlEvent.AdapterGuid
- MicrosoftNLB_NodeControlEvent.ClusterIPAddress
- MicrosoftNLB_NodeControlEvent.HostPriority
- MicrosoftNLB_NodeControlEvent.Id
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MicrosoftNLB\_NodeControlEvent class

The **MicrosoftNLB\_NodeControlEvent** class is a [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a Network Load Balancing (NLB) node control event.

The following syntax is simplified from MOF code, and includes all inherited properties.

## Syntax

``` syntax
[WMI, Dynamic, Provider("WmiProv"), guid("{BB066205-531F-4e55-9E70-F47DFDF5235F}"), AMENDMENT]
class MicrosoftNLB_NodeControlEvent : WmiEvent
{
  uint8   SECURITY_DESCRIPTOR[];
  uint64  TIME_CREATED;
  string  InstanceName;
  boolean Active;
  string  AdapterGuid;
  string  ClusterIPAddress;
  uint32  HostPriority;
  uint32  Id;
};
```

## Members

The **MicrosoftNLB\_NodeControlEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MicrosoftNLB\_NodeControlEvent** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved

</dd> <dt>

**AdapterGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (1), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (39)
</dt> </dl>

**GUID** of the network adapter that has NLB bound to it, in the format "{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}".

</dd> <dt>

**ClusterIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (2), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (40)
</dt> </dl>

IP Address of the NLB cluster.

</dd> <dt>

**HostPriority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (3)
</dt> </dl>

Priority of the host in the NLB cluster.

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4)
</dt> </dl>

<dt>

<span id="NLB_EVENT_NODE_STARTED"></span><span id="nlb_event_node_started"></span>

<span id="NLB_EVENT_NODE_STARTED"></span><span id="nlb_event_node_started"></span>**NLB\_EVENT\_NODE\_STARTED** (1)


</dt> <dd>

The node is started.

</dd> <dt>

<span id="NLB_EVENT_NODE_STOPPED"></span><span id="nlb_event_node_stopped"></span>

<span id="NLB_EVENT_NODE_STOPPED"></span><span id="nlb_event_node_stopped"></span>**NLB\_EVENT\_NODE\_STOPPED** (2)


</dt> <dd>

The node is stopped.

</dd> <dt>

<span id="NLB_EVENT_NODE_DRAINING"></span><span id="nlb_event_node_draining"></span>

<span id="NLB_EVENT_NODE_DRAINING"></span><span id="nlb_event_node_draining"></span>**NLB\_EVENT\_NODE\_DRAINING** (3)


</dt> <dd>

The node is [*draining*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-11-gly).

</dd> <dt>

<span id="NLB_EVENT_NODE_SUSPENDED"></span><span id="nlb_event_node_suspended"></span>

<span id="NLB_EVENT_NODE_SUSPENDED"></span><span id="nlb_event_node_suspended"></span>**NLB\_EVENT\_NODE\_SUSPENDED** (4)


</dt> <dd>

The node is suspended.

</dd> <dt>

<span id="NLB_EVENT_NODE_RESUMED"></span><span id="nlb_event_node_resumed"></span>

<span id="NLB_EVENT_NODE_RESUMED"></span><span id="nlb_event_node_resumed"></span>**NLB\_EVENT\_NODE\_RESUMED** (5)


</dt> <dd>

The node is resumed.

</dd> <dt>

<span id="NLB_EVENT_NODE_RELOADED"></span><span id="nlb_event_node_reloaded"></span>

<span id="NLB_EVENT_NODE_RELOADED"></span><span id="nlb_event_node_reloaded"></span>**NLB\_EVENT\_NODE\_RELOADED** (6)


</dt> <dd>

</dd> <dt>

<span id="NLB_EVENT_NODE_BOUND_AND_STARTED"></span><span id="nlb_event_node_bound_and_started"></span>

<span id="NLB_EVENT_NODE_BOUND_AND_STARTED"></span><span id="nlb_event_node_bound_and_started"></span>**NLB\_EVENT\_NODE\_BOUND\_AND\_STARTED** (7)


</dt> <dd>

</dd> <dt>

<span id="NLB_EVENT_NODE_BOUND_AND_STOPPED"></span><span id="nlb_event_node_bound_and_stopped"></span>

<span id="NLB_EVENT_NODE_BOUND_AND_STOPPED"></span><span id="nlb_event_node_bound_and_stopped"></span>**NLB\_EVENT\_NODE\_BOUND\_AND\_STOPPED** (8)


</dt> <dd>

</dd> <dt>

<span id="NLB_EVENT_NODE_BOUND_AND_SUSPENDED"></span><span id="nlb_event_node_bound_and_suspended"></span>

<span id="NLB_EVENT_NODE_BOUND_AND_SUSPENDED"></span><span id="nlb_event_node_bound_and_suspended"></span>**NLB\_EVENT\_NODE\_BOUND\_AND\_SUSPENDED** (9)


</dt> <dd>

</dd> <dt>

<span id="NLB_EVENT_NODE_UNBOUND"></span><span id="nlb_event_node_unbound"></span>

<span id="NLB_EVENT_NODE_UNBOUND"></span><span id="nlb_event_node_unbound"></span>**NLB\_EVENT\_NODE\_UNBOUND** (10)


</dt> <dd>

</dd> </dl>

Event Id

</dd> <dt>

**InstanceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reserved

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

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> </dl>

## Remarks

The **MicrosoftNLB\_NodeControlEvent** class is derived from the [**WMIEvent**](https://msdn.microsoft.com/library/windows/desktop/aa394532) class.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**WmiEvent**](wmievent.md)
</dt> <dt>

[Network Load Balancing WMI Classes](network-load-balancing-wmi-classes.md)
</dt> <dt>

[**WMIEvent**](https://msdn.microsoft.com/library/windows/desktop/aa394532)
</dt> </dl>

 

 





