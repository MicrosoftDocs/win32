---
description: Occurs when the user releases a mouse button while the mouse is over the InkEdit control.
ms.assetid: 3c9e0229-c7e2-4b5c-9532-18fbf8a3667d
title: InkEdit.MouseUp event (Inked.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkEdit.MouseUp event

Occurs when the user releases a mouse button while the mouse is over the [InkEdit](inkedit-control-reference.md) control.

## Syntax


```C++
HRESULT MouseUp(
   short Button,
   short ShiftKey,
   long  xMouse,
   long  yMouse
);
```



## Parameters

<dl> <dt>

*Button* 
</dt> <dd>

A member of the [**MouseButton**](/windows/desktop/api/inked/ne-inked-mousebutton) enumeration that indicates which mouse buttons were released.



| Value                                                                                                                                                            | Meaning                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <span id="NO_BUTTON_"></span><span id="no_button_"></span><dl> <dt>**NO\_BUTTON** </dt> </dl>             | Default. No mouse button was pressed. <br/> |
| <span id="LEFT_BUTTON_"></span><span id="left_button_"></span><dl> <dt>**LEFT\_BUTTON** </dt> </dl>       | The left mouse button was pressed. <br/>    |
| <span id="RIGHT_BUTTON_"></span><span id="right_button_"></span><dl> <dt>**RIGHT\_BUTTON** </dt> </dl>    | The right mouse button was pressed. <br/>   |
| <span id="MIDDLE_BUTTON_"></span><span id="middle_button_"></span><dl> <dt>**MIDDLE\_BUTTON** </dt> </dl> | The middle mouse button was pressed. <br/>  |



 

</dd> <dt>

*ShiftKey* 
</dt> <dd>

A member of the [**InkShiftKeyModifierFlags**](/windows/desktop/api/msinkaut/ne-msinkaut-inkshiftkeymodifierflags) enumeration that indicates which modifier keys are depressed at the time of the event.



| Value                                                                                                                                                                                     | Meaning                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <span id="IKM_Shift"></span><span id="ikm_shift"></span><span id="IKM_SHIFT"></span><dl> <dt>**IKM\_Shift**</dt> </dl>             | Specifies that the SHIFT key was used as a modifier. <br/> |
| <span id="IKM_Control_"></span><span id="ikm_control_"></span><span id="IKM_CONTROL_"></span><dl> <dt>**IKM\_Control** </dt> </dl> | Specifies that the CTRL key was used as a modifier. <br/>  |
| <span id="IKM_Alt_"></span><span id="ikm_alt_"></span><span id="IKM_ALT_"></span><dl> <dt>**IKM\_Alt** </dt> </dl>                 | Specifies that the ALT key was used as a modifier. <br/>   |



 

</dd> <dt>

*xMouse* 
</dt> <dd>

The current x coordinate, in pixels, of the mouse pointer.

</dd> <dt>

*yMouse* 
</dt> <dd>

The current y coordinate, in pixels, of the mouse pointer.

</dd> </dl>

## Return value

If this event succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If a mouse button is pressed while the pointer is over an [InkEdit](inkedit-control-reference.md) control, that control captures the mouse and receives all mouse events up to and including the last **MouseUp** event. This implies that the (x, y) mouse-pointer coordinates returned by a mouse event may not always be in the internal area of the object that receives them.

If mouse buttons are pressed in succession, the object that captures the mouse after the first press receives all mouse events until all buttons are released.

This event method is defined in the **\_IInkEditEvents** interface. The **\_IInkEditEvents** interface implements the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface with an identifier of DISPID\_IeeMouseUp.

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

[**InkMouseButton Enumeration**](/windows/desktop/api/msinkaut/ne-msinkaut-inkmousebutton)
</dt> <dt>

[**InkShiftKeyModifierFlags Enumeration**](/windows/desktop/api/msinkaut/ne-msinkaut-inkshiftkeymodifierflags)
</dt> <dt>

[**MouseDown Event \[InkEdit Control\]**](inkedit-mousedown.md)
</dt> <dt>

[**MouseMove Event \[InkEdit Control\]**](inkedit-mousemove.md)
</dt> </dl>

 

