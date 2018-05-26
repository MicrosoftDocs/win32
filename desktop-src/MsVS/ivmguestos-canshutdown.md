---
title: IVMGuestOS CanShutdown property
description: The CanShutdown property contains whether the guest operating system can be cleanly shut down.
ms.assetid: 4626d972-7292-44dd-b393-d3361940f6a5
keywords:
- CanShutdown property Virtual Server
- CanShutdown property Virtual Server , IVMGuestOS interface
- IVMGuestOS interface Virtual Server , CanShutdown property
- CanShutdown property Virtual Server , VMGuestOS interface
- VMGuestOS interface Virtual Server , CanShutdown property
topic_type:
- apiref
api_name:
- IVMGuestOS.CanShutdown
- IVMGuestOS.get_CanShutdown
- VMGuestOS.CanShutdown
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

# IVMGuestOS::CanShutdown property

The **CanShutdown** property contains whether the guest operating system can be cleanly shut down.

This property is read-only.

## Syntax


```C++
HRESULT get_CanShutdown(
  [out] VARIANT_BOOL *canShutdown
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
<td><pre><code>VMGuestOS.CanShutdown( _
  ByRef canShutdown _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the guest operating system supports the shutdown operation.

This property value is read-only.

## Error codes



| Name                                                                                                    | Meaning                                                                                                        |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                        | The operation was successful.<br/>                                                                       |
| <dl> <dt>E\_POINTER</dt> </dl>                   | The *additionsVersion* parameter is **NULL**.<br/>                                                       |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>           | The virtual machine could not be found.<br/>                                                             |
| <dl> <dt>VM\_E\_ADDITIONS\_NOT\_AVAIL</dt> </dl> | Additions are not installed in this virtual machine, or the virtual machine has never been started.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>           | An unexpected error occurred.<br/>                                                                       |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMGuestOS**](ivmguestos.md)
</dt> </dl>

 

 





