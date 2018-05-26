---
Description: Occurs when the mouse wheel moves while the InkCollector or InkOverlay object has focus.
ms.assetid: 418cf67c-0ec0-49e3-a17f-9eaeb40bb602
title: InkCollector.MouseWheel event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InkCollector.MouseWheel event

Occurs when the mouse wheel moves while the [**InkCollector**](/windows/win32/msinkaut/?branch=master) or [**InkOverlay**](/windows/win32/msinkaut/?branch=master) object has focus.

## Syntax


```C++
void MouseWheel(
  [in]      InkMouseButton           Button,
  [in]      InkShiftKeyModifierFlags Shift,
  [in]      long                     Delta,
  [in]      long                     x,
  [in]      long                     y,
  [in, out] VARIANT_BOOL             *Cancel
);
```



## Parameters

<dl> <dt>

*Button* \[in\]
</dt> <dd>

The mouse button that was pressed.

</dd> <dt>

*Shift* \[in\]
</dt> <dd>

The state of the SHIFT key.

</dd> <dt>

*Delta* \[in\]
</dt> <dd>

A signed count of the number of detents the mouse wheel has rotated. A detent is one notch of the mouse wheel.

</dd> <dt>

*x* \[in\]
</dt> <dd>

The x-coordinate, in pixels, of a mouse click.

</dd> <dt>

*y* \[in\]
</dt> <dd>

The y-coordinate, in pixels, of a mouse click.

</dd> <dt>

*Cancel* \[in, out\]
</dt> <dd>

**VARIANT\_TRUE** to cancel the event for the parent control; otherwise, **VARIANT\_FALSE**. The default value is **VARIANT\_FALSE**.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

> [!Note]  
> The properties *pX* and *pY* are in pixels, and not the HIMETRIC units that are associated with the ink space. This is because this event replaces the related mouse event of a pen-unaware application and this type of application understands only pixels.

 

This event method is defined in the \_IInkCollectorEvents, \_IInkOverlayEvents, and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_IPEMouseWheel.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**InkCollector Class**](/windows/win32/msinkaut/?branch=master)
</dt> <dt>

[**InkMouseButton Enumeration**](/windows/win32/msinkaut/ne-msinkaut-inkmousebutton?branch=master)
</dt> <dt>

[**InkShiftKeyModifierFlags Enumeration**](/windows/win32/msinkaut/ne-msinkaut-inkshiftkeymodifierflags?branch=master)
</dt> </dl>

 

 




