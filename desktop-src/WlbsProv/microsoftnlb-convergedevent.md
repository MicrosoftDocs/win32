---
title: MicrosoftNLB\_ConvergedEvent class
description: The MicrosoftNLB\_ConvergedEvent class is a WMI class that represents a Network Load Balancing (NLB) cluster \ 32;converged event.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f9fcea94-6c96-448c-a048-638925d4757e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MicrosoftNLB_ConvergedEvent class", "MicrosoftNLB_ConvergedEvent class, described"]
topic_type:
- apiref
api_name:
- MicrosoftNLB_ConvergedEvent
- MicrosoftNLB_ConvergedEvent.SECURITY_DESCRIPTOR
- MicrosoftNLB_ConvergedEvent.TIME_CREATED
- MicrosoftNLB_ConvergedEvent.InstanceName
- MicrosoftNLB_ConvergedEvent.Active
- MicrosoftNLB_ConvergedEvent.AdapterGuid
- MicrosoftNLB_ConvergedEvent.ClusterIPAddress
- MicrosoftNLB_ConvergedEvent.HostPriority
- MicrosoftNLB_ConvergedEvent.HostMap
api_location:
- WlbsProv.dll
api_type:
- DllExport
---

# MicrosoftNLB\_ConvergedEvent class

The **MicrosoftNLB\_ConvergedEvent** class is a [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a Network Load Balancing (NLB) [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) [*converged*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-8-gly) event.

The following syntax is simplified from MOF code, and includes all inherited properties.

## Syntax

``` syntax
[WMI, Dynamic, Provider("WmiProv"), guid("{7131AA4D-F5D0-4d5d-A232-49785088F74E}"), AMENDMENT]
class MicrosoftNLB_ConvergedEvent : WmiEvent
{
  uint8   SECURITY_DESCRIPTOR[];
  uint64  TIME_CREATED;
  string  InstanceName;
  boolean Active;
  string  AdapterGuid;
  string  ClusterIPAddress;
  uint32  HostPriority;
  uint32  HostMap;
};
```

## Members

The **MicrosoftNLB\_ConvergedEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MicrosoftNLB\_ConvergedEvent** class has these properties.

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

**HostMap**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4)
</dt> </dl>

Bit map of the hosts in the NLB cluster.

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

The **MicrosoftNLB\_ConvergedEvent** class is derived from the [**WMIEvent**](https://msdn.microsoft.com/library/windows/desktop/aa394532) class.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
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

 

 





