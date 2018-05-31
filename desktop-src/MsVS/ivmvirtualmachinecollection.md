---
title: IVMVirtualMachineCollection interface
description: The IVMVirtualMachineCollection interface defines the collection of virtual machines within Virtual Server. An IVMVirtualMachineCollection object is returned from the IVMVirtualServer VirtualMachines property.
ms.assetid: 4904b2e8-0acc-4fc3-8bf9-8baacf5d5f4c
keywords:
- IVMVirtualMachineCollection interface Virtual Server
- IVMVirtualMachineCollection interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMVirtualMachineCollection
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachineCollection interface

The **IVMVirtualMachineCollection** interface defines the collection of virtual machines within Virtual Server. An **IVMVirtualMachineCollection** object is returned from the [**IVMVirtualServer::VirtualMachines**](ivmvirtualserver-virtualmachines.md) property.

## Members

The **IVMVirtualMachineCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMVirtualMachineCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMVirtualMachineCollection** interface has these properties.



| Property                                                             | Access type          | Description                                                                                                                  |
|:---------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmvirtualmachinecollection--newenum.md)<br/> | Read-only<br/> | An **IEnumVariant** enumerator for the collection.<br/>                                                                |
| [**Count**](ivmvirtualmachinecollection-count.md)<br/>        | Read-only<br/> | The number of virtual machines in this collection.<br/>                                                                |
| [**Item**](ivmvirtualmachinecollection-item.md)<br/>          | Read-only<br/> | The [**IVMVirtualMachine**](ivmvirtualmachine.md) object that corresponds to the given index in this collection.<br/> |



 

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

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





