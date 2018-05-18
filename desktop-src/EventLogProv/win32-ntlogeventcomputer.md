---
Description: 'The Win32\_NTLogEventComputer association WMI class relates a computer and an event.'
ms.assetid: '2fa41dc6-824a-4f4a-b3cf-9f33f848b241'
title: 'Win32\_NTLogEventComputer class'
---

# Win32\_NTLogEventComputer class

The **Win32\_NTLogEventComputer** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a computer and an event.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_NTLogEventComputer
{
  Win32_ComputerSystem REF Computer;
  Win32_NTLogEvent     REF Record;
};
```

## Members

The **Win32\_NTLogEventComputer** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_NTLogEventComputer** class has these properties.

<dl> <dt>

**Computer**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reference to the instance on which this event occurred.

</dd> <dt>

**Record**
</dt> <dd> <dl> <dt>

Data type: **Win32\_NTLogEvent**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reference to the instance representing the event.

</dd> </dl>

## Remarks

Starting with Windows Vista, an associations query, such as [ASSOCIATORS OF](https://msdn.microsoft.com/library/aa384793), [**SWbemObject.Associators**](https://msdn.microsoft.com/library/aa393767), or \_[**SWbemServices.AssociatorsOf**](https://msdn.microsoft.com/library/aa393858), that uses **Win32\_NTLogEventComputer** does not work unless [Windows Event Log](https://msdn.microsoft.com/library/windows/desktop/aa385780) has the compatibility mode set.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Ntevt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntevt.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




