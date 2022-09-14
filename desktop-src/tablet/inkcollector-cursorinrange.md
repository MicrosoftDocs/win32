---
description: InkCollector.CursorInRange event - Occurs when a cursor enters the physical detection range (proximity) of the tablet context.
ms.assetid: d05b240c-ba64-4008-b25d-e06c052eb5b0
title: InkCollector.CursorInRange event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkCollector.CursorInRange event

Occurs when a cursor enters the physical detection range (proximity) of the tablet context.

## Syntax


```C++
void CursorInRange(
  [in] IInkCursor   *Cursor,
  [in] VARIANT_BOOL NewCursor,
  [in] VARIANT      ButtonsState
);
```



## Parameters

<dl> <dt>

*Cursor* \[in\]
</dt> <dd>

The [**IInkCursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object that generated the **CursorInRange** event.

</dd> <dt>

*NewCursor* \[in\]
</dt> <dd>

**VARIANT\_TRUE** to indicate that this is the first time this ink collector has come in contact with the [**IInkCursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object that generated the **CursorInRange** event; otherwise, **VARIANT\_FALSE**.

</dd> <dt>

*ButtonsState* \[in\]
</dt> <dd>

The state of the buttons for the cursor that generated the **CursorInRange** event.

For more information about the VARIANT structure, see [Using the COM Library](using-the-com-library.md).

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

TThis event method is defined in the \_IInkCollectorEvents, \_IInkOverlayEvents, and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_ICECursorInRange.

The **CursorInRange** event is fired even when in select or erase mode, not just when in ink mode. This requires that you monitor the editing mode (which you are responsible for setting) and be aware of the mode before interpreting the event. The advantage of this requirement is greater freedom to innovate on the platform through greater awareness of platform events.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**InkCollector Class**](inkcollector-class.md)
</dt> <dt>

[**CursorOutOfRange Event**](inkcollector-cursoroutofrange.md)
</dt> <dt>

[**InkCursorButtonState Enumeration**](/windows/desktop/api/msinkaut/ne-msinkaut-inkcursorbuttonstate)
</dt> <dt>

[**IInkCursor Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor)
</dt> </dl>

 

 




