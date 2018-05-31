---
title: IVMParallelPort interface
description: The IVMParallelPort interface defines a parallel port inside a virtual machine.
ms.assetid: 01eab5ea-f537-44e7-9242-fa2c6ec8f959
keywords:
- IVMParallelPort interface Virtual Server
- IVMParallelPort interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMParallelPort
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

# IVMParallelPort interface

The **IVMParallelPort** interface defines a parallel port inside a virtual machine. This interface allows you to configure parallel ports inside a virtual machine. You can retrieve an **IVMParallelPort** object from the [**IVMParallelPortCollection**](ivmparallelportcollection.md) object returned from the [**IVMVirtualMachine::ParallelPorts**](ivmvirtualmachine-parallelports.md) property.

## Members

The **IVMParallelPort** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMParallelPort** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMParallelPort** interface has these properties.



| Property                                        | Access type           | Description                                       |
|:------------------------------------------------|:----------------------|:--------------------------------------------------|
| [**\_ID**](ivmparallelport--id.md)<br/>  | Read-only<br/>  | The internal ID of this parallel port.<br/> |
| [**Name**](ivmparallelport-name.md)<br/> | Read/write<br/> | The name of the parallel port.<br/>         |



 

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

 

 





