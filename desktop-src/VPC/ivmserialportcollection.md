---
title: IVMSerialPortCollection interface (VPCCOMInterfaces.h)
description: Defines the collection of serial ports within the virtual machine. To obtain an IVMSerialPortCollection object, use the IVMVirtualMachine SerialPorts property.
ms.assetid: c0ee9799-f3f7-477e-b33b-52f424752aad
keywords:
- IVMSerialPortCollection interface Virtual PC
- IVMSerialPortCollection interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMSerialPortCollection
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMSerialPortCollection interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Defines the collection of serial ports within the virtual machine. To obtain an **IVMSerialPortCollection** object, use the [**IVMVirtualMachine::SerialPorts**](ivmvirtualmachine-serialports.md) property.

## Members

The **IVMSerialPortCollection** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMSerialPortCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMSerialPortCollection** interface has these properties.



| Property                                                         | Access type          | Description                                                                |
|:-----------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------|
| [**\_NewEnum**](ivmserialportcollection--newenum.md)<br/> | Read-only<br/> | An enumerator for the collection.<br/>                               |
| [**Count**](ivmserialportcollection-count.md)<br/>        | Read-only<br/> | The number of serial ports in this collection.<br/>                  |
| [**Item**](ivmserialportcollection-item.md)<br/>          | Read-only<br/> | The serial port object that corresponds to the specified index.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMSerialPortCollection is defined as dd3c6175-1f04-4341-9f85-104074880289<br/>    |



## See also

<dl> <dt>

[**IVMSerialPort**](ivmserialport.md)
</dt> <dt>

[**IVMVirtualMachine::SerialPorts**](ivmvirtualmachine-serialports.md)
</dt> </dl>

 

