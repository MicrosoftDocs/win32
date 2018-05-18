---
title: Win32\_ThreadTrace class
description: The Win32\_ThreadTrace event WMI class is the base event class for thread events.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd3d1db33-c91a-41b8-80e4-f8d675acc966'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Win32_ThreadTrace class", "Win32_ThreadTrace class, described"]
topic_type:
- apiref
api_name:
- Win32_ThreadTrace
- Win32_ThreadTrace.SECURITY_DESCRIPTOR
- Win32_ThreadTrace.TIME_CREATED
- Win32_ThreadTrace.ProcessID
- Win32_ThreadTrace.ThreadID
api_location:
- Krnlprov.dll
api_type:
- DllExport
---

# Win32\_ThreadTrace class

The **Win32\_ThreadTrace** event [WMI class](https://msdn.microsoft.com/library/aa393244) is the base event class for thread events.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[AMENDMENT]
class Win32_ThreadTrace : Win32_SystemTrace
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  uint32 ProcessID;
  uint32 ThreadID;
};
```

## Members

The **Win32\_ThreadTrace** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ThreadTrace** class has these properties.

<dl> <dt>

**ProcessID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Process identifier of the thread involved in the event.

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

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Times (UTC) format.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634).

</dd> </dl>

## Remarks

The **Win32\_ThreadTrace** class is derived from the [**Win32\_SystemTrace**](win32-systemtrace.md) class.

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

[**Win32\_SystemTrace**](win32-systemtrace.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





