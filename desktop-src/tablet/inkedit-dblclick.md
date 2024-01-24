---
description: Occurs when the InkEdit control is double-clicked.
ms.assetid: 380499e4-8697-4823-8153-29f24b2f234c
title: InkEdit.DblClick event (Inked.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkEdit.DblClick event

Occurs when the [InkEdit](inkedit-control-reference.md) control is double-clicked.

## Syntax


```C++
void DblClick(
  [in, out] VARIANT_BOOL *Cancel
);
```



## Parameters

<dl> <dt>

*Cancel* \[in, out\]
</dt> <dd>

**VARIANT\_TRUE** to cancel the event for the parent control; otherwise, **VARIANT\_FALSE**.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

> [!Note]  
> To distinguish between the left, right, and middle mouse buttons, use the [**MouseDown**](inkedit-mousedown.md) and [**MouseUp**](inkedit-mouseup.md) events. If there is code in the [**Click**](inkedit-click.md) event, the **DblClick** event will never trigger.

 

This event method is defined in the **\_IInkEditEvents** interface. The **\_IInkEditEvents** interface implements the IDispatch interface with an identifier of **DISPID\_IeeDblClick**.

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

 

 




