---
title: IVMHardDisk MergeTo method (VPCCOMInterfaces.h)
description: Merges a differencing virtual hard disk with all of its parents.
ms.assetid: 3c63f892-7c05-4ed6-a59a-914a921ec391
keywords:
- MergeTo method Virtual PC
- MergeTo method Virtual PC , IVMHardDisk interface
- IVMHardDisk interface Virtual PC , MergeTo method
topic_type:
- apiref
api_name:
- IVMHardDisk.MergeTo
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMHardDisk::MergeTo method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Merges a differencing virtual hard disk with all of its parents (up to and including the root parent virtual hard disk) to a new hard disk file.

## Syntax


```C++
HRESULT MergeTo(
  [in]          BSTR           newDiskImagePath,
  [in]          VMHardDiskType newDiskImageType,
  [out, retval] IVMTask        **mergeTask
);
```



## Parameters

<dl> <dt>

*newDiskImagePath* \[in\]
</dt> <dd>

The path to the new target disk image where the selected disk images will be merged.

</dd> <dt>

*newDiskImageType* \[in\]
</dt> <dd>

The type of new target disk image. The image types allowed for the new target disk image are **vmDiskType\_Dynamic** and **vmDiskType\_FixedSize**. For more information, see [**VMHardDiskType**](vmharddisktype.md).

</dd> <dt>

*mergeTask* \[out, retval\]
</dt> <dd>

An [**IVMTask**](ivmtask.md) object that is used to track the completion of the merging process.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                    | The operation was successful.<br/>                                                                                                                                                                                                                                                                      |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                      | A parameter is **NULL**.<br/>                                                                                                                                                                                                                                                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                                   | The *newDiskImagePath* parameter is empty.<br/>                                                                                                                                                                                                                                                         |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_FILE\_NOT\_FOUND)**</dt> <dt>0x80070002</dt> </dl>   | The system cannot find the file specified by the *newDiskImagePath* parameter.<br/>                                                                                                                                                                                                                     |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_PATH\_NOT\_FOUND)**</dt> <dt>0x80070003</dt> </dl>   | The system cannot find the path specified by the *newDiskImagePath* parameter.<br/>                                                                                                                                                                                                                     |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_INVALID\_NAME)**</dt> <dt>0x8007007b</dt> </dl>      | The *newDiskImagePath* parameter contains an invalid character (one of the following: "\*?<>/\|":").<br/>                                                                                                                                                                                         |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BAD\_PATHNAME)**</dt> <dt>0x800700a1</dt> </dl>      | The *newDiskImagePath* parameter specifies an empty or relative path. An absolute path is required.<br/>                                                                                                                                                                                                |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BUFFER\_OVERFLOW)**</dt> <dt>0x8007006f</dt> </dl>   | The path specified by the *newDiskImagePath* parameter is too long. The path must be less than 260 characters.<br/>                                                                                                                                                                                     |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_SHARING\_VIOLATION)**</dt> <dt>0x80070020</dt> </dl> | Either the virtual hard disk referenced by this object is in use or the parent of this virtual hard disk is in use.<br/>                                                                                                                                                                                |
| <dl> <dt>**VM\_E\_WRONG\_HD\_IMAGE\_TYPE**</dt> <dt>0xA004067B</dt> </dl>                   | This error is caused either because the virtual hard disk image referenced by this [**IVMHardDisk**](ivmharddisk.md) object is not a differencing disk image or because the parameter *newDiskImageType* is not one of the accepted values, **vmDiskType\_Dynamic** or **vmDiskType\_FixedSize**.<br/> |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_ALREADY\_EXISTS)**</dt> <dt>0x800700b7</dt> </dl>    | The file referenced by the *newDiskImagePath* parameter already exists.<br/>                                                                                                                                                                                                                            |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_DISK\_FULL)**</dt> <dt>0x80070070</dt> </dl>         | The host volume does not have enough space to merge this virtual hard disk.<br/>                                                                                                                                                                                                                        |
| <dl> <dt>**VM\_E\_PARENT\_PATH\_NOT\_FOUND**</dt> <dt>0xA0040677</dt> </dl>                 | The parent of the virtual hard disk referenced by this object does not exist.<br/>                                                                                                                                                                                                                      |
| <dl> <dt>**VM\_E\_APP\_SHUTTING\_DOWN**</dt> <dt>0xA0040209</dt> </dl>                      | The virtual hard disk image cannot be merged because the application is shutting down.<br/>                                                                                                                                                                                                             |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                              | An unexpected error has occurred.<br/>                                                                                                                                                                                                                                                                  |



 

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

 

