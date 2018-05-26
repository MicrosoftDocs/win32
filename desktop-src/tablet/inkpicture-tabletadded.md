---
Description: Occurs when a IInkTablet is added to the system.
ms.assetid: 5df10efd-7055-43fa-881f-67eb5fd6adcf
title: InkPicture.TabletAdded event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InkPicture.TabletAdded event

Occurs when a [**IInkTablet**](/windows/win32/msinkaut/nn-msinkaut-iinktablet?branch=master) is added to the system.

## Syntax


```C++
void TabletAdded(
  [in] IInkTablet *Tablet
);
```



## Parameters

<dl> <dt>

*Tablet* \[in\]
</dt> <dd>

The [**IInkTablet**](/windows/win32/msinkaut/nn-msinkaut-iinktablet?branch=master) object that has been added to the system.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the **\_IInkCollectorEvents**, **\_IInkOverlayEvents**, and **\_IInkPictureEvents** dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_ICETabletAdded.

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
</dt> <dt>

[**IInkTablet Interface**](/windows/win32/msinkaut/nn-msinkaut-iinktablet?branch=master)
</dt> </dl>

 

 




