---
title: IVMMouse VerticalPosition property
description: The VerticalPosition property contains the y-coordinate of the mouse.
ms.assetid: 165f6b8c-6e94-4965-8a18-c18392510c3f
keywords:
- VerticalPosition property Virtual Server
- VerticalPosition property Virtual Server , IVMMouse interface
- IVMMouse interface Virtual Server , VerticalPosition property
- VerticalPosition property Virtual Server , VMMouse interface
- VMMouse interface Virtual Server , VerticalPosition property
topic_type:
- apiref
api_name:
- IVMMouse.VerticalPosition
- IVMMouse.get_VerticalPosition
- IVMMouse.put_VerticalPosition
- VMMouse.VerticalPosition
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

# IVMMouse::VerticalPosition property

The **VerticalPosition** property contains the y-coordinate of the mouse.

This property is read/write.

## Syntax


```C++
HRESULT put_VerticalPosition(
  [in]  long position
);

HRESULT get_VerticalPosition(
  [out] long *position
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
<td><pre><code>VMMouse.VerticalPosition( _
  ByRef position, _
  ByVal position _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The y-coordinate of the mouse. When using absolute coordinates, this value specifies the new y-coordinate of the mouse. When using relative coordinates, this value specifies the number of pixels the mouse should be moved in the y direction.

This property value is read/write.

## Error codes



| Name                                                                                                             | Meaning                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                                 | The operation was successful.<br/>                                                                                        |
| <dl> <dt>E\_POINTER</dt> </dl>                            | The parameter is **NULL**.<br/>                                                                                           |
| <dl> <dt>VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL</dt> </dl> | Additions must be installed to retrieve the mouse position, or to set the mouse position using absolute coordinates.<br/> |
| <dl> <dt>VM\_E\_USING\_RELATIVE\_COORDINATES</dt> </dl>   | The mouse device is currently set to use relative mouse coordinates.<br/>                                                 |
| <dl> <dt>VM\_E\_MOUSE\_NOT\_ACTIVE</dt> </dl>             | The mouse device has not been powered up, or is not currently active in the virtual machine.<br/>                         |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl>                   | An unexpected error occurred.<br/>                                                                                        |



## Remarks

This property cannot be retrieved when using relative coordinates.

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

 

 





