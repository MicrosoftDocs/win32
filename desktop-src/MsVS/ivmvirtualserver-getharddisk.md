---
title: IVMVirtualServer GetHardDisk method
description: The GetHardDisk method returns a IVMHardDisk object corresponding to an existing disk image file.
ms.assetid: 41960ce7-8e7b-4eeb-baed-490ec36ce996
keywords:
- GetHardDisk method Virtual Server
- GetHardDisk method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , GetHardDisk method
topic_type:
- apiref
api_name:
- IVMVirtualServer.GetHardDisk
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

# IVMVirtualServer::GetHardDisk method

The **GetHardDisk** method returns a [**IVMHardDisk**](ivmharddisk.md) object corresponding to an existing disk image file.

## Syntax


```C++
HRESULT GetHardDisk(
  [in]  BSTR        imagePath,
  [out] IVMHardDisk **hardDisk
);
```



## Parameters

<dl> <dt>

*imagePath* \[in\]
</dt> <dd>

The full path to an existing disk image file.

</dd> <dt>

*hardDisk* \[out\]
</dt> <dd>

[**IVMHardDisk**](ivmharddisk.md) object corresponding to this disk image.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                        | Description                                                                                                                      |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | The operation was successful.<br/>                                                                                         |
| <dl> <dt>**E\_POINTER**</dt> </dl>          | The *imagePath* or *hardDisk* parameter is **NULL**.<br/>                                                                  |
| <dl> <dt>**E\_FILE\_NOT\_FOUND**</dt> </dl> | The system cannot find the file specified by the *imagePath* parameter.<br/>                                               |
| <dl> <dt>**E\_PATH\_NOT\_FOUND**</dt> </dl> | The system cannot find the path specified by the *imagePath* parameter.<br/>                                               |
| <dl> <dt>**E\_INVALID\_NAME**</dt> </dl>    | The *imagePath* parameter contains an invalid character (one of "\*?:&lt;&gt;/\|"").<br/>                                  |
| <dl> <dt>**E\_BAD\_PATHNAME**</dt> </dl>    | The *imagePath* parameter specifies an empty or relative path. An absolute path is required.<br/>                          |
| <dl> <dt>**E\_BUFFER\_OVERFLOW**</dt> </dl> | The path specified by the *imagePath* parameter is too long. The length of the path must be less than 260 characters.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>  | An unexpected error occurred.<br/>                                                                                         |



 

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

 

 





