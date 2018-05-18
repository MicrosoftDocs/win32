---
title: IVMSerialPort Configure method
description: The Configure method configures the serial port.
ms.assetid: 'f984cd0d-bd06-4c19-a242-8aa0d2b38919'
keywords: ["Configure method Virtual Server", "Configure method Virtual Server , IVMSerialPort interface", "IVMSerialPort interface Virtual Server , Configure method", "Configure method Virtual Server , VMSerialPort interface", "VMSerialPort interface Virtual Server , Configure method"]
topic_type:
- apiref
api_name:
- IVMSerialPort.Configure
- VMSerialPort.Configure
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMSerialPort::Configure method

The **Configure** method configures the serial port.

## Syntax


```C++
HRESULT Configure(
  [in] VMSerialPortType portType,
  [in] BSTR             portName,
  [in] VARIANT_BOOL     connectImmediately
);
```



## Parameters

<dl> <dt>

*portType* \[in\]
</dt> <dd>

Type of serial port.

</dd> <dt>

*portName* \[in\]
</dt> <dd>

Name of the serial port (for example, **COM1** for [**vmSerialPortHostPort**](vmserialporttype.md), **C:\\SerialPort.txt** for **vmSerialPortTextFile**, or **\\\\servername\\pipe\\pipename** for **vmSerialPortNamedPipe**).

</dd> <dt>

*connectImmediately* \[in\]
</dt> <dd>

**TRUE** if the host serial port should be opened immediately when the virtual machine is started. Ignored if type is not [**vmSerialPortHostPort**](vmserialporttype.md).

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                | Description                                       |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                      | The operation was successful.<br/>          |
| <dl> <dt> **E\_POINTER**</dt> </dl>                 | The *portName* parameter is **NULL**<br/>   |
| <dl> <dt> **E\_INVALIDARG**</dt> </dl>              | The *portType* parameter is not valid.<br/> |
| <dl> <dt> **VM\_E\_VM\_UNKNOWN**</dt> </dl>         | The configuration is unknown.<br/>          |
| <dl> <dt>**VM\_E\_PREF\_ILLEGAL\_VALUE**</dt> </dl> | The specified port is already in use.<br/>  |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>         | An unexpected error occurred.<br/>          |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSerialPort**](ivmserialport.md)
</dt> <dt>

[**VMSerialPortType**](vmserialporttype.md)
</dt> </dl>

 

 





