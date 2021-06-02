---
description: Represents an object that is useful for annotation scenarios where users are not concerned with performing recognition on ink but instead are interested in the size, shape, color, and position of the ink.
ms.assetid: 61191ab3-075e-458b-9e0f-4bc255687b3c
title: InkOverlay class (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkOverlay
- InkOverlay.IInkOverlay
api_type: 
- COM
api_location: 
- InkObj.dll
- InkObj.dll.dll
---

# InkOverlay class

Represents an object that is useful for annotation scenarios where users are not concerned with performing recognition on ink but instead are interested in the size, shape, color, and position of the ink.

Creating the **InkOverlay** control behind a transparent control (such as a GroupBox with the WS\_EX\_TRANSPARENT property set) will prevent **InkOverlay** from collecting ink.

**InkOverlay** has these types of members:

-   [Events](#events)
-   [Interfaces](#interfaces)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **InkOverlay** class has these events.



| Event                                                     | Description                                                                                                                                                                                                                                               |
|:----------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CursorButtonDown**](inkcollector-cursorbuttondown.md) | Occurs when the **InkOverlay** detects a cursor button that is down.<br/>                                                                                                                                                                           |
| [**CursorButtonUp**](inkcollector-cursorbuttonup.md)     | Occurs when the **InkOverlay** detects a cursor button that is up.<br/>                                                                                                                                                                             |
| [**CursorDown**](inkcollector-cursordown.md)             | Occurs when the cursor tip contacts the digitizing tablet surface.<br/>                                                                                                                                                                             |
| [**CursorInRange**](inkcollector-cursorinrange.md)       | Occurs when a cursor enters the physical detection range (proximity) of the tablet context.<br/>                                                                                                                                                    |
| [**CursorOutOfRange**](inkcollector-cursoroutofrange.md) | Occurs when the cursor leaves the physical detection range (proximity) of the tablet context.<br/>                                                                                                                                                  |
| [**DoubleClick**](inkcollector-doubleclick.md)           | Occurs when the **InkOverlay** object is double-clicked.<br/>                                                                                                                                                                                       |
| [**Gesture**](inkcollector-gesture.md)                   | Occurs when an application-specific gesture is recognized.<br/>                                                                                                                                                                                     |
| [**MouseDown**](inkcollector-mousedown.md)               | Occurs when the mouse pointer is over the **InkOverlay** object and a mouse button is pressed.<br/>                                                                                                                                                 |
| [**MouseMove**](inkcollector-mousemove.md)               | Occurs when the mouse pointer is moved over the **InkOverlay** object.<br/>                                                                                                                                                                         |
| [**MouseUp**](inkcollector-mouseup.md)                   | Occurs when the mouse pointer is over the **InkOverlay** object and a mouse button is released.<br/>                                                                                                                                                |
| [**MouseWheel**](inkcollector-mousewheel.md)             | Occurs when the mouse wheel moves while the **InkOverlay** object has focus.<br/>                                                                                                                                                                   |
| [**NewInAirPackets**](inkcollector-newinairpackets.md)   | Occurs when an in-air packet is seen, which happens when a user moves a pen near the tablet and the cursor is within the **InkOverlay** object's window or the user moves a mouse within the **InkOverlay** object object's associated window.<br/> |
| [**NewPackets**](inkcollector-newpackets.md)             | Occurs when the **InkOverlay** object receives packets.<br/>                                                                                                                                                                                        |
| [**Painted**](inkoverlay-painted.md)                     | Occurs when the **InkOverlay** object has completed redrawing itself.<br/>                                                                                                                                                                          |
| [**Painting**](inkoverlay-painting.md)                   | Occurs before the **InkOverlay** object redraws itself.<br/>                                                                                                                                                                                        |
| [**SelectionChanged**](inkoverlay-selectionchanged.md)   | Occurs when the selection of ink within the control has changed, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_selection) property.<br/>                                       |
| [**SelectionChanging**](inkoverlay-selectionchanging.md) | Occurs when the selection of ink within the control is about to change, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_selection) property.<br/>                                |
| [**SelectionMoved**](inkoverlay-selectionmoved.md)       | Occurs when the position of the current selection has changed, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_selection) property.<br/>                                         |
| [**SelectionMoving**](inkoverlay-selectionmoving.md)     | Occurs when the position of the current selection is about to change, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_selection) property.<br/>                                  |
| [**SelectionResized**](inkoverlay-selectionresized.md)   | Occurs when the size of the current selection has changed, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_selection) property.<br/>                                             |
| [**SelectionResizing**](inkoverlay-selectionresizing.md) | Occurs when the size of the current selection is about to change, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_selection) property.<br/>                                      |
| [**Stroke**](inkcollector-stroke.md)                     | Occurs when the user finishes drawing a new stroke on any tablet.<br/>                                                                                                                                                                              |
| [**StrokesDeleted**](inkoverlay-strokesdeleted.md)       | Occurs after strokes have been deleted from the [**Ink**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_ink) property.<br/>                                                                                                                                                      |
| [**StrokesDeleting**](inkoverlay-strokesdeleting.md)     | Occurs before strokes are deleted from the [**Ink**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_ink) property.<br/>                                                                                                                                                           |
| [**SystemGesture**](inkcollector-systemgesture.md)       | Occurs when a system gesture is recognized.<br/>                                                                                                                                                                                                    |
| [**TabletAdded**](inkcollector-tabletadded.md)           | Occurs when an [**IInkTablet**](/windows/desktop/api/msinkaut/nn-msinkaut-iinktablet) is added to the system.<br/>                                                                                                                                                                        |
| [**TabletRemoved**](inkcollector-tabletremoved.md)       | Occurs when a [**Tablet**](/windows/desktop/api/msinkaut/nn-msinkaut-iinktablet) is removed from the system.<br/>                                                                                                                                                                         |



 

