---
title: IVMHardDisk SizeInGuest property (VPCCOMInterfaces.h)
description: Retrieves the size of the virtual hard disk in the guest operating system.
ms.assetid: 895598db-cd54-414c-8783-13102cfbd453
keywords:
- SizeInGuest property Virtual PC
- SizeInGuest property Virtual PC , IVMHardDisk interface
- IVMHardDisk interface Virtual PC , SizeInGuest property
topic_type:
- apiref
api_name:
- IVMHardDisk.SizeInGuest
- IVMHardDisk.get_SizeInGuest
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMHardDisk::SizeInGuest property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the size of the virtual hard disk in the guest operating system.

This property is read-only.

## Syntax


```C++
HRESULT get_SizeInGuest(
  [out, retval] VARIANT *fileSize
);
```



## Property value

The size, in bytes, of the hard disk image. This value is a **VARIANT** of type VT\_DECIMAL.

## Error codes



| Name/value                                                                                                                                                                               | Meaning                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                                  | The operation was successful.<br/>                                                  |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                                    | The parameter is **NULL**.<br/>                                                     |
| <dl> <dt>HRESULT\_FROM\_WIN32(ERROR\_FILE\_NOT\_FOUND)</dt> <dt>0x80070002</dt> </dl> | The current virtual hard disk file could not be found.<br/>                         |
| <dl> <dt>VM\_E\_HD\_IMAGE\_OPEN\_FAIL</dt> <dt>0xA004067C</dt> </dl>                  | An error occurred while attempting to open the current hard disk image file.<br/>   |
| <dl> <dt>VM\_E\_HD\_IMAGE\_ACCESS</dt> <dt>0xA0040681</dt> </dl>                      | An error occurred while attempting to access the current hard disk image file.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                            | An unexpected error has occurred.<br/>                                              |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMHardDisk is defined as ffa14ae6-48f5-42a4-8a22-186f2e5c7db0<br/>                |



## See also

<dl> <dt>

[**IVMHardDisk**](ivmharddisk.md)
</dt> </dl>

 

