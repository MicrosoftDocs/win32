---
title: Win32\_SystemTrace class
description: The Win32\_SystemTrace event WMI class is the base class for all system trace events. System trace events are fired by the kernel logger, using the Event Tracing application programming interface (API).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd4e54029-44c3-4020-b63e-c4c1ce4b006e'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Win32_SystemTrace class", "Win32_SystemTrace class, described"]
topic_type:
- apiref
api_name:
- Win32_SystemTrace
- Win32_SystemTrace.SECURITY_DESCRIPTOR
- Win32_SystemTrace.TIME_CREATED
api_location:
- Krnlprov.dll
api_type:
- DllExport
---

# Win32\_SystemTrace class

The **Win32\_SystemTrace** event [WMI class](https://msdn.microsoft.com/library/aa393244) is the base class for all system trace events. System trace events are fired by the kernel logger, using the Event Tracing application programming interface (API).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[AMENDMENT]
class Win32_SystemTrace : __ExtrinsicEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
};
```

## Members

The **Win32\_SystemTrace** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SystemTrace** class has these properties.

<dl> <dt>

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

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> </dl>

## Remarks

The **Win32\_SystemTrace** class is derived from the WMI [**\_\_ExtrinsicEvent**](https://msdn.microsoft.com/library/aa394646) system class.

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

[**\_\_ExtrinsicEvent**](https://msdn.microsoft.com/library/aa394646)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





