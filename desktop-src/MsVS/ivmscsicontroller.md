---
title: IVMSCSIController interface
description: The IVMSCSIController interface provides access to a SCSI controller attached to a virtual machine.
ms.assetid: bea79ee3-a2aa-4479-b63e-6713a07a1088
keywords:
- IVMSCSIController interface Virtual Server
- IVMSCSIController interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMSCSIController
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IVMSCSIController interface

The **IVMSCSIController** interface provides access to a SCSI controller attached to a virtual machine. A SCSI controller can be added and removed from a virtual machine by using [**IVMVirtualMachine::AddSCSIController**](ivmvirtualmachine-addscsicontroller.md) and [**IVMVirtualMachine::RemoveSCSIController**](ivmvirtualmachine-removescsicontroller.md). You can also retrieve an **IVMSCSIController** object from the [**IVMSCSIControllerCollection**](ivmscsicontrollercollection.md) object returned from the [**IVMVirtualMachine::SCSIControllers**](ivmvirtualmachine-scsicontrollers.md) property.

## Members

The **IVMSCSIController** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMSCSIController** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMSCSIController** interface has these methods.



| Method                                           | Description                                                                                |
|:-------------------------------------------------|:-------------------------------------------------------------------------------------------|
| [**Configure**](ivmscsicontroller-configure.md) | Configures the SCSI controller to be used on an independent or on a shared bus.<br/> |



 

### Properties

The **IVMSCSIController** interface has these properties.



| Property                                                        | Access type          | Description                                                               |
|:----------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------|
| [**\_ID**](ivmscsicontroller--id.md)<br/>                | Read-only<br/> | The internal ID of this SCSI controller.<br/>                       |
| [**IsBusShared**](ivmscsicontroller-isbusshared.md)<br/> | Read-only<br/> | Indicates whether the SCSI controller is on a shared SCSI bus.<br/> |
| [**SCSIID**](ivmscsicontroller-scsiid.md)<br/>           | Read-only<br/> | The ID of the controller on a SCSI bus.<br/>                        |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> </dl>

 

 





