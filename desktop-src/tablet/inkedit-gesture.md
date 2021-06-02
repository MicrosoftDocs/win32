---
description: Occurs when an application gesture is recognized.
ms.assetid: 736715f4-c610-42cc-9fbb-c2b579da69e5
title: InkEdit.Gesture event (Inked.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkEdit.Gesture event

Occurs when an application gesture is recognized.

## Syntax


```C++
HRESULT Gesture(
  [in]      IInkCursor   *Cursor,
  [in]      IInkStrokes  *Strokes,
  [in]      VARIANT      Gestures,
  [in, out] VARIANT_BOOL *Cancel
);
```



## Parameters

<dl> <dt>

*Cursor* \[in\]
</dt> <dd>

The [**IInkCursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object that was used to create this gesture.

</dd> <dt>

*Strokes* \[in\]
</dt> <dd>

The [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection that contains the [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects that make up this gesture.

</dd> <dt>

*Gestures* \[in\]
</dt> <dd>

An array of [**IInkGesture**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkgesture) objects, in order of confidence.

For more information about the VARIANT structure, see [Using the COM Library](using-the-com-library.md).

</dd> <dt>

*Cancel* \[in, out\]
</dt> <dd>

Whether the [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection that makes up this gesture should be canceled, so as not to erase the ink and to fire the [**Stroke**](inkedit-stroke.md) event.

</dd> </dl>

## Return value

If this event succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This event method is defined in the **\_IInkEditEvents** interface. The **\_IInkEditEvents** interface implements the IDispatch interface with an identifier of DISPID\_IeeGesture.

A **Gesture** event is raised only if the [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) for the [**IInkGesture**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkgesture) object is the first **IInkStrokeDisp** object since the last call to the [**Recognize**](/windows/desktop/api/inked/nf-inked-iinkedit-recognize) method or the last firing of the recognition timeout.

If the **Gesture** event is canceled, the [**Stroke**](inkedit-stroke.md) event is raised for the [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection that raised the **Gesture** event.

For this event to occur, the [InkEdit](inkedit-control-reference.md) control must subscribe to a set of application gestures. To set the InkEdit control's interest in a set of gestures, call the [**SetGestureStatus**](/windows/desktop/api/inked/nf-inked-iinkedit-setgesturestatus) method.

For a list of application gestures, see the [**InkApplicationGesture**](/windows/desktop/api/msinkaut/ne-msinkaut-inkapplicationgesture) enumeration type.

The [InkEdit](inkedit-control-reference.md) control does not recognize multiple stroke gestures.

The [InkEdit](inkedit-control-reference.md) control subscribes to the following gestures.



| Gesture                              | Action               |
|--------------------------------------|----------------------|
| Down-left ,Down-left-long<br/> | Enter<br/>     |
| Right<br/>                     | Space<br/>     |
| Left<br/>                      | Backspace<br/> |
| Up-right, Up-right-long<br/>   | Tab<br/>       |



 

To alter the default action for a gesture:

1.  Add event handlers for the **Gesture** and [**Stroke**](inkedit-stroke.md) events.
2.  In the **Gesture** event handler, cancel the **Gesture** event for the gesture, and perform the alternate action for the gesture.
3.  In the [**Stroke**](inkedit-stroke.md) event handler, cancel the **Stroke** event for the [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) object that raised the canceled **Gesture** event.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>Inked.h (also requires inked\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkEd.dll</dt> </dl>                          |



## See also

<dl> <dt>

[InkEdit](inkedit-control-reference.md)
</dt> <dt>

[**InkApplicationGesture Enumeration**](/windows/desktop/api/msinkaut/ne-msinkaut-inkapplicationgesture)
</dt> <dt>

[**SetGestureStatus Method \[InkEdit Control\]**](/windows/desktop/api/inked/nf-inked-iinkedit-setgesturestatus)
</dt> <dt>

[**RecoTimeout Property**](/windows/desktop/api/inked/nf-inked-iinkedit-get_recognitiontimeout)
</dt> <dt>

[**Stroke Event \[InkEdit Control\]**](inkedit-stroke.md)
</dt> <dt>

[Using Gestures](using-gestures.md)
</dt> </dl>

 

