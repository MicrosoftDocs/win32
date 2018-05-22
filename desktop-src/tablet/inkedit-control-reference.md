---
Description: 'The InkEdit control enables you to collect ink, recognize ink, and display ink as text.'
ms.assetid: '52761cb2-4433-4824-ba19-fe597de2faf0'
title: InkEdit Control Reference
---

# InkEdit Control Reference

The InkEdit control enables you to collect ink, recognize ink, and display ink as text. This control allows you to enable smart forms, which improves the accuracy of text input.

This control is a superset of the [**RichEdit**](https://msdn.microsoft.com/library/windows/desktop/bb774306) control. It extends the **RichEdit** control with the ability to capture, recognize, and display ink.

This object can be instantiated by calling the [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615) method in C++.

Creating the InkEdit control behind a transparent control (such as a GroupBox with the WS\_EX\_TRANSPARENT property set) will prevent InkEdit from collecting ink.

## Members



| Enumeration                                            | Description                                                                                                                                                                |
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AppearanceConstants**](appearanceconstants.md)     | Defines values that specify whether the control appears flat or 3-D.<br/>                                                                                            |
| [**BorderStyleConstants**](borderstyleconstants.md)   | Defines values that specify whether the control has a border.<br/>                                                                                                   |
| [**InkApplicationGesture**](inkapplicationgesture.md) | Defines values that set the interest in a set of application-specific gestures.<br/>                                                                                 |
| [**InkDisplayMode**](inkdisplaymode.md)               | Defines values that specify whether a selection appears as ink or text.<br/>                                                                                         |
| [**InkEditStatus**](inkeditstatus.md)                 | Defines values that specify whether the InkEdit control is idle, collecting ink, or recognizing ink.<br/>                                                            |
| [**InkInsertMode**](inkinsertmode.md)                 | Defines values that specify how ink is inserted onto the InkEdit control.<br/>                                                                                       |
| [**InkMode**](inkmode.md)                             | Defines values that specify the collection mode settings for drawn ink-whether ink collection is disabled, ink is collected, or ink and gestures are collected.<br/> |
| [**InkMouseButton**](inkmousebutton.md)               | Defines values that specify which mouse button was pressed.<br/>                                                                                                     |
| [**InkMousePointer**](inkmousepointer.md)             | Defines values that specify the type of mouse pointer that appears.<br/>                                                                                             |
| [**MouseButton**](mousebutton.md)                     | Defines values that specify which mouse button was pressed.<br/>                                                                                                     |
| [**ScrollBarsConstants**](scrollbarsconstants.md)     | Defines values that specify how the scroll bars of an InkEdit control appear on the screen.<br/>                                                                     |
| [**SelAlignmentConstants**](selalignmentconstants.md) | Defines values that specify the alignment of the paragraph relative to the margins of the InkEdit control.<br/>                                                      |



 



| Event notification message                                   | Description                                                                                            |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [IECN\_STROKE](inkedit-messages--win32-only-.md)            | This message is sent through a WM\_NOTIFY message when a stroke is completed (Win32 only).<br/>  |
| [IECN\_GESTURE](inkedit-messages--win32-only-.md)           | This message is sent through a WM\_NOTIFY message when a gesture is completed (Win32 only).<br/> |
| [IECN\_RECOGNITIONRESULT](inkedit-messages--win32-only-.md) | This message is sent through a WM\_NOTIFY message when recognition occurs (Win32 only).<br/>     |



 



| Event                                                  | Description                                                                                                                                                                                 |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Change**](inkedit-change.md)                       | Occurs when the contents of the control or a property value change.<br/>                                                                                                              |
| [**Click**](inkedit-click.md)                         | Occurs when the control is clicked.<br/>                                                                                                                                              |
| [**DblClick**](inkedit-dblclick.md)                   | Occurs when the control is double-clicked.<br/>                                                                                                                                       |
| [**Gesture**](inkedit-gesture.md)                     | Occurs when an application gesture is recognized.<br/>                                                                                                                                |
| [**KeyDown**](inkedit-keydown.md)                     | Occurs when the user presses a key while the InkEdit control has focus.<br/>                                                                                                          |
| [**KeyPress**](inkedit-keypress.md)                   | Occurs when a key is pressed while the InkEdit control has focus.<br/>                                                                                                                |
| [**KeyUp**](inkedit-keyup.md)                         | Occurs when a key is released while the InkEdit control has focus.<br/>                                                                                                               |
| [**MouseDown**](inkedit-mousedown.md)                 | Occurs when the mouse pointer is over the InkEdit control and a mouse button is pressed.<br/>                                                                                         |
| [**MouseMove**](inkedit-mousemove.md)                 | Occurs when the mouse pointer is moved over the InkEdit control.<br/>                                                                                                                 |
| [**MouseUp**](inkedit-mouseup.md)                     | Occurs when the mouse pointer is over the InkEdit control and a mouse button is released.<br/>                                                                                        |
| [**RecognitionResult**](inkedit-recognitionresult.md) | Occurs when the InkEdit control gets results manually from a call to the [**Recognize**](inkedit-recognize.md) method or automatically after the recognition timeout has fired.<br/> |
| [**SelChange**](inkedit-selchange.md)                 | Occurs when the selection of ink within the InkEdit control changes.<br/>                                                                                                             |
| [**Stroke**](inkedit-stroke.md)                       | Occurs when the user draws a new [**IInkStrokeDisp**](iinkstrokedisp.md) object on any [**IInkTablet**](iinktablet.md) object.<br/>                                                 |



 



