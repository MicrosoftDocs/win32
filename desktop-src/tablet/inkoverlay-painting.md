---
description: Occurs before the InkOverlay object or InkPicture has completed redrawing itself.
ms.assetid: abfd37fb-2d2b-4d60-96a1-08f68b73417b
title: InkOverlay.Painting event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkOverlay.Painting event

Occurs before the [**InkOverlay**](inkoverlay-class.md) object or [InkPicture](inkpicture-control-reference.md) has completed redrawing itself.

## Syntax


```C++
void Painting(
  [in]      long          hDC,
  [in]      IInkRectangle *Rect,
  [in, out] VARIANT_BOOL  *Allow
);
```



## Parameters

<dl> <dt>

*hDC* \[in\]
</dt> <dd>

The device context on which painting will occur.

</dd> <dt>

*Rect* \[in\]
</dt> <dd>

The rectangle that is to be repainted.

</dd> <dt>

*Allow* \[in, out\]
</dt> <dd>

Whether the repaint will occur.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the \_IInkOverlayEvents and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_IOEPainting.

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

 

 




