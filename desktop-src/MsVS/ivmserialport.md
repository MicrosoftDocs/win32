---
title: IVMSerialPort interface
description: The IVMSerialPort interface defines a serial port inside a virtual machine.
ms.assetid: 6b24012f-d1b2-47aa-93a5-e5d5c4650e87
keywords:
- IVMSerialPort interface Virtual Server
- IVMSerialPort interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMSerialPort
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

# IVMSerialPort interface

The **IVMSerialPort** interface defines a serial port inside a virtual machine. This interface allows you to configure serial ports inside a virtual machine. You can retrieve an **IVMSerialPort** object from the [**IVMSerialPortCollection**](ivmserialportcollection.md) object returned from the [**IVMVirtualMachine::SerialPorts**](ivmvirtualmachine-serialports.md) property.

## Members

The **IVMSerialPort** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMSerialPort** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMSerialPort** interface has these methods.



| Method                                       | Description                            |
|:---------------------------------------------|:---------------------------------------|
| [**Configure**](ivmserialport-configure.md) | Configures the serial port.<br/> |



 

### Properties

The **IVMSerialPort** interface has these properties.



| Property                                                                  | Access type          | Description                                                                                                       |
|:--------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------|
| [**\_ID**](ivmserialport--id.md)<br/>                              | Read-only<br/> | The internal ID of the serial port.<br/>                                                                    |
| [**ConnectImmediately**](ivmserialport-connectimmediately.md)<br/> | Read-only<br/> | Indicates whether the serial port should be opened without waiting for a modem command to be received.<br/> |
| [**Name**](ivmserialport-name.md)<br/>                             | Read-only<br/> | The name of the serial port.<br/>                                                                           |
| [**Type**](ivmserialport-type.md)<br/>                             | Read-only<br/> | The type of the serial port.<br/>                                                                           |



 

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

 

 