### Interfaces

The **InkOverlay** class defines these interfaces.



| Interface       | Description                                                          |
|:----------------|:---------------------------------------------------------------------|
| **IInkOverlay** | This object implements the **IInkOverlay** COM interface.<br/> |



 

### Methods

The **InkOverlay** class has these methods.



| Method                                                                              | Description                                                                                                                                                |
|:------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Draw**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-draw)                                                     | Sets a rectangle in which to redraw the ink within the **InkOverlay** object.<br/>                                                                   |
| [**GetEventInterest**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-geteventinterest)                           | Returns the current state of a particular **InkOverlay** object event, that is, whether the event is being listened for or used.<br/>                |
| [**GetGestureStatus**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-getgesturestatus)                           | Returns whether the **InkOverlay** object is interested in a particular gesture.<br/>                                                                |
| [**GetWindowInputRectangle**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-getwindowinputrectangle)             | Retrieves the window rectangle, in pixels, within which ink is drawn.<br/>                                                                           |
| [**HitTestSelection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-hittestselection)                             | Determines what portion of the selection was hit during a hit test.<br/>                                                                             |
| [**SetAllTabletsMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-setalltabletsmode)                         | This mode allows the **InkOverlay** object to collect ink from any tablet attached to the Tablet PC.<br/>                                            |
| [**SetEventInterest**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-seteventinterest)                           | Sets whether a specific event should be listened for or used.<br/>                                                                                   |
| [**SetGestureStatus**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-setgesturestatus)                           | Sets the interest of the **InkOverlay** object in a known gesture.<br/>                                                                              |
| [**SetSingleTabletIntegratedMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-setsingletabletintegratedmode) | This mode allows the **InkOverlay** object to collect ink from only one tablet. Ink from other tablets is ignored by the **InkOverlay** object.<br/> |
| [**SetWindowInputRectangle**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-setwindowinputrectangle)             | Sets the window rectangle, in pixels, to use to map drawn ink to the window.<br/>                                                                    |



 

### Properties

The **InkOverlay** class has these properties.



