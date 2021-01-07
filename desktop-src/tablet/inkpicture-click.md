---
description: Occurs when a user clicks the InkPicture control.
ms.assetid: 326bac37-2d5d-434b-916c-8a675bab5052
title: InkPicture.Click event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkPicture.Click event

Occurs when a user clicks the [InkPicture](inkpicture-control-reference.md) control.

## Syntax


```C++
void Click();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

Clicking a control generates [**MouseDown**](inkpicture-mousedown.md) and [**MouseUp**](inkpicture-mouseup.md) events in addition to the Click event.

> [!Note]  
> To distinguish between the left, right, and middle mouse buttons, use the [**MouseDown**](inkpicture-mousedown.md) and [**MouseUp**](inkpicture-mouseup.md) events.

 

If there is code in the **Click** event, the [**DblClick**](inkpicture-dblclick.md) event will never trigger, because the **Click** event is the first event to trigger between the two. As a result, the mouse click is intercepted by the **Click** event, so the **DblClick** event doesn't occur.

This event method is defined in the **\_IInkPictureEvents** interface. The **\_IInkPictureEvents** interface implements the IDispatch interface with an identifier of **DISPID\_IPEClick**.

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
</dt> </dl>

 

 




