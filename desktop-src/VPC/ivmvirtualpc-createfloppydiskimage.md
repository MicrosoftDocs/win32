---
title: IVMVirtualPC CreateFloppyDiskImage method (VPCCOMInterfaces.h)
description: Creates a floppy disk image file.
ms.assetid: 474e86a4-2019-41bd-9361-e494291d1961
keywords:
- CreateFloppyDiskImage method Virtual PC
- CreateFloppyDiskImage method Virtual PC , IVMVirtualPC interface
- IVMVirtualPC interface Virtual PC , CreateFloppyDiskImage method
topic_type:
- apiref
api_name:
- IVMVirtualPC.CreateFloppyDiskImage
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC::CreateFloppyDiskImage method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Creates a floppy disk image file.

## Syntax


```C++
HRESULT CreateFloppyDiskImage(
  [in] BSTR                  imagePath,
  [in] VMFloppyDiskImageType imageType
);
```



## Parameters

<dl> <dt>

*imagePath* \[in\]
</dt> <dd>

The full path to the new disk image file. The containing folder will be created if it does not exist.

</dd> <dt>

*imageType* \[in\]
</dt> <dd>

The type of floppy disk image to create. Only **vmFloppyDiskImage\_LowDensity** (1) and **vmFloppyDiskImage\_HighDensity** (2) are supported. See [**VMFloppyDiskImageType**](vmfloppydiskimagetype.md).

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                            | Description                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                                                                                         | The operation was successful.<br/>                                                                                                                  |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                    | The *imagePath* parameter is **NULL**.<br/>                                                                                                         |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                                 | The *imageType* parameter is not [**vmFloppyDiskImage\_LowDensity**](vmfloppydiskimagetype.md) (1) or **vmFloppyDiskImage\_HighDensity** (2).<br/> |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_PATH\_NOT\_FOUND)**</dt> <dt>0x80070003</dt> </dl> | The system cannot find the path specified by the *imagePath* parameter.<br/>                                                                        |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_INVALID\_NAME)**</dt> <dt>0x8007007b</dt> </dl>    | The *imagePath* parameter contains an invalid character (one of "\*?:<>/\|"").<br/>                                                           |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BAD\_PATHNAME)**</dt> <dt>0x800700a1</dt> </dl>    | The *imagePath* parameter specifies an empty or relative path. An absolute path is required.<br/>                                                   |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BUFFER\_OVERFLOW)**</dt> <dt>0x8007006f</dt> </dl> | The path specified by the *imagePath* parameter is too long. The length of the path must be less than 260 characters.<br/>                          |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_ALREADY\_EXISTS)**</dt> <dt>0x800700b7</dt> </dl>  | The file referenced by the parameter *imagePath* already exists.<br/>                                                                               |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_DISK\_FULL)**</dt> <dt>0x80070070</dt> </dl>       | There is insufficient space on the host volume to create the virtual floppy disk image.<br/>                                                        |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                            | An unexpected error occurred.<br/>                                                                                                                  |
| <dl> <dt>**VM\_E\_HARDWARE\_VIRTUALIZATION\_DISABLED**</dt> <dt>0xA0040951</dt> </dl>     | The processor does not support Hardware Accelerated Virtualization (HAV) extensions.<br/>                                                           |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualPC is defined as 236ba0d9-a24a-4292-a132-27c1421dfd01<br/>               |



## See also

<dl> <dt>

[**IVMVirtualPC**](ivmvirtualpc.md)
</dt> </dl>

 

