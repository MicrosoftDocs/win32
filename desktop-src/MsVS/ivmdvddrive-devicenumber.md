---
title: IVMDVDDrive DeviceNumber property
description: The DeviceNumber property contains the device number to which this DVD drive is attached.
ms.assetid: bdfce5c4-00d6-4ba9-81a2-536655ea5d97
keywords:
- DeviceNumber property Virtual Server
- DeviceNumber property Virtual Server , IVMDVDDrive interface
- IVMDVDDrive interface Virtual Server , DeviceNumber property
- DeviceNumber property Virtual Server , VMDVDDrive interface
- VMDVDDrive interface Virtual Server , DeviceNumber property
topic_type:
- apiref
api_name:
- IVMDVDDrive.DeviceNumber
- IVMDVDDrive.get_DeviceNumber
- VMDVDDrive.DeviceNumber
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

# IVMDVDDrive::DeviceNumber property

The **DeviceNumber** property contains the device number to which this DVD drive is attached.

This property is read-only.

## Syntax


```C++
HRESULT get_DeviceNumber(
  [out] long *deviceNumber
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
<td><pre><code>VMDVDDrive.DeviceNumber( _
  ByRef deviceNumber _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The device number to which this DVD drive is attached.

This property value is read-only.

## Error codes



| Name                                                                                             | Meaning                                                                           |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                 | The operation was successful.<br/>                                          |
| <dl> <dt>E\_POINTER</dt> </dl>            | The parameter is **NULL**.<br/>                                             |
| <dl> <dt>VM\_E\_DRIVE\_INVALID</dt> </dl> | The bus location for this DVD drive has not been properly initialized.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>    | An unexpected error occurred.<br/>                                          |



## Remarks

For example, on an IDE bus, this value would represent either the primary or secondary location.

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

 

 





