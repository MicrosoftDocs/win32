---
Description: 'Occurs when the size of the current selection has changed, for example through alterations to the user interface, cut-and-paste procedures, or the Selection property.'
ms.assetid: '606d4bdf-b02e-459f-a4cf-050daac6c309'
title: 'InkOverlay.SelectionResized event'
---

# InkOverlay.SelectionResized event

Occurs when the size of the current selection has changed, for example through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](inkoverlay-selection.md) property.

## Syntax


```C++
void SelectionResized(
  [in] IInkRectangle *OldSelectionRect
);
```



## Parameters

<dl> <dt>

*OldSelectionRect* \[in\]
</dt> <dd>

The bounding rectangle of the selected [InkStrokes](inkstrokes-collection.md) collection as it existed before the **SelectionResized** event fired.

> [!Note]  
> This rectangle is specified in ink space coordinates, which allows for undo scenarios.

 

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the \_IInkOverlayEvents and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_IOESelectionResized.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**InkOverlay Class**](inkoverlay-class.md)
</dt> <dt>

[**Selection Property**](inkoverlay-selection.md)
</dt> <dt>

[**InkRectangle Class**](inkrectangle-class.md)
</dt> </dl>

 

 




