---
description: Deprecated. The PenInputPanel has been replaced by the Text Input Panel (TIP).Occurs when input focus changes before the PenInputPanel object was able to insert user input into the attached control.
ms.assetid: a5928f78-29d6-40e8-8f87-17c188e51ba9
title: PenInputPanel.InputFailed event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PenInputPanel.InputFailed event

Deprecated. The [**PenInputPanel**](peninputpanel-class.md) has been replaced by the [Text Input Panel (TIP)](text-input-panel-reference.md).

Occurs when input focus changes before the [**PenInputPanel**](peninputpanel-class.md) object was able to insert user input into the attached control.

## Syntax


```C++
HRESULT InputFailed(
  [in] long  hWnd,
  [in] long  Key,
  [in] BSTR  Text,
  [in] short ShiftKey
);
```



## Parameters

<dl> <dt>

*hWnd* \[in\]
</dt> <dd>

The window handle of the control that invoked the [**PenInputPanel**](peninputpanel-class.md) object.

</dd> <dt>

*Key* \[in\]
</dt> <dd>

The virtual key corresponding to the key pressed.

</dd> <dt>

*Text* \[in\]
</dt> <dd>

The string that was to be inserted into the control represented by the *hWnd* parameter when the **InputFailed** event was raised.

For more information about the BSTR data type, see [Using the COM Library](using-the-com-library.md).

</dd> <dt>

*ShiftKey* \[in\]
</dt> <dd>

The state of the keyboard modifiers, including SHIFT, CAPS, CTRL, and ALT.

</dd> </dl>

## Return value

If this event succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The **InputFailed** event occurs when input focus changes before user input was inserted into the attached control. For example, if the user enters ink into the writing pad, then taps on another edit control before the recognizer has had a chance to finish, this event fires.

Using the window handle passed into this event, you can choose to insert the text yourself when this event occurs.

> [!Note]  
> Starting with Microsoft Windows XP Tablet PC Edition 2005, the **InputFailed** event no longer applies. Text is always inserted before focus changes.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**PenInputPanel**](peninputpanel-class.md)
</dt> </dl>

 

 




