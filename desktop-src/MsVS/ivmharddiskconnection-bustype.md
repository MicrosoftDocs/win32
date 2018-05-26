---
title: IVMHardDiskConnection BusType property
description: The BusType property contains the type of bus (that is, IDE or SCSI) that corresponds with this connection.
ms.assetid: 9a0f2623-4678-4d35-ad3f-599defcb5012
keywords:
- BusType property Virtual Server
- BusType property Virtual Server , IVMHardDiskConnection interface
- IVMHardDiskConnection interface Virtual Server , BusType property
- BusType property Virtual Server , VMHardDiskConnection interface
- VMHardDiskConnection interface Virtual Server , BusType property
topic_type:
- apiref
api_name:
- IVMHardDiskConnection.BusType
- IVMHardDiskConnection.get_BusType
- VMHardDiskConnection.BusType
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

# IVMHardDiskConnection::BusType property

The **BusType** property contains the type of bus (that is, IDE or SCSI) that corresponds with this connection.

This property is read-only.

## Syntax


```C++
HRESULT get_BusType(
  [out] VMDriveBusType *busType
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
<td><pre><code>VMHardDiskConnection.BusType( _
  ByRef busType _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The type of bus that corresponds with this connection.

This property value is read-only.

## Error codes



| Name                                                                                              | Meaning                                                                            |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                  | The operation was successful.<br/>                                           |
| <dl> <dt>E\_POINTER</dt> </dl>             | The parameter is **NULL** or invalid.<br/>                                   |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>     | The current virtual machine configuration is invalid.<br/>                   |
| <dl> <dt> VM\_E\_DRIVE\_INVALID</dt> </dl> | The bus location for this connection has not been properly initialized.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>     | An unexpected error occurred.<br/>                                           |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHardDiskConnection**](ivmharddiskconnection.md)
</dt> <dt>

[**VMDriveBusType**](vmdrivebustype.md)
</dt> </dl>

 

 





