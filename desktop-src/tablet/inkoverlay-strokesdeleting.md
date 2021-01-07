---
description: Occurs before strokes are deleted from the Ink property.
ms.assetid: 09468416-ad08-48ea-aa4a-3af0fe553f3d
title: InkOverlay.StrokesDeleting event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkOverlay.StrokesDeleting event

Occurs before strokes are deleted from the [**Ink**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_ink) property.

## Syntax


```C++
void StrokesDeleting(
  [in] IInkStrokes *Strokes
);
```



## Parameters

<dl> <dt>

*Strokes* \[in\]
</dt> <dd>

The [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection deleted when the **StrokesDeleting** event fires.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the \_IInkOverlayEvents and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_IOEStrokesDeleting.

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

 

