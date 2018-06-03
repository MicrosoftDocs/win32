---
title: Win32\_ProcessStartTrace class
description: Indicates that a new process has started.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9262051e-5106-4a00-a7b7-56ff65f111d4
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_ProcessStartTrace class
- Win32_ProcessStartTrace class, described
topic_type:
- apiref
api_name:
- Win32_ProcessStartTrace
- Win32_ProcessStartTrace.SECURITY_DESCRIPTOR
- Win32_ProcessStartTrace.TIME_CREATED
- Win32_ProcessStartTrace.ProcessID
- Win32_ProcessStartTrace.ParentProcessID
- Win32_ProcessStartTrace.Sid
- Win32_ProcessStartTrace.ProcessName
- Win32_ProcessStartTrace.SessionID
api_location:
- Krnlprov.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_ProcessStartTrace class

The **Win32\_ProcessStartTrace** event [WMI class](https://msdn.microsoft.com/library/aa393244)indicates that a new process has started.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[AMENDMENT]
class Win32_ProcessStartTrace : Win32_ProcessTrace
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  uint32 ProcessID;
  uint32 ParentProcessID;
  uint8  Sid[];
  string ProcessName;
  uint32 SessionID;
};
```

## Members

The **Win32\_ProcessStartTrace** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ProcessStartTrace** class has these properties.

<dl> <dt>

**ParentProcessID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Process that starts an event.

This property is inherited from [**Win32\_ProcessTrace**](win32-processtrace.md).

</dd> <dt>

**ProcessID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **ProcessID** property identifies the process involved in the event.

This property is inherited from [**Win32\_ProcessTrace**](win32-processtrace.md).

</dd> <dt>

**ProcessName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the process. You can use this name to get the instance of the [**Win32\_Process**](https://msdn.microsoft.com/library/aa394372) for same process.

This property is inherited from [**Win32\_ProcessTrace**](win32-processtrace.md).

</dd> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634). For more information about constants used to set this security descriptor, see [WMI Security Constants](https://msdn.microsoft.com/library/aa394576).

</dd> <dt>

**SessionID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Session under which the process exists.

This property is inherited from [**Win32\_ProcessTrace**](win32-processtrace.md).

</dd> <dt>

**Sid**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Sid property is the security identifier representing the user context under which the event happened.

This property is inherited from [**Win32\_ProcessTrace**](win32-processtrace.md).

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

The **Win32\_ProcessStartTrace** class is derived from [**Win32\_ProcessTrace**](win32-processtrace.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Krnlprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Krnlprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ProcessTrace**](win32-processtrace.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> <dt>

[**Win32\_Process**](https://msdn.microsoft.com/library/aa394372)
</dt> </dl>

 

 





