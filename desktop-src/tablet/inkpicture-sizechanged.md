---
description: Occurs after the InkPicture control has been resized, specifically, after the Width or Height property value changes.
ms.assetid: a5fc6c82-f9c8-4104-8abe-082c47c56be9
title: InkPicture.SizeChanged event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkPicture.SizeChanged event

Occurs after the [InkPicture](inkpicture-control-reference.md) control has been resized, specifically, after the [**Width**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_width) or [**Height**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_height) property value changes.

## Syntax


```C++
void SizeChanged(
  [in] long Left,
  [in] long Top,
  [in] long Right,
  [in] long Bottom
);
```



## Parameters

<dl> <dt>

*Left* \[in\]
</dt> <dd>

The x-coordinate of the left side of the [InkPicture](inkpicture-control-reference.md) control.

</dd> <dt>

*Top* \[in\]
</dt> <dd>

The y-coordinate of the top of the [InkPicture](inkpicture-control-reference.md) control.

</dd> <dt>

*Right* \[in\]
</dt> <dd>

The x-coordinate of the right side of the [InkPicture](inkpicture-control-reference.md) control.

</dd> <dt>

*Bottom* \[in\]
</dt> <dd>

The y-coordinate of the bottom of the [InkPicture](inkpicture-control-reference.md) control.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the **\_IInkPictureEvents** interface. The **\_IInkPictureEvents** interface implements the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface with an identifier of DISPID\_IPESizeChanged.

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

 

