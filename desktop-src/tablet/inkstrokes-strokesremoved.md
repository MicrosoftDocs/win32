---
Description: 'Occurs when one or more strokes are deleted from the InkStrokes collection.'
ms.assetid: '58d78143-c733-45dc-ae5f-fe13136010db'
title: 'InkStrokes.StrokesRemoved event'
---

# InkStrokes.StrokesRemoved event

Occurs when one or more strokes are deleted from the [InkStrokes](inkstrokes-collection.md) collection.

## Syntax


```C++
void StrokesRemoved(
  [in] VARIANT StrokeIds
);
```



## Parameters

<dl> <dt>

*StrokeIds* \[in\]
</dt> <dd>

The integer array of identifiers for every [**IInkStrokeDisp**](iinkstrokedisp.md) object deleted when this event occurs.

For more information about the VARIANT structure, see [Using the COM Library](using-the-com-library.md).

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the \_IInkEvents interface. The \_IInkEvents interface implements the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface with an identifier of DISPID\_SEStrokesRemoved.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[InkStrokes Collection](inkstrokes-collection.md)
</dt> <dt>

[**Remove Method \[InkStrokes Collection\]**](inkstrokes-remove.md)
</dt> <dt>

[**InkDisp Class**](inkdisp-class.md)
</dt> </dl>

 

 




