---
Description: 'Occurs when the size of the current selection is about to change, such as through alterations to the user interface, cut-and-paste procedures, or the Selection property.'
ms.assetid: 'da708712-2773-45f5-9d9b-49fabe7fdb5a'
title: 'InkPicture.SelectionResizing event'
---

# InkPicture.SelectionResizing event

Occurs when the size of the current selection is about to change, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](inkpicture-selection.md) property.

## Syntax


```C++
void SelectionResizing(
  [in] IInkRectangle *CurSelectionRect
);
```



## Parameters

<dl> <dt>

*CurSelectionRect* \[in\]
</dt> <dd>

The bounding rectangle of the selection after the **SelectionResizing** event.

> [!Note]  
> This rectangle is specified in client window coordinates, which allows for scenarios such as maintaining the aspect ratio when resizing.

 

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the **\_IInkOverlayEvents** and **\_IInkPictureEvents** dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_IOESelectionResizing.

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

 

 




