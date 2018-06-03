---
title: MicrosoftNLB\_StartupEvent class
description: The MicrosoftNLB\_StartupEvent class is a WMI class that represents a Network Load Balancing (NLB) startup event.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d70c9c31-b205-4c29-8607-0e730bcc2d2f
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MicrosoftNLB_StartupEvent class
- MicrosoftNLB_StartupEvent class, described
topic_type:
- apiref
api_name:
- MicrosoftNLB_StartupEvent
- MicrosoftNLB_StartupEvent.SECURITY_DESCRIPTOR
- MicrosoftNLB_StartupEvent.TIME_CREATED
- MicrosoftNLB_StartupEvent.InstanceName
- MicrosoftNLB_StartupEvent.Active
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MicrosoftNLB\_StartupEvent class

The **MicrosoftNLB\_StartupEvent** class is a [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a Network Load Balancing (NLB) startup event.

The following syntax is simplified from MOF code, and includes all inherited properties.

## Syntax

``` syntax
[WMI, Dynamic, Provider("WmiProv"), guid("{98E0E934-4952-434e-A7BA-F4E891E96A02}"), AMENDMENT]
class MicrosoftNLB_StartupEvent : WmiEvent
{
  uint8   SECURITY_DESCRIPTOR[];
  uint64  TIME_CREATED;
  string  InstanceName;
  boolean Active;
};
```

## Members

The **MicrosoftNLB\_StartupEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MicrosoftNLB\_StartupEvent** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved

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

The **MicrosoftNLB\_StartupEvent** class is derived from the [**WMIEvent**](https://msdn.microsoft.com/library/windows/desktop/aa394532) class.

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

 

 