| Get/Set message                                               | Description                                                                                                                                                                     |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [EM\_GETINKMODE](inkedit-messages--win32-only-.md)           | Gets the ink mode of the control (Win32 only).<br/>                                                                                                                       |
| [EM\_SETINKMODE](inkedit-messages--win32-only-.md)           | Sets the ink mode of the control (Win32 only).<br/>                                                                                                                       |
| [EM\_GETINKINSERTMODE](inkedit-messages--win32-only-.md)     | Gets the ink insertion mode of the control (Win32 only).<br/>                                                                                                             |
| [EM\_SETINKINSERTMODE](inkedit-messages--win32-only-.md)     | Sets the ink insertion mode of the control (Win32 only).<br/>                                                                                                             |
| [EM\_GETDRAWATTR](inkedit-messages--win32-only-.md)          | Gets the current drawing attributes of the control (Win32 only).<br/>                                                                                                     |
| [EM\_SETDRAWATTR](inkedit-messages--win32-only-.md)          | Sets the drawing attributes to use for future ink collection (Win32 only).<br/>                                                                                           |
| [EM\_GETRECOTIMEOUT](inkedit-messages--win32-only-.md)       | Gets the recognition timeout for the control (Win32 only).<br/>                                                                                                           |
| [EM\_SETRECOTIMEOUT](inkedit-messages--win32-only-.md)       | Sets the recognition timeout for the control (Win32 only).<br/>                                                                                                           |
| [EM\_GETGESTURESTATUS](inkedit-messages--win32-only-.md)     | Gets the gesture status for the control (Win32 only).<br/>                                                                                                                |
| [EM\_SETGESTURESTATUS](inkedit-messages--win32-only-.md)     | Sets the gesture status for the control (Win32 only).<br/>                                                                                                                |
| [EM\_GETRECOGNIZER](inkedit-messages--win32-only-.md)        | Gets the recognizer that the control uses (Win32 only).<br/>                                                                                                              |
| [EM\_SETRECOGNIZER](inkedit-messages--win32-only-.md)        | Sets the recognizer that the control uses (Win32 only).<br/>                                                                                                              |
| [EM\_GETFACTOID](inkedit-messages--win32-only-.md)           | Gets the factoid to use for recognition (Win32 only).<br/>                                                                                                                |
| [EM\_SETFACTIOD](inkedit-messages--win32-only-.md)           | Sets the factoid to use for recognition (Win32 only).<br/>                                                                                                                |
| [EM\_GETSELINK](inkedit-messages--win32-only-.md)            | Gets the ink in the selection (Win32 only).<br/>                                                                                                                          |
| [EM\_SETSELINK](inkedit-messages--win32-only-.md)            | Sets the ink in the selection (Win32 only).<br/>                                                                                                                          |
| [EM\_GETSELINKDISPLAYMODE](inkedit-messages--win32-only-.md) | Returns the current appearance of the ink in the selected range by using one of the values of the [**InkDisplayMode**](inkdisplaymode.md) enumeration (Win32 only).<br/> |
| [EM\_SETSELINKDISPLAYMODE](inkedit-messages--win32-only-.md) | Sets the appearance of the ink in the selected range by using one of the values of the [**InkDisplayMode**](inkdisplaymode.md) enumeration (Win32 only).<br/>            |
| [EM\_GETSTATUS](inkedit-messages--win32-only-.md)            | Gets the status of the control (Win32 only).<br/>                                                                                                                         |
| [EM\_RECOGNIZE](inkedit-messages--win32-only-.md)            | Forces recognition (Win32 only).<br/>                                                                                                                                     |
| [EM\_GETMOUSEICON](inkedit-messages--win32-only-.md)         | Gets the mouse icon (Win32 only).<br/>                                                                                                                                    |
| [EM\_SETMOUSEICON](inkedit-messages--win32-only-.md)         | Sets the mouse icon (Win32 only).<br/>                                                                                                                                    |
| [EM\_GETMOUSEPOINTER](inkedit-messages--win32-only-.md)      | Gets the mouse pointer (Win32 only).<br/>                                                                                                                                 |
| [EM\_SETMOUSEPOINTER](inkedit-messages--win32-only-.md)      | Sets the mouse pointer Win32 only).<br/>                                                                                                                                  |
| [EM\_GETUSEMOUSEFORINPUT](inkedit-messages--win32-only-.md)  | Gets the state of whether mouse input is treated like pen input (Win32 only).<br/>                                                                                        |
| [EM\_SETUSEMOUSEFORINPUT](inkedit-messages--win32-only-.md)  | Sets the state of whether mouse input is treated like pen input (Win32 only).<br/>                                                                                        |



 



