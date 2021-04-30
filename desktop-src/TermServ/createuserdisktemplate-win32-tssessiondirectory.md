---
title: CreateUserDiskTemplate method of the Win32_TSSessionDirectory class
description: Creates a user disk template.
ms.assetid: 4036a418-b082-4376-a400-16f48b98f071
ms.tgt_platform: multiple
keywords:
- CreateUserDiskTemplate method Remote Desktop Services
- CreateUserDiskTemplate method Remote Desktop Services , Win32_TSSessionDirectory class
- Win32_TSSessionDirectory class Remote Desktop Services , CreateUserDiskTemplate method
topic_type:
- apiref
api_name:
- Win32_TSSessionDirectory.CreateUserDiskTemplate
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CreateUserDiskTemplate method of the Win32\_TSSessionDirectory class

Creates a user disk template.

## Syntax


```mof
uint32 CreateUserDiskTemplate(
  [in] string UserDisksStorageUrl,
  [in] uint32 UserDiskMaxSizeInGB
);
```



## Parameters

<dl> <dt>

*UserDisksStorageUrl* \[in\]
</dt> <dd>

The location of the share where all user disks are stored.

</dd> <dt>

*UserDiskMaxSizeInGB* \[in\]
</dt> <dd>

The maximum size in gigabytes, for all user disks.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSSessionDirectory**](win32-tssessiondirectory.md)
</dt> </dl>

 

 





