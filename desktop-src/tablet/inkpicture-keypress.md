---
description: Occurs when a key is pressed while the InkPicture control has focus.
ms.assetid: adb61eff-a92c-40b0-940c-02e14cd34e5f
title: InkPicture.KeyPress event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkPicture.KeyPress event

Occurs when a key is pressed while the [InkPicture](inkpicture-control-reference.md) control has focus.

## Syntax


```C++
void KeyPress(
  [in, out] short *KeyAscii
);
```



## Parameters

<dl> <dt>

*KeyAscii* \[in, out\]
</dt> <dd>

The ASCII value of the key that is being pressed.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the **\_IInkPictureEvents** interface. The **\_IInkPictureEvents** interface implements the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface with an identifier of DISPID\_IPEKeyPress.

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

 

