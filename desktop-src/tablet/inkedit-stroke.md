---
Description: 'Occurs when the user draws a new IInkStrokeDisp object on any IInkTablet object.'
ms.assetid: 'fac5104d-d0da-40b1-a4a6-00a34718d09f'
title: 'InkEdit.Stroke event'
---

# InkEdit.Stroke event

Occurs when the user draws a new [**IInkStrokeDisp**](iinkstrokedisp.md) object on any [**IInkTablet**](iinktablet.md) object.

## Syntax


```C++
HRESULT Stroke(
  [in]      IInkCursor     *Cursor,
  [in]      IInkStrokeDisp *Stroke,
  [in, out] VARIANT_BOOL   *Cancel
);
```



## Parameters

<dl> <dt>

*Cursor* \[in\]
</dt> <dd>

The [**IInkCursor**](iinkcursor.md) object.

</dd> <dt>

*Stroke* \[in\]
</dt> <dd>

The collected [**IInkStrokeDisp**](iinkstrokedisp.md) object.

</dd> <dt>

*Cancel* \[in, out\]
</dt> <dd>

**VARIANT\_TRUE** to cancel the collection of the [**IInkStrokeDisp**](iinkstrokedisp.md) object; **VARIANT\_FALSE** to collect the **IInkStrokeDisp** object and continue with the **Stroke** even.

</dd> </dl>

## Return value

If this event succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This event method is defined in the **\_IInkEditEvents** interface. The **\_IInkEditEvents** interface implements the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface with an identifier of DISPID\_IeeStroke.

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>Inked.h (also requires inked\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkEd.dll</dt> </dl>                          |



## See also

<dl> <dt>

[InkEdit](inkedit-control-reference.md)
</dt> <dt>

[**IInkCursor Interface**](iinkcursor.md)
</dt> <dt>

[**IInkStrokeDisp Interface**](iinkstrokedisp.md)
</dt> </dl>

 

 




