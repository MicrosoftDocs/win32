---
title: GetVirtualDesktopDetails method of the Win32_RDMSVirtualDesktop class
description: Retrieves the additional information about the virtual desktop.
ms.assetid: 487e3a02-4306-4639-a44e-5b9519163a67
ms.tgt_platform: multiple
keywords:
- GetVirtualDesktopDetails method Remote Desktop Services
- GetVirtualDesktopDetails method Remote Desktop Services , Win32_RDMSVirtualDesktop class
- Win32_RDMSVirtualDesktop class Remote Desktop Services , GetVirtualDesktopDetails method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktop.GetVirtualDesktopDetails
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetVirtualDesktopDetails method of the Win32\_RDMSVirtualDesktop class

Retrieves the additional information about the virtual desktop.

## Syntax


```mof
uint32 GetVirtualDesktopDetails(
  [out] uint32  RAMSizeInMB,
  [out] boolean RemoteFXEnabled,
  [out] string  OSVersion
);
```



## Parameters

<dl> <dt>

*RAMSizeInMB* \[out\]
</dt> <dd>

Receives the amount of RAM assigned to the virtual desktop, in bytes.

</dd> <dt>

*RemoteFXEnabled* \[out\]
</dt> <dd>

Receives a value that indicates whether RemoteFX is enabled on the virtual desktop. **TRUE** if RemoteFX is enabled; otherwise, **FALSE**.

</dd> <dt>

*OSVersion* \[out\]
</dt> <dd>

Receives the OS version of the virtual desktop.

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

[**Win32\_RDMSVirtualDesktop**](win32-rdmsvirtualdesktop.md)
</dt> </dl>

 

 





