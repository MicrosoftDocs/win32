---
title: IVMSupportDriverCollection interface
description: The IVMSupportDriverCollection interface defines the collection of support drivers installed on the Host computer. An IVMSupportDriverCollection object is returned from the IVMVirtualServer SupportDrivers property.
ms.assetid: b91164c0-977c-4fdc-acb3-9688e7e65a72
keywords:
- IVMSupportDriverCollection interface Virtual Server
- IVMSupportDriverCollection interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMSupportDriverCollection
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

# IVMSupportDriverCollection interface

The **IVMSupportDriverCollection** interface defines the collection of support drivers installed on the Host computer. An **IVMSupportDriverCollection** object is returned from the [**IVMVirtualServer::SupportDrivers**](ivmvirtualserver-supportdrivers.md) property.

## Members

The **IVMSupportDriverCollection** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMSupportDriverCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMSupportDriverCollection** interface has these properties.



| Property                                                            | Access type          | Description                                                                                                                |
|:--------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmsupportdrivercollection--newenum.md)<br/> | Read-only<br/> | An **IEnumVariant** enumerator for the collection.<br/>                                                              |
| [**Count**](ivmsupportdrivercollection-count.md)<br/>        | Read-only<br/> | The number of support driver objects contained in this collection.<br/>                                              |
| [**Item**](ivmsupportdrivercollection-item.md)<br/>          | Read-only<br/> | The [**IVMSupportDriver**](ivmsupportdriver.md) object that corresponds to the given index in this collection.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[**IVMSupportDriver**](ivmsupportdriver.md)
</dt> </dl>

 

 





