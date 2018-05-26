---
title: MicrosoftNLB\_ConvergingEvent class
description: The MicrosoftNLB\_ConvergingEvent class is a WMI class that represents a Network Load Balancing (NLB) cluster \ 32;converging event.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9791222c-bdad-4f26-b3ad-fb06dc00b04b
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MicrosoftNLB_ConvergingEvent class
- MicrosoftNLB_ConvergingEvent class, described
topic_type:
- apiref
api_name:
- MicrosoftNLB_ConvergingEvent
- MicrosoftNLB_ConvergingEvent.SECURITY_DESCRIPTOR
- MicrosoftNLB_ConvergingEvent.TIME_CREATED
- MicrosoftNLB_ConvergingEvent.InstanceName
- MicrosoftNLB_ConvergingEvent.Active
- MicrosoftNLB_ConvergingEvent.AdapterGuid
- MicrosoftNLB_ConvergingEvent.ClusterIPAddress
- MicrosoftNLB_ConvergingEvent.HostPriority
- MicrosoftNLB_ConvergingEvent.Cause
- MicrosoftNLB_ConvergingEvent.InitiatorDedicatedIP
- MicrosoftNLB_ConvergingEvent.InitiatorHostPriority
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MicrosoftNLB\_ConvergingEvent class

The **MicrosoftNLB\_ConvergingEvent** class is a [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a Network Load Balancing (NLB) [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) [*converging*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-8-gly) event.

The following syntax is simplified from MOF code, and includes all inherited properties.

## Syntax

``` syntax
[WMI, Dynamic, Provider("WmiProv"), guid("{812C7978-7D1B-40dc-89D7-D3C9D36A77B4}"), AMENDMENT]
class MicrosoftNLB_ConvergingEvent : WmiEvent
{
  uint8   SECURITY_DESCRIPTOR[];
  uint64  TIME_CREATED;
  string  InstanceName;
  boolean Active;
  string  AdapterGuid;
  string  ClusterIPAddress;
  uint32  HostPriority;
  uint32  Cause;
  string  InitiatorDedicatedIP;
  uint32  InitiatorHostPriority;
};
```

## Members

The **MicrosoftNLB\_ConvergingEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MicrosoftNLB\_ConvergingEvent** class has these properties.

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

**Cause**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4)
</dt> </dl>

Cause for convergence.

<dt>

<span id="NLB_EVENT_CONVERGING_BAD_CONFIG"></span><span id="nlb_event_converging_bad_config"></span>

**NLB\_EVENT\_CONVERGING\_BAD\_CONFIG** (1)


</dt> <dd></dd> <dt>

<span id="NLB_EVENT_CONVERGING_NEW_MEMBER"></span><span id="nlb_event_converging_new_member"></span>

**NLB\_EVENT\_CONVERGING\_NEW\_MEMBER** (2)


</dt> <dd></dd> <dt>

<span id="NLB_EVENT_CONVERGING_UNKNOWN"></span><span id="nlb_event_converging_unknown"></span>

**NLB\_EVENT\_CONVERGING\_UNKNOWN** (3)


</dt> <dd></dd> <dt>

<span id="NLB_EVENT_CONVERGING_DUPLICATE_HOST_ID"></span><span id="nlb_event_converging_duplicate_host_id"></span>

**NLB\_EVENT\_CONVERGING\_DUPLICATE\_HOST\_ID** (4)


</dt> <dd></dd> <dt>

<span id="NLB_EVENT_CONVERGING_NUM_RULES"></span><span id="nlb_event_converging_num_rules"></span>

**NLB\_EVENT\_CONVERGING\_NUM\_RULES** (5)


</dt> <dd></dd> <dt>

<span id="NLB_EVENT_CONVERGING_MODIFIED_RULES"></span><span id="nlb_event_converging_modified_rules"></span>

**NLB\_EVENT\_CONVERGING\_MODIFIED\_RULES** (6)


</dt> <dd></dd> <dt>

<span id="NLB_EVENT_CONVERGING_MEMBER_LOST"></span><span id="nlb_event_converging_member_lost"></span>

**NLB\_EVENT\_CONVERGING\_MEMBER\_LOST** (7)


</dt> <dd></dd> <dt>

<span id="NLB_EVENT_CONVERGING_MODIFIED_PARAMS"></span><span id="nlb_event_converging_modified_params"></span>

**NLB\_EVENT\_CONVERGING\_MODIFIED\_PARAMS** (8)


</dt> <dd></dd> <dt>

<span id="NLB_EVENT_CONVERGING_DEPRECATED_LEGACY_HOST"></span><span id="nlb_event_converging_deprecated_legacy_host"></span>

**NLB\_EVENT\_CONVERGING\_DEPRECATED\_LEGACY\_HOST** (9)


</dt> <dd></dd> <dt>

<span id="NLB_EVENT_CONVERGING_CLIENT_STICKINESS_SYNCHRONISATION_FAILURE"></span><span id="nlb_event_converging_client_stickiness_synchronisation_failure"></span>

**NLB\_EVENT\_CONVERGING\_CLIENT\_STICKINESS\_SYNCHRONISATION\_FAILURE** (10)


</dt> <dd></dd> </dl>

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

**InitiatorDedicatedIP**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (5), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (40)
</dt> </dl>

IP Address of the host in the NLB cluster that is the cause of convergence.

</dd> <dt>

**InitiatorHostPriority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (6)
</dt> </dl>

Priority of the host in the NLB cluster that is the cause of convergence.

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

The **MicrosoftNLB\_ConvergingEvent** class is derived from the [**WMIEvent**](https://msdn.microsoft.com/library/windows/desktop/aa394532) class.

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

 

 





