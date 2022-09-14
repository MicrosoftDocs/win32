---
description: InkPicture.Stroke event - Occurs when the user draws a new stroke on any tablet.
ms.assetid: 2829b65a-6120-402e-91e3-5587d1f456f9
title: InkPicture.Stroke event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkPicture.Stroke event

Occurs when the user draws a new stroke on any tablet.

## Syntax


```C++
void Stroke(
  [in]      IInkCursor     *Cursor,
  [in]      IInkStrokeDisp *Stroke,
  [in, out] VARIANT_BOOL   *Cancel
);
```



## Parameters

<dl> <dt>

*Cursor* \[in\]
</dt> <dd>

The [**IInkCursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object that generated the **Stroke** event.

</dd> <dt>

*Stroke* \[in\]
</dt> <dd>

The collected [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) object.

</dd> <dt>

*Cancel* \[in, out\]
</dt> <dd>

**VARIANT\_TRUE** to cancel the collection of the stroke; otherwise, **VARIANT\_FALSE**.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the **\_IInkCollectorEvents**, **\_IInkOverlayEvents**, and **\_IInkPictureEvents** dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_ICEStroke.

The **Stroke** event occurs when in select or erase mode, not just when inserting ink. This requires that you monitor the editing mode (which you are responsible for setting) and are aware of the mode before interpreting the event. The advantage of this requirement is greater freedom to innovate on the platform through greater awareness of platform events.

> [!Note]  
> The **Stroke** event occurs when the user finishes drawing a stroke, not when a stroke is added to the [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection. When the user first starts to draw a stroke, it is added immediately to the InkStrokes collection; however, the **Stroke** event does not occur until the stroke is complete. Therefore, strokes can exist in the InkStrokes collection that the **Stroke** event handler has not seen.

 

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

[**StrokesAdded Event \[InkPicture Control\]**](inkpicture-strokesadded.md)
</dt> <dt>

[**StrokesDeleted Event \[InkPicture Control\]**](inkpicture-strokesdeleted.md)
</dt> <dt>

[**IInkCursor Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor)
</dt> <dt>

[**IInkStrokeDisp Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp)
</dt> </dl>

 

