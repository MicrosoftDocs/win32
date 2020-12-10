---
title: AddDesktopAssignment method of the Win32_RDMSDesktopAssignment class
description: Add a desktop assignment.
ms.assetid: 3690f70e-d0c3-444a-a0b7-cec6994eb3b8
ms.tgt_platform: multiple
keywords:
- AddDesktopAssignment method Remote Desktop Services
- AddDesktopAssignment method Remote Desktop Services , Win32_RDMSDesktopAssignment class
- Win32_RDMSDesktopAssignment class Remote Desktop Services , AddDesktopAssignment method
topic_type:
- apiref
api_name:
- Win32_RDMSDesktopAssignment.AddDesktopAssignment
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# AddDesktopAssignment method of the Win32\_RDMSDesktopAssignment class

Add a desktop assignment

## Syntax


```mof
uint32 AddDesktopAssignment(
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

 

 





