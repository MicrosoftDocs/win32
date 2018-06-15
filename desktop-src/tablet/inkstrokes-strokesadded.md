---
Description: Occurs when one or more strokes are added to the InkStrokes collection.
ms.assetid: d32dcaef-3beb-4ee1-84d6-5944278936f6
title: InkStrokes.StrokesAdded event
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# InkStrokes.StrokesAdded event

Occurs when one or more strokes are added to the [InkStrokes](https://msdn.microsoft.com/en-us/library/ms703293(v=VS.85).aspx) collection.

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

The integer array of identifiers for every [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) object added when this event occurs.

For more information about the VARIANT structure, see [Using the COM Library](using-the-com-library.md).

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the \_IInkEvents interface. The \_IInkEvents interface implements the [**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx) interface with an identifier of DISPID\_SEStrokesAdded.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[InkStrokes Collection](https://msdn.microsoft.com/en-us/library/ms703293(v=VS.85).aspx)
</dt> <dt>

[**Add Method \[InkStrokes Collection\]**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokes-add)
</dt> <dt>

[**InkDisp Class**](https://msdn.microsoft.com/en-us/library/ms704893(v=VS.85).aspx)
</dt> </dl>

 

 




