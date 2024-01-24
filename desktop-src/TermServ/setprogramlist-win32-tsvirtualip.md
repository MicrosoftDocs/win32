---
title: SetProgramList method of the Win32_TSVirtualIP class
description: Overwrites the list of programs that use IP virtualization.
ms.assetid: 4137c9b0-5b4d-4ab6-af2e-2cd98ba53563
ms.tgt_platform: multiple
keywords:
- SetProgramList method Remote Desktop Services
- SetProgramList method Remote Desktop Services , Win32_TSVirtualIP class
- Win32_TSVirtualIP class Remote Desktop Services , SetProgramList method
topic_type:
- apiref
api_name:
- Win32_TSVirtualIP.SetProgramList
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetProgramList method of the Win32\_TSVirtualIP class

Overwrites the list of programs that use IP virtualization.

## Syntax


```mof
unint32 SetProgramList(
  [in] string ProgramList[]
);
```



## Parameters

<dl> <dt>

*ProgramList* \[in\]
</dt> <dd>

Type: **string\[\]**

An array of strings that contain the path and file names of the programs that use IP virtualization.

</dd> </dl>

## Return value

Type: **unint32**

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values. The method returns an error if the setting is under group policy control.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                       |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSVirtualIP**](win32-tsvirtualip.md)
</dt> </dl>

 

 





