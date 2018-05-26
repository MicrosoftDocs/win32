---
title: IVMDVDDrive BusNumber property
description: The BusNumber property contains the bus number to which this DVD drive is attached. For example, on an IDE bus, this value would represent either the primary or secondary location.
ms.assetid: 02da951c-add8-4560-9403-6b8b08c40d80
keywords:
- BusNumber property Virtual Server
- BusNumber property Virtual Server , IVMDVDDrive interface
- IVMDVDDrive interface Virtual Server , BusNumber property
- BusNumber property Virtual Server , VMDVDDrive interface
- VMDVDDrive interface Virtual Server , BusNumber property
topic_type:
- apiref
api_name:
- IVMDVDDrive.BusNumber
- IVMDVDDrive.get_BusNumber
- VMDVDDrive.BusNumber
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

# IVMDVDDrive::BusNumber property

The **BusNumber** property contains the bus number to which this DVD drive is attached. For example, on an IDE bus, this value would represent either the primary or secondary location.

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
<td><pre><code>VMDVDDrive.BusNumber( _
  ByRef busNumber _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The bus number to which this DVD drive is attached.

This property value is read-only.

## Error codes



| Name                                                                                             | Meaning                                                                           |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                 | The operation was successful.<br/>                                          |
| <dl> <dt>E\_POINTER</dt> </dl>            | The parameter is **NULL**.<br/>                                             |
| <dl> <dt>VM\_E\_DRIVE\_INVALID</dt> </dl> | The bus location for this DVD drive has not been properly initialized.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>    | An unexpected error occurred.<br/>                                          |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDVDDrive**](ivmdvddrive.md)
</dt> </dl>

 

 





