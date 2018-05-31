---
title: IVMSCSIControllerCollection interface
description: The IVMSCSIControllerCollection interface defines the collection of SCSI controllers within a virtual machine. You can retrieve an IVMSCSIControllerCollection object from the IVMVirtualMachine SCSIControllers property.
ms.assetid: 8dad0aae-c49d-4743-b59e-1a018b1987ad
keywords:
- IVMSCSIControllerCollection interface Virtual Server
- IVMSCSIControllerCollection interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMSCSIControllerCollection
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

# IVMSCSIControllerCollection interface

The **IVMSCSIControllerCollection** interface defines the collection of SCSI controllers within a virtual machine. You can retrieve an **IVMSCSIControllerCollection** object from the [**IVMVirtualMachine::SCSIControllers**](ivmvirtualmachine-scsicontrollers.md) property.

## Members

The **IVMSCSIControllerCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMSCSIControllerCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMSCSIControllerCollection** interface has these properties.



| Property                                                             | Access type          | Description                                                                                                                  |
|:---------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmscsicontrollercollection--newenum.md)<br/> | Read-only<br/> | An **IEnumVariant** enumerator for the collection.<br/>                                                                |
| [**Count**](ivmscsicontrollercollection-count.md)<br/>        | Read-only<br/> | The number of controllers defined in this collection.<br/>                                                             |
| [**Item**](ivmscsicontrollercollection-item.md)<br/>          | Read-only<br/> | The [**IVMSCSIController**](ivmscsicontroller.md) object that corresponds to the given index in this collection.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[**IVMSCSIController**](ivmscsicontroller.md)
</dt> </dl>

 

 





