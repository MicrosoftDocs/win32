---
description: Occurs when the user presses and releases a key while the InkEdit control has focus.
ms.assetid: 8284ab41-dfac-4da2-b101-6968a43b15d7
title: InkEdit.KeyPress event (Inked.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkEdit.KeyPress event

Occurs when the user presses and releases a key while the [InkEdit](inkedit-control-reference.md) control has focus.

## Syntax


```C++
HRESULT KeyPress(
   Long *Char
);
```



## Parameters

<dl> <dt>

*Char* 
</dt> <dd>

An integer that returns a standard numeric ANSI keycode. The *Char* parameter is passed by reference; changing it sends a different character to the control. Changing the *Char* parameter to 0 cancels the event.

</dd> </dl>

## Return value

If this event succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This event method is defined in the **\_IInkEditEvents** interface. The **\_IInkEditEvents** interface implements the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface with an identifier of DISPID\_IeeKeyPress.

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
</dt> <dt>

[**KeyDown Event \[InkEdit Control\]**](inkedit-keydown.md)
</dt> <dt>

[**KeyUp Event \[InkEdit Control\]**](inkedit-keyup.md)
</dt> </dl>

 

