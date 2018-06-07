---
Description: Occurs when a key is released while the InkPicture control has focus.
ms.assetid: e22633b5-40fe-4b94-a660-684c4f5c96f3
title: InkPicture.KeyUp event
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# InkPicture.KeyUp event

Occurs when a key is released while the [InkPicture](inkpicture-control-reference.md) control has focus.

## Syntax


```C++
void KeyUp(
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

This event method is defined in the **\_IInkPictureEvents** interface. The **\_IInkPictureEvents** interface implements the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface with an identifier of DISPID\_IPEKeyUp.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[InkPicture](inkpicture-control-reference.md)
</dt> </dl>

 

 




