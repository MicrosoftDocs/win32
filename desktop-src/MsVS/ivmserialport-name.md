---
title: IVMSerialPort Name property
description: The Name property contains the name of the serial port.
ms.assetid: '55a4b625-0b78-4521-b1d3-555af8ce245e'
keywords: ["Name property Virtual Server", "Name property Virtual Server , IVMSerialPort interface", "IVMSerialPort interface Virtual Server , Name property", "Name property Virtual Server , VMSerialPort interface", "VMSerialPort interface Virtual Server , Name property"]
topic_type:
- apiref
api_name:
- IVMSerialPort.Name
- IVMSerialPort.get_Name
- VMSerialPort.Name
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMSerialPort::Name property

The **Name** property contains the name of the serial port.

This property is read-only.

## Syntax


```C++
HRESULT get_Name(
  [out] BSTR *portName
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VMSerialPort.Name( _
  ByRef portName _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The name of the serial port (for example, COM1 for [**vmSerialPortHostPort**](vmserialporttype.md), C:\\SerialPort.txt for **vmSerialPortTextFile**, or \\\\*servername*\\pipe\\*pipename* for **vmSerialPortNamedPipe**).

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                          |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                         |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *portName* parameter is **NULL**.<br/>                 |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The current virtual machine configuration is invalid.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                         |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSerialPort**](ivmserialport.md)
</dt> </dl>

 

 





