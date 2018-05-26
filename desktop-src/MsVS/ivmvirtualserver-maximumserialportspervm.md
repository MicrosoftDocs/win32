---
title: IVMVirtualServer MaximumSerialPortsPerVM property
description: The MaximumSerialPortsPerVM property contains the maximum number of serial ports per virtual machine.
ms.assetid: f1fa97c0-206c-4065-863e-ff6f167bf751
keywords:
- MaximumSerialPortsPerVM property Virtual Server
- MaximumSerialPortsPerVM property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , MaximumSerialPortsPerVM property
- MaximumSerialPortsPerVM property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , MaximumSerialPortsPerVM property
topic_type:
- apiref
api_name:
- IVMVirtualServer.MaximumSerialPortsPerVM
- IVMVirtualServer.get_MaximumSerialPortsPerVM
- VMVirtualServer.MaximumSerialPortsPerVM
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMVirtualServer::MaximumSerialPortsPerVM property

The **MaximumSerialPortsPerVM** property contains the maximum number of serial ports per virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_MaximumSerialPortsPerVM(
  [out] long *maxPorts
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
<td><pre><code>VMVirtualServer.MaximumSerialPortsPerVM( _
  ByRef maxPorts _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The maximum number of serial ports per virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                  |
|-----------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>         | *maxPorts* is **NULL**.<br/>       |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/> |



## Examples

The following example displays the **MaximumSerialPortsPerVM** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Maximum serial ports per VM: " & objVS.MaximumSerialPortsPerVM
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





