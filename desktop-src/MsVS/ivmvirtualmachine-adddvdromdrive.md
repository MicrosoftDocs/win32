---
title: IVMVirtualMachine AddDVDROMDrive method
description: The AddDVDROMDrive method adds a new CD or DVD drive to the virtual machine.
ms.assetid: 3f4fa53a-c80b-4cb0-b170-aa3b3b84ea0c
keywords:
- AddDVDROMDrive method Virtual Server
- AddDVDROMDrive method Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , AddDVDROMDrive method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.AddDVDROMDrive
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

# IVMVirtualMachine::AddDVDROMDrive method

The **AddDVDROMDrive** method adds a new CD or DVD drive to the virtual machine.

## Syntax


```C++
HRESULT AddDVDROMDrive(
  [in]  VMDriveBusType busType,
  [in]  long           busNumber,
  [in]  long           deviceNumber,
  [out] IVMDVDDrive    **dvdDrive
);
```



## Parameters

<dl> <dt>

*busType* \[in\]
</dt> <dd>

Bus to attach the CD or DVD drive to.

</dd> <dt>

*busNumber* \[in\]
</dt> <dd>

Bus number to attach the CD or DVD drive to. For IDE, this number can be 0-1. DVDROM drives cannot be attached to the SCSI bus.

</dd> <dt>

*deviceNumber* \[in\]
</dt> <dd>

Device number to attach the CD or DVD drive to. For IDE, this number can be 0-1. DVDROM drives cannot be attached to the SCSI bus.

</dd> <dt>

*dvdDrive* \[out\]
</dt> <dd>

A new [**IVMDVDDrive**](ivmdvddrive.md) object.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                                     | Description                                                      |
|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                           | The operation was successful.<br/>                         |
| <dl> <dt> **E\_POINTER**</dt> </dl>                      | *dvdDrive* is **NULL**.<br/>                               |
| <dl> <dt> **E\_INVALIDARG**</dt> </dl>                   | *busType*, *busNumber*, or *deviceNumber* is invalid.<br/> |
| <dl> <dt> **VM\_E\_VM\_UNKNOWN**</dt> </dl>              | The configuration is unknown.<br/>                         |
| <dl> <dt> **VM\_E\_VM\_RUNNING**</dt> </dl>              | Virtual machine is running or saved.<br/>                  |
| <dl> <dt> **VM\_E\_DRIVE\_BUS\_LOC\_IN\_USE**</dt> </dl> | The specified bus location is in use.<br/>                 |
| <dl> <dt> **VM\_E\_DRIVE\_INVALID**</dt> </dl>           | Invalid drive specified.<br/>                              |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>              | An unexpected error has occurred.<br/>                     |



 

## Remarks

You can only add a new CD or DVD drive to a stopped virtual machine.

## Examples

The following example adds a DVD drive to the secondary IDE controller as the primary device.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")
Set objDVD = objVM.AddDVDROMDrive(0,1,0)
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> <dt>

[**VMDriveBusType**](vmdrivebustype.md)
</dt> </dl>

 

 





