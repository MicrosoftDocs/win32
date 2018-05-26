---
title: IVMHardDisk Convert method
description: The Convert method converts a disk image to either a dynamically expanding disk image or a fixed-size disk image.
ms.assetid: e3010258-7128-459e-8dec-03aa1d1b04f4
keywords:
- Convert method Virtual Server
- Convert method Virtual Server , IVMHardDisk interface
- IVMHardDisk interface Virtual Server , Convert method
- Convert method Virtual Server , VMHardDisk interface
- VMHardDisk interface Virtual Server , Convert method
topic_type:
- apiref
api_name:
- IVMHardDisk.Convert
- VMHardDisk.Convert
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

# IVMHardDisk::Convert method

The **Convert** method converts a disk image to either a dynamically expanding disk image or a fixed-size disk image.

## Syntax


```C++
HRESULT Convert(
  [in]  BSTR           convertedDiskImagePath,
  [in]  VMHardDiskType convertedDiskImageType,
  [out] IVMTask        **convertTask
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

The type of the target disk image. This parameter must be either vmDiskType\_Dynamic or vmDiskType\_FixedSize. See [**VMHardDiskType**](vmharddisktype.md).

</dd> <dt>

*convertTask* \[out\]
</dt> <dd>

The task which is used to track the completion of the conversion process.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                    | Description                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                          | The operation was successful.<br/>                                                                                        |
| <dl> <dt> **E\_POINTER**</dt> </dl>                     | The *convertedDiskImagePath* or *convertTask* parameter is **NULL**.<br/>                                                 |
| <dl> <dt>**E\_PATH\_NOT\_FOUND**</dt> </dl>             | The system cannot find the path specified by the *convertedDiskImagePath* parameter.<br/>                                 |
| <dl> <dt>**E\_INVALID\_NAME**</dt> </dl>                | The *convertedDiskImagePath* parameter contains an invalid character (one of "\*?&lt;&gt;/\|":").<br/>                    |
| <dl> <dt>**E\_BAD\_PATHNAME**</dt> </dl>                | The *convertedDiskImagePath* parameter specifies an empty or relative path. An absolute path is required.<br/>            |
| <dl> <dt>**E\_BUFFER\_OVERFLOW**</dt> </dl>             | The path specified by the *convertedDiskImagePath* parameter is too long. The path must be less than 260 characters.<br/> |
| <dl> <dt>**E\_SHARING\_VIOLATION**</dt> </dl>           | Either the virtual hard disk referenced by this object is in use or the parent of this virtual hard disk is in use.<br/>  |
| <dl> <dt>**E\_DISK\_FULL**</dt> </dl>                   | The host volume does not have enough space to convert this virtual hard disk.<br/>                                        |
| <dl> <dt>**E\_ALREADY\_EXISTS**</dt> </dl>              | The file referenced by the *convertedDiskImagePath* parameter already exists.<br/>                                        |
| <dl> <dt> **VM\_E\_WRONG\_HD\_IMAGE\_TYPE**</dt> </dl>  | The *convertedDiskImageType* parameter must be either vmDiskType\_Dynamic or vmDiskType\_FixedSize.<br/>                  |
| <dl> <dt> **VM\_E\_INVALID\_HD\_FILE**</dt> </dl>       | The virtual hard disk image referenced by this **IVMHardDisk** object does not seem to be a valid image.<br/>             |
| <dl> <dt>**VM\_E\_PARENT\_PATH\_NOT\_FOUND**</dt> </dl> | The parent of the virtual hard disk referenced by this object does not exist.<br/>                                        |
| <dl> <dt>**VM\_E\_APP\_SHUTTING\_DOWN**</dt> </dl>      | The virtual hard disk image cannot be converted because the application is shutting down.<br/>                            |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>             | An unexpected error occurred.<br/>                                                                                        |



 

## Remarks

The source file is left intact after the conversion process.

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

 

 





