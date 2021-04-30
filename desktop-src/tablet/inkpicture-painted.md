---
description: Occurs when the InkPicture control has completed redrawing itself.
ms.assetid: a8194cff-ed94-402e-8564-08d370f958b4
title: InkPicture.Painted event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkPicture.Painted event

Occurs when the [InkPicture](inkpicture-control-reference.md) control has completed redrawing itself.

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

This event method is defined in the **\_IInkOverlayEvents** and **\_IInkPictureEvents** dispinterfaces with an ID of DISPID\_IOEPainted.

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

 

 




