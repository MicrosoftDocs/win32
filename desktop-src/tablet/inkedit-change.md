---
description: Occurs when the content of the InkEdit control changes.
ms.assetid: 6c65fcca-c84a-414c-a4e5-c5fdffb13e51
title: InkEdit.Change event (Inked.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkEdit.Change event

Occurs when the content of the [InkEdit](inkedit-control-reference.md) control changes.

## Syntax


```C++
void Change();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

This event occurs whenever any properties that affect the contents of the [InkEdit](inkedit-control-reference.md) control change.

This event method is defined in the **\_IInkEditEvents** interface. The **\_IInkEditEvents** interface implements the IDispatch interface with an identifier of **DISPID\_IeeChange**.

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

 

 




