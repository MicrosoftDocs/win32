---
title: IVMHostInfo SerialPorts property
description: The SerialPorts property contains a list of serial ports on the host computer.
ms.assetid: dceb2443-2c4e-4a49-96dc-7e031daaf3da
keywords:
- SerialPorts property Virtual Server
- SerialPorts property Virtual Server , IVMHostInfo interface
- IVMHostInfo interface Virtual Server , SerialPorts property
- SerialPorts property Virtual Server , VMHostInfo interface
- VMHostInfo interface Virtual Server , SerialPorts property
topic_type:
- apiref
api_name:
- IVMHostInfo.SerialPorts
- IVMHostInfo.get_SerialPorts
- VMHostInfo.SerialPorts
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

# IVMHostInfo::SerialPorts property

The **SerialPorts** property contains a list of serial ports on the host computer.

This property is read-only.

## Syntax


```C++
HRESULT get_SerialPorts(
  [out] BSTR *serialPorts
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
<td><pre><code>VMHostInfo.SerialPorts( _
  ByRef serialPorts _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains a semicolon delimited list of serial port names.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                              |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>             | The operation was successful.<br/>             |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *serialPorts* parameter was **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>             |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHostInfo**](ivmhostinfo.md)
</dt> </dl>

 

 





