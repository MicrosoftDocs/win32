---
Description: 'The Win32\_NTLogEventLog association WMI class relates a Windows event with a Windows event log file.'
ms.assetid: 'e746895e-3927-427a-838c-4bdf8d9038fa'
title: 'Win32\_NTLogEventLog class'
---

# Win32\_NTLogEventLog class

The **Win32\_NTLogEventLog** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a Windows event with a Windows event log file.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_NTLogEventLog
{
  Win32_NTEventLogFile REF Log;
  Win32_NTLogEvent     REF Record;
};
```

## Members

The **Win32\_NTLogEventLog** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_NTLogEventLog** class has these properties.

<dl> <dt>

**Log**
</dt> <dd> <dl> <dt>

Data type: **Win32\_NTEventLogFile**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reference to the instance representing the event log file.

</dd> <dt>

**Record**
</dt> <dd> <dl> <dt>

Data type: **Win32\_NTLogEvent**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reference to the instance representing the event being logged.

</dd> </dl>

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

 

 




