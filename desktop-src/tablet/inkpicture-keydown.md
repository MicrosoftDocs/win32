---
description: Occurs when a key is pressed and in the down position while the InkPicture control has focus.
ms.assetid: d83823ea-d863-4eb7-8f6b-fa7a3396e64b
title: InkPicture.KeyDown event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkPicture.KeyDown event

Occurs when a key is pressed and in the down position while the [InkPicture](inkpicture-control-reference.md) control has focus.

## Syntax


```C++
void KeyDown(
  [in, out] short *KeyCode,
  [in, out] short *Shift
);
```



## Parameters

<dl> <dt>

*KeyCode* \[in, out\]
</dt> <dd>

The ASCII value of the key that is being pressed.

</dd> <dt>

*Shift* \[in, out\]
</dt> <dd>

The state of the SHIFT key.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the **\_IInkPictureEvents** interface. The **\_IInkPictureEvents** interface implements the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface with an identifier of DISPID\_IPEKeyDown.

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

 

