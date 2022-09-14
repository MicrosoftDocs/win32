---
title: IVMHardDisk Merge method (VPCCOMInterfaces.h)
description: Merges a differencing virtual hard disk with its parent disk image.
ms.assetid: e2aca4d3-79c1-416a-b135-f4680c03d200
keywords:
- Merge method Virtual PC
- Merge method Virtual PC , IVMHardDisk interface
- IVMHardDisk interface Virtual PC , Merge method
topic_type:
- apiref
api_name:
- IVMHardDisk.Merge
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMHardDisk::Merge method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Merges a differencing virtual hard disk with its parent disk image.

## Syntax


```C++
HRESULT Merge(
  [out, retval] IVMTask **mergeTask
);
```



## Parameters

<dl> <dt>

*mergeTask* \[out, retval\]
</dt> <dd>

An [**IVMTask**](ivmtask.md) object that is used to track the completion of the merging process.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                              | Description                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                    | The operation was successful.<br/>                                                                                                                                                                                          |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                      | The parameter is **NULL**.<br/>                                                                                                                                                                                             |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_SHARING\_VIOLATION)**</dt> <dt>0x80070020</dt> </dl> | The virtual hard disk image referenced by this [**IVMHardDisk**](ivmharddisk.md) object is in use or the parent of this virtual hard disk image is in use. Or, these hard disk images could be part of a saved state.<br/> |
| <dl> <dt>**VM\_E\_WRONG\_HD\_IMAGE\_TYPE**</dt> <dt>0xA004067B</dt> </dl>                   | The virtual hard disk image referenced by this [**IVMHardDisk**](ivmharddisk.md) object must be a differencing disk image.<br/>                                                                                            |
| <dl> <dt>**VM\_E\_FILE\_READ\_ONLY**</dt> <dt>0xA004067A</dt> </dl>                         | The parent of virtual hard disk image referenced by this [**IVMHardDisk**](ivmharddisk.md) object is marked as read only.<br/>                                                                                             |
| <dl> <dt>**VM\_E\_PARENT\_PATH\_NOT\_FOUND**</dt> <dt>0xA0040677</dt> </dl>                 | The parent of the virtual hard disk referenced by this [**IVMHardDisk**](ivmharddisk.md) object does not exist.<br/>                                                                                                       |
| <dl> <dt>**VM\_E\_APP\_SHUTTING\_DOWN**</dt> <dt>0xA0040209</dt> </dl>                      | The virtual hard disk image cannot be merged because the application is shutting down.<br/>                                                                                                                                 |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                              | An unexpected error has occurred.<br/>                                                                                                                                                                                      |



 

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

 

