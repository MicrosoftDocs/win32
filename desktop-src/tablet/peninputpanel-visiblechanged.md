---
description: Deprecated. The PenInputPanel has been replaced by the Text Input Panel (TIP).Occurs when the PenInputPanel object has shown or hidden itself.
ms.assetid: bf4651f4-2cf4-4952-a93e-3c6ba4846722
title: PenInputPanel.VisibleChanged event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PenInputPanel.VisibleChanged event

Deprecated. The [**PenInputPanel**](peninputpanel-class.md) has been replaced by the [Text Input Panel (TIP)](text-input-panel-reference.md).

Occurs when the [**PenInputPanel**](peninputpanel-class.md) object has shown or hidden itself.

## Syntax


```C++
HRESULT VisibleChanged(
  [in] VARIANT_BOOL NewVisibility
);
```



## Parameters

<dl> <dt>

*NewVisibility* \[in\]
</dt> <dd>

**VARIANT\_TRUE** to cause the [**PenInputPanel**](peninputpanel-class.md) object to become visible; otherwise, **VARIANT\_FALSE**.

</dd> </dl>

## Return value

If this event succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The **VisibleChanged** event applies to the Tablet PC Input Panel hover target. However, it is not raised when the hover target expands to show the full Tablet PC Input Panel.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**PenInputPanel**](peninputpanel-class.md)
</dt> </dl>

 

 




