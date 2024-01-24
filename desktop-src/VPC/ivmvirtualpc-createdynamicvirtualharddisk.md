---
title: IVMVirtualPC CreateDynamicVirtualHardDisk method (VPCCOMInterfaces.h)
description: Creates a dynamically resizing virtual hard disk.
ms.assetid: 2373ac41-c4c4-44c6-93e1-92814cd40b81
keywords:
- CreateDynamicVirtualHardDisk method Virtual PC
- CreateDynamicVirtualHardDisk method Virtual PC , IVMVirtualPC interface
- IVMVirtualPC interface Virtual PC , CreateDynamicVirtualHardDisk method
topic_type:
- apiref
api_name:
- IVMVirtualPC.CreateDynamicVirtualHardDisk
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC::CreateDynamicVirtualHardDisk method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Creates a dynamically resizing virtual hard disk.

## Syntax


```C++
HRESULT CreateDynamicVirtualHardDisk(
  [in]          BSTR    imagePath,
  [in]          long    size,
  [out, retval] IVMTask **diskTask
);
```



## Parameters

<dl> <dt>

*imagePath* \[in\]
</dt> <dd>

The full path to the new disk image file. The containing folder will be created if it does not exist.

</dd> <dt>

*size* \[in\]
</dt> <dd>

The size of the image, in megabytes. This value can be at most 2,088,960 MB (2040GB).

</dd> <dt>

*diskTask* \[out, retval\]
</dt> <dd>

An [**IVMTask**](ivmtask.md) object that is used to track the creation of the image.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                            | Description                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                  | The operation was successful.<br/>                                                                                                                                                                                                       |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                    | A parameter is **NULL**.<br/>                                                                                                                                                                                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                                 | The *size* parameter is less than or equal to 0.<br/>                                                                                                                                                                                    |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_PATH\_NOT\_FOUND)**</dt> <dt>0x80070003</dt> </dl> | The system cannot find the path specified by the *imagePath* parameter.<br/>                                                                                                                                                             |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_INVALID\_DRIVE)**</dt> <dt>0x8007000f</dt> </dl>   | The file specified by the *imagePath* parameter is on a CD-ROM or DVD-ROM.<br/>                                                                                                                                                          |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_INVALID\_NAME)**</dt> <dt>0x8007007b</dt> </dl>    | The *imagePath* parameter contains an invalid character (one of "\*?:<>/\|"").<br/>                                                                                                                                                |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BAD\_PATHNAME)**</dt> <dt>0x800700a1</dt> </dl>    | Both the *imagePath* parameter specifies an empty or relative path. At least one of the parameters must be an absolute path.<br/>                                                                                                        |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BUFFER\_OVERFLOW)**</dt> <dt>0x8007006f</dt> </dl> | The path specified by the *imagePath* parameter is too long. The length of the path must be less than 260 characters.<br/>                                                                                                               |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_ALREADY\_EXISTS)**</dt> <dt>0x800700b7</dt> </dl>  | The file referenced by the *imagePath* parameter already exists.<br/>                                                                                                                                                                    |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_DISK\_FULL)**</dt> <dt>0x80070070</dt> </dl>       | The dynamically expanding virtual hard disk image needs at least 8 MB free on the host volume.<br/>                                                                                                                                      |
| <dl> <dt>**VM\_E\_IMAGE\_SIZE\_TOO\_LARGE**</dt> <dt>0xA0040683</dt> </dl>                | The parameter *size* must be less than 2,088,960 MB. If the format is FAT16, then size must be less than 2000 MB.<br/>                                                                                                                   |
| <dl> <dt>**VM\_E\_IMAGE\_SIZE\_TOO\_SMALL**</dt> <dt>0xA0040684</dt> </dl>                | Unformatted and FAT16 formatted virtual hard disk images must be at least 3 MB. FAT32 formatted virtual hard disk images must be at least 514 MB.<br/>                                                                                   |
| <dl> <dt>**VM\_E\_FILE\_TOO\_LARGE\_FOR\_VOLUME**</dt> <dt>0xA0040679</dt> </dl>          | The host volume cannot support a file this size if the dynamically expanding virtual hard disk image expands to its full limit. The maximum file size for a FAT32 volume is 4 GB. The maximum file size for a FAT16 volume is 2 GB.<br/> |
| <dl> <dt>**VM\_E\_APP\_SHUTTING\_DOWN**</dt> <dt>0xA0040209</dt> </dl>                    | The virtual hard disk cannot be created after the application has started shutting down.<br/>                                                                                                                                            |
| <dl> <dt>**VM\_E\_HARDWARE\_VIRTUALIZATION\_DISABLED**</dt> <dt>0xA0040951</dt> </dl>     | The processor does not support Hardware Accelerated Virtualization (HAV) extensions.<br/>                                                                                                                                                |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                            | An unexpected error has occurred.<br/>                                                                                                                                                                                                   |



 

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

 

