---
Description: Occurs when the selection of ink within the InkPicture control has changed, such as through alterations to the user interface, cut-and-paste procedures, or the Selection property.
ms.assetid: e300ec91-e8f3-473f-b526-efeafafaa32a
title: InkPicture.SelectionChanged event
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# InkPicture.SelectionChanged event

Occurs when the selection of ink within the [InkPicture](inkpicture-control-reference.md) control has changed, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_selection) property.

## Syntax


```C++
void SelectionChanged();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

For further details about this event, refer to the [**InkOverlay**](https://msdn.microsoft.com/en-us/library/ms698599(v=VS.85).aspx) object's [**SelectionChanged**](inkoverlay-selectionchanged.md) event, which has the same functionality.

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

[**Selection Property \[InkPicture Control\]**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_selection)
</dt> </dl>

 

 




