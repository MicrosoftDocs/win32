---
description: The InkPicture control provides the ability to place an image in an application and enable users to add ink on top of it.
ms.assetid: e9fa6807-6e2a-44ec-9b8f-a560185e4367
title: InkPicture Control Reference
ms.topic: article
ms.date: 05/31/2018
---

# InkPicture Control Reference

The InkPicture control provides the ability to place an image in an application and enable users to add ink on top of it. It is intended for scenarios in which ink is not recognized as text but is instead stored as ink.

The InkPicture control can be instantiated by calling the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) method in C++.

> [!Note]  
> The InkPicture control is not marked safe for scripting. The InkPicture control should not be used in HTML or ASP.NET pages.

 

Creating the InkPicture control behind a transparent control (such as a GroupBox with the WS\_EX\_TRANSPARENT property set) will prevent InkPicture from collecting ink.

## Members



| Enumeration                                      | Description                                                                                              |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**InkPictureSizeMode**](/windows/desktop/api/msinkaut/ne-msinkaut-inkpicturesizemode) | Defines values that specify how the background picture behaves inside the InkPicture control.<br/> |



 



| Event                                                                              | Description                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ChangeUICues**                                                                   | Deprecated.<br/>                                                                                                                                                                                                                                                                                             |
| [**Click**](inkpicture-click.md)                                                  | Occurs when a user clicks the InkPicture control.<br/>                                                                                                                                                                                                                                                       |
| [**CursorButtonDown Event**](inkpicture-cursorbuttondown.md)                      | Occurs when the [**InkCollector**](inkcollector-class.md) control detects an [**IInkCursorButton**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursorbutton) object that is down.<br/>                                                                                                                                                         |
| [**CursorButtonUp Event**](inkpicture-cursorbuttonup.md)                          | Occurs when the InkPicture control detects an [**IInkCursorButton**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursorbutton) that is up.<br/>                                                                                                                                                                                                  |
| [**CursorDown Event**](inkpicture-cursordown.md)                                  | Occurs when the cursor tip contacts the digitizing tablet surface.<br/>                                                                                                                                                                                                                                      |
| [**CursorInRange Event**](inkpicture-cursorinrange.md)                            | Occurs when a cursor enters the physical detection range (proximity) of the tablet context.<br/>                                                                                                                                                                                                             |
| [**CursorOutOfRange Event**](inkpicture-cursoroutofrange.md)                      | Occurs when the cursor leaves the physical detection range (proximity) of the tablet context.<br/>                                                                                                                                                                                                           |
| [**DblClick**](inkpicture-dblclick.md)                                            | Occurs when the InkPicture control is double-clicked.<br/> This event method is defined in the **\_IInkPictureEvents** interface. The **\_IInkPictureEvents** interface implements the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface with an identifier of DISPID\_IPEDblClick.<br/> |
| [**Gesture Event**](inkpicture-gesture.md)                                        | Occurs when an application gesture is recognized.<br/>                                                                                                                                                                                                                                                       |
| [**KeyDown Event \[InkPicture Control\]**](inkpicture-keydown.md)                 | Occurs when a key is pressed and in the down position while the InkPicture control has focus.<br/>                                                                                                                                                                                                           |
| [**KeyPress Event\[InkPicture Control\]**](inkpicture-keypress.md)                | Occurs when a key is pressed while the InkPicture control has focus.<br/>                                                                                                                                                                                                                                    |
| [**KeyUp Event \[InkPicture Control\]**](inkpicture-keyup.md)                     | Occurs when a key is released while the InkPicture control has focus.<br/>                                                                                                                                                                                                                                   |
| [**MouseDown Event \[InkPicture Control\]**](inkpicture-mousedown.md)             | Occurs when the mouse pointer is over the InkPicture control and a mouse button is pressed.<br/>                                                                                                                                                                                                             |
| [**MouseEnter**](inkpicture-mouseenter.md)                                        | Occurs when the mouse pointer enters the InkPicture control.<br/>                                                                                                                                                                                                                                            |
| [**MouseHover**](inkpicture-mousehover.md)                                        | Occurs when the mouse pointer hovers over the InkPicture control.<br/>                                                                                                                                                                                                                                       |
| [**MouseLeave**](inkpicture-mouseleave.md)                                        | Occurs when the mouse pointer leaves the InkPicture control.<br/>                                                                                                                                                                                                                                            |
| [**MouseMove Event \[InkPicture Control\]**](inkpicture-mousemove.md)             | Occurs when the mouse pointer is moved over the InkPicture control.<br/>                                                                                                                                                                                                                                     |
| [**MouseUp Event \[InkPicture Control\]**](inkpicture-mouseup.md)                 | Occurs when the mouse pointer is over the InkPicture control and a mouse button is released.<br/>                                                                                                                                                                                                            |
| [**MouseWheel**](inkpicture-mousewheel.md)                                        | Occurs when the mouse wheel moves while the InkPicture control has focus.<br/>                                                                                                                                                                                                                               |
| [**NewInAirPackets Event**](inkpicture-newinairpackets.md)                        | Occurs when an in-air packet is seen.<br/>                                                                                                                                                                                                                                                                   |
| [**NewPackets Event**](inkpicture-newpackets.md)                                  | Occurs when the InkPicture control receives a packet.<br/>                                                                                                                                                                                                                                                   |
| [**Painted**](inkpicture-painted.md)                                              | Occurs when the InkPicture control has completed redrawing itself.<br/>                                                                                                                                                                                                                                      |
| [**Painting**](inkpicture-painting.md)                                            | Occurs before the InkPicture control redraws itself.<br/>                                                                                                                                                                                                                                                    |
| [**Resize**](inkpicture-resize.md)                                                | Occurs when the InkPicture control is resized.<br/>                                                                                                                                                                                                                                                          |
| [**SelectionChanged**](inkpicture-selectionchanged.md)                            | Occurs when the selection of text within the InkPicture control has changed, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_selection) property.<br/>                                                                                    |
| [**SelectionChanging**](inkpicture-selectionchanging.md)                          | Occurs when the selection of text within the InkPicture control is about to change, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_selection) property.<br/>                                                                             |
| [**SelectionMoved**](inkpicture-selectionmoved.md)                                | Occurs when the position of the current selection has changed, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_selection) property.<br/>                                                                                                  |
| [**SelectionMoving Event \[InkPicture Control\]**](inkpicture-selectionmoving.md) | Occurs when the position of the current selection is about to change, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_selection) property.<br/>                                                                                           |
| [**SelectionResized**](inkpicture-selectionresized.md)                            | Occurs when the size of the current selection has changed, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_selection) property.<br/>                                                                                                      |
| [**SelectionResizing**](inkpicture-selectionresizing.md)                          | Occurs when the size of the current selection is about to change, such as through alterations to the user interface, cut-and-paste procedures, or the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_selection) property.<br/>                                                                                               |
| [**SizeChanged**](inkpicture-sizechanged.md)                                      | Occurs after the InkPicture control has been resized, specifically, after the [**Width**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_width) or [**Height**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_height) property value changes.<br/>                                                                                                      |
| [**SizeModeChanged**](inkpicture-sizemodechanged.md)                              | Occurs after the [**SizeMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_sizemode) property of the InkPicture control has been changed.<br/>                                                                                                                                                                                           |
| **StyleChanged**                                                                   | Not implemented.<br/>                                                                                                                                                                                                                                                                                        |
| [**Stroke**](inkpicture-stroke.md)                                                | Occurs when the user draws a new stroke on any tablet.<br/>                                                                                                                                                                                                                                                  |
| [**StrokesDeleted**](inkpicture-strokesdeleted.md)                                | Occurs after [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects have been deleted from the [**Ink**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_ink) property.<br/>                                                                                                                                                                        |
| [**StrokesDeleting**](inkpicture-strokesdeleting.md)                              | Occurs before [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects are deleted from the [**Ink**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_ink) property.<br/>                                                                                                                                                                             |
| [**SystemColorsChanged**](inkpicture-systemcolorschanged.md)                      | Occurs after the system colors change.<br/>                                                                                                                                                                                                                                                                  |
| [**SystemGesture**](inkpicture-systemgesture.md)                                  | Occurs when a system gesture is recognized.<br/>                                                                                                                                                                                                                                                             |
| [**TabletAdded Event**](inkpicture-tabletadded.md)                                | Occurs when a tablet is added to the system.<br/>                                                                                                                                                                                                                                                            |
| [**TabletRemoved Event**](inkpicture-tabletremoved.md)                            | Occurs when a tablet is removed from the system.<br/>                                                                                                                                                                                                                                                        |



 



| Method                                                                                   | Description                                                                                                                                                                    |
|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetEventInterest Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-geteventinterest)                           | Returns a value that indicates whether the InkPicture control has interest in a particular event.<br/>                                                                   |
| [**GetGestureStatus**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-getgesturestatus)                                  | Returns a value that indicates whether the InkPicture control has interest in a particular application gesture.<br/>                                                     |
| [**GetWindowInputRectangle Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-getwindowinputrectangle)             | Returns the window rectangle, in pixels, within which ink is drawn.<br/>                                                                                                 |
| [**HitTestSelection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-hittestselection)                                  | Returns a member of the [**SelectionHitResult**](/windows/desktop/api/msinkaut/ne-msinkaut-selectionhitresult) enumeration, which specifies which part of a selection, if any, was hit during a hit test.<br/> |
| [**SetAllTabletsMode Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-setalltabletsmode)                         | Enables the InkPicture control to collect ink from any tablet attached to the Tablet PC.<br/>                                                                            |
| [**SetEventInterest Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-seteventinterest)                           | Sets a value that indicates whether an InkPicture control has interest in a specified event.<br/>                                                                        |
| SetFocus                                                                                 | Moves the focus to the InkPicture control.<br/>                                                                                                                          |
| [**SetGestureStatus Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-setgesturestatus)                           | Sets the interest of the InkPicture object in a specified application gesture.<br/>                                                                                      |
| [**SetSingleTabletIntegratedMode Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-setsingletabletintegratedmode) | Sets the InkPicture control to collect ink from only one tablet attached to the Tablet PC. Ink from other tablets is ignored.<br/>                                       |
| [**SetWindowInputRectangle Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-setwindowinputrectangle)             | Specifies the window rectangle to set, in window coordinates, within which ink is drawn.<br/>                                                                            |
| ShowWhatsThis                                                                            | Displays a selected topic in a Help file using the "What's This" popup provided by Help in 32-bit Microsoft Windows operating systems (design-time only).<br/>           |
| ZOrder                                                                                   | Places the control at the front or back of the z-order within its graphical level (design-time only).<br/>                                                               |



 




| Property | Description | 
|----------|-------------|
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_autoredraw"><strong>AutoRedraw Property</strong></a> | Gets or sets a value that specifies whether the InkPicture control repaints when the window is invalidated (whether the <a href="inkdisp-class.md"><strong>InkDisp</strong></a> object currently associated with InkPicture control is automatically redrawn when the window associated with the InkPicture receives a WM_PAINT message).<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_backcolor"><strong>BackColor</strong></a> | Gets or sets the background color for the InkPicture control. The default background color is the system window background color, which is typically white.<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_collectingink"><strong>CollectingInk Property</strong></a> | Gets the value that specifies whether the InkPicture control is collecting ink (run time only).<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_collectionmode"><strong>CollectionMode</strong></a> | Gets or sets the collection mode that determines whether ink, gestures, or ink and gestures are recognized as the user writes.<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_cursors"><strong>Cursors Property</strong></a> | Gets the <a href="/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursors"><strong>IInkCursors</strong></a> collection available for use in the InkPicture control's inking region.<br /> | 
| <a href="/previous-versions/windows/desktop/legacy/ms703274(v=vs.85)"><strong>CustomStrokes</strong></a> | Gets the <a href="/windows/desktop/api/msinkaut/nn-msinkaut-iinkcustomstrokes"><strong>IInkCustomStrokes</strong></a> collection to be persisted with the ink (design-time only).<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_defaultdrawingattributes"><strong>DefaultDrawingAttributes Property</strong></a> | Gets or sets the default <a href="inkdrawingattributes-class.md"><strong>InkDrawingAttributes</strong></a> collection to use when drawing and displaying ink (run time only).<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_desiredpacketdescription"><strong>DesiredPacketDescription Property</strong></a> | Gets or sets the packet description of the InkPicture control (run time only).<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_dynamicrendering"><strong>DynamicRendering Property</strong></a> | Gets or sets the value that specifies whether the InkPicture control dynamically renders the ink as it is collected.<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_editingmode"><strong>EditingMode</strong></a> | Gets or sets a value that specifies whether the InkPicture control is in ink mode, deletion mode, or selecting/editing mode.<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_enabled"><strong>Enabled</strong></a> | Gets or sets a value that determines whether the InkPicture control can respond to user-generated events.<br /><blockquote>[!Note]<br />This property is equivalent to the <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_inkenabled"><strong>InkEnabled</strong></a> property.</blockquote><br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_erasermode"><strong>EraserMode</strong></a> | Gets or sets the value that specifies whether ink is erased by stroke or by point.<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_eraserwidth"><strong>EraserWidth</strong></a> | Gets or sets the value that specifies the width of the eraser pen tip.<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_hwnd"><strong>hWnd</strong></a> | Gets the window handle to which the InkPicture control is bound. (run time only)<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_ink"><strong>Ink</strong></a> | Gets or sets the <a href="inkdisp-class.md"><strong>InkDisp</strong></a> object that is associated with the InkPicture control (run time only).<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_inkenabled"><strong>InkEnabled</strong></a> | Gets or sets a value that specifies whether the InkPicture control collects pen input (in-air packets, cursor in range events, and so on).<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_marginx"><strong>MarginX Property</strong></a> | Gets or sets the x-axis margin around the window rectangle in screen coordinates.<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_marginy"><strong>MarginY Property</strong></a> | Gets or sets the y-axis margin around the window rectangle in screen coordinates.<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_mouseicon"><strong>MouseIcon Property</strong></a> | Gets or sets the current custom mouse icon.<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_mousepointer"><strong>MousePointer Property</strong></a> | Gets or sets a value that indicates the type of mouse pointer that appears when the mouse is over a particular part of the InkPicture control.<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_picture"><strong>Picture</strong></a> | Gets the graphics file to appear on the InkPicture control.<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_renderer"><strong>Renderer Property</strong></a> | Gets or sets the <a href="inkrenderer-class.md"><strong>InkRenderer</strong></a> object that is used to draw ink on the InkPicture control (run time only).<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_selection"><strong>Selection</strong></a> | Gets the <a href="/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)">InkStrokes</a> collection currently selected inside the InkPicture control (run time only).<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_sizemode"><strong>SizeMode</strong></a> | Gets or sets how the control handles image placement and sizing.<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_supporthighcontrastink"><strong>SupportHighContrastInk Property</strong></a> | Gets a value that specifies whether ink is rendered as just one color, Color = COLOR_WINDOWTEXT (from the GetSystemMetrics call) when the system is in High Contrast mode.<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_supporthighcontrastselectionui"><strong>SupportHighContrastSelectionUI</strong></a> | Gets or sets a value that specifies whether all selection user interfaces (selection bounding box and selection handles) are drawn in high contrast when the system is in High Contrast mode.<br /> | 
| <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_tablet"><strong>Tablet Property</strong></a> | Gets the <a href="/windows/desktop/api/msinkaut/nn-msinkaut-iinktablet"><strong>IInkTablet</strong></a> object that the InkPicture control is currently using to collect input.<br /> | 




 

## Remarks

The run time user interface for the InkPicture control is a window with an opaque background (single color, picture background, or both) that contains opaque ink.

You can use the InkPicture control to render ink in Microsoft Windows 2000, Windows Server 2003, any edition of Windows XP other than Windows XP Tablet PC Edition, and any version of Windows Vista. However, you can input ink, accept gestures, or recognize handwriting only under the following conditions:

-   Ink can be input and recognized if Windows Vista or XP Tablet PC Edition 2005 is installed.
-   Gestures can be recognized as well.
-   Handwriting can be recognized as text if the handwriting originated on machines running older versions of Windows as long as recognizers are present.

If you use Windows 2000, Windows Server 2003, any edition of Windows XP other than Windows XP Tablet PC Edition 2005, you can assign values to the ambient properties of the InkPicture control, then copy and paste ink to other applications. However, the value of its InkEnabled property will always be **FALSE**.

Persisted [**InkDisp**](inkdisp-class.md) objects can be loaded and displayed on all editions of Windows Vista and XP and on systems that have only the Windows XP Tablet PC Edition Software Development Kit (SDK) installed. **InkDisp** objects can only be converted to text (recognized), if Windows Vista or the Windows XP Tablet PC Edition 2005 is installed.

If operations on this control do not succeed, a legal HRESULT is returned. If error conditions result, check the returned HRESULT against the error.

For more information about ink controls, see [Ink](ink-controls.md).

For information about which threads raise particular events, see [Threads on Which an Event Can Fire](threads-on-which-an-event-can-fire.md).

To improve your application's performance, manually dispose of an InkPicture control when it is no longer needed.

> [!Note]  
> When an InkPicture control is overlayed with another control, such as a **GroupBox** set to transparent, the InkPicture will not collect ink. The InkPicture must be the top-most control in the Z-order or it must be a child of the **GroupBox**.

 

## COM Implementation

This object implements the **IInkPicture** COM interface.

## Related topics

<dl> <dt>

[InkEdit Control Reference](inkedit-control-reference.md)
</dt> <dt>

[**InkOverlay Class**](inkoverlay-class.md)
</dt> </dl>

