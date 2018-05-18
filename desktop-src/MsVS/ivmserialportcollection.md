---
title: VMSerialPortCollection interface
description: The IVMSerialPortCollection interface defines the collection of serial ports within the virtual machine. An IVMSerialPortCollection object is returned from the IVMVirtualMachine SerialPorts property.
ms.assetid: 'e7cf9fdb-6b04-4da8-833f-c076ba4b8346'
keywords: ["VMSerialPortCollection interface Virtual Server", "VMSerialPortCollection interface Virtual Server , described"]
topic_type:
- apiref
api_name:
- VMSerialPortCollection
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# VMSerialPortCollection interface

The **IVMSerialPortCollection** interface defines the collection of serial ports within the virtual machine. An **IVMSerialPortCollection** object is returned from the [**IVMVirtualMachine::SerialPorts**](ivmvirtualmachine-serialports.md) property.

## Members

The **VMSerialPortCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **VMSerialPortCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **VMSerialPortCollection** interface has these properties.



| Property                                                         | Access type          | Description                                                                                                          |
|:-----------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmserialportcollection--newenum.md)<br/> | Read-only<br/> | An **IEnumVariant** enumerator for the collection.<br/>                                                        |
| [**Count**](ivmserialportcollection-count.md)<br/>        | Read-only<br/> | The number of serial ports defined in this collection.<br/>                                                    |
| [**Item**](ivmserialportcollection-item.md)<br/>          | Read-only<br/> | The [**IVMSerialPort**](ivmserialport.md) object that corresponds to the given index in this collection.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[**IVMSerialPort**](ivmserialport.md)
</dt> </dl>

 

 





