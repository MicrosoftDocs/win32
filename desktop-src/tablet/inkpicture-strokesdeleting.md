---
Description: Occurs before IInkStrokeDisp objects are deleted from the Ink property.
ms.assetid: 747e0fdf-c68b-4805-bdc8-aa05e95ec0f7
title: InkPicture.StrokesDeleting event
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# InkPicture.StrokesDeleting event

Occurs before [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects are deleted from the [**Ink**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_ink) property.

## Syntax


```C++
void StrokesDeleting(
  [in] IInkStrokes *Strokes
);
```



## Parameters

<dl> <dt>

*Strokes* \[in\]
</dt> <dd>

The [InkStrokes](https://msdn.microsoft.com/en-us/library/ms703293(v=VS.85).aspx) collection deleted when the **StrokesDeleting** event fires.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the **\_IInkOverlayEvents** and **\_IInkPictureEvents** dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_IOEStrokesDeleting.

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

 

 