| Method                                               | Description                                                                     |
|------------------------------------------------------|---------------------------------------------------------------------------------|
| [**GetGestureStatus**](inkedit-getgesturestatus.md) | Gets the interest of the InkEdit control in a known set of gestures.<br/> |
| [**Recognize**](inkedit-recognize.md)               | Specifies that recognition should occur.<br/>                             |
| [**Refresh**](peninputpanel-refresh.md)             | Causes the control to redraw.<br/>                                        |
| [**SetGestureStatus**](inkedit-setgesturestatus.md) | Sets the interest of the InkEdit control in a known set of gestures.<br/> |



 



| Property                                                 | Description                                                                                                                                                                           |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Appearance**](inkedit-appearance.md)                 | Gets or sets a value that determines whether the InkEdit control appears flat or 3-D.<br/>                                                                                      |
| [**BackColor**](inkedit-backcolor.md)                   | Gets or sets the background color for the InkEdit control.<br/>                                                                                                                 |
| [**BorderStyle**](inkedit-borderstyle.md)               | Gets or sets a value that determines whether the InkEdit control has a border.<br/>                                                                                             |
| [**DisableNoScroll**](inkedit-disablenoscroll.md)       | Gets or sets a value that determines whether scroll bars in the InkEdit control are disabled.<br/>                                                                              |
| [**DrawingAttributes**](inkedit-drawingattributes.md)   | Gets or sets the drawing attributes for ink that is yet to be drawn on the InkEdit control.<br/>                                                                                |
| [**Enabled**](inkedit-enabled.md)                       | Gets or sets a value that determines whether the InkEdit control can respond to user-generated events.<br/>                                                                     |
| [**Factoid**](inkedit-factoid.md)                       | Gets or sets the [Factoid](factoid-constants.md) constant that a [**IInkRecognizer**](iinkrecognizer.md) object uses to constrain its search for the recognition result.<br/> |
| [**Font**](inkedit-font.md)                             | Gets or sets the font of the text that the InkEdit control displays.<br/>                                                                                                       |
| [**hWnd**](inkedit-hwnd.md)                             | Gets the window handle to which the [**InkDisp**](inkdisp-class.md) control is bound.<br/>                                                                                     |
| [**InkInsertMode**](inkedit-inkinsertmode.md)           | Gets or sets a value that specifies how ink is inserted onto the InkEdit control, either as text or as ink.<br/>                                                                |
| [**InkMode**](inkedit-inkmode.md)                       | Gets or sets a value that specifies whether ink collection is disabled, ink is collected, or ink and gestures are collected.<br/>                                               |
| [**Locked**](inkedit-locked.md)                         | Gets or sets a value that specifies whether the InkEdit control is read-only or not.<br/>                                                                                       |
| [**MaxLength**](inkedit-maxlength.md)                   | Gets or sets a value indicating whether an InkEdit control can hold a maximum number of characters and, if so, specifies the maximum number of characters.<br/>                 |
| [**MouseIcon**](inkedit-mouseicon.md)                   | Gets or sets the current custom mouse icon.<br/>                                                                                                                                |
| [**MousePointer**](inkedit-mousepointer.md)             | Gets or sets a value that indicates the type of mouse pointer that appears when the mouse is over a particular part of the InkEdit control.<br/>                                |
| [**MultiLine**](inkedit-multiline.md)                   | Gets or sets a value that indicates whether this is a multiline InkEdit control.<br/>                                                                                           |
| [**RecognitionTimeout**](inkedit-recotimeout.md)        | Gets or sets the length of time, in milliseconds, between the last [**IInkStrokeDisp**](iinkstrokedisp.md) object collected and the beginning of text recognition.<br/>        |
| [**Recognizer**](inkedit-recognizer.md)                 | Gets or sets the [**IInkRecognizer**](iinkrecognizer.md) object to use for recognition.<br/>                                                                                   |
| [**ScrollBars**](inkedit-scrollbars.md)                 | Gets or sets the type of scroll bars that appear in the InkEdit control.<br/>                                                                                                   |
| [**SelAlignment**](inkedit-selalignment.md)             | Gets or sets the alignment to apply to the current selection or insertion point (run time only).<br/>                                                                           |
| [**SelBold**](inkedit-selbold.md)                       | Gets or sets a value that specifies whether the font style of the currently selected text in the InkEdit control is bold (run time only).<br/>                                  |
| [**SelCharOffset**](inkedit-selcharoffset.md)           | Gets or sets whether text in the InkEdit control appears on the baseline, as a superscript, or as a subscript (run time only).<br/>                                             |
| [**SelColor**](inkedit-selcolor.md)                     | Gets or sets the text color of the current text selection or insertion point (run time only).<br/>                                                                              |
| [**SelFontName**](inkedit-selfontname.md)               | Gets or sets the font name of the selected text within the InkEdit control (run time only).<br/>                                                                                |
| [**SelFontSize**](inkedit-selfontsize.md)               | Gets or sets the font size of the selected text within the InkEdit control (run time only).<br/>                                                                                |
| [**SelInks**](inkedit-selinks.md)                       | Gets or sets the array of embedded [**InkDisp**](inkdisp-class.md) objects (if displayed as ink) that the current selection contains.<br/>                                     |
| [**SelInksDisplayMode**](inkedit-selinksdisplaymode.md) | Gets or sets a value that allows toggling the appearance of the selection between ink and text.<br/>                                                                            |
| [**SelItalic**](inkedit-selitalic.md)                   | Gets or sets a value that specifies whether the font style of the currently selected text in the InkEdit control is italic (run time only).<br/>                                |
| [**SelLength**](inkedit-sellength.md)                   | Gets or sets the number of characters that are selected in the InkEdit control (run time only).<br/>                                                                            |
| [**SelRTF**](inkedit-selrtf.md)                         | Gets or sets the currently selected Rich Text Format (RTF) formatted text in the InkEdit control (run time only).<br/>                                                          |
| [**SelStart**](inkedit-selstart.md)                     | Gets or sets the starting point of the text that is selected in the text box (run time only).<br/>                                                                              |
| [**SelText**](inkedit-seltext.md)                       | Gets or sets the selected text within the InkEdit control (run time only).<br/>                                                                                                 |
| [**SelUnderline**](inkedit-selunderline.md)             | Gets or sets a value that specifies whether the font style of the currently selected text in the InkEdit control is underlined (run time only).<br/>                            |
| [**Status**](inkedit-status.md)                         | Gets a value that specifies whether the InkEdit control is idle, collecting ink, or recognizing ink (run time only).<br/>                                                       |
| [**Text**](inkedit-text.md)                             | Gets or sets the current text in the text box.<br/>                                                                                                                             |
| [**TextRTF**](inkedit-textrtf.md)                       | Gets or sets the text of the InkEdit control, including all RTF codes.<br/>                                                                                                     |
| [**UseMouseForInput**](inkedit-usemouseforinput.md)     | Gets or sets a value that indicates whether the mouse can be used as an input device.<br/>                                                                                      |



 



| Structure                                                                    | Description                                                                                  |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**IEC\_STROKEINFO**](iec-strokeinfo--win32-only-.md)                       | Contains information about a [**Stroke**](inkedit-stroke.md) event (Win32 only).<br/> |
| [**IEC\_GESTUREINFO**](iec-gestureinfo--win32-only-.md)                     | Contains information about a specific gesture (Win32 only).<br/>                       |
| [**IEC\_RECOGNITIONRESULTINFO**](iec-recognitionresultinfo--win32-only-.md) | Contains information about a recognition result (Win32 only).<br/>                     |



 

## COM Implementation

This object implements the **IInkEdit** COM interface.

## Related topics

<dl> <dt>

[**InkOverlay Class**](inkoverlay-class.md)
</dt> <dt>

[InkPicture Control Reference](inkpicture-control-reference.md)
</dt> <dt>

[**InkRecognizerContext Class**](inkrecognizercontext-class.md)
</dt> </dl>

 

 




