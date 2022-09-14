---
title: IVMHardDisk Compact method (VPCCOMInterfaces.h)
description: Compacts a dynamically expanding virtual hard disk image.
ms.assetid: bd3ec493-1bc0-4c28-8b41-56beac3d0d6d
keywords:
- Compact method Virtual PC
- Compact method Virtual PC , IVMHardDisk interface
- IVMHardDisk interface Virtual PC , Compact method
topic_type:
- apiref
api_name:
- IVMHardDisk.Compact
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMHardDisk::Compact method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Compacts a dynamically expanding virtual hard disk image.

## Syntax


```C++
HRESULT Compact(
  [out, retval] IVMTask **compactTask
);
```



## Parameters

<dl> <dt>

*compactTask* \[out, retval\]
</dt> <dd>

An [**IVMTask**](ivmtask.md) object that is used to track the completion the compaction process.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                              | Description                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                    | The operation was successful.<br/>                                                                                                        |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                              | An unexpected error has occurred.<br/>                                                                                                    |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                      | The parameter is **NULL**.<br/>                                                                                                           |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_SHARING\_VIOLATION)**</dt> <dt>0x80070020</dt> </dl> | The virtual hard disk image referenced by this [**IVMHardDisk**](ivmharddisk.md) object is in use.<br/>                                  |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_DISK\_FULL)**</dt> <dt>0x80070070</dt> </dl>         | The host volume does not have enough space to create a temporary file needed for the compaction of this virtual hard disk image.<br/>     |
| <dl> <dt>**VM\_E\_APP\_SHUTTING\_DOWN**</dt> <dt>0xA0040209</dt> </dl>                      | The virtual hard disk image cannot be compacted because the application is shutting down.<br/>                                            |
| <dl> <dt>**VM\_E\_FILE\_READ\_ONLY**</dt> <dt>0xA004067A</dt> </dl>                         | The virtual hard disk image referenced by this [**IVMHardDisk**](ivmharddisk.md) object is marked as read only.<br/>                     |
| <dl> <dt>**VM\_E\_WRONG\_HD\_IMAGE\_TYPE**</dt> <dt>0xA004067B</dt> </dl>                   | The virtual hard disk image referenced by this [**IVMHardDisk**](ivmharddisk.md) object must be a **vmDiskTypeDynamic** image type.<br/> |
| <dl> <dt>**VM\_E\_INVALID\_HD\_FILE**</dt> <dt>0xA0040682</dt> </dl>                        | The virtual hard disk image referenced by this [**IVMHardDisk**](ivmharddisk.md) object does not seem to be a valid image.<br/>          |



 

## Remarks

To compact a dynamically expanding hard disk image, free space on the disk image should first be zeroed.

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

 

