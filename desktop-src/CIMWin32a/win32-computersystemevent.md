---
title: Win32\_ComputerSystemEvent class
description: The Win32\_ComputerSystemEvent \ 32;WMI class represents events related to a computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b3f7a784-8fa9-42e0-9872-5c1ef4bcc01e'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Win32_ComputerSystemEvent class", "Win32_ComputerSystemEvent class, described"]
topic_type:
- apiref
api_name:
- Win32_ComputerSystemEvent
- Win32_ComputerSystemEvent.SECURITY_DESCRIPTOR
- Win32_ComputerSystemEvent.TIME_CREATED
- Win32_ComputerSystemEvent.MachineName
api_location:
- Wmipcima.dll
api_type:
- DllExport
---

# Win32\_ComputerSystemEvent class

The **Win32\_ComputerSystemEvent** [WMI class](https://msdn.microsoft.com/library/aa393244) represents events related to a computer system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("{999A286E-CF9C-4f0c-8F0F-827C4C0D9CC6}"), AMENDMENT]
class Win32_ComputerSystemEvent : __ExtrinsicEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  string MachineName;
};
```

## Members

The **Win32\_ComputerSystemEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ComputerSystemEvent** class has these properties.

<dl> <dt>

**MachineName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the computer for which the event occurred.

</dd> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event.

For more information about constants used to set this security descriptor, see [WMI Security Constants](https://msdn.microsoft.com/library/aa394576).

This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Times (UTC) format.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634).

</dd> </dl>

## Remarks

The **Win32\_ComputerSystemEvent** class is derived from [**\_\_ExtrinsicEvent**](https://msdn.microsoft.com/library/aa394646).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipcima.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipcima.dll</dt> </dl> |



## See also

<dl> <dt>

[**\_\_ExtrinsicEvent**](https://msdn.microsoft.com/library/aa394646)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





