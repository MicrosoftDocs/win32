---
title: RemoveVirtualDesktop method of the Win32_RDMSVirtualDesktopCollection class
description: Removes a virtual desktop from the virtual desktop collection.
ms.assetid: 287ebbb2-86db-4b4a-8dbb-ac5472789e72
ms.tgt_platform: multiple
keywords:
- RemoveVirtualDesktop method Remote Desktop Services
- RemoveVirtualDesktop method Remote Desktop Services , Win32_RDMSVirtualDesktopCollection class
- Win32_RDMSVirtualDesktopCollection class Remote Desktop Services , RemoveVirtualDesktop method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktopCollection.RemoveVirtualDesktop
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RemoveVirtualDesktop method of the Win32\_RDMSVirtualDesktopCollection class

Removes a virtual desktop from the virtual desktop collection.

## Syntax


```mof
uint32 RemoveVirtualDesktop(
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

 

 





