---
title: IVMParallelPortCollection interface
description: The IVMParallelPortCollection interface defines the collection of parallel ports within the virtual machine. An IVMParallelPortCollection object is returned from the IVMVirtualMachine ParallelPorts property.
ms.assetid: e9a81900-7285-4588-a743-f3c99c2fd8fd
keywords:
- IVMParallelPortCollection interface Virtual Server
- IVMParallelPortCollection interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMParallelPortCollection
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

# IVMParallelPortCollection interface

The **IVMParallelPortCollection** interface defines the collection of parallel ports within the virtual machine. An **IVMParallelPortCollection** object is returned from the [**IVMVirtualMachine::ParallelPorts**](ivmvirtualmachine-parallelports.md) property.

## Members

The **IVMParallelPortCollection** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMParallelPortCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMParallelPortCollection** interface has these properties.



| Property                                                           | Access type          | Description                                                                                                              |
|:-------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmparallelportcollection--newenum.md)<br/> | Read-only<br/> | An **IEnumVariant** enumerator for the collection.<br/>                                                            |
| [**Count**](ivmparallelportcollection-count.md)<br/>        | Read-only<br/> | The number of parallel ports defined in this collection.<br/>                                                      |
| [**Item**](ivmparallelportcollection-item.md)<br/>          | Read-only<br/> | The [**IVMParallelPort**](ivmparallelport.md) object that corresponds to the given index in this collection.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





