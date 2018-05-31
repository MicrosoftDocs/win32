---
title: IVMVirtualServer GetFloppyDiskImageType method
description: The GetFloppyDiskImageType method returns the type of an existing floppy disk image file.
ms.assetid: ba4bd5bd-5698-4771-89df-ba976a7ada1d
keywords:
- GetFloppyDiskImageType method Virtual Server
- GetFloppyDiskImageType method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , GetFloppyDiskImageType method
topic_type:
- apiref
api_name:
- IVMVirtualServer.GetFloppyDiskImageType
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMVirtualServer::GetFloppyDiskImageType method

The **GetFloppyDiskImageType** method returns the type of an existing floppy disk image file.

## Syntax


```C++
HRESULT GetFloppyDiskImageType(
  [in]  BSTR                  imagePath,
  [out] VMFloppyDiskImageType *imageType
);
```



## Parameters

<dl> <dt>

*imagePath* \[in\]
</dt> <dd>

The full path to the disk image file.

</dd> <dt>

*imageType* \[out\]
</dt> <dd>

Retrieves the type of the image. See [**VMFloppyDiskImageType**](vmfloppydiskimagetype.md).

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                         | Description                                                                                                                      |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>               | The operation was successful.<br/>                                                                                         |
| <dl> <dt>**E\_POINTER**</dt> </dl>           | The *imagePath* or *imageType* parameter is **NULL**.<br/>                                                                 |
| <dl> <dt>**E\_FILE\_NOT\_FOUND**</dt> </dl>  | The system cannot find the file specified by the *imagePath* parameter.<br/>                                               |
| <dl> <dt>**E\_PATH\_NOT\_FOUND**</dt> </dl>  | The system cannot find the path specified by the *imagePath* parameter.<br/>                                               |
| <dl> <dt>**E\_INVALID\_NAME**</dt> </dl>     | The *imagePath* parameter contains an invalid character (one of "\*?:&lt;&gt;/\|"").<br/>                                  |
| <dl> <dt>**E\_BAD\_PATHNAME**</dt> </dl>     | The *imagePath* parameter specifies an empty or relative path. An absolute path is required.<br/>                          |
| <dl> <dt> **E\_BUFFER\_OVERFLOW**</dt> </dl> | The path specified by the *imagePath* parameter is too long. The length of the path must be less than 260 characters.<br/> |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>  | The file specified by *imagePath* is not a floppy image, or an unexpected error occurred.<br/>                             |



 

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

 

 





