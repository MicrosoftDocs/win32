---
description: InkCollector.SystemGesture event - Occurs when a system gesture is recognized.
ms.assetid: 11071d6f-8aa3-4902-94fd-89ad0cf17729
title: InkCollector.SystemGesture event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkCollector.SystemGesture event

Occurs when a system gesture is recognized.

## Syntax


```C++
void SystemGesture(
  [in] IInkCursor       *Cursor,
  [in] InkSystemGesture Id,
  [in] long             X,
  [in] long             Y,
  [in] long             Modifier,
  [in] BSTR             Character,
  [in] long             CursorMode
);
```



## Parameters

<dl> <dt>

*Cursor* \[in\]
</dt> <dd>

The [**IInkCursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object that generated the **SystemGesture** event.

</dd> <dt>

*Id* \[in\]
</dt> <dd>

The value of the system gesture.

</dd> <dt>

*X* \[in\]
</dt> <dd>

The x-coordinate of the location of the gesture.

</dd> <dt>

*Y* \[in\]
</dt> <dd>

The y-coordinate of the location of the gesture.

</dd> <dt>

*Modifier* \[in\]
</dt> <dd>

Reserved.

</dd> <dt>

*Character* \[in\]
</dt> <dd>

Reserved.

</dd> <dt>

*CursorMode* \[in\]
</dt> <dd>

A value that indicates whether the [**IInkCursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object is in normal mode or eraser mode. 1 is for normal mode and 2 are for eraser mode.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

System gestures are useful because they give information about the [**IInkCursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object that is being used to create the gesture. They also provide shortcuts to combinations of mouse events and are "cheaper" ways to detect mouse events.

For example, instead of looking for a [**MouseUp Event**](inkcollector-mouseup.md) / [**MouseDown Event**](inkcollector-mousedown.md) pair of events with no other mouse events occurring in between, you can look for the [**Tap**](/windows/desktop/api/msinkaut/ne-msinkaut-inksystemgesture) or **RightTap** system gestures.

As another example, instead of listening for [**MouseDown Event**](inkcollector-mousedown.md) / [**MouseMove Event**](inkcollector-mousemove.md) events and getting numerous **MouseMove Event** messages, you can watch for the [**Drag**](/windows/desktop/api/msinkaut/ne-msinkaut-inksystemgesture) or **RightDrag** system gestures as long as you're not interested in the (x, y) coordinates of every position of the mouse. This allows you to receive only one message instead of numerous **MouseMove Event** messages.

For a list of specific system gestures, see the [**InkSystemGesture**](/windows/desktop/api/msinkaut/ne-msinkaut-inksystemgesture) enumeration type. For more information about system gestures, see [Using Gestures](using-gestures.md) and [Command Input on the Tablet PC](/previous-versions//dd314533(v=vs.85)).

This event method is defined in the \_IInkCollectorEvents, \_IInkOverlayEvents, and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_ICESystemGesture.

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

[**InkSystemGesture Enumeration**](/windows/desktop/api/msinkaut/ne-msinkaut-inksystemgesture)
</dt> <dt>

[**IInkCursor Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor)
</dt> <dt>

[Using Gestures](using-gestures.md)
</dt> <dt>

[Pen Input, Ink, and Recognition](pen-input--ink--and-recognition.md)
</dt> <dt>

[Command Input on the Tablet PC](/previous-versions//dd314533(v=vs.85))
</dt> </dl>

 

