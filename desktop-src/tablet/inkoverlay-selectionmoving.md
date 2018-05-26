---
Description: Occurs when the position of the current selection is about to change, such as through alterations to the user interface, cut-and-paste procedures, or the Selection property.
ms.assetid: 7cd7a5b1-4ae6-4038-afd0-6ef9d0700938
title: InkOverlay.SelectionMoving event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InkOverlay.SelectionMoving event

Occurs when the position of the current selection is about to change, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/win32/msinkaut/?branch=master) property.

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

This event method is defined in the \_IInkOverlayEvents and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID off DISPID\_IOESelectionMoving.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**InkOverlay Class**](/windows/win32/msinkaut/?branch=master)
</dt> <dt>

**InkOverlay Class**
</dt> <dt>

[**Selection Property**](/windows/win32/msinkaut/?branch=master)
</dt> <dt>

[**InkRectangle Class**](/windows/win32/msinkaut/?branch=master)
</dt> </dl>

 

 




