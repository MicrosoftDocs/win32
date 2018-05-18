---
title: IVMVirtualServer CreateHostDriveVirtualHardDisk method
description: The CreateHostDriveVirtualHardDisk method creates a virtual hard disk that is linked to a host drive.
ms.assetid: '78a439fb-1daf-437f-b417-db579fc54b14'
keywords: ["CreateHostDriveVirtualHardDisk method Virtual Server", "CreateHostDriveVirtualHardDisk method Virtual Server , IVMVirtualServer interface", "IVMVirtualServer interface Virtual Server , CreateHostDriveVirtualHardDisk method"]
topic_type:
- apiref
api_name:
- IVMVirtualServer.CreateHostDriveVirtualHardDisk
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::CreateHostDriveVirtualHardDisk method

The **CreateHostDriveVirtualHardDisk** method creates a virtual hard disk that is linked to a host drive.

## Syntax


```C++
HRESULT CreateHostDriveVirtualHardDisk(
  [in]  BSTR         imagePath,
  [in]  BSTR         hostDriveIdentifier,
  [in]  VARIANT_BOOL mountReadOnly,
  [out] IVMTask      **diskTask
);
```



## Parameters

<dl> <dt>

*imagePath* \[in\]
</dt> <dd>

The full path to the new disk image file. The containing folder will be created if it does not exist.

</dd> <dt>

*hostDriveIdentifier* \[in\]
</dt> <dd>

An identifier used to distinguish between the host drives. Use [**IVMHostInfo::HostDrives**](ivmhostinfo-hostdrives.md) to get valid drive identifiers.

</dd> <dt>

*mountReadOnly* \[in\]
</dt> <dd>

This parameter is only valid if the host drive is unmounted. If the host drive is already mounted, then the virtual hard disk image will always mount as read-only.

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
| <dl> <dt>**E\_POINTER**</dt> </dl>                           | The *imagePath*, *hostDriveIdentifier*, or *diskTask* parameter is **NULL**.<br/>                                                                                                      |
| <dl> <dt>**E\_PATH\_NOT\_FOUND**</dt> </dl>                  | The system cannot find the path specified by the *imagePath* parameter.<br/>                                                                                                           |
| <dl> <dt>**E\_INVALID\_NAME**</dt> </dl>                     | The *imagePath* parameter contains an invalid character (one of "\*?:&lt;&gt;/\|"").<br/>                                                                                              |
| <dl> <dt>**E\_BAD\_PATHNAME**</dt> </dl>                     | The *imagePath* parameter specifies an empty or relative path. An absolute path is required.<br/>                                                                                      |
| <dl> <dt>**E\_BUFFER\_OVERFLOW**</dt> </dl>                  | The path specified by the *imagePath* parameter is too long. The length of the path must be less than 260 characters.<br/>                                                             |
| <dl> <dt>**E\_ALREADY\_EXISTS**</dt> </dl>                   | The file referenced by the parameter *imagePath* already exists.<br/>                                                                                                                  |
| <dl> <dt>**E\_DISK\_FULL**</dt> </dl>                        | The dynamically expanding virtual hard disk image needs at least 8 MB free on the host volume.<br/>                                                                                    |
| <dl> <dt>**VM\_E\_IMAGE\_SIZE\_TOO\_LARGE**</dt> </dl>       | The parameter *size* must be less than 2,088,960 MB. If *format* is "vmDiskFormat\_FAT16", then *size* must be less than 2,000 MB.<br/>                                                |
| <dl> <dt>**VM\_E\_IMAGE\_SIZE\_TOO\_SMALL**</dt> </dl>       | Unformatted and FAT16 formatted virtual hard disk images must be at least 3 MB. FAT32 formatted virtual hard disk images must be at least 514 MB.<br/>                                 |
| <dl> <dt>**VM\_E\_FILE\_TOO\_LARGE\_FOR\_VOLUME**</dt> </dl> | The host volume cannot support a file this size if the dynamically expanding virtual hard disk image expands to its full limit. The maximum file size for a FAT32 volume is 4 GB.<br/> |
| <dl> <dt>**VM\_E\_APP\_SHUTTING\_DOWN**</dt> </dl>           | The virtual hard disk cannot be created after the application has started shutting down.<br/>                                                                                          |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>                   | An unexpected error occurred.<br/>                                                                                                                                                     |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





