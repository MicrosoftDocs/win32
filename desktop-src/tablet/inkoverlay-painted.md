---
description: Occurs when the InkOverlay object or InkPicture control has completed redrawing itself.
ms.assetid: de3c69de-4a33-46e4-96e5-462805681bda
title: InkOverlay.Painted event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkOverlay.Painted event

Occurs when the [**InkOverlay**](inkoverlay-class.md) object or [InkPicture](inkpicture-control-reference.md) control has completed redrawing itself.

## Syntax


```C++
void Painted(
  [in] long         hDC,
  [in] InkRectangle *Rect
);
```



## Parameters

<dl> <dt>

*hDC* \[in\]
</dt> <dd>

The device context on which the event occurred.

</dd> <dt>

*Rect* \[in\]
</dt> <dd>

The [**InkRectangle**](inkrectangle-class.md) that was repainted.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the \_IInkOverlayEvents and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_IOEPainted.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**InkOverlay Class**](inkoverlay-class.md)
</dt> </dl>

 

 




