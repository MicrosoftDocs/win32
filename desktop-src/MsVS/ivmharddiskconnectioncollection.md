---
title: IVMHardDiskConnectionCollection interface
description: The IVMHardDiskConnectionCollection interface defines the collection of hard disk connections within the virtual machine. You can retrieve an IVMHardDiskConnectionCollection object from the IVMVirtualMachine HardDiskConnections property.
ms.assetid: 08b3da93-8aaf-4cc6-a206-963bb134e9b8
keywords:
- IVMHardDiskConnectionCollection interface Virtual Server
- IVMHardDiskConnectionCollection interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMHardDiskConnectionCollection
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMHardDiskConnectionCollection interface

The **IVMHardDiskConnectionCollection** interface defines the collection of hard disk connections within the virtual machine. You can retrieve an **IVMHardDiskConnectionCollection** object from the [**IVMVirtualMachine::HardDiskConnections**](ivmvirtualmachine-harddiskconnections.md) property.

## Members

The **IVMHardDiskConnectionCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMHardDiskConnectionCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMHardDiskConnectionCollection** interface has these properties.



| Property                                                                 | Access type          | Description                                                                                                                          |
|:-------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmharddiskconnectioncollection--newenum.md)<br/> | Read-only<br/> | An **IEnumVariant** enumerator for the collection.<br/>                                                                        |
| [**Count**](ivmharddiskconnectioncollection-count.md)<br/>        | Read-only<br/> | The number of connections defined in this collection.<br/>                                                                     |
| [**Item**](ivmharddiskconnectioncollection-item.md)<br/>          | Read-only<br/> | The [**IVMHardDiskConnection**](ivmharddiskconnection.md) object that corresponds to the given index in this collection.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





