---
title: IVMFloppyDrive AttachHostDrive method
description: The AttachHostDrive method attaches a physical floppy drive on the host machine to the floppy drive in the virtual machine.
ms.assetid: 'b00af8c2-7cdd-439a-9e23-3e5f8802b085'
keywords: ["AttachHostDrive method Virtual Server", "AttachHostDrive method Virtual Server , IVMFloppyDrive interface", "IVMFloppyDrive interface Virtual Server , AttachHostDrive method", "AttachHostDrive method Virtual Server , VMFloppyDrive interface", "VMFloppyDrive interface Virtual Server , AttachHostDrive method"]
topic_type:
- apiref
api_name:
- IVMFloppyDrive.AttachHostDrive
- VMFloppyDrive.AttachHostDrive
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMFloppyDrive::AttachHostDrive method

The **AttachHostDrive** method attaches a physical floppy drive on the host machine to the floppy drive in the virtual machine.

## Syntax


```C++
HRESULT AttachHostDrive(
  [in] BSTR driveLetter
);
```



## Parameters

<dl> <dt>

*driveLetter* \[in\]
</dt> <dd>

The drive letter of the physical floppy drive on the host machine that is to be attached.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                       | Description                                                                          |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                              | The operation was successful.<br/>                                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                      | The parameter is **NULL**, or the given path is empty.<br/>                    |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>                 | The configuration for this virtual machine is invalid or cannot be found.<br/> |
| <dl> <dt>**VM\_E\_HOST\_FLOPPY\_CAPTURE\_FAIL**</dt> </dl> | The host drive specified could not be captured.<br/>                           |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>                 | An unexpected error occurred.<br/>                                             |



 

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

 

 





