---
title: IVMFloppyDrive AttachImage method
description: The AttachImage method attaches a floppy media image residing on the host machine to the floppy drive in the virtual machine.
ms.assetid: 'e0dcd0fb-2d59-4051-aa29-6a96c2e67ce2'
keywords: ["AttachImage method Virtual Server", "AttachImage method Virtual Server , IVMFloppyDrive interface", "IVMFloppyDrive interface Virtual Server , AttachImage method", "AttachImage method Virtual Server , VMFloppyDrive interface", "VMFloppyDrive interface Virtual Server , AttachImage method"]
topic_type:
- apiref
api_name:
- IVMFloppyDrive.AttachImage
- VMFloppyDrive.AttachImage
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMFloppyDrive::AttachImage method

The **AttachImage** method attaches a floppy media image residing on the host machine to the floppy drive in the virtual machine.

## Syntax


```C++
HRESULT AttachImage(
  [in] BSTR mediaImagePath
);
```



## Parameters

<dl> <dt>

*mediaImagePath* \[in\]
</dt> <dd>

The full path to the floppy media image that is to be attached.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                | Description                                                                          |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | The operation was successful.<br/>                                             |
| <dl> <dt>**E\_POINTER**</dt> </dl>                  | The *mediaImagePath* parameter is **NULL**.<br/>                               |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>          | The configuration for this virtual machine is invalid or cannot be found.<br/> |
| <dl> <dt>**VM\_E\_IMAGE\_CAPTURE\_FAIL**</dt> </dl> | The image file specified could not be captured.<br/>                           |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>          | An unexpected error occurred.<br/>                                             |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMFloppyDrive**](ivmfloppydrive.md)
</dt> </dl>

 

 





