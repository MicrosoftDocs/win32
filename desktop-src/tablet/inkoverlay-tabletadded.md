---
Description: 'Occurs when a IInkTablet is added to the system.'
ms.assetid: '2076a520-bd37-43b5-b57f-030828b096cb'
title: 'InkOverlay.TabletAdded event'
---

# InkOverlay.TabletAdded event

Occurs when a [**IInkTablet**](iinktablet.md) is added to the system.

## Syntax


```C++
void TabletAdded(
  [in] IInkTablet *Tablet
);
```



## Parameters

<dl> <dt>

*Tablet* \[in\]
</dt> <dd>

The [**IInkTablet**](iinktablet.md) object that has been added to the system.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the \_IInkCollectorEvents, \_IInkOverlayEvents, and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_ICETabletAdded.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**InkOverlay Class**](inkoverlay-class.md)
</dt> <dt>

[**IInkTablet Interface**](iinktablet.md)
</dt> </dl>

 

 




