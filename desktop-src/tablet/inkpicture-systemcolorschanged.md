---
Description: Occurs after the system colors change.
ms.assetid: 5d77c24a-dc01-4ea0-b142-e83b1023acc1
title: InkPicture.SystemColorsChanged event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InkPicture.SystemColorsChanged event

Occurs after the system colors change.

## Syntax


```C++
void SystemColorsChanged();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

This event method is defined in the **\_IInkPictureEvents** interface. The **\_IInkPictureEvents** interface implements the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface with an identifier of DISPID\_IPESystemColorsChanged.

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

 

 




