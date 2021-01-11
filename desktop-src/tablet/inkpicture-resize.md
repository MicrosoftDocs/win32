---
description: Occurs when the InkPicture control is resized (when the Width and/or Height property values change).
ms.assetid: 436db420-f9ea-46f1-b922-c8663371edd5
title: InkPicture.Resize event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkPicture.Resize event

Occurs when the [InkPicture](inkpicture-control-reference.md) control is resized (when the Width and/or Height property values change).

## Syntax


```C++
void Resize(
   long Left,
   long Top,
   long Right,
   long Bottom
);
```



## Parameters

<dl> <dt>

*Left* 
</dt> <dd>

The number of pixels from the left side of the window that contains the control to the left side of the control.

</dd> <dt>

*Top* 
</dt> <dd>

The number of pixels from the top of the window that contains the control to the top of the control.

</dd> <dt>

*Right* 
</dt> <dd>

The number of pixels from the left side of the window that contains the control to the right side of the control.

</dd> <dt>

*Bottom* 
</dt> <dd>

The number of pixels from the top of the window that contains the control to the bottom of the control.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The new width of the control in pixels will be equal to the difference between the *Right* and *Left* parameters. Likewise, the new height will be equal to the difference between *Bottom* and *Top*.

This event method is defined in the **\_IInkPictureEvents** interface. The **\_IInkPictureEvents** interface implements the IDispatch interface with an identifier of **DISPID\_IPEResize**.

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

 

 




