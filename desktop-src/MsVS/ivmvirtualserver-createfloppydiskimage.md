---
title: IVMVirtualServer CreateFloppyDiskImage method
description: The CreateFloppyDiskImage method creates a floppy disk image file.
ms.assetid: '2d19c5c6-beca-4b97-b0fa-6816c54d3903'
keywords: ["CreateFloppyDiskImage method Virtual Server", "CreateFloppyDiskImage method Virtual Server , IVMVirtualServer interface", "IVMVirtualServer interface Virtual Server , CreateFloppyDiskImage method"]
topic_type:
- apiref
api_name:
- IVMVirtualServer.CreateFloppyDiskImage
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::CreateFloppyDiskImage method

The **CreateFloppyDiskImage** method creates a floppy disk image file.

## Syntax


```C++
HRESULT CreateFloppyDiskImage(
  [in] BSTR                  imagePath,
  [in] VMFloppyDiskImageType imageType
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

The type of floppy disk image to create. Only [**vmFloppyDiskImage\_LowDensity**](vmfloppydiskimagetype.md) and **vmFloppyDiskImage\_HighDensity** are supported. See **VMFloppyDiskImageType**.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                         | Description                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>               | The operation was successful.<br/>                                                                                                          |
| <dl> <dt>**E\_POINTER**</dt> </dl>           | The *imagePath* parameter is **NULL**.<br/>                                                                                                 |
| <dl> <dt> **E\_INVALIDARG**</dt> </dl>       | The *imageType* parameter is not [**vmFloppyDiskImage\_LowDensity**](vmfloppydiskimagetype.md) or **vmFloppyDiskImage\_HighDensity**.<br/> |
| <dl> <dt>**E\_PATH\_NOT\_FOUND**</dt> </dl>  | The system cannot find the path specified by the *imagePath* parameter.<br/>                                                                |
| <dl> <dt>**E\_INVALID\_NAME**</dt> </dl>     | The *imagePath* parameter contains an invalid character (one of "\*?:&lt;&gt;/\|"").<br/>                                                   |
| <dl> <dt>**E\_BAD\_PATHNAME**</dt> </dl>     | The *imagePath* parameter specifies an empty or relative path. An absolute path is required.<br/>                                           |
| <dl> <dt> **E\_BUFFER\_OVERFLOW**</dt> </dl> | The path specified by the *imagePath* parameter is too long. The length of the path must be less than 260 characters.<br/>                  |
| <dl> <dt>**E\_ALREADY\_EXISTS**</dt> </dl>   | The file referenced by the parameter *imagePath* already exists.<br/>                                                                       |
| <dl> <dt> **E\_DISK\_FULL**</dt> </dl>       | There is insufficient space on the host volume to create the virtual floppy disk image.<br/>                                                |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>  | An unexpected error occurred.<br/>                                                                                                          |



 

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

 

 





