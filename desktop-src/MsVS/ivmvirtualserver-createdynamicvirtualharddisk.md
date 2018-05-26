---
title: IVMVirtualServer CreateDynamicVirtualHardDisk method
description: The CreateDynamicVirtualHardDisk method creates a dynamically resizing virtual hard disk.
ms.assetid: e46069d0-4985-41e9-b235-f3d0acd41b02
keywords:
- CreateDynamicVirtualHardDisk method Virtual Server
- CreateDynamicVirtualHardDisk method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , CreateDynamicVirtualHardDisk method
topic_type:
- apiref
api_name:
- IVMVirtualServer.CreateDynamicVirtualHardDisk
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMVirtualServer::CreateDynamicVirtualHardDisk method

The **CreateDynamicVirtualHardDisk** method creates a dynamically resizing virtual hard disk.

## Syntax


```C++
HRESULT CreateDynamicVirtualHardDisk(
  [in]  BSTR    imagePath,
  [in]  long    size,
  [out] IVMTask **diskTask
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

Size, in megabytes, of the image. Can be at most 2,088,960 MB (2040 GB).

</dd> <dt>

*diskTask* \[out\]
</dt> <dd>

Retrieves the task which is used to track the creation of the image.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                         | Description                                                                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                | The operation was successful.<br/>                                                                                                                                                     |
| <dl> <dt>**E\_POINTER**</dt> </dl>                           | The *imagePath* or *diskTask* parameter is **NULL**.<br/>                                                                                                                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                        | The *size* parameter is less than or equal to 0.<br/>                                                                                                                                  |
| <dl> <dt>**E\_PATH\_NOT\_FOUND**</dt> </dl>                  | The system cannot find the path specified by the *imagePath* parameter.<br/>                                                                                                           |
| <dl> <dt>**E\_INVALID\_NAME**</dt> </dl>                     | The *imagePath* parameter contains an invalid character (one of "\*?:&lt;&gt;/\|"").<br/>                                                                                              |
| <dl> <dt>**E\_BAD\_PATHNAME**</dt> </dl>                     | The *imagePath* parameter specifies an empty or relative path. An absolute path is required.<br/>                                                                                      |
| <dl> <dt>**E\_BUFFER\_OVERFLOW**</dt> </dl>                  | The path specified by the *imagePath* parameter is too long. The length of the path must be less than 260 characters.<br/>                                                             |
| <dl> <dt>**E\_ALREADY\_EXISTS**</dt> </dl>                   | The file referenced by the parameter *imagePath* already exists.<br/>                                                                                                                  |
| <dl> <dt>**E\_DISK\_FULL**</dt> </dl>                        | The dynamically expanding virtual hard disk image needs at least 8 MB free on the host volume.<br/>                                                                                    |
| <dl> <dt>**VM\_E\_IMAGE\_SIZE\_TOO\_LARGE**</dt> </dl>       | The parameter *size* must be less than 2,088,960 MB. If *format* is "vmDiskFormat\_FAT16", then *size* must be less than 2000 MB.<br/>                                                 |
| <dl> <dt>**VM\_E\_IMAGE\_SIZE\_TOO\_SMALL**</dt> </dl>       | Unformatted and FAT16 formatted virtual hard disk images must be at least 3 MB. FAT32 formatted virtual hard disk images must be at least 514 MB.<br/>                                 |
| <dl> <dt>**VM\_E\_FILE\_TOO\_LARGE\_FOR\_VOLUME**</dt> </dl> | The host volume cannot support a file this size if the dynamically expanding virtual hard disk image expands to its full limit. The maximum file size for a FAT32 volume is 4 GB.<br/> |
| <dl> <dt>**VM\_E\_APP\_SHUTTING\_DOWN**</dt> </dl>           | The virtual hard disk cannot be created after the application has started shutting down.<br/>                                                                                          |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>                   | An unexpected error occurred.<br/>                                                                                                                                                     |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





