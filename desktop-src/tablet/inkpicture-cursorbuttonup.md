---
description: InkPicture.CursorButtonUp event - Occurs when the InkCollector detects a cursor button that is up.
ms.assetid: bb10b032-a88d-4b52-9062-c0b63dfe98e9
title: InkPicture.CursorButtonUp event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkPicture.CursorButtonUp event

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

This event method is defined in the **\_IInkCollectorEvents**, **\_IInkOverlayEvents**, and **\_IInkPictureEvents** dispinterfaces with an ID of DISPID\_ICECursorButtonUp.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[InkPicture](inkpicture-control-reference.md)
</dt> <dt>

[**CursorButtonDown Event**](inkpicture-cursorbuttondown.md)
</dt> <dt>

[**CursorDown Event**](inkpicture-cursordown.md)
</dt> <dt>

[**IInkCursor Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor)
</dt> <dt>

[**IInkCursorButton Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursorbutton)
</dt> </dl>

 

 




