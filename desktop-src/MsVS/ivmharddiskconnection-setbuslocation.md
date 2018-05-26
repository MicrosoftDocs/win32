---
title: IVMHardDiskConnection SetBusLocation method
description: The SetBusLocation method sets the bus location to which this hard disk is attached.
ms.assetid: c29099c2-a16d-4f27-9d38-a6f4d54cb864
keywords:
- SetBusLocation method Virtual Server
- SetBusLocation method Virtual Server , IVMHardDiskConnection interface
- IVMHardDiskConnection interface Virtual Server , SetBusLocation method
- SetBusLocation method Virtual Server , VMHardDiskConnection interface
- VMHardDiskConnection interface Virtual Server , SetBusLocation method
topic_type:
- apiref
api_name:
- IVMHardDiskConnection.SetBusLocation
- VMHardDiskConnection.SetBusLocation
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

# IVMHardDiskConnection::SetBusLocation method

The **SetBusLocation** method sets the bus location to which this hard disk is attached.

## Syntax


```C++
HRESULT SetBusLocation(
  [in] VMDriveBusType busType,
  [in] long           busNumber,
  [in] long           deviceNumber
);
```



## Parameters

<dl> <dt>

*busType* \[in\]
</dt> <dd>

The type of bus to use.

</dd> <dt>

*busNumber* \[in\]
</dt> <dd>

Which bus number to use. If the *busType* is [**vmDriveBusTypeIDE**](vmdrivebustype.md), the *busNumber* must be in the range of 0 through 1. If the *busType* is **vmDriveBusTypeSCSI**, the *busNumber* must be in the range of 0 through 3.

</dd> <dt>

*deviceNumber* \[in\]
</dt> <dd>

Which device number to use on the selected bus. If the *busType* is [**vmDriveBusTypeIDE**](vmdrivebustype.md), the *deviceNumber* must be in the range of 0 through 1. If the *busType* is **vmDriveBusTypeSCSI**, the *deviceNumber* must be in the range of 0 through 6. If the *busType* is **vmDriveBusTypeSCSI** and the bus is being used for a shared SCSI bus, the *deviceNumber* must be 0.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                                     | Description                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                           | The operation was successful.<br/>                                                                    |
| <dl> <dt> **E\_INVALIDARG**</dt> </dl>                   | The bus location specified is invalid.<br/>                                                           |
| <dl> <dt> **VM\_E\_VM\_RUNNING**</dt> </dl>              | The bus location could not be set because the virtual machine is currently running.<br/>              |
| <dl> <dt> **VM\_E\_DRIVE\_BUS\_LOC\_IN\_USE**</dt> </dl> | The bus location could not be set because another device is currently attached to this location.<br/> |
| <dl> <dt> **VM\_E\_DRIVE\_INVALID**</dt> </dl>           | The current drive is invalid.<br/>                                                                    |
| <dl> <dt> **VM\_E\_VM\_UNKNOWN**</dt> </dl>              | The current virtual machine is invalid.<br/>                                                          |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>              | An unexpected error occurred.<br/>                                                                    |



 

## Remarks

Only one disk device is allowed on a shared SCSI controller.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHardDiskConnection**](ivmharddiskconnection.md)
</dt> <dt>

[**VMDriveBusType**](vmdrivebustype.md)
</dt> </dl>

 

 





