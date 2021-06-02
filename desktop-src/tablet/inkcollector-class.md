---
description: Represents the object that is used to capture ink from available tablet devices.
ms.assetid: 189f430e-9d00-4e29-bb8c-8ac195896793
title: InkCollector class (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkCollector
- InkCollector.IInkCollector
api_type: 
- COM
api_location: 
- InkObj.dll
- InkObj.dll.dll
---

# InkCollector class

Represents the object that is used to capture ink from available tablet devices.

Creating the **InkCollector** control behind a transparent control (such as a GroupBox with the **WS\_EX\_TRANSPARENT** property set) will prevent **InkCollector** from collecting ink.

**InkCollector** has these types of members:

-   [Events](#events)
-   [Interfaces](#interfaces)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **InkCollector** class has these events.



| Event                                                     | Description                                                                                                                                                                                                                                                   |
|:----------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CursorButtonDown**](inkcollector-cursorbuttondown.md) | Occurs when the **InkCollector** detects a cursor button that is down.<br/>                                                                                                                                                                             |
| [**CursorButtonUp**](inkcollector-cursorbuttonup.md)     | Occurs when the **InkCollector** detects a cursor button that is up.<br/>                                                                                                                                                                               |
| [**CursorDown**](inkcollector-cursordown.md)             | Occurs when the cursor tip contacts the digitizing tablet surface.<br/>                                                                                                                                                                                 |
| [**CursorInRange**](inkcollector-cursorinrange.md)       | Occurs when a cursor enters the physical detection range (proximity) of the tablet context.<br/>                                                                                                                                                        |
| [**CursorOutOfRange**](inkcollector-cursoroutofrange.md) | Occurs when the cursor leaves the physical detection range (proximity) of the tablet context.<br/>                                                                                                                                                      |
| [**DoubleClick**](inkcollector-doubleclick.md)           | Occurs when the **InkCollector** object is double-clicked.<br/>                                                                                                                                                                                         |
| [**Gesture**](inkcollector-gesture.md)                   | Occurs when an application-specific gesture is recognized.<br/>                                                                                                                                                                                         |
| [**MouseDown**](inkcollector-mousedown.md)               | Occurs when the mouse pointer is over the **InkCollector** object and a mouse button is pressed.<br/>                                                                                                                                                   |
| [**MouseMove**](inkcollector-mousemove.md)               | Occurs when the mouse pointer is moved over the **InkCollector** object.<br/>                                                                                                                                                                           |
| [**MouseUp**](inkcollector-mouseup.md)                   | Occurs when the mouse pointer is over the **InkCollector** object and a mouse button is released.<br/>                                                                                                                                                  |
| [**MouseWheel**](inkcollector-mousewheel.md)             | Occurs when the mouse wheel moves while the **InkCollector** object has focus.<br/>                                                                                                                                                                     |
| [**NewInAirPackets**](inkcollector-newinairpackets.md)   | Occurs when an in-air packet is seen, which happens when a user moves a pen near the tablet and the cursor is within the **InkCollector** object's window or the user moves a mouse within the **InkCollector** object object's associated window.<br/> |
| [**NewPackets**](inkcollector-newpackets.md)             | Occurs when the **InkCollector** object receives packets.<br/>                                                                                                                                                                                          |
| [**Stroke**](inkcollector-stroke.md)                     | Occurs when the user finishes drawing a new stroke on any tablet.<br/>                                                                                                                                                                                  |
| [**SystemGesture**](inkcollector-systemgesture.md)       | Occurs when a system gesture is recognized.<br/>                                                                                                                                                                                                        |
| [**TabletAdded**](inkcollector-tabletadded.md)           | Occurs when a [**Tablet**](/windows/desktop/api/msinkaut/nn-msinkaut-iinktablet) is added to the system.<br/>                                                                                                                                                                                 |
| [**TabletRemoved**](inkcollector-tabletremoved.md)       | Occurs when a [**Tablet**](/windows/desktop/api/msinkaut/nn-msinkaut-iinktablet) is removed from the system.<br/>                                                                                                                                                                             |



 

### Interfaces

The **InkCollector** class defines these interfaces.



| Interface         | Description                                                            |
|:------------------|:-----------------------------------------------------------------------|
| **IInkCollector** | This object implements the **IInkCollector** COM interface.<br/> |



 

### Methods

The **InkCollector** class has these methods.



| Method                                                                              | Description                                                                                                                                                    |
|:------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetEventInterest**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-geteventinterest)                           | Retrieves the current state of a particular **InkCollector** object event, that is, whether the event is being listened for or used.<br/>                |
| [**GetGestureStatus**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-getgesturestatus)                           | Retrieves whether the **InkCollector** object is interested in a particular gesture.<br/>                                                                |
| [**GetWindowInputRectangle**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-getwindowinputrectangle)             | Retrieves the window rectangle, in pixels, within which ink is drawn.<br/>                                                                               |
| [**SetAllTabletsMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-setalltabletsmode)                         | This mode allows the **InkCollector** object to collect ink from any tablet attached to the Tablet PC.<br/>                                              |
| [**SetEventInterest**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-seteventinterest)                           | Modifies a value that indicates whether a specific event should be listened for or used.<br/>                                                            |
| [**SetGestureStatus**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-setgesturestatus)                           | Modifies the interest of the **InkCollector** object in a known gesture.<br/>                                                                            |
| [**SetSingleTabletIntegratedMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-setsingletabletintegratedmode) | This mode allows the **InkCollector** object to collect ink from only one tablet. Ink from other tablets is ignored by the **InkCollector** object.<br/> |
| [**SetWindowInputRectangle**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-setwindowinputrectangle)             | Modifies the window rectangle, in pixels, to use to map drawn ink to the window.<br/>                                                                    |



 

### Properties

The **InkCollector** class has these properties.



| Property                                                                             | Access type          | Description                                                                                                                                                                                  |
|:-------------------------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AutoRedraw**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_autoredraw)<br/>                             | Read-only<br/> | Gets or sets a value that specifies whether the **InkCollector** repaints the ink when the window is invalidated.<br/>                                                                 |
| [**CollectingInk**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_collectingink)<br/>                       | Read-only<br/> | Gets a value that specifies whether ink is currently being drawn on an **InkCollector** object.<br/>                                                                                   |
| [**CollectionMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_collectionmode)<br/>                     | Read-only<br/> | Gets or sets the collection mode that determines whether ink, gestures, or both are recognized as the user writes.<br/>                                                                |
| [**Cursors**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_cursors)<br/>                                   | Read-only<br/> | Gets the [**Cursors**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursors) collection that is available for use in the inking region.<br/>                                                                                |
| [**DefaultDrawingAttributes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_defaultdrawingattributes)<br/> | Read-only<br/> | Gets or sets the default [**InkDrawingAttributes**](inkdrawingattributes-class.md) object, which specifies the drawing attributes that are used when drawing and displaying ink.<br/> |
| [**DesiredPacketDescription**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_desiredpacketdescription)<br/> | Read-only<br/> | Gets or sets interest in aspects of the packet associated with ink drawn on the **InkCollector** object.<br/>                                                                          |
| [**DynamicRendering**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_dynamicrendering)<br/>                   | Read-only<br/> | Gets or sets a value that indicates whether ink is rendered as it is drawn.<br/>                                                                                                       |
| [**Enabled**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_enabled)<br/>                                   | Read-only<br/> | Gets or sets a value that specifies whether the **InkCollector** object collects pen input.<br/>                                                                                       |
| [**Handle**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_hwnd)<br/>                                       | Read-only<br/> | Gets or sets the handle of the window to which the **InkCollector** object is attached.<br/>                                                                                           |
| [**Ink**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_ink)<br/>                                           | Read-only<br/> | Gets or sets the [**InkDisp**](inkdisp-class.md) object that is associated with the **InkCollector** object.<br/>                                                                     |
| [**MarginX**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_marginx)<br/>                                   | Read-only<br/> | Gets or sets the margins along the x-axis, in pixels.<br/>                                                                                                                             |
| [**MarginY**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_marginy)<br/>                                   | Read-only<br/> | Gets or sets the margins along the y-axis, in pixels.<br/>                                                                                                                             |
| [**MouseIcon**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_mouseicon)<br/>                               | Read-only<br/> | Gets or sets the current custom mouse icon.<br/>                                                                                                                                       |
| [**MousePointer**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_mousepointer)<br/>                         | Read-only<br/> | Gets or sets a value that indicates the type of mouse pointer that appears when the mouse is over a particular part of the object.<br/>                                                |
| [**Renderer**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_renderer)<br/>                                 | Read-only<br/> | Gets or sets the [**InkRenderer**](inkrenderer-class.md) object that is used to draw ink.<br/>                                                                                        |
| [**SupportHighContrastInk**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_supporthighcontrastink)<br/>     | Read-only<br/> | Gets or sets a value that specifies whether ink is rendered as just one color when the system is in High Contrast mode.<br/>                                                           |
| [**Tablet**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcursor-get_tablet)<br/>                                        | Read-only<br/> | Gets the tablet device that the **InkCollector** object is currently using to collect input.<br/>                                                                                      |



 

