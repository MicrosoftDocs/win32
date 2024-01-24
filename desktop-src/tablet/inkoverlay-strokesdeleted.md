---
description: Occurs after strokes have been deleted from the Ink property.
ms.assetid: 60ee8bbd-9230-4b6a-a4b0-4783195e3173
title: InkOverlay.StrokesDeleted event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkOverlay.StrokesDeleted event

Occurs after strokes have been deleted from the [**Ink**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_ink) property.

## Syntax


```C++
void StrokesDeleted();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

There is no event data.

This event method is defined in the \_IInkOverlayEvents and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_IOEStrokesDeleted.

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
</dt> <dt>

[**Ink Property \[InkCollector/InkOverLay Class\]**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_ink)
</dt> </dl>

 

 




