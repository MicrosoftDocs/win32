---
description: Deprecated. The PenInputPanel has been replaced by the Text Input Panel (TIP).Occurs when the PenInputPanel object changes between layouts.
ms.assetid: 21d38406-7ed9-4741-a092-ed3a369dc0dc
title: PenInputPanel.PanelChanged event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PenInputPanel.PanelChanged event

Deprecated. The [**PenInputPanel**](peninputpanel-class.md) has been replaced by the [Text Input Panel (TIP)](text-input-panel-reference.md).

Occurs when the [**PenInputPanel**](peninputpanel-class.md) object changes between layouts.

## Syntax


```C++
HRESULT PanelChanged(
  [in] PanelType NewPanelType
);
```



## Parameters

<dl> <dt>

*NewPanelType* \[in\]
</dt> <dd>

The new panel type used for input within the [**PenInputPanel**](peninputpanel-class.md) object, after the **PanelChanged** event fires.

</dd> </dl>

## Return value

If this event succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

When creating a [**PenInputPanel**](peninputpanel-class.md) object, [**Handwriting**](/windows/win32/api/peninputpanel/ne-peninputpanel-paneltype) is the default **PanelType**. If you change the panel by setting the [**CurrentPanel**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_currentpanel) property before the pen input panel becomes active for the first time, a **PanelChanged** event occurs.

The **PanelChanged** event is not raised when the user changes between Lined and Boxed writing pads.

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

 

 
