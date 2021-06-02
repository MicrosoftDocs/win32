---
title: AddVirtualDesktop method of the Win32_RDMSVirtualDesktopCollection class
description: Adds a virtual desktop to the virtual desktop collection.
ms.assetid: 31a3aa28-6e5d-4f8a-81ff-ab011f568b6a
ms.tgt_platform: multiple
keywords:
- AddVirtualDesktop method Remote Desktop Services
- AddVirtualDesktop method Remote Desktop Services , Win32_RDMSVirtualDesktopCollection class
- Win32_RDMSVirtualDesktopCollection class Remote Desktop Services , AddVirtualDesktop method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktopCollection.AddVirtualDesktop
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# AddVirtualDesktop method of the Win32\_RDMSVirtualDesktopCollection class

Adds a virtual desktop to the virtual desktop collection.

## Syntax


```mof
uint32 AddVirtualDesktop(
  [in] string VMName
);
```



## Parameters

<dl> <dt>

*VMName* \[in\]
</dt> <dd>

The name of the virtual machine that hosts the virtual desktop.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSVirtualDesktopCollection**](win32-rdmsvirtualdesktopcollection.md)
</dt> </dl>

 

 





