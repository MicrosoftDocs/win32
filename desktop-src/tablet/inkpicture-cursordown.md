---
Description: Occurs when the cursor tip contacts the digitizing tablet surface.
ms.assetid: 6d524400-1341-45da-86b2-098e34ed5a1c
title: InkPicture.CursorDown event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InkPicture.CursorDown event

Occurs when the cursor tip contacts the digitizing tablet surface.

## Syntax


```C++
void CursorDown(
  [in] IInkCursor     *Cursor,
  [in] IInkStrokeDisp *Stroke
);
```



## Parameters

<dl> <dt>

*Cursor* \[in\]
</dt> <dd>

The [**IInkCursor**](/windows/win32/msinkaut/nn-msinkaut-iinkcursor?branch=master) object that generated the **CursorDown** event.

</dd> <dt>

*Stroke* \[in\]
</dt> <dd>

The [**IInkStrokeDisp**](/windows/win32/msinkaut/nn-msinkaut-iinkstrokedisp?branch=master) object that was started when the [**IInkCursor**](/windows/win32/msinkaut/nn-msinkaut-iinkcursor?branch=master) object caused the **CursorDown** event to fire.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

These event methods are defined in the **\_IInkCollectorEvents**, **\_IInkOverlayEvents**, and **\_IInkPictureEvents** interfaces. The **\_IInkCollectorEvents**, **\_IInkOverlayEvents**, and **\_IInkPictureEvents** interfaces implements the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface with an identifier of DISPID\_ICECursorDown.

Use this event carefully because it could have an adverse effect on ink performance if too much code is executed in the event handlers. To improve real-time ink performance, hide or show the mouse cursor in the [**MouseDown**](inkpicture-mousedown.md) and [**MouseUp**](inkpicture-mouseup.md) event handlers.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[InkPicture](inkpicture-control-reference.md)
</dt> <dt>

[**CursorButtonUp Event**](inkpicture-cursorbuttonup.md)
</dt> <dt>

[**CursorButtonDown Event**](inkpicture-cursorbuttondown.md)
</dt> <dt>

[**IInkCursor Interface**](/windows/win32/msinkaut/nn-msinkaut-iinkcursor?branch=master)
</dt> <dt>

[**IInkStrokeDisp Interface**](/windows/win32/msinkaut/nn-msinkaut-iinkstrokedisp?branch=master)
</dt> </dl>

 

 




