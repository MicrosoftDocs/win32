---
title: IVMDisplay Height property
description: The Height property contains the current height, in pixels, of the virtual machines display.
ms.assetid: f7db5335-2c0b-44c4-9b6f-c41929905645
keywords:
- Height property Virtual Server
- Height property Virtual Server , IVMDisplay interface
- IVMDisplay interface Virtual Server , Height property
- Height property Virtual Server , VMDisplay interface
- VMDisplay interface Virtual Server , Height property
topic_type:
- apiref
api_name:
- IVMDisplay.Height
- IVMDisplay.get_Height
- VMDisplay.Height
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

# IVMDisplay::Height property

The **Height** property contains the current height, in pixels, of the virtual machine's display.

This property is read-only.

## Syntax


```C++
HRESULT get_Height(
  [out] long *displayPixelHeight
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
<td><pre><code>VMDisplay.Height( _
  ByRef displayPixelHeight _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The height, in pixels, of the virtual machine's display.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                                |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>             | The operation was successful.<br/>                               |
| <dl> <dt> E\_POINTER</dt> </dl>        | The parameter is **NULL**.<br/>                                  |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The virtual machine is invalid or is not currently running.<br/> |
| <dl> <dt>VM\_E\_NO\_DISPLAY</dt> </dl> | Unable to locate a valid display for the virtual machine.<br/>   |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                               |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDisplay**](ivmdisplay.md)
</dt> </dl>

 

 





