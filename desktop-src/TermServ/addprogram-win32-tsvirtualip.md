---
title: AddProgram method of the Win32_TSVirtualIP class (Bdaiface.h)
description: Adds a program to the list of programs that use IP virtualization.
ms.assetid: 4d142774-fa7a-4cfb-9305-5a61b0ef5438
ms.tgt_platform: multiple
keywords:
- AddProgram method Remote Desktop Services
- AddProgram method Remote Desktop Services , Win32_TSVirtualIP class
- Win32_TSVirtualIP class Remote Desktop Services , AddProgram method
topic_type:
- apiref
api_name:
- Win32_TSVirtualIP.AddProgram
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# AddProgram method of the Win32\_TSVirtualIP class

Adds a program to the list of programs that use IP virtualization.

## Syntax


```mof
uint32 AddProgram(
  [in] string ProgramPath
);
```



## Parameters

<dl> <dt>

*ProgramPath* \[in\]
</dt> <dd>

Type: **string**

The path and file name of the program to add to the list.

</dd> </dl>

## Return value

Type: **uint32**

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values. The method returns an error if the setting is under group policy control.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                       |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| Header<br/>                   | <dl> <dt>Bdaiface.h</dt> </dl>   |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSVirtualIP**](win32-tsvirtualip.md)
</dt> </dl>

 

 





