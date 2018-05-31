---
title: IVMHardDiskConnection BusNumber property
description: The BusNumber property contains the bus number that corresponds with this connection.
ms.assetid: b9e426e5-57f6-40bb-84f6-59d1962dee7e
keywords:
- BusNumber property Virtual Server
- BusNumber property Virtual Server , IVMHardDiskConnection interface
- IVMHardDiskConnection interface Virtual Server , BusNumber property
- BusNumber property Virtual Server , VMHardDiskConnection interface
- VMHardDiskConnection interface Virtual Server , BusNumber property
topic_type:
- apiref
api_name:
- IVMHardDiskConnection.BusNumber
- IVMHardDiskConnection.get_BusNumber
- VMHardDiskConnection.BusNumber
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

# IVMHardDiskConnection::BusNumber property

The **BusNumber** property contains the bus number that corresponds with this connection.

This property is read-only.

## Syntax


```C++
HRESULT get_BusNumber(
  [out] long *busNumber
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
<td><pre><code>VMHardDiskConnection.BusNumber( _
  ByRef busNumber _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The bus number that corresponds with this connection.

This property value is read-only.

## Error codes



| Name                                                                                             | Meaning                                                                            |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                 | The operation was successful.<br/>                                           |
| <dl> <dt>E\_POINTER</dt> </dl>            | The parameter is **NULL** or invalid.<br/>                                   |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>    | The current virtual machine configuration is invalid.<br/>                   |
| <dl> <dt>VM\_E\_DRIVE\_INVALID</dt> </dl> | The bus location for this connection has not been properly initialized.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>    | An unexpected error occurred.<br/>                                           |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHardDiskConnection**](ivmharddiskconnection.md)
</dt> </dl>

 

 





