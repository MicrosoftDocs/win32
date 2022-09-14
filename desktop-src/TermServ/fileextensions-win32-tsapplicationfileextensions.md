---
title: FileExtensions method of the Win32_TSApplicationFileExtensions class
description: Provides a list of the file name extensions that are handled by an application.
ms.assetid: 833a1b68-86ed-4361-bbcb-a8d1c4a9306d
ms.tgt_platform: multiple
keywords:
- FileExtensions method Remote Desktop Services
- FileExtensions method Remote Desktop Services , Win32_TSApplicationFileExtensions class
- Win32_TSApplicationFileExtensions class Remote Desktop Services , FileExtensions method
topic_type:
- apiref
api_name:
- Win32_TSApplicationFileExtensions.FileExtensions
api_location:
- TsPubWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# FileExtensions method of the Win32\_TSApplicationFileExtensions class

Provides a list of the file name extensions that are handled by an application.

## Syntax


```mof
uint32 FileExtensions(
  [in]  string AppPath,
  [out] string Extensions[]
);
```



## Parameters

<dl> <dt>

*AppPath* \[in\]
</dt> <dd>

The path of the application.

</dd> <dt>

*Extensions* \[out\]
</dt> <dd>

The file name extensions that are handled by the application.

</dd> </dl>

## Remarks

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>Tsallow.mof</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>TsPubWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSApplicationFileExtensions**](win32-tsapplicationfileextensions.md)
</dt> </dl>

 

