---
title: IVMGuestOS2 ComputerName property
description: The computer name of the guest operating system running in the virtual machine.
ms.assetid: 980635ec-6e91-4199-a04c-23e246b5cee4
keywords:
- ComputerName property Virtual Server
- ComputerName property Virtual Server , IVMGuestOS2 interface
- IVMGuestOS2 interface Virtual Server , ComputerName property
- ComputerName property Virtual Server , VMGuestOS2 interface
- VMGuestOS2 interface Virtual Server , ComputerName property
topic_type:
- apiref
api_name:
- IVMGuestOS2.ComputerName
- IVMGuestOS2.get_ComputerName
- VMGuestOS2.ComputerName
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

# IVMGuestOS2::ComputerName property

The computer name of the guest operating system running in the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_ComputerName(
  [out] BSTR *guestComputerName
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
<td><pre><code>VMGuestOS2.ComputerName( _
  ByRef guestComputerName _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The computer name of the guest operating system.

This property value is read-only.

## Error codes



| Name                                                                                                             | Meaning                                                                     |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                                 | The operation was successful.<br/>                                    |
| <dl> <dt>E\_INVALIDARG</dt> </dl>                         | The *guestComputerName* parameter is not valid or not specified.<br/> |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> </dl>               | The virtual machine is not running.<br/>                              |
| <dl> <dt>VM\_E\_VM\_PAUSED</dt> </dl>                     | The virtual machine is paused.<br/>                                   |
| <dl> <dt>VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL</dt> </dl> | Additions are not installed in this virtual machine.<br/>             |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>                    | An unexpected error has occurred.<br/>                                |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMGuestOS2**](ivmguestos2.md)
</dt> </dl>

 

 