## Remarks

This object can be instantiated by calling the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) method in C++.

The **InkCollector** object collects only ink and gestures that are input into the specific window with which it is associated. The sole purpose of the **InkCollector** is to collect ink from the hardware (for example, through an [**IInkCursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) and [**IInkTablet**](/windows/desktop/api/msinkaut/nn-msinkaut-iinktablet) object) and deliver it to an application. It essentially acts as the source that distributes ink into one or many different [**InkDisp**](inkdisp-class.md) objects, which act as container that hold the distributed ink.

To use an **InkCollector**, you create it, tell it on which window to collect drawn ink, and enable it. After it is enabled, it can be set to collect in only one of three modes (the mode is specified in the [**InkCollectionMode**](/windows/desktop/api/msinkaut/ne-msinkaut-inkcollectionmode) enumeration):

-   InkOnly, in which an [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) object is created.
-   GestureOnly, in which an [**IInkGesture**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkgesture) object is created.
-   InkAndGesture, in which a stroke, a gesture, or potentially both are created, depending on how the application handles events.

This means that, for every movement of a cursor that is within range of a tablet, the **InkCollector** always collects either a stroke or a gesture and sometimes both. Gesture support is built in using the Microsoft gesture recognizer.

An **InkCollector** handles all tablet input. Ink can be collected from all attached tablets (including the mouse) simultaneously. Changes in the [**IInkCursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) and [**IInkCursorButton**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursorbutton) objects can cause **InkCollector** object to fire an event.

