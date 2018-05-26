---
Description: Occurs when the cursor leaves the physical detection range (proximity) of the tablet context.
ms.assetid: a3a570ed-570b-4579-b120-ed5457630bc2
title: InkCollector.CursorOutOfRange event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

The [**IInkCursor Interface**](/windows/win32/msinkaut/nn-msinkaut-iinkcursor?branch=master) object that generated the **CursorOutOfRange** event.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the \_IInkCollectorEvents, \_IInkOverlayEvents, and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_ICECursorOutOfRange.

The **CursorOutOfRange** event is fired even when in select or erase mode, not just when in ink mode. This requires that you monitor the editing mode (which you are responsible for setting) and be aware of the mode before interpreting the event. The advantage of this requirement is greater freedom to innovate on the platform through greater awareness of platform events.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**InkCollector Class**](/windows/win32/msinkaut/?branch=master)
</dt> <dt>

[**CursorInRange Event**](inkcollector-cursorinrange.md)
</dt> <dt>

[**IInkCursor Interface**](/windows/win32/msinkaut/nn-msinkaut-iinkcursor?branch=master)
</dt> </dl>

 

 




