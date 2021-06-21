---
description: InkCollector.CursorOutOfRange event - Occurs when the cursor leaves the physical detection range (proximity) of the tablet context.
ms.assetid: a3a570ed-570b-4579-b120-ed5457630bc2
title: InkCollector.CursorOutOfRange event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkCollector.CursorOutOfRange event

Occurs when the cursor leaves the physical detection range (proximity) of the tablet context.

## Syntax


```C++
void CursorOutOfRange(
  [in] IInkCursor *Cursor
);
```



## Parameters

<dl> <dt>

*Cursor* \[in\]
</dt> <dd>

The [**IInkCursor Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object that generated the **CursorOutOfRange** event.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the \_IInkCollectorEvents, \_IInkOverlayEvents, and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_ICECursorOutOfRange.

The **CursorOutOfRange** event is fired even when in select or erase mode, not just when in ink mode. This requires that you monitor the editing mode (which you are responsible for setting) and be aware of the mode before interpreting the event. The advantage of this requirement is greater freedom to innovate on the platform through greater awareness of platform events.

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

[**CursorInRange Event**](inkcollector-cursorinrange.md)
</dt> <dt>

[**IInkCursor Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor)
</dt> </dl>

 

 




