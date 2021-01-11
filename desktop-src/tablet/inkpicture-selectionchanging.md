---
description: Occurs when the selection of ink within the InkPicture control is about to change, such as through alterations to the user interface, cut-and-paste procedures, or the Selection property.
ms.assetid: a8ae30ff-fb0d-44cc-a5d3-295117addafd
title: InkPicture.SelectionChanging event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkPicture.SelectionChanging event

Occurs when the selection of ink within the [InkPicture](inkpicture-control-reference.md) control is about to change, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_selection) property.

## Syntax


```C++
void SelectionChanging(
  [in] IInkStrokes *NewSelection
);
```



## Parameters

<dl> <dt>

*NewSelection* \[in\]
</dt> <dd>

The new collection of [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) that is being selected.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the **\_IInkOverlayEvents** and **\_IInkPictureEvents** dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_IOESelectionChanging.

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
</dt> </dl>

 

