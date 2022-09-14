---
description: Occurs when a user clicks the InkEdit control.
ms.assetid: 99fd7ef0-02cf-4390-9026-00ef2bbc1e37
title: InkEdit.Click event (Inked.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkEdit.Click event

Occurs when a user clicks the [InkEdit](inkedit-control-reference.md) control.

## Syntax


```C++
void Click();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

Clicking a control generates [**MouseDown**](inkedit-mousedown.md) and [**MouseUp**](inkedit-mouseup.md) events in addition to the Click event.

> [!Note]  
> To distinguish between the left, right, and middle mouse buttons, use the [**MouseDown**](inkedit-mousedown.md) and [**MouseUp**](inkedit-mouseup.md) events.

 

If there is code in the **Click** event, the [**DblClick**](inkedit-dblclick.md) event will never trigger, because the **Click** event is the first event to trigger between the two. As a result, the mouse click is intercepted by the **Click** event, so the **DblClick** event doesn't occur.

This event method is defined in the **\_IInkEditEvents** interface. The **\_IInkEditEvents** interface implements the IDispatch interface with an identifier of **DISPID\_IeeClick**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>Inked.h (also requires inked\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkEd.dll</dt> </dl>                          |



## See also

<dl> <dt>

[InkEdit](inkedit-control-reference.md)
</dt> </dl>

 

 




