---
title: IVMSerialPort interface (VPCCOMInterfaces.h)
description: Defines a serial port inside a virtual machine.
ms.assetid: a6568885-bfdf-4559-8886-02ca59096ca0
keywords:
- IVMSerialPort interface Virtual PC
- IVMSerialPort interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMSerialPort
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMSerialPort interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines a serial port inside a virtual machine. This interface allows you to configure serial ports inside a virtual machine. You can retrieve an **IVMSerialPort** object from the [**IVMSerialPortCollection**](ivmserialportcollection.md) object returned from the [**IVMVirtualMachine::SerialPorts**](ivmvirtualmachine-serialports.md) property.

## Members

The **IVMSerialPort** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMSerialPort** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMSerialPort** interface has these methods.



| Method                                       | Description                                                      |
|:---------------------------------------------|:-----------------------------------------------------------------|
| [**\_ID**](ivmserialport--id.md)            | Retrieves the internal identifier of the serial port.<br/> |
| [**Configure**](ivmserialport-configure.md) | Configures the serial port.<br/>                           |



 

### Properties

The **IVMSerialPort** interface has these properties.



| Property                                                                  | Access type          | Description                                                                                                       |
|:--------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------|
| [**ConnectImmediately**](ivmserialport-connectimmediately.md)<br/> | Read-only<br/> | Indicates whether the serial port should be opened without waiting for a modem command to be received.<br/> |
| [**Name**](ivmserialport-name.md)<br/>                             | Read-only<br/> | The name of the serial port.<br/>                                                                           |
| [**Type**](ivmserialport-type.md)<br/>                             | Read-only<br/> | The type of the serial port.<br/>                                                                           |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMSerialPort is defined as 2ce4460d-1d3f-4458-bf8b-44084b816815<br/>              |



 

