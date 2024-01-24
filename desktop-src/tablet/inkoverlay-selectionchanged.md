---
description: Occurs when the selection of ink within the control has changed, such as through alterations to the user interface, cut-and-paste procedures, or the Selection property.
ms.assetid: 6b4cd9fe-b09f-4a70-9aa5-92ef9409ff1b
title: InkOverlay.SelectionChanged event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkOverlay.SelectionChanged event

Occurs when the selection of ink within the control has changed, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_selection) property.

## Syntax


```C++
void SelectionChanged();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

There are no event data.

This event method is defined in the \_IInkOverlayEvents and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_IOESelectionChanged.

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

[**Selection Property**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_selection)
</dt> </dl>

 

 




