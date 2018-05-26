---
title: IVMMouse ScrollWheelPosition property
description: The ScrollWheelPosition property contains the current z-coordinate of the mouse. The indicated value can only represent relative coordinates.
ms.assetid: ba6eee2c-d009-49c3-9c6b-67a21ade234e
keywords:
- ScrollWheelPosition property Virtual Server
- ScrollWheelPosition property Virtual Server , IVMMouse interface
- IVMMouse interface Virtual Server , ScrollWheelPosition property
- ScrollWheelPosition property Virtual Server , VMMouse interface
- VMMouse interface Virtual Server , ScrollWheelPosition property
topic_type:
- apiref
api_name:
- IVMMouse.ScrollWheelPosition
- IVMMouse.put_ScrollWheelPosition
- VMMouse.ScrollWheelPosition
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

# IVMMouse::ScrollWheelPosition property

The **ScrollWheelPosition** property contains the current z-coordinate of the mouse. The indicated value can only represent relative coordinates.

This property is write-only.

## Syntax


```C++
HRESULT put_ScrollWheelPosition(
  [in] long position
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
<td><pre><code>VMMouse.ScrollWheelPosition( _
  ByVal position _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Sets the z-coordinate indicating the number of pixels the mouse is to be moved along the z-axis.

This property value is write-only.

## Error codes



| Name                                                                                                           | Meaning                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                               | The operation was successful.<br/>                                                                |
| <dl> <dt> VM\_E\_MOUSE\_NOT\_ACTIVE</dt> </dl>          | The mouse device has not been powered up, or is not currently active in the virtual machine.<br/> |
| <dl> <dt>VM\_E\_USING\_ABSOLUTE\_COORDINATES</dt> </dl> | The scroll wheel position cannot be set when the mouse device is using absolute coordinates.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>                  | An unexpected error occurred.<br/>                                                                |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMMouse**](ivmmouse.md)
</dt> </dl>

 

 





