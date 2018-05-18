---
title: IVMHardDiskConnection DeviceNumber property
description: The DeviceNumber property contains the device number that corresponds with this connection.
ms.assetid: 'a267f74f-1db3-4c7b-a393-ecef4d4d4848'
keywords: ["DeviceNumber property Virtual Server", "DeviceNumber property Virtual Server , IVMHardDiskConnection interface", "IVMHardDiskConnection interface Virtual Server , DeviceNumber property", "DeviceNumber property Virtual Server , VMHardDiskConnection interface", "VMHardDiskConnection interface Virtual Server , DeviceNumber property"]
topic_type:
- apiref
api_name:
- IVMHardDiskConnection.DeviceNumber
- IVMHardDiskConnection.get_DeviceNumber
- VMHardDiskConnection.DeviceNumber
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMHardDiskConnection::DeviceNumber property

The **DeviceNumber** property contains the device number that corresponds with this connection.

This property is read-only.

## Syntax


```C++
HRESULT get_DeviceNumber(
  [out] long *deviceNumber
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
<td><pre><code>VMHardDiskConnection.DeviceNumber( _
  ByRef deviceNumber _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The device number that corresponds with this connection.

This property value is read-only.

## Error codes



| Name                                                                                             | Meaning                                                                            |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                 | The operation was successful.<br/>                                           |
| <dl> <dt> E\_POINTER</dt> </dl>           | The parameter is **NULL** or invalid.<br/>                                   |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>    | The current virtual machine configuration is invalid.<br/>                   |
| <dl> <dt>VM\_E\_DRIVE\_INVALID</dt> </dl> | The bus location for this connection has not been properly initialized.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>    | An unexpected error occurred.<br/>                                           |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHardDiskConnection**](ivmharddiskconnection.md)
</dt> </dl>

 

 