| Property                                                                                       | Access type           | Description                                                                                                                                                                                  |
|:-----------------------------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AttachMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_attachmode)<br/>                                         | Read/write<br/> | Gets or sets the value that specifies whether the **InkOverlay** object is attached behind or in front of the known window.<br/>                                                       |
| [**AutoRedraw**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_autoredraw)<br/>                                       | Read/write<br/> | Gets or sets a value that specifies whether the **InkOverlay** repaints the ink when the window is invalidated.<br/>                                                                   |
| [**CollectingInk**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_collectingink)<br/>                                 | Read-only<br/>  | Gets a value that specifies whether ink is currently being drawn on an **InkOverlay** object.<br/>                                                                                     |
| [**CollectionMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_collectionmode)<br/>                               | Read/write<br/> | Gets or sets the collection mode that determines whether ink, gestures, or both are recognized as the user writes.<br/>                                                                |
| [**Cursors**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_cursors)<br/>                                             | Read-only<br/>  | Gets the [**Cursors**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursors) collection that is available for use in the inking region.<br/>                                                                                |
| [**DefaultDrawingAttributes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_defaultdrawingattributes)<br/>           | Read/write<br/> | Gets or sets the default [**InkDrawingAttributes**](inkdrawingattributes-class.md) object, which specifies the drawing attributes that are used when drawing and displaying ink.<br/> |
| [**DesiredPacketDescription**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_desiredpacketdescription)<br/>           | Read/write<br/> | Gets or sets interest in aspects of the packet associated with ink drawn on the **InkOverlay** object.<br/>                                                                            |
| [**DynamicRendering**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_dynamicrendering)<br/>                             | Read/write<br/> | Gets or sets a value that indicates whether ink is rendered as it is drawn.<br/>                                                                                                       |
| [**EditingMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_editingmode)<br/>                                       | Read/write<br/> | Gets or sets a value that indicates whether the **InkOverlay** is in ink mode, deletion mode, or selecting/editing mode.<br/>                                                          |
| [**Enabled**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_enabled)<br/>                                             | Read/write<br/> | Gets or sets a value that specifies whether the **InkOverlay** object collects pen input.<br/>                                                                                         |
| [**EraserMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_erasermode)<br/>                                         | Read/write<br/> | Gets or sets a value that indicates whether ink is erased by stroke or by point.<br/>                                                                                                  |
| [**EraserWidth**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_eraserwidth)<br/>                                       | Read/write<br/> | Gets or sets a value that specifies the width of the eraser pen tip.<br/>                                                                                                              |
| [**Handle**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_hwnd)<br/>                                                 | Read/write<br/> | Gets or sets the handle of the window to which the **InkOverlay** object is attached.<br/>                                                                                             |
| [**Ink**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_ink)<br/>                                                       | Read/write<br/> | Gets or sets the [**InkDisp**](inkdisp-class.md) object that is associated with the **InkOverlay** object.<br/>                                                                       |
| [**MarginX**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_marginx)<br/>                                             | Read/write<br/> | Gets or sets the margins along the x-axis, in pixels.<br/>                                                                                                                             |
| [**MarginY**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_marginy)<br/>                                             | Read/write<br/> | Gets or sets the margins along the y-axis, in pixels.<br/>                                                                                                                             |
| [**MouseIcon**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_mouseicon)<br/>                                         | Read/write<br/> | Gets or sets the current custom mouse icon.<br/>                                                                                                                                       |
| [**MousePointer**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_mousepointer)<br/>                                   | Read/write<br/> | Gets or sets a value that indicates the type of mouse pointer that appears when the mouse is over a particular part of the object.<br/>                                                |
| [**Renderer**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_renderer)<br/>                                           | Read/write<br/> | Gets or sets the [**InkRenderer**](inkrenderer-class.md) object that is used to draw ink.<br/>                                                                                        |
| [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_selection)<br/>                                           | Read/write<br/> | Gets or sets the [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection that is currently selected inside the **InkOverlay** control.<br/>                                                 |
| [**SupportHighContrastInk**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_supporthighcontrastink)<br/>               | Read/write<br/> | Gets or sets a value that specifies whether ink is rendered as just one color when the system is in High Contrast mode.<br/>                                                           |
| [**SupportHighContrastSelectionUI**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_supporthighcontrastselectionui)<br/> | Read/write<br/> | Gets or sets a value that specifies whether all selection UI is drawn in high contrast when the system is in High Contrast mode.<br/>                                                  |
| [**Tablet**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcursor-get_tablet)<br/>                                                  | Read-only<br/>  | Gets the tablet device that the **InkOverlay** object is currently using to collect input.<br/>                                                                                        |



 

## MFC Implementation Notes

If you attached the InkOverlay object to a CView object, release the InkOverlay object in response to the WM\_DESTROY message as shown in the following example:


```C++
BOOL CRecognitionAlternatesSampleCppView::OnWndMsg(UINT msg, WPARAM wp, PARAM lp, LRESULT *pLR)
{
    if(WM_DESTROY == msg)
        m_spInkOverlay.Release();
    return CView::OnWndMsg(msg, wp, lp, pLR);
}
```



## Remarks

This object can be instantiated by calling the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) method in C++.

The **InkOverlay** object is well suited for note taking and basic scribbling. The primary intended use of this object is to display ink as ink.

In general, the run-time user interface for this object is a transparent window with opaque ink.

The [**MouseDown**](inkcollector-mousedown.md), [**MouseMove**](inkcollector-mousemove.md), [**MouseUp**](inkcollector-mouseup.md), and [**MouseWheel**](inkcollector-mousewheel.md) events return x-coordinates and y-coordinates in pixels, and not the HIMETRIC units that are associated with the ink space. This is because these events replace the mouse events of pen-unaware applications and these applications understand only pixels.

> [!Caution]  
> If you are setting the **InkOverlay** object's [**AttachMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_attachmode) property to InFront then create the **InkOverlay** object in the thread in which the form is running. Your application may stop responding if the **InkOverlay** object is created in a different thread and its **AttachMode** property is set to InFront.

 

> [!Note]  
> The **InkOverlay** object cannot be safely released on a non-UI thread.

 

To improve your application's performance, dispose your **InkOverlay** object when it is no longer needed.

If you attached the InkOverlay object to a CView object, release the InkOverlay object in response to the WM\_DESTROY message as shown in the following example:


```C++
BOOL CRecognitionAlternatesSampleCppView::OnWndMsg(UINT msg, WPARAM wp, PARAM lp, LRESULT *pLR)
{
    if(WM_DESTROY == msg)
        m_spInkOverlay.Release();
    return CView::OnWndMsg(msg, wp, lp, pLR);
}
```



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

[InkPicture Control Reference](inkpicture-control-reference.md)
</dt> <dt>

[InkEdit Control Reference](inkedit-control-reference.md)
</dt> </dl>

 

