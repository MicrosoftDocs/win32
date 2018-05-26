---
Description: Deprecated. The PenInputPanel has been replaced by the Text Input Panel (TIP).Occurs when the PenInputPanel object is moving.
ms.assetid: 0c51d875-cef9-4087-b17d-5c5af04f81a5
title: PenInputPanel.PanelMoving event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PenInputPanel.PanelMoving event

Deprecated. The [**PenInputPanel**](/windows/win32/msinkaut/?branch=master) has been replaced by the [Text Input Panel (TIP)](text-input-panel-reference.md).

Occurs when the [**PenInputPanel**](/windows/win32/msinkaut/?branch=master) object is moving.

## Syntax


```C++
HRESULT PanelMoving(
  [in, out] long *Left,
  [in, out] long *Top
);
```



## Parameters

<dl> <dt>

*Left* \[in, out\]
</dt> <dd>

The new horizontal, or x-axis, position of the left edge of the [**PenInputPanel**](/windows/win32/msinkaut/?branch=master) object, in screen coordinates.

</dd> <dt>

*Top* \[in, out\]
</dt> <dd>

The new vertical, or y-axis, position of the left edge of the [**PenInputPanel**](/windows/win32/msinkaut/?branch=master) object, in screen coordinates.

</dd> </dl>

## Return value

If this event succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The **PanelMoving** event is designed to be used to change the position of the pen input panel by changing the *Left* and *Top* parameters.

The [**MoveTo**](/windows/win32/peninputpanel/?branch=master) and [**Refresh**](/windows/win32/peninputpanel/?branch=master) methods cause the [**PenInputPanel**](/windows/win32/msinkaut/?branch=master) object to call its auto-positioning code which triggers a **PanelMoving** event. Consequently, calling these methods inside a **PanelMoving** handler can result in a recursive endless loop.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**PenInputPanel**](/windows/win32/msinkaut/?branch=master)
</dt> </dl>

 

 




