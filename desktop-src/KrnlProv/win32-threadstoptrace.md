---
title: Win32\_ThreadStopTrace class
description: The Win32\_ThreadStopTrace event WMI class indicates that a thread has terminated.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7837e045-8ef6-47fe-9dc3-97d6ca4be922
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_ThreadStopTrace class
- Win32_ThreadStopTrace class, described
topic_type:
- apiref
api_name:
- Win32_ThreadStopTrace
- Win32_ThreadStopTrace.SECURITY_DESCRIPTOR
- Win32_ThreadStopTrace.TIME_CREATED
- Win32_ThreadStopTrace.ProcessID
- Win32_ThreadStopTrace.ThreadID
api_location:
- Krnlprov.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_ThreadStopTrace class

The **Win32\_ThreadStopTrace** event [WMI class](https://msdn.microsoft.com/library/aa393244) indicates that a thread has terminated.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[AMENDMENT]
class Win32_ThreadStopTrace : Win32_ThreadTrace
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  uint32 ProcessID;
  uint32 ThreadID;
};
```

## Members

The **Win32\_ThreadStopTrace** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ThreadStopTrace** class has these properties.

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

</dd> </dl>

## Remarks

The **Win32\_ThreadStopTrace** class is derived from [**Win32\_ThreadTrace**](win32-threadtrace.md).

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

[**Win32\_ThreadTrace**](win32-threadtrace.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





