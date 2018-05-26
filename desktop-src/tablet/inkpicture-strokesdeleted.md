---
Description: Occurs after IInkStrokeDisp objects have been deleted from the Ink property.
ms.assetid: 395544e1-dc93-45d3-ac7a-d54712f3c027
title: InkPicture.StrokesDeleted event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InkPicture.StrokesDeleted event

Occurs after [**IInkStrokeDisp**](/windows/win32/msinkaut/nn-msinkaut-iinkstrokedisp?branch=master) objects have been deleted from the [**Ink**](/windows/win32/msinkaut/?branch=master) property.

## Syntax


```C++
void StrokesDeleted();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

There is no event data.

This event method is defined in the **\_IInkOverlayEvents** and **\_IInkPictureEvents** dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_IOEStrokesDeleted.

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

 

 




