---
description: Occurs before the InkPicture control redraws itself.
ms.assetid: 97d017ce-fdab-49e5-9ea6-0bcc5d7b14fb
title: InkPicture.Painting event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkPicture.Painting event

Occurs before the [InkPicture](inkpicture-control-reference.md) control redraws itself.

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

The ink rectangle that is to be repainted.

</dd> <dt>

*Allow* \[in, out\]
</dt> <dd>

Whether the repaint will occur.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the **\_IInkOverlayEvents** and **\_IInkPictureEvents** dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_IOEPainting.

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
</dt> </dl>

 

 




