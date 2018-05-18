---
title: Win32\_ModuleLoadTrace class
description: The Win32\_ModuleLoadTrace event WMI class indicates that a process has loaded a new module.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b11d4786-0d4e-496d-9e4e-52f11dd1b60c'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Win32_ModuleLoadTrace class", "Win32_ModuleLoadTrace class, described"]
topic_type:
- apiref
api_name:
- Win32_ModuleLoadTrace
- Win32_ModuleLoadTrace.SECURITY_DESCRIPTOR
- Win32_ModuleLoadTrace.TIME_CREATED
- Win32_ModuleLoadTrace.FileName
- Win32_ModuleLoadTrace.DefaultBase
- Win32_ModuleLoadTrace.ImageBase
- Win32_ModuleLoadTrace.ImageChecksum
- Win32_ModuleLoadTrace.ImageSize
- Win32_ModuleLoadTrace.ProcessID
- Win32_ModuleLoadTrace.TimeDateSTamp
api_location:
- Krnlprov.dll
api_type:
- DllExport
---

# Win32\_ModuleLoadTrace class

The **Win32\_ModuleLoadTrace** event [WMI class](https://msdn.microsoft.com/library/aa393244) indicates that a process has loaded a new module.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[AMENDMENT]
class Win32_ModuleLoadTrace : Win32_ModuleTrace
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  string FileName;
  uint64 DefaultBase;
  uint64 ImageBase;
  uint32 ImageChecksum;
  uint64 ImageSize;
  uint32 ProcessID;
  uint32 TimeDateSTamp;
};
```

## Members

The **Win32\_ModuleLoadTrace** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ModuleLoadTrace** class has these properties.

<dl> <dt>

**DefaultBase**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Default base address for loading the image, as listed in the binary image header. If the requested address is unavailable, the image is loaded at the **ImageBase** address, which causes recalculation of images addresses.

</dd> <dt>

**FileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

File name of the loaded module from the binary image header.

</dd> <dt>

**ImageBase**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Base address where the module is loaded into process memory.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**ImageChecksum**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Binary image checksum for the module as listed in the image header. The image checksum is a hash that is used to verify that the image has not been changed. The hash is usually set when the module is linked and is not an encryption mechanism.

</dd> <dt>

**ImageSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Size, in bytes, of the loaded module.

</dd> <dt>

**ProcessID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies the process that loaded the module.

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

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**TimeDateSTamp**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Binary image time stamp as listed in the image header. **TimeDateSTamp** is used with **FileName** and **ImageSize** to identify the binary image uniquely.

</dd> </dl>

## Remarks

The **Win32\_ModuleLoadTrace** class is derived from [**Win32\_ModuleTrace**](win32-moduletrace.md).

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

[**Win32\_ModuleTrace**](win32-moduletrace.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





