---
title: IVMSerialPort ConnectImmediately property
description: The ConnectImmediately property contains whether the serial port should be opened without waiting for a modem command to be received.
ms.assetid: 7d2c9eda-41a4-4065-a23f-b14f0c2976fd
keywords:
- ConnectImmediately property Virtual Server
- ConnectImmediately property Virtual Server , IVMSerialPort interface
- IVMSerialPort interface Virtual Server , ConnectImmediately property
- ConnectImmediately property Virtual Server , VMSerialPort interface
- VMSerialPort interface Virtual Server , ConnectImmediately property
topic_type:
- apiref
api_name:
- IVMSerialPort.ConnectImmediately
- IVMSerialPort.get_ConnectImmediately
- VMSerialPort.ConnectImmediately
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

# IVMSerialPort::ConnectImmediately property

The **ConnectImmediately** property contains whether the serial port should be opened without waiting for a modem command to be received.

This property is read-only.

## Syntax


```C++
HRESULT get_ConnectImmediately(
  [out] VARIANT_BOOL *connectImmediately
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
<td><pre><code>VMSerialPort.ConnectImmediately( _
  ByRef connectImmediately _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the serial port should be opened without waiting for a modem command to be received.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                          |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                         |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *connectImmediately* parameter is **NULL**.<br/>       |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The current virtual machine configuration is invalid.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                         |



## Remarks

Only valid for port type [**vmSerialPortHostPort**](vmserialporttype.md).

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSerialPort**](ivmserialport.md)
</dt> </dl>

 

 





