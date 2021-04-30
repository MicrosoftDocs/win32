---
title: FileAssociations method of the Win32_TSApplicationFileExtensions class
description: Scans the registry to get the current file associations for an application.
ms.assetid: d2c55b59-f3aa-401b-b176-b287c2e26192
ms.tgt_platform: multiple
keywords:
- FileAssociations method Remote Desktop Services
- FileAssociations method Remote Desktop Services , Win32_TSApplicationFileExtensions class
- Win32_TSApplicationFileExtensions class Remote Desktop Services , FileAssociations method
topic_type:
- apiref
api_name:
- Win32_TSApplicationFileExtensions.FileAssociations
api_location:
- TsPubWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# FileAssociations method of the Win32\_TSApplicationFileExtensions class

Scans the registry to get the current file associations for an application.

## Syntax


```mof
uint32 FileAssociations(
  [in]  string                  AppPath,
  [out] Win32_RDFileAssociation FileAssociations[]
);
```



## Parameters

<dl> <dt>

*AppPath* \[in\]
</dt> <dd>

Specifies the path to the application.

</dd> <dt>

*FileAssociations* \[out\]
</dt> <dd>

On successful completion contains the file associations for this application.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TsAllow.mof</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>TsPubWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSApplicationFileExtensions**](win32-tsapplicationfileextensions.md)
</dt> <dt>

[**Win32\_RDFileAssociation**](win32-rdfileassociation.md)
</dt> </dl>

 

 





