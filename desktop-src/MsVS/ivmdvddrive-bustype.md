---
title: IVMDVDDrive BusType property
description: The BusType property contains the bus type (that is, IDE or SCSI) to which this DVD drive is attached.
ms.assetid: de5208fa-013e-4f2f-8770-7d25f6aafb45
keywords:
- BusType property Virtual Server
- BusType property Virtual Server , IVMDVDDrive interface
- IVMDVDDrive interface Virtual Server , BusType property
- BusType property Virtual Server , VMDVDDrive interface
- VMDVDDrive interface Virtual Server , BusType property
topic_type:
- apiref
api_name:
- IVMDVDDrive.BusType
- IVMDVDDrive.get_BusType
- VMDVDDrive.BusType
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

# IVMDVDDrive::BusType property

The **BusType** property contains the bus type (that is, IDE or SCSI) to which this DVD drive is attached.

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
<td><pre><code>VMDVDDrive.BusType( _
  ByRef busType _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The bus type to which this DVD drive is attached.

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
</dt> <dt>

[**VMDriveBusType**](vmdrivebustype.md)
</dt> </dl>

 

 





