---
title: Win32\_ThreadStartTrace class
description: Indicates that a new thread has started.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bfd1705d-3942-4905-b92b-4b92a74cd444'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Win32_ThreadStartTrace class", "Win32_ThreadStartTrace class, described"]
topic_type:
- apiref
api_name:
- Win32_ThreadStartTrace
- Win32_ThreadStartTrace.SECURITY_DESCRIPTOR
- Win32_ThreadStartTrace.TIME_CREATED
- Win32_ThreadStartTrace.ProcessID
- Win32_ThreadStartTrace.ThreadID
- Win32_ThreadStartTrace.StackBase
- Win32_ThreadStartTrace.StackLimit
- Win32_ThreadStartTrace.StartAddr
- Win32_ThreadStartTrace.UserStackBase
- Win32_ThreadStartTrace.UserStackLimit
- Win32_ThreadStartTrace.WaitMode
- Win32_ThreadStartTrace.Win32StartAddr
api_location:
- Krnlprov.dll
api_type:
- DllExport
---

# Win32\_ThreadStartTrace class

The **Win32\_ThreadStartTrace** event [WMI class](https://msdn.microsoft.com/library/aa393244) indicates that a new thread has started.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[AMENDMENT]
class Win32_ThreadStartTrace : Win32_ThreadTrace
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  uint32 ProcessID;
  uint32 ThreadID;
  uint64 StackBase;
  uint64 StackLimit;
  uint64 StartAddr;
  uint64 UserStackBase;
  uint64 UserStackLimit;
  uint32 WaitMode;
  uint64 Win32StartAddr;
};
```

## Members

The **Win32\_ThreadStartTrace** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ThreadStartTrace** class has these properties.

<dl> <dt>

**ProcessID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Process identifier of the thread involved in the event.

This property is inherited from [**Win32\_ThreadTrace**](win32-threadtrace.md).

</dd> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634). For more information about constants used to set this security descriptor, see [WMI Security Constants](https://msdn.microsoft.com/library/aa394576).

</dd> <dt>

**StackBase**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Base address of the thread's stack.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**StackLimit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Limit of the thread's stack.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**StartAddr**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Memory address at which the trace starts.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**ThreadID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Thread identifier of the thread involved in the event.

This property is inherited from [**Win32\_ThreadTrace**](win32-threadtrace.md).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Times (UTC) format. This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**UserStackBase**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Base address of the thread's user-mode stack.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**UserStackLimit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Limit of the thread's user-mode stack.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**WaitMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Processor mode in which the wait is to occur.

<dt>

0
</dt> <dd>

Kernel

</dd> <dt>

1
</dt> <dd>

User

</dd> </dl>

</dd> <dt>

**Win32StartAddr**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Starting address of the function to be executed by this thread.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> </dl>

## Remarks

The **Win32\_ThreadStartTrace** class is derived from [**Win32\_ThreadTrace**](win32-threadtrace.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Krnlprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Krnlprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ThreadTrace**](win32-threadtrace.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





