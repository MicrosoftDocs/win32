---
title: IVMSupportDriver interface
description: The IVMSupportDriver interface defines an interface to a support driver installed on the host computer.
ms.assetid: '16d42b51-a2fb-45a8-9ab9-be4c54bf6784'
keywords: ["IVMSupportDriver interface Virtual Server", "IVMSupportDriver interface Virtual Server , described"]
topic_type:
- apiref
api_name:
- IVMSupportDriver
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMSupportDriver interface

The **IVMSupportDriver** interface defines an interface to a support driver installed on the host computer. This interface is used to retrieve basic information about the driver. You can retrieve an **IVMSupportDriver** object from the [**IVMSupportDriverCollection**](ivmsupportdrivercollection.md) object returned from the [**IVMVirtualServer::SupportDrivers**](ivmvirtualserver-supportdrivers.md) property.

## Members

The **IVMSupportDriver** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMSupportDriver** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMSupportDriver** interface has these properties.



| Property                                                         | Access type          | Description                                       |
|:-----------------------------------------------------------------|:---------------------|:--------------------------------------------------|
| [**Date**](ivmsupportdriver-date.md)<br/>                 | Read-only<br/> | The build date of the driver.<br/>          |
| [**Description**](ivmsupportdriver-description.md)<br/>   | Read-only<br/> | The driver's description.<br/>              |
| [**Manufacturer**](ivmsupportdriver-manufacturer.md)<br/> | Read-only<br/> | The name of the driver's manufacturer.<br/> |
| [**Provider**](ivmsupportdriver-provider.md)<br/>         | Read-only<br/> | The name of the driver's provider.<br/>     |
| [**Type**](ivmsupportdriver-type.md)<br/>                 | Read-only<br/> | The type of support driver.<br/>            |
| [**Version**](ivmsupportdriver-version.md)<br/>           | Read-only<br/> | The version number of the driver.<br/>      |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |
| IID<br/>      | IID\_IVMSupportDriver is defined as D4CCAE0F-391E-4f31-A4EF-FE8B000FEFD5<br/>               |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[Virtual Server Interfaces](interfaces.md)
</dt> </dl>

 

 





