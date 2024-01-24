---
title: IVMSerialPort Type property (VPCCOMInterfaces.h)
description: Retrieves the type of the serial port.
ms.assetid: 0ec9c9d7-9387-458e-befe-42d58c38df35
keywords:
- Type property Virtual PC
- Type property Virtual PC , IVMSerialPort interface
- IVMSerialPort interface Virtual PC , Type property
topic_type:
- apiref
api_name:
- IVMSerialPort.Type
- IVMSerialPort.get_Type
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMSerialPort::Type property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the type of the serial port.

This property is read-only.

## Syntax


```C++
HRESULT get_Type(
  [out, retval] VMSerialPortType *portType
);
```



## Property value

The type of serial port. For a list of values, see [**VMSerialPortType**](vmserialporttype.md).

## Error codes



| Name/value                                                                                                                                                    | Meaning                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>                            |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is NULL.<br/>                                   |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl> | The configuration for this virtual machine is not valid.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>                        |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMSerialPort is defined as 2ce4460d-1d3f-4458-bf8b-44084b816815<br/>              |



## See also

<dl> <dt>

[**IVMSerialPort**](ivmserialport.md)
</dt> </dl>

 

