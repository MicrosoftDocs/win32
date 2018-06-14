---
Description: Occurs when a key is pressed while the InkPicture control has focus.
ms.assetid: adb61eff-a92c-40b0-940c-02e14cd34e5f
title: InkPicture.KeyPress event
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
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

This event method is defined in the **\_IInkPictureEvents** interface. The **\_IInkPictureEvents** interface implements the [**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx) interface with an identifier of DISPID\_IPEKeyPress.

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

 

 




