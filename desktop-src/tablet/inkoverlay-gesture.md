---
Description: Occurs when an application-specific gesture is recognized.
ms.assetid: 11b48fbc-0c93-4c3c-b218-258028822544
title: InkOverlay.Gesture event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InkOverlay.Gesture event

Occurs when an application-specific gesture is recognized.

## Syntax


```C++
void Gesture(
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

The [**IInkCursor**](/windows/win32/msinkaut/nn-msinkaut-iinkcursor?branch=master) object that generated the [**Gesture**](inkcollector-gesture.md) event.

</dd> <dt>

*Strokes* \[in\]
</dt> <dd>

The [IInkStrokes](/windows/win32/msinkaut/?branch=master) collection that the recognizer returned as the gesture.

</dd> <dt>

*Gestures* \[in\]
</dt> <dd>

An array of [**IInkGesture**](/windows/win32/msinkaut/nn-msinkaut-iinkgesture?branch=master) objects, in order of confidence, from the recognizer.

For more information about the VARIANT structure, see [Using the COM Library](using-the-com-library.md).

</dd> <dt>

*Cancel* \[in, out\]
</dt> <dd>

Whether the collection of this gesture should be canceled, such as not to erase the ink and to fire the [**Stroke**](inkcollector-stroke.md) event.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the \_IInkCollectorEvents, \_IInkOverlayEvents, and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_ICEGesture.

When the [**CollectionMode**](/windows/win32/msinkaut/nf-msinkaut-iinkcollector-put_collectionmode?branch=master) property is set to [**GestureOnly**](/windows/win32/msinkaut/ne-msinkaut-inkcollectionmode?branch=master), the timeout between when a user adds a gesture and when the [**Gesture**](inkcollector-gesture.md) event occurs is a fixed value that you cannot alter programmatically. Gesture recognition is faster in **InkAndGesture** mode.

To prevent the collection of ink while in [**InkAndGesture**](/windows/win32/msinkaut/ne-msinkaut-inkcollectionmode?branch=master) mode:

-   Set [**CollectionMode**](/windows/win32/msinkaut/nf-msinkaut-iinkcollector-put_collectionmode?branch=master) to [**InkAndGesture**](/windows/win32/msinkaut/ne-msinkaut-inkcollectionmode?branch=master).
-   Delete the stroke in the [**Stroke**](inkcollector-stroke.md) event.
-   Process the gesture in the [**Gesture**](inkcollector-gesture.md) event.

To prevent the flow of ink while gesturing, set [**DynamicRendering**](/windows/win32/msinkaut/?branch=master) property to **FALSE**.

In addition to when inserting ink, the [**Gesture**](inkcollector-gesture.md) event is fired when in select or erase mode. You are responsible for tracking the editing mode and should be aware of the mode before interpreting the event.

> [!Note]  
> To recognize gestures, you must use an object or control that can collect ink.

 

Application gestures are defined as gestures that are supported within your application.

For this event to occur, the object or control must have interest in a set of application gestures. To set the objects or controls interest in a set of gestures, call the [**SetGestureStatus**](/windows/win32/msinkaut/?branch=master) method of the object or control.

For a list of specific application gestures, see the [**InkApplicationGesture**](/windows/win32/msinkaut/ne-msinkaut-inkapplicationgesture?branch=master) enumeration type.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**InkOverlay Class**](/windows/win32/msinkaut/?branch=master)
</dt> <dt>

[**InkApplicationGesture Enumeration**](/windows/win32/msinkaut/ne-msinkaut-inkapplicationgesture?branch=master)
</dt> <dt>

[**SetGestureStatus Method**](/windows/win32/msinkaut/?branch=master)
</dt> <dt>

[Using Gestures](using-gestures.md)
</dt> </dl>

 

 




