---
description: InkOverlay.DoubleClick event - Occurs when the InkCollector or InkOverlay object is double-clicked.
ms.assetid: 76ea40d4-82cf-420a-a9eb-66cb0492b43b
title: InkOverlay.DoubleClick event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkOverlay.DoubleClick event

Occurs when the [**InkCollector**](inkcollector-class.md) or [**InkOverlay**](inkoverlay-class.md) object is double-clicked.

## Syntax


```C++
void DoubleClick(
  [in, out] VARIANT_BOOL *Cancel
);
```



## Parameters

<dl> <dt>

*Cancel* \[in, out\]
</dt> <dd>

Whether the event should be canceled for the parent control.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the \_IInkCollectorEvents, \_IInkOverlayEvents, and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_IPEDblClick.

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

 

 




