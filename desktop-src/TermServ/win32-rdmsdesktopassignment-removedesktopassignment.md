---
title: RemoveDesktopAssignment method of the Win32_RDMSDesktopAssignment class
description: Removes a desktop assignment.
ms.assetid: e1a8cf03-1d21-4bf4-a868-3da4d5bbf43b
ms.tgt_platform: multiple
keywords:
- RemoveDesktopAssignment method Remote Desktop Services
- RemoveDesktopAssignment method Remote Desktop Services , Win32_RDMSDesktopAssignment class
- Win32_RDMSDesktopAssignment class Remote Desktop Services , RemoveDesktopAssignment method
topic_type:
- apiref
api_name:
- Win32_RDMSDesktopAssignment.RemoveDesktopAssignment
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RemoveDesktopAssignment method of the Win32\_RDMSDesktopAssignment class

Removes a desktop assignment

## Syntax


```mof
uint32 RemoveDesktopAssignment(
  [in] string CollectionAlias,
  [in] string DesktopName,
  [in] string UserDomain,
  [in] string UserName
);
```



## Parameters

<dl> <dt>

*CollectionAlias* \[in\]
</dt> <dd>

The collection alias.

</dd> <dt>

*DesktopName* \[in\]
</dt> <dd>

The name of the desktop.

</dd> <dt>

*UserDomain* \[in\]
</dt> <dd>

The user account domain name.

</dd> <dt>

*UserName* \[in\]
</dt> <dd>

The user account name.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSDesktopAssignment**](win32-rdmsdesktopassignment.md)
</dt> </dl>

 

 





