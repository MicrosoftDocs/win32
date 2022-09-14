---
description: InkCollector.CursorButtonUp event - Occurs when the InkCollector detects a cursor button that is up.
ms.assetid: f07daad7-e0d1-45cf-a708-5486a5dfda8b
title: InkCollector.CursorButtonUp event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkCollector.CursorButtonUp event

Occurs when the [**InkCollector**](inkcollector-class.md) detects a cursor button that is up.

## Syntax


```C++
void CursorButtonUp(
  [in] IInkCursor       *Cursor,
  [in] IInkCursorButton *Button
);
```



## Parameters

<dl> <dt>

*Cursor* \[in\]
</dt> <dd>

The [**IInkCursor Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object that generated the **CursorButtonUp** event.

</dd> <dt>

*Button* \[in\]
</dt> <dd>

The button that was released.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

A button on a pen tip is up when the user completes a stroke and lifts the pen from the digitizer. A button on a barrel is up when the button is not pressed.

When you release the right mouse button, you actually receive two **CursorButtonUp** events - one for right button up and one for left button up.

This event method is defined in the \_IInkCollectorEvents, \_IInkOverlayEvents, and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_ICECursorButtonUp.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**InkCollector Class**](inkcollector-class.md)
</dt> <dt>

[**CursorButtonDown Event**](inkcollector-cursorbuttondown.md)
</dt> <dt>

[**CursorDown Event**](inkcollector-cursordown.md)
</dt> <dt>

[**IInkCursor Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor)
</dt> <dt>

[**IInkCursorButton Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursorbutton)
</dt> </dl>

 

 




