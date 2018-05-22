---
Description: 'Occurs when the position of the current selection has changed, such as through alterations to the user interface, cut-and-paste procedures, or the Selection property.'
ms.assetid: '669dc6c2-1620-40f3-b4b5-7ab8967e739a'
title: 'InkPicture.SelectionMoved event'
---

# InkPicture.SelectionMoved event

Occurs when the position of the current selection has changed, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](inkpicture-selection.md) property.

## Syntax


```C++
void SelectionMoved(
  [in] IInkRectangle *OldSelectionRect
);
```



## Parameters

<dl> <dt>

*OldSelectionRect* \[in\]
</dt> <dd>

The bounding rectangle of the selected [InkStrokes](inkstrokes-collection.md) collection as it existed before the **SelectionMoved** event fired.

> [!Note]  
> This rectangle is specified in ink space coordinates, which allows for undo scenarios.

 

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the **\_IInkOverlayEvents** and **\_IInkPictureEvents** dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_IOESelectionMoved.

To get the new bounding rectangle of the collection of strokes that have been moved, call the [**Selection.GetBoundingBox**](iinkstrokedisp-getboundingbox.md) method.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[InkPicture](inkpicture-control-reference.md)
</dt> <dt>

[**Selection Property \[InkPicture Control\]**](inkpicture-selection.md)
</dt> <dt>

[**InkRectangle Class**](inkrectangle-class.md)
</dt> </dl>

 

 




