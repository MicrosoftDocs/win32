---
title: MicrosoftNLB\_PortControlEvent class
description: The MicrosoftNLB\_PortControlEvent class is a WMI class that represents a Network Load Balancing (NLB) port control event.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2aae9f4e-9426-4a59-80f3-c7055c8fc7bf
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MicrosoftNLB_PortControlEvent class
- MicrosoftNLB_PortControlEvent class, described
topic_type:
- apiref
api_name:
- MicrosoftNLB_PortControlEvent
- MicrosoftNLB_PortControlEvent.SECURITY_DESCRIPTOR
- MicrosoftNLB_PortControlEvent.TIME_CREATED
- MicrosoftNLB_PortControlEvent.InstanceName
- MicrosoftNLB_PortControlEvent.Active
- MicrosoftNLB_PortControlEvent.AdapterGuid
- MicrosoftNLB_PortControlEvent.ClusterIPAddress
- MicrosoftNLB_PortControlEvent.HostPriority
- MicrosoftNLB_PortControlEvent.VirtualIPAddress
- MicrosoftNLB_PortControlEvent.Port
- MicrosoftNLB_PortControlEvent.Id
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MicrosoftNLB\_PortControlEvent class

The **MicrosoftNLB\_PortControlEvent** class is a [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a Network Load Balancing (NLB) port control event.

The following syntax is simplified from MOF code, and includes all inherited properties.

## Syntax

``` syntax
[WMI, Dynamic, Provider("WmiProv"), guid("{490BB97C-7D3B-4777-8216-DC11FCC02705}"), AMENDMENT]
class MicrosoftNLB_PortControlEvent : WmiEvent
{
  uint8   SECURITY_DESCRIPTOR[];
  uint64  TIME_CREATED;
  string  InstanceName;
  boolean Active;
  string  AdapterGuid;
  string  ClusterIPAddress;
  uint32  HostPriority;
  string  VirtualIPAddress;
  uint32  Port;
  uint32  Id;
};
```

## Members

The **MicrosoftNLB\_PortControlEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MicrosoftNLB\_PortControlEvent** class has these properties.

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

Cluster IP Address of the NLB cluster

</dd> <dt>

**HostPriority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (3)
</dt> </dl>

Host Priority of the host in the NLB cluster

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (6)
</dt> </dl>

Event Id

<dt>

<span id="NLB_EVENT_PORT_ENABLED"></span><span id="nlb_event_port_enabled"></span>

**NLB\_EVENT\_PORT\_ENABLED** (1)


</dt> <dd></dd> <dt>

<span id="NLB_EVENT_PORT_DISABLED"></span><span id="nlb_event_port_disabled"></span>

**NLB\_EVENT\_PORT\_DISABLED** (2)


</dt> <dd></dd> <dt>

<span id="NLB_EVENT_PORT_DRAINING"></span><span id="nlb_event_port_draining"></span>

**NLB\_EVENT\_PORT\_DRAINING** (3)


</dt> <dd></dd> </dl>

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

**Port**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (5)
</dt> </dl>

Port number of the affected port rule(s)

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

</dd> <dt>

**VirtualIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (40)
</dt> </dl>

Virtual IP Address of the affected port rule(s)

</dd> </dl>

## Remarks

The **MicrosoftNLB\_PortControlEvent** class is derived from the [**WMIEvent**](https://msdn.microsoft.com/library/windows/desktop/aa394532) class.

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

 

 





