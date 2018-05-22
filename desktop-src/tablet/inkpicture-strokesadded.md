---
Description: 'Occurs when one or more IInkStrokeDisp objects are added to the InkStrokes collection.'
ms.assetid: '577ad52b-ecd3-4a49-8997-481ebdb47203'
title: 'InkPicture.StrokesAdded event'
---

# InkPicture.StrokesAdded event

Occurs when one or more [**IInkStrokeDisp**](iinkstrokedisp.md) objects are added to the [InkStrokes](inkstrokes-collection.md) collection.

## Syntax


```C++
void StrokesAdded(
  [in] VARIANT StrokeIds
);
```



## Parameters

<dl> <dt>

*StrokeIds* \[in\]
</dt> <dd>

The integer array of identifiers for every [**IInkStrokeDisp**](iinkstrokedisp.md) object added when this event occurs.

For more information about the VARIANT structure, see [Using the COM Library](using-the-com-library.md).

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the **\_IInkStrokesEvents** interface. The **\_IInkStrokesEvents** interface implements the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface with an identifier of DISPID\_SEStrokesAdded.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[InkPicture](inkpicture-control-reference.md)
</dt> </dl>

 

 




