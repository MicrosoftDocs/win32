---
title: IVMHardDisk Convert method (VPCCOMInterfaces.h)
description: Converts a fixed-size virtual hard disk to a dynamically expanding virtual hard disk or converts a dynamically expanding virtual hard disk to a fixed-size virtual hard disk.
ms.assetid: 0dee802a-1cac-499e-918a-7dbb6c98415f
keywords:
- Convert method Virtual PC
- Convert method Virtual PC , IVMHardDisk interface
- IVMHardDisk interface Virtual PC , Convert method
topic_type:
- apiref
api_name:
- IVMHardDisk.Convert
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMHardDisk::Convert method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Converts a fixed-size virtual hard disk to a dynamically expanding virtual hard disk or converts a dynamically expanding virtual hard disk to a fixed-size virtual hard disk.

## Syntax


```C++
HRESULT Convert(
  [in]          BSTR           convertedDiskImagePath,
  [in]          VMHardDiskType convertedDiskImageType,
  [out, retval] IVMTask        **convertTask
);
```



## Parameters

<dl> <dt>

*convertedDiskImagePath* \[in\]
</dt> <dd>

The path to the target disk image file.

</dd> <dt>

*convertedDiskImageType* \[in\]
</dt> <dd>

The type of the target disk image. For a list of values, see [**VMHardDiskType**](vmharddisktype.md).

</dd> <dt>

*convertTask* \[out, retval\]
</dt> <dd>

An [**IVMTask**](ivmtask.md) object that is used to track the completion of the conversion process.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                              | Description                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                    | The operation was successful.<br/>                                                                                                        |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                                   | The *convertedDiskImagePath* parameter is empty or missing the .vhd extension on the file name.<br/>                                      |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                      | A parameter is **NULL**.<br/>                                                                                                             |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_PATH\_NOT\_FOUND)**</dt> <dt>0x80070003</dt> </dl>   | The system cannot find the path specified by the *convertedDiskImagePath* parameter.<br/>                                                 |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_INVALID\_NAME)**</dt> <dt>0x8007007b</dt> </dl>      | The *convertedDiskImagePath* parameter contains an invalid character (one of "\*?<>/\|":").<br/>                                    |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BAD\_PATHNAME)**</dt> <dt>0x800700a1</dt> </dl>      | The *convertedDiskImagePath* parameter specifies an empty or relative path. An absolute path is required.<br/>                            |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BUFFER\_OVERFLOW)**</dt> <dt>0x8007006f</dt> </dl>   | The path specified by the *convertedDiskImagePath* parameter is too long. The path must be less than **MAX\_PATH** (260) characters.<br/> |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_SHARING\_VIOLATION)**</dt> <dt>0x80070020</dt> </dl> | Either the virtual hard disk referenced by this object is in use or the parent of this virtual hard disk is in use.<br/>                  |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_DISK\_FULL)**</dt> <dt>0x80070070</dt> </dl>         | The host volume does not have enough space to convert this virtual hard disk.<br/>                                                        |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_ALREADY\_EXISTS)**</dt> <dt>0x800700b7</dt> </dl>    | The file referenced by the *convertedDiskImagePath* parameter already exists.<br/>                                                        |
| <dl> <dt>**VM\_E\_WRONG\_HD\_IMAGE\_TYPE**</dt> <dt>0xA004067B</dt> </dl>                   | The *convertedDiskImagePath* parameter must be either **vmDiskType\_Dynamic** or **vmDiskType\_FixedSize**.<br/>                          |
| <dl> <dt>**VM\_E\_INVALID\_HD\_FILE**</dt> <dt>0xA0040682</dt> </dl>                        | The virtual hard disk image referenced by this [**IVMHardDisk**](ivmharddisk.md) object does not seem to be a valid image.<br/>          |
| <dl> <dt>**VM\_E\_PARENT\_PATH\_NOT\_FOUND**</dt> <dt>0xA0040677</dt> </dl>                 | The parent of the virtual hard disk referenced by this object does not exist.<br/>                                                        |
| <dl> <dt>**VM\_E\_APP\_SHUTTING\_DOWN**</dt> <dt>0xA0040209</dt> </dl>                      | The virtual hard disk image cannot be converted because the application is shutting down.<br/>                                            |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                              | An unexpected error has occurred.<br/>                                                                                                    |



 

## Remarks

The source file is left intact after the conversion process.

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

 

