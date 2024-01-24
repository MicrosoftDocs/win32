---
description: InkPicture.SelectionMoving event - Occurs when the position of the current selection is about to change, such as through alterations to the user interface, cut-and-paste procedures, or the Selection property.
ms.assetid: 310003a1-f282-4efa-9a75-c575a9193a77
title: InkPicture.SelectionMoving event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkPicture.SelectionMoving event

Occurs when the position of the current selection is about to change, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_selection) property.

## Syntax


```C++
void SelectionMoving(
  [in] IInkRectangle *CurSelectionRect
);
```



## Parameters

<dl> <dt>

*CurSelectionRect* \[in\]
</dt> <dd>

The rectangle to which the selection is moved after the **SelectionMoving** event.

> [!Note]  
> This rectangle is specified in client window coordinates, which allows for scenarios such as maintaining the aspect ratio when resizing.

 

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the **\_IInkOverlayEvents** and **\_IInkPictureEvents** dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_IOESelectionMoving.

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

[**Selection Property \[InkPicture Control\]**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_selection)
</dt> <dt>

[**InkRectangle Class**](inkrectangle-class.md)
</dt> </dl>

 

 




