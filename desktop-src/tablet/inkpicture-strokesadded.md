---
Description: Occurs when one or more IInkStrokeDisp objects are added to the InkStrokes collection.
ms.assetid: 577ad52b-ecd3-4a49-8997-481ebdb47203
title: InkPicture.StrokesAdded event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InkPicture.StrokesAdded event

Occurs when one or more [**IInkStrokeDisp**](/windows/win32/msinkaut/nn-msinkaut-iinkstrokedisp?branch=master) objects are added to the [InkStrokes](/windows/win32/msinkaut/?branch=master) collection.

## Syntax


```C++
void StrokesAdded(
  [in] VARIANT StrokeIds
);
```



## Parameters

<dl> <dt>

*StrokeIds* \[in\]
</dt> <dd>

The integer array of identifiers for every [**IInkStrokeDisp**](/windows/win32/msinkaut/nn-msinkaut-iinkstrokedisp?branch=master) object added when this event occurs.

For more information about the VARIANT structure, see [Using the COM Library](using-the-com-library.md).

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the **\_IInkStrokesEvents** interface. The **\_IInkStrokesEvents** interface implements the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface with an identifier of DISPID\_SEStrokesAdded.

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

 

 




