---
title: IVMFloppyDrive ReleaseImage method
description: The ReleaseImage method releases the currently attached floppy media image from the floppy drive in the virtual machine.
ms.assetid: '86e0c9bb-8ef1-4e8f-8cfb-d3b90de4be43'
keywords: ["ReleaseImage method Virtual Server", "ReleaseImage method Virtual Server , IVMFloppyDrive interface", "IVMFloppyDrive interface Virtual Server , ReleaseImage method", "ReleaseImage method Virtual Server , VMFloppyDrive interface", "VMFloppyDrive interface Virtual Server , ReleaseImage method"]
topic_type:
- apiref
api_name:
- IVMFloppyDrive.ReleaseImage
- VMFloppyDrive.ReleaseImage
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMFloppyDrive::ReleaseImage method

The **ReleaseImage** method releases the currently attached floppy media image from the floppy drive in the virtual machine.

## Syntax


```C++
HRESULT ReleaseImage();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                               | Description                                                                          |
|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | The operation was successful.<br/>                                             |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>         | The configuration for this virtual machine is invalid or cannot be found.<br/> |
| <dl> <dt>**VM\_E\_MEDIA\_WRONG\_TYPE**</dt> </dl>  | The media attached to this floppy drive is not a floppy disk image.<br/>       |
| <dl> <dt>**VM\_E\_NO\_MEDIA\_CAPTURED**</dt> </dl> | There is no media attached to this floppy drive.<br/>                          |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>         | An unexpected error occurred.<br/>                                             |



 

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

 

 





