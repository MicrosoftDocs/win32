---
title: IVMTaskCollection interface
description: The IVMTaskCollection interface defines the collection of task objects. An IVMTaskCollection object is returned from the IVMVirtualServer Tasks property.
ms.assetid: fc9272c1-5af9-4ac8-b75e-6d9bc8f69099
keywords:
- IVMTaskCollection interface Virtual Server
- IVMTaskCollection interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMTaskCollection
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

# IVMTaskCollection interface

The **IVMTaskCollection** interface defines the collection of task objects. An **IVMTaskCollection** object is returned from the [**IVMVirtualServer::Tasks**](ivmvirtualserver-tasks.md) property.

## Members

The **IVMTaskCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMTaskCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMTaskCollection** interface has these properties.



| Property                                                   | Access type          | Description                                                                                              |
|:-----------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmtaskcollection--newenum.md)<br/> | Read-only<br/> | An **IEnumVariant** enumerator for the collection.<br/>                                            |
| [**Count**](ivmtaskcollection-count.md)<br/>        | Read-only<br/> | The number of tasks defined in this collection.<br/>                                               |
| [**Item**](ivmtaskcollection-item.md)<br/>          | Read-only<br/> | The [**IVMTask**](ivmtask.md) object that corresponds to the given index in this collection.<br/> |



 

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

[**IVMTask**](ivmtask.md)
</dt> </dl>

 

 





