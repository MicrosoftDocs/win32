---
title: IVMHardDisk HostFreeDiskSpace property (VPCCOMInterfaces.h)
description: Retrieves the amount of remaining disk space available on the host for the virtual hard disk.
ms.assetid: 08574bd3-e96d-465c-a1fc-265085fb3847
keywords:
- HostFreeDiskSpace property Virtual PC
- HostFreeDiskSpace property Virtual PC , IVMHardDisk interface
- IVMHardDisk interface Virtual PC , HostFreeDiskSpace property
topic_type:
- apiref
api_name:
- IVMHardDisk.HostFreeDiskSpace
- IVMHardDisk.get_HostFreeDiskSpace
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMHardDisk::HostFreeDiskSpace property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the amount of remaining disk space available on the host for the virtual hard disk.

This property is read-only.

## Syntax


```C++
HRESULT get_HostFreeDiskSpace(
  [out, retval] VARIANT *freeBytes
);
```



## Property value

The amount of remaining disk space available on the host computer for the current hard disk image file. This value is a **VARIANT** of type VT\_DECIMAL.

## Error codes



| Name/value                                                                                                                                                                            | Meaning                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                               | The operation was successful.<br/>                                |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                                 | The parameter is **NULL**.<br/>                                   |
| <dl> <dt>HRESULT\_FROM\_WIN32(ERROR\_BAD\_PATHNAME)</dt> <dt>0x800700a1</dt> </dl> | The path to the current virtual hard disk file is not valid.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                         | An unexpected error has occurred.<br/>                            |



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

 

