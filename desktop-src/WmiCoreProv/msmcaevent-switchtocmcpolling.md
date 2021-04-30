---
description: Represents the corrected machine check (CMC) handling to be switched from the interrupt driver to polling. This class is available only in 64-bit Windows systems.
ms.assetid: c5e99e13-0f65-40bc-8863-b2ca7ea221df
title: MSMCAEvent_SwitchToCMCPolling class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSMCAEvent_SwitchToCMCPolling
- MSMCAEvent_SwitchToCMCPolling.Active
- MSMCAEvent_SwitchToCMCPolling.InstanceName
api_type: 
- DllExport
api_location: 
- Wmiprov.dll
---

# MSMCAEvent\_SwitchToCMCPolling class

The **MSMCAEvent\_SwitchToCMCPolling** class represents the corrected machine check (CMC) handling to be switched from the interrupt driver to polling. In some cases, the kernel polls the system abstraction layer (SAL) for any CMC or corrected platform error (CPE) that occurred within the previous polling interval. This class is available only in 64-bit Windows systems.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class MSMCAEvent_SwitchToCMCPolling : WMIEvent
{
  boolean Active;
  string  InstanceName;
};
```

## Members

The **MSMCAEvent\_SwitchToCMCPolling** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSMCAEvent\_SwitchToCMCPolling** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE**, if this instance of the class is active; otherwise, **FALSE**.

</dd> <dt>

**InstanceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

Unique identifier of this instance of the class.

</dd> </dl>

## Remarks

The **MSMCAEvent\_SwitchToCMCPolling** class is derived from [**WMIEvent**](wmievent.md).

The system abstraction layer (SAL) is code burned onto ROM that the operating system calls to perform platform-dependent operations. It is similar to the BIOS on an x86 platform. In cases where the platform does not support interrupts for CMC or CPE polling, the operating system polls every minute, checking if an error occurred previously. If the platform does support interrupts and the operating system receives a user defined amount of CMC or CPE polls within one minute, then it disables the interrupt and poll. If the user does not define the number of polls within one minute, the system sets a default to 10 polls per minute.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\wmi<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>Wmicore.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[MSMCA Classes](msmca-classes.md)
</dt> <dt>

[**WMIEvent**](wmievent.md)
</dt> </dl>

 

