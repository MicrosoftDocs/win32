---
title: IVMDVDDrive AttachImage method
description: The AttachImage method attaches an ISO image to the DVD drive within the virtual machine.
ms.assetid: 'b60735ee-c888-4601-afd5-223c5c13281c'
keywords: ["AttachImage method Virtual Server", "AttachImage method Virtual Server , IVMDVDDrive interface", "IVMDVDDrive interface Virtual Server , AttachImage method", "AttachImage method Virtual Server , VMDVDDrive interface", "VMDVDDrive interface Virtual Server , AttachImage method"]
topic_type:
- apiref
api_name:
- IVMDVDDrive.AttachImage
- VMDVDDrive.AttachImage
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMDVDDrive::AttachImage method

The **AttachImage** method attaches an ISO image to the DVD drive within the virtual machine.

## Syntax


```C++
HRESULT AttachImage(
  [in] BSTR imagePath
);
```



## Parameters

<dl> <dt>

*imagePath* \[in\]
</dt> <dd>

The full path to the ISO image that is to be attached.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                          | Description                                                                                                  |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                 | The operation was successful.<br/>                                                                     |
| <dl> <dt>**E\_POINTER**</dt> </dl>            | The *imagePath* parameter is **NULL**.<br/>                                                            |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>    | The virtual machine could not be found.<br/>                                                           |
| <dl> <dt>**VM\_E\_DRIVE\_IN\_USE**</dt> </dl> | A host DVD drive or ISO image is already attached to this drive.<br/>                                  |
| <dl> <dt>**VM\_E\_DRIVE\_INVALID**</dt> </dl> | The bus location for this drive is invalid, or the drive does not appear to be a valid DVD drive.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>    | An unexpected error occurred.<br/>                                                                     |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDVDDrive**](ivmdvddrive.md)
</dt> </dl>

 

 