An **InkCollector** also manages the list of cursors that it encounters during its existence. When the **InkCollector** encounters a new cursor, the [**CursorInRange**](inkcollector-cursorinrange.md) event fires with the *newCursor* parameter set to **VARIANT\_TRUE**. Applications use the **InkCollector** to manage new cursors.

More than one **InkCollector** can be associated with a particular window handle, even if their collection areas, set in the constructor or with the [**SetWindowInputRectangle**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-setwindowinputrectangle) method, overlap. However, the only way this scenario works is if each **InkCollector** calls [**SetSingleTabletIntegratedMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-setsingletabletintegratedmode) and uses a unique tablet. This behavior makes it easy to store ink in a separate object for each tablet.

An error occurs if the window input rectangle of one enabled **InkCollectors** (set with the [**Enabled**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_enabled) property) overlaps the window input rectangle of another enabled **InkCollector**.

> [!Note]  
> Overlap can occur without an error as long as only one of the input rectangles is enabled at any known time.

 

The [**MouseDown**](inkcollector-mousedown.md), [**MouseMove**](inkcollector-mousemove.md), [**MouseUp**](inkcollector-mouseup.md), and [**MouseWheel**](inkcollector-mousewheel.md) events return x and y-coordinates in pixels, and not the HIMETRIC units that are associated with the ink space. This is because these events replace the mouse events of pen-unaware applications and these applications understand only pixels.

> [!Note]  
> The **InkCollector** object cannot be safely released on a non-UI thread.

 

To improve your application's performance, dispose of your **InkCollector** object when it is no longer needed.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[InkEdit Control Reference](inkedit-control-reference.md)
</dt> <dt>

[**InkDisp Class**](inkdisp-class.md)
</dt> <dt>

[**InkOverlay Class**](inkoverlay-class.md)
</dt> <dt>

[InkPicture Control Reference](inkpicture-control-reference.md)
</dt> </dl>

 

