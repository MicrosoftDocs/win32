---
description: Occurs when the user releases a key while the InkEdit control has focus.
ms.assetid: 973d99f2-df09-4315-aaab-72877272100b
title: InkEdit.KeyUp event (Inked.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkEdit.KeyUp event

Occurs when the user releases a key while the [InkEdit](inkedit-control-reference.md) control has focus.

## Syntax


```C++
HRESULT KeyUp(
   Long  *pKey,
   short ShiftKey
);
```



## Parameters

<dl> <dt>

*pKey* 
</dt> <dd>

The virtual-key code of the key pressed by the user.

</dd> <dt>

*ShiftKey* 
</dt> <dd>

A member of the [**InkShiftKeyModifierFlags**](/windows/desktop/api/msinkaut/ne-msinkaut-inkshiftkeymodifierflags) enumeration that indicates which modifier keys are depressed at the time of the event.



| Value                                                                                                                                                                                     | Meaning                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <span id="IKM_Shift"></span><span id="ikm_shift"></span><span id="IKM_SHIFT"></span><dl> <dt>**IKM\_Shift**</dt> </dl>             | Specifies that the SHIFT key was used as a modifier. <br/> |
| <span id="IKM_Control_"></span><span id="ikm_control_"></span><span id="IKM_CONTROL_"></span><dl> <dt>**IKM\_Control** </dt> </dl> | Specifies that the CTRL key was used as a modifier. <br/>  |
| <span id="IKM_Alt_"></span><span id="ikm_alt_"></span><span id="IKM_ALT_"></span><dl> <dt>**IKM\_Alt** </dt> </dl>                 | Specifies that the ALT key was used as a modifier. <br/>   |



 

</dd> </dl>

## Return value

If this event succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This event method is defined in the **\_IInkEditEvents** interface. The **\_IInkEditEvents** interface implements the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface with an identifier of DISPID\_IeeKeyUp.

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

[**InkShiftKeyModifierFlags Enumeration**](/windows/desktop/api/msinkaut/ne-msinkaut-inkshiftkeymodifierflags)
</dt> <dt>

[**KeyDown Event \[InkEdit Control\]**](inkedit-keydown.md)
</dt> <dt>

[**KeyPress Event \[InkEdit Control\]**](inkedit-keypress.md)
</dt> </dl>

 

