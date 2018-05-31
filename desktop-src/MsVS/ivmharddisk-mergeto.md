---
title: IVMHardDisk MergeTo method
description: The MergeTo method merges a differencing hard disk image with all of its parents (up to and including the root parent hard disk image) to a new hard disk file.
ms.assetid: 4104e560-0444-4614-9abd-5afdf4809d33
keywords:
- MergeTo method Virtual Server
- MergeTo method Virtual Server , IVMHardDisk interface
- IVMHardDisk interface Virtual Server , MergeTo method
- MergeTo method Virtual Server , VMHardDisk interface
- VMHardDisk interface Virtual Server , MergeTo method
topic_type:
- apiref
api_name:
- IVMHardDisk.MergeTo
- VMHardDisk.MergeTo
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

# IVMHardDisk::MergeTo method

The **MergeTo** method merges a differencing hard disk image with all of its parents (up to and including the root parent hard disk image) to a new hard disk file.

## Syntax


```C++
HRESULT MergeTo(
  [in]  BSTR           newDiskImagePath,
  [in]  VMHardDiskType newDiskImageType,
  [out] IVMTask        **mergeTask
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

The type of new target disk image. The image types allowed for the new target disk image are vmDiskType\_Dynamic and vmDiskType\_FixedSize. See [**VMHardDiskType**](vmharddisktype.md).

</dd> <dt>

*mergeTask* \[out\]
</dt> <dd>

The task which is used to track the completion of the merging process.

</dd> </dl>

## Return value



| Return code                                                                                                    | Description                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                          | The operation was successful.<br/>                                                                                                                                                                                                                                                              |
| <dl> <dt> **E\_POINTER**</dt> </dl>                     | The *newDiskImagePath* or *mergeTask* parameter is **NULL**.<br/>                                                                                                                                                                                                                               |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                   | The *newDiskImagePath* parameter is empty.<br/>                                                                                                                                                                                                                                                 |
| <dl> <dt>**E\_FILE\_NOT\_FOUND**</dt> </dl>             | The system cannot find the file specified by the *newDiskImagePath* parameter.<br/>                                                                                                                                                                                                             |
| <dl> <dt>**E\_PATH\_NOT\_FOUND**</dt> </dl>             | The system cannot find the path specified by the *newDiskImagePath* parameter.<br/>                                                                                                                                                                                                             |
| <dl> <dt>**E\_INVALID\_NAME**</dt> </dl>                | The *newDiskImagePath* parameter contains an invalid character (one of the following: \*?&lt;&gt;/\|":).<br/>                                                                                                                                                                                   |
| <dl> <dt>**E\_BAD\_PATHNAME**</dt> </dl>                | The *newDiskImagePath* parameter specifies an empty or relative path. An absolute path is required.<br/>                                                                                                                                                                                        |
| <dl> <dt>**E\_BUFFER\_OVERFLOW**</dt> </dl>             | The path specified by the *newDiskImagePath* parameter is too long. The path must be less than 260 characters.<br/>                                                                                                                                                                             |
| <dl> <dt>**E\_SHARING\_VIOLATION**</dt> </dl>           | Either the virtual hard disk referenced by this object is in use or the parent of this virtual hard disk is in use.<br/>                                                                                                                                                                        |
| <dl> <dt> **VM\_E\_WRONG\_HD\_IMAGE\_TYPE**</dt> </dl>  | This error is caused either because the virtual hard disk image referenced by this [**IVMHardDisk**](ivmharddisk.md) object is not a differencing disk image or because the parameter *newDiskImageType* is not one of the accepted values, vmDiskType\_Dynamic or vmDiskType\_FixedSize.<br/> |
| <dl> <dt>**E\_ALREADY\_EXISTS**</dt> </dl>              | The file referenced by the *newDiskImagePath* parameter already exists.<br/>                                                                                                                                                                                                                    |
| <dl> <dt>**E\_DISK\_FULL**</dt> </dl>                   | The host volume does not have enough space to merge this virtual hard disk.<br/>                                                                                                                                                                                                                |
| <dl> <dt>**VM\_E\_PARENT\_PATH\_NOT\_FOUND**</dt> </dl> | The parent of the virtual hard disk referenced by this object does not exist.<br/>                                                                                                                                                                                                              |
| <dl> <dt>**VM\_E\_APP\_SHUTTING\_DOWN**</dt> </dl>      | The virtual hard disk image cannot be merged because the application is shutting down.<br/>                                                                                                                                                                                                     |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>             | An unexpected error occurred.<br/>                                                                                                                                                                                                                                                              |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHardDisk**](ivmharddisk.md)
</dt> </dl>

 

 





