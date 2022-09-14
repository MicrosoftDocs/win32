---
title: IVMVirtualPC GetHardDisk method (VPCCOMInterfaces.h)
description: Retrieves an object corresponding to an existing disk image file.
ms.assetid: 648a3f8a-5114-4c14-b9a9-f175941333ab
keywords:
- GetHardDisk method Virtual PC
- GetHardDisk method Virtual PC , IVMVirtualPC interface
- IVMVirtualPC interface Virtual PC , GetHardDisk method
topic_type:
- apiref
api_name:
- IVMVirtualPC.GetHardDisk
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC::GetHardDisk method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves an object corresponding to an existing disk image file.

## Syntax


```C++
HRESULT GetHardDisk(
  [in]          BSTR        imagePath,
  [out, retval] IVMHardDisk **hardDisk
);
```



## Parameters

<dl> <dt>

*imagePath* \[in\]
</dt> <dd>

The full path to an existing disk image file.

</dd> <dt>

*hardDisk* \[out, retval\]
</dt> <dd>

An [**IVMHardDisk**](ivmharddisk.md) object corresponding to this disk image.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                            | Description                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                  | The operation was successful.<br/>                                                                                         |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                    | The *imagePath* or *hardDisk* parameter is **NULL**.<br/>                                                                  |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_FILE\_NOT\_FOUND)**</dt> <dt>0x80070002</dt> </dl> | The system cannot find the file specified by the *imagePath* parameter.<br/>                                               |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_PATH\_NOT\_FOUND)**</dt> <dt>0x80070003</dt> </dl> | The system cannot find the path specified by the *imagePath* parameter.<br/>                                               |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_INVALID\_NAME)**</dt> <dt>0x8007007b</dt> </dl>    | The *imagePath* parameter contains an invalid character (one of "\*?:<>/\|"").<br/>                                  |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BAD\_PATHNAME)**</dt> <dt>0x800700a1</dt> </dl>    | The *imagePath* parameter specifies an empty or relative path. An absolute path is required.<br/>                          |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BUFFER\_OVERFLOW)**</dt> <dt>0x8007006f</dt> </dl> | The path specified by the *imagePath* parameter is too long. The length of the path must be less than 260 characters.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                            | An unexpected error has occurred.<br/>                                                                                     |
| <dl> <dt>**VM\_E\_HARDWARE\_VIRTUALIZATION\_DISABLED**</dt> <dt>0xA0040951</dt> </dl>     | The processor does not support Hardware Accelerated Virtualization (HAV) extensions.<br/>                                  |



 

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

 

