---
title: IVMSerialPort Type property
description: The Type property contains the type of the serial port.
ms.assetid: 83d2f927-95c9-4b36-a64d-ce41ed777cb8
keywords:
- Type property Virtual Server
- Type property Virtual Server , IVMSerialPort interface
- IVMSerialPort interface Virtual Server , Type property
- Type property Virtual Server , VMSerialPort interface
- VMSerialPort interface Virtual Server , Type property
topic_type:
- apiref
api_name:
- IVMSerialPort.Type
- IVMSerialPort.get_Type
- VMSerialPort.Type
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMSerialPort::Type property

The **Type** property contains the type of the serial port.

This property is read-only.

## Syntax


```C++
HRESULT get_Type(
  [out] VMSerialPortType *portType
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
<td><pre><code>VMSerialPort.Type( _
  ByRef portType _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The type of the serial port.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                          |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                         |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *portType* parameter is **NULL**.<br/>                 |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The current virtual machine configuration is invalid.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                         |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSerialPort**](ivmserialport.md)
</dt> <dt>

[**VMSerialPortType**](vmserialporttype.md)
</dt> </dl>

 

 





