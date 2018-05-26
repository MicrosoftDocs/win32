---
title: IVMVirtualMachine RemoveDVDROMDrive method
description: The RemoveDVDROMDrive method removes the specified CD or DVD drive from the virtual machine.
ms.assetid: 2c8b79d8-cd00-47c3-9262-baee3567b187
keywords:
- RemoveDVDROMDrive method Virtual Server
- RemoveDVDROMDrive method Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , RemoveDVDROMDrive method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.RemoveDVDROMDrive
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

# IVMVirtualMachine::RemoveDVDROMDrive method

The **RemoveDVDROMDrive** method removes the specified CD or DVD drive from the virtual machine.

## Syntax


```C++
HRESULT RemoveDVDROMDrive(
  [in] IVMDVDDrive *dvdDrive
);
```



## Parameters

<dl> <dt>

*dvdDrive* \[in\]
</dt> <dd>

The DVDROM drive to be removed.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                           | Description                                                                                     |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                 | The operation was successful.<br/>                                                        |
| <dl> <dt> **E\_POINTER**</dt> </dl>            | The *dvdDrive* parameter is **NULL**.<br/>                                                |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>     | The configuration is unknown.<br/>                                                        |
| <dl> <dt> **VM\_E\_VM\_RUNNING**</dt> </dl>    | Virtual machine is running or saved.<br/>                                                 |
| <dl> <dt> **VM\_E\_DRIVE\_INVALID**</dt> </dl> | Invalid drive specified (e.g. no CD or DVD drive is connected to this bus location).<br/> |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>    | An unexpected error has occurred.<br/>                                                    |



 

## Remarks

You can only remove an existing CD or DVD drive from a stopped virtual machine.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





