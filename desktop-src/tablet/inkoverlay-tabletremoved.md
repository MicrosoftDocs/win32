---
Description: Occurs when a IInkTablet is removed from the system.
ms.assetid: 2217a69e-5b39-4827-82cd-99a02e9d39c6
title: InkOverlay.TabletRemoved event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InkOverlay.TabletRemoved event

Occurs when a [**IInkTablet**](/windows/win32/msinkaut/nn-msinkaut-iinktablet?branch=master) is removed from the system.

## Syntax


```C++
void TabletRemoved(
  [in] long TabletId
);
```



## Parameters

<dl> <dt>

*TabletId* \[in\]
</dt> <dd>

The long value that was used as the ID for the [**IInkTablet**](/windows/win32/msinkaut/nn-msinkaut-iinktablet?branch=master) object that was removed.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the \_IInkCollectorEvents, \_IInkOverlayEvents, and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_ICETabletRemoved.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**InkOverlay Class**](/windows/win32/msinkaut/?branch=master)
</dt> <dt>

[**IInkTablet Interface**](/windows/win32/msinkaut/nn-msinkaut-iinktablet?branch=master)
</dt> </dl>

 

 




