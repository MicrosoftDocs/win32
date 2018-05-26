---
Description: The InkEdit control is a super class of the RichEdit control.
ms.assetid: 26023012-9ab1-4bd9-beff-41587bc74f5e
title: InkEdit Messages (Win32 Only)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InkEdit Messages (Win32 Only)

The [InkEdit](inkedit-control-reference.md) control is a super class of the [**RichEdit**](https://msdn.microsoft.com/library/windows/desktop/bb774306) control. Every **RichEdit** message is passed on, directly in most cases, and has exactly the same effect as in **RichEdit**. This also applies to event notification messages.

To send these messages, call the SendMessage function with the following parameters:



<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre data-space="preserve"><code>LRESULT SendMessage(
  HWND hWnd,      // handle to destination window
  UINT Msg,       // message
  WPARAM wParam,  // first message parameter
  LPARAM lParam   // second message parameter
);</code></pre></td>
</tr>
</tbody>
</table>



 

## Message

The parent window of the [InkEdit](inkedit-control-reference.md) control receives event notification messages through the WM\_NOTIFY message:


```C++
LRESULT CALLBACK WindowProc(
    HWND hWnd,                // handle to window
    UINT uMsg,                // WM_NOTIFY
    WPARAM wParam,        // InkEdit control identifier
    LPARAM lParam            // see documentation for notification messages
);
```





| Get/set message                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EM\_GETINKMODE<br/>           | Gets the inking mode of the [InkEdit](inkedit-control-reference.md) control.<br/> Parameters:<br/> This message has no parameters; *wParam* and *lParam* must be 0.<br/> Return values:<br/> This message returns one of the values that are defined in the [**InkMode**](/windows/win32/inked/ne-inked-inkmode?branch=master) enumeration, which specifies whether ink collection is disabled, whether ink is collected, or whether ink and gestures are collected.<br/>                                                                                                                                                                                                                                                         |
| EM\_SETINKMODE<br/>           | Sets the inking mode of the [InkEdit](inkedit-control-reference.md) control.<br/> Parameters:<br/>*wParam*Specifies one of the values of the [**InkMode**](/windows/win32/inked/ne-inked-inkmode?branch=master) enumeration, which specifies whether ink collection is disabled, whether ink is collected, or whether ink and gestures are collected.<br/>*lParam*This parameter is not used; it must be 0.<br/> Return Values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/> Remarks:<br/> This should only be used if the EM\_GETSTATUS returns IES\_Idle.<br/>                                                                                                               |
| EM\_GETINKINSERTMODE<br/>     | Gets the ink insertion mode of the [InkEdit](inkedit-control-reference.md) control.<br/> Parameters:<br/> This message has no parameters; *wParam* and *lParam* must be 0.<br/> Return values:<br/> This message returns one of the values of the [**InkInsertMode**](/windows/win32/inked/ne-inked-inkinsertmode?branch=master) enumeration, which specifies whether ink is inserted into the control as text or as ink.<br/>                                                                                                                                                                                                                                                                                                    |
| EM\_SETINKINSERTMODE<br/>     | Sets the ink insertion mode of the [InkEdit](inkedit-control-reference.md) control. Sending this message has no effect if used with any operating system installed other than Microsoft Windows XP Tablet PC Edition.<br/> Parameters:<br/>*wParam*Specifies one of the values of the [**InkInsertMode**](/windows/win32/inked/ne-inked-inkinsertmode?branch=master) enumeration, which specifies whether ink is inserted into the control as text or as ink.<br/>*lParam*This parameter is not used; it must be 0.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/>                                                                                                       |
| EM\_GETDRAWATTR<br/>          | Gets the current drawing attributes of the [InkEdit](inkedit-control-reference.md) control.<br/> Parameters:<br/>*wParam*This parameter is not used; it must be 0.<br/>*lParam*Specifies a pointer (IInkDrawingAttributes \*\*pDrawAttr) to receive the current [**InkDrawingAttributes**](/windows/win32/msinkaut/?branch=master) object.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/>                                                                                                                                                                                                                                                |
| EM\_SETDRAWATTR<br/>          | Sets the drawing attributes to use for future ink collection.<br/> Parameters:<br/>*wParam*This parameter is not used; it must be 0.<br/>*lParam*Specifies a pointer (IInkDrawingAttributes \*pDrawAttr) to an [**InkDrawingAttributes**](/windows/win32/msinkaut/?branch=master) object.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/>                                                                                                                                                                                                                                                                                                  |
| EM\_GETRECOTIMEOUT<br/>       | Gets the recognition timeout, in milliseconds, for the [InkEdit](inkedit-control-reference.md) control.<br/> Parameters:<br/> This message has no parameters; *wParam* and *lParam* must be 0.<br/> Return values:<br/> This message returns the recognition timeout, in milliseconds.<br/>                                                                                                                                                                                                                                                                                                                                                                                               |
| EM\_SETRECOTIMEOUT<br/>       | Sets the recognition timeout, in milliseconds, for the [InkEdit](inkedit-control-reference.md) control.<br/> Parameters:<br/>*wParam*Specifies the recognition timeout, in milliseconds.<br/>*lParam*This parameter is not used; it must be 0.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/>                                                                                                                                                                                                                                                                                                                                    |
| EM\_GETGESTURESTATUS<br/>     | Gets the gesture status for the [InkEdit](inkedit-control-reference.md) control.<br/> Parameters:<br/>*wParam*Specifies the type of gesture, as defined in the [**InkApplicationGesture**](/windows/win32/msinkaut/ne-msinkaut-inkapplicationgesture?branch=master) enumeration.<br/>*lParam*This parameter is not used; it must be 0.<br/> Return values:<br/> This message returns **TRUE** if the [InkEdit](inkedit-control-reference.md) control subscribes to the gesture or **FALSE** if the InkEdit control does not subscribe to the gesture.<br/>                                                                                                                                                                       |
| EM\_SETGESTURESTATUS<br/>     | Sets the gesture status for the [InkEdit](inkedit-control-reference.md) control.<br/> Parameters:<br/>*wParam*Specifies the type of gesture, as defined in the [**InkApplicationGesture**](/windows/win32/msinkaut/ne-msinkaut-inkapplicationgesture?branch=master) enumeration.<br/>*lParam*Specifies **TRUE** if subscribing to the gesture is enabled or **FALSE** if listening to the gesture is not enabled.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/> Remarks:<br/> This should only be used if the EM\_GETSTATUS returns IES\_Idle.<br/>                                                                                                               |
| EM\_GETRECOGNIZER<br/>        | Gets the recognizer that the [InkEdit](inkedit-control-reference.md) control uses.<br/> Parameters:<br/>*wParam*This parameter is not used; it must be 0.<br/>*lParam*Specifies a pointer to an IInkRecognizer\* to receive the [**IInkRecognizer**](/windows/win32/msinkaut/nn-msinkaut-iinkrecognizer?branch=master) object that the [InkEdit](inkedit-control-reference.md) control uses.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/>                                                                                                                                                                                                                                   |
| EM\_SETRECOGNIZER<br/>        | Sets the recognizer that the [InkEdit](inkedit-control-reference.md) control uses. If a [Factoid](factoid-constants.md) is used for the InkEdit control, it must be reapplied after sending this message.<br/> Parameters:<br/>*wParam*This parameter is not used; it must be 0.<br/>*lParam*Specifies a pointer to an IInkRecognizer\* to set the [**IInkRecognizer**](/windows/win32/msinkaut/nn-msinkaut-iinkrecognizer?branch=master) object that the [InkEdit](inkedit-control-reference.md) control uses for later use.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/> Remarks:<br/> This should only be used if the EM\_GETSTATUS returns IES\_Idle.<br/> |
| EM\_GETFACTOID<br/>           | Gets the [Factoid](factoid-constants.md) to use for recognition.<br/> Parameters:<br/>*wParam*This parameter is not used; it must be 0.<br/>*lParam*Specifies a pointer to a BSTR to receive the factoid string.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/>                                                                                                                                                                                                                                                                                                                                                                  |
| EM\_SETFACTOID<br/>           | Sets the [Factoid](factoid-constants.md) to use for recognition.<br/> Parameters:<br/>*wParam*This parameter is not used; it must be 0.<br/>*lParam*Specifies the BSTR that contains the factoid string.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/> Remarks:<br/> This should only be used if the EM\_GETSTATUS returns IES\_Idle.<br/>                                                                                                                                                                                                                                                                          |
| EM\_GETSELINK<br/>            | Gets the ink within the selection. Ink must be recognized before being accessed through this message. If it is not recognized first, EM\_GETSELINK always returns zero [**InkDisp**](/windows/win32/msinkaut/?branch=master) objects.<br/> Parameters:<br/>*wParam*This parameter is not used; it must be 0.<br/>*lParam*Specifies a pointer to a VARIANT to receive a safe array to receive [**InkDisp**](/windows/win32/msinkaut/?branch=master) objects within the current selection.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/>                                                                                                                                     |
| EM\_SETSELINK<br/>            | Sets the ink within the selection. Sending this message has no effect if used with any operating system installed other than Windows XP Tablet PC Edition.<br/> Parameters:<br/>*wParam*This parameter is not used; it must be 0.<br/>*lParam*Specifies a pointer to a VARIANT with a safe array of [**InkDisp**](/windows/win32/msinkaut/?branch=master) objects to replace the current selection.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/>                                                                                                                                                                                                     |
| EM\_GETSELINKDISPLAYMODE<br/> | Returns the current appearance of the ink in the selected range by using one of the values of the [**InkDisplayMode**](/windows/win32/inked/ne-inked-inkdisplaymode?branch=master) enumeration.<br/> Parameters:<br/> This message has no parameters; *wParam* and *lParam* must be 0.<br/> Return values:<br/> This message returns one of the values of the [**InkDisplayMode**](/windows/win32/inked/ne-inked-inkdisplaymode?branch=master) enumeration (IDM\_Text or IDM\_Ink), which specifies how a selection appears on the control.<br/>                                                                                                                                                                                                                           |
| EM\_SETSELINKDISPLAYMODE<br/> | Sets the appearance of the ink in the selected range by using one of the values of the [**InkDisplayMode**](/windows/win32/inked/ne-inked-inkdisplaymode?branch=master) enumeration.<br/> Parameters:<br/>*wParam*This parameter is not used; it must be 0.<br/>*lParam*Specifies how ink appears in the selected range, as defined in the [**InkDisplayMode**](/windows/win32/inked/ne-inked-inkdisplaymode?branch=master) enumeration.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs. Sending this message has no effect if used with any operating system installed other than Windows XP Tablet PC Edition.<br/>                                                                                                   |
| EM\_GETSTATUS<br/>            | Gets the status of the [InkEdit](inkedit-control-reference.md) control.<br/> Parameters:<br/> This message has no parameters; *wParam* and *lParam* must be 0.<br/> Return values:<br/> This message returns one of the values of the [**InkEditStatus**](/windows/win32/inked/ne-inked-inkeditstatus?branch=master) enumeration, which specifies whether the control is idle, collecting ink, or recognizing ink.<br/>                                                                                                                                                                                                                                                                                                           |
| EM\_RECOGNIZE<br/>            | Forces recognition.<br/> Parameters:<br/> This message has no parameters; *wParam* and *lParam* must be 0.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| EM\_GETMOUSEICON<br/>         | Gets the mouse icon.<br/> Parameters:<br/>*wParam*This parameter is not used; it must be 0.<br/>*lParam*Specifies a HICON\* pointer that is filled in with the current [**MouseIcon**](/windows/win32/msinkaut/?branch=master) HICON. This HICON can be either a HICON or a **NULL** value.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/>                                                                                                                                                                                                                                                                                                    |
| EM\_SETMOUSEICON<br/>         | Sets the mouse icon.<br/> Parameters:<br/>*wParam*Specifies a BOOLEAN value that is set to **TRUE** if the [InkEdit](inkedit-control-reference.md) control should own the HICON handle or **FALSE** if the InkEdit control should not own the HICON handle. If the InkEdit control owns the HICON, then it takes care of and destroys the HICON appropriately. Otherwise, the caller owns the HICON and is responsible for deleting it.<br/>*lParam*Specifies the new HICON value. Use **NULL** to clear the value. The default value is **NULL**.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/>                                |
| EM\_GETMOUSEPOINTER<br/>      | Gets the mouse pointer.<br/> Parameters:<br/>*wParam*This parameter is not used; it must be 0.<br/>*lParam*Contains an InkMousePointer\* pointer that is filled in with the current [**MousePointer**](/windows/win32/msinkaut/nf-msinkaut-iinkcollector-put_mousepointer?branch=master) value. This behaves the same as the **InkCollector::get\_MousePointer** property.<br/> Return Values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/>                                                                                                                                                                                                                                                            |
| EM\_SETMOUSEPOINTER<br/>      | Sets the mouse pointer.<br/> Parameters:<br/>*wParam*This parameter is not used; it must be 0.<br/>*lParam*Contains the new [**MousePointer**](/windows/win32/msinkaut/nf-msinkaut-iinkcollector-put_mousepointer?branch=master) value, which is defined in the [**InkMousePointer**](/windows/win32/msinkaut/ne-msinkaut-inkmousepointer?branch=master) enumeration. This behaves the same as the **InkCollector::put\_MousePointer** property.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/>                                                                                                                                                                                                                                    |
| EM\_GETUSEMOUSEFORINPUT<br/>  | Gets the state of whether mouse input is treated as pen input.<br/> Parameters:<br/> This message has no parameters; *wParam* and *lParam* must be 0.<br/> Return values:<br/> This message returns 0 if **FALSE** or 1 if **TRUE**.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| EM\_SETUSEMOUSEFORINPUT<br/>  | Sets the state of whether mouse input is treated as pen input.<br/> Parameters:<br/>*wParam*Specifies a Boolean value that determines whether to treat mouse input as pen input.<br/>*lParam*This parameter is not used; it must be 0.<br/> Return values:<br/> This message returns 0 if successful or nonzero if an error occurs.<br/> Remarks:<br/> This should only be used if the EM\_GETSTATUS returns IES\_Idle.<br/>                                                                                                                                                                                                                                             |



 



| Event notification message         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IECN\_STROKE<br/>            | Notifies the [InkEdit](inkedit-control-reference.md) control's parent window that a [**IInkStrokeDisp**](/windows/win32/msinkaut/nn-msinkaut-iinkstrokedisp?branch=master) has been created. This is sent in a WM\_NOTIFY message with the following parameters.<br/> Parameters:<br/>*wParam*Specifies the identifier of the control that sent the message.<br/>*lParam*Specifies a pointer to the [**IEC\_STROKEINFO**](/windows/win32/inked/ns-inked-iec_strokeinfo?branch=master) structure.<br/> Return values:<br/> The client returns 0 to accept the stroke and 1 to cancel the stroke.<br/> |
| IECN\_GESTURE<br/>           | Notifies the [InkEdit](inkedit-control-reference.md) control's parent window that a gesture has been recognized. This is sent in a WM\_NOTIFY message with the following parameters.<br/> Parameters:<br/>*wParam*Specifies the identifier of the control that sent the message.<br/>*lParam*Specifies a pointer to the [**IEC\_GESTUREINFO**](/windows/win32/inked/ns-inked-iec_gestureinfo?branch=master) structure.<br/> Return values:<br/> The client returns 0 to accept the gesture and 1 to cancel the gesture.<br/>                           |
| IECN\_RECOGNITIONRESULT<br/> | Notifies the [InkEdit](inkedit-control-reference.md) control's parent window that recognition has occurred. This is sent in a WM\_NOTIFY message with the following parameters.<br/> Parameters:<br/>*wParam*Specifies the identifier of the control that sent the message.<br/>*lParam*Specifies a pointer to the [**IEC\_RECOGNITIONRESULTINFO**](/windows/win32/inked/ns-inked-iec_recognitionresultinfo?branch=master) structure.<br/> Return values:<br/> The client returns 0 if it processes the message.<br/>                                  |



 

## Applies To

-   [InkEdit](inkedit-control-reference.md)

## Related topics

<dl> <dt>

[**IEC\_GESTUREINFO Structure (Win32 Only)**](/windows/win32/inked/ns-inked-iec_gestureinfo?branch=master)
</dt> <dt>

[**IEC\_STROKEINFO Structure (Win32 Only)**](/windows/win32/inked/ns-inked-iec_strokeinfo?branch=master)
</dt> <dt>

[**IEC\_RECOGNITIONRESULTINFO Structure (Win32 Only)**](/windows/win32/inked/ns-inked-iec_recognitionresultinfo?branch=master)
</dt> <dt>

[**MousePointer Property**](/windows/win32/msinkaut/nf-msinkaut-iinkcollector-put_mousepointer?branch=master)
</dt> <dt>

[**InkEditStatus Enumeration**](/windows/win32/inked/ne-inked-inkeditstatus?branch=master)
</dt> <dt>

[**InkInsertMode Enumeration**](/windows/win32/inked/ne-inked-inkinsertmode?branch=master)
</dt> <dt>

[**InkMode Enumeration**](/windows/win32/inked/ne-inked-inkmode?branch=master)
</dt> <dt>

[**IInkCursor Interface**](/windows/win32/msinkaut/nn-msinkaut-iinkcursor?branch=master)
</dt> <dt>

[**InkDrawingAttributes Class**](/windows/win32/msinkaut/?branch=master)
</dt> <dt>

[**IInkRecognitionResult Interface**](/windows/win32/msinkaut/nn-msinkaut-iinkrecognitionresult?branch=master)
</dt> <dt>

[**IInkRecognizer Interface**](/windows/win32/msinkaut/nn-msinkaut-iinkrecognizer?branch=master)
</dt> <dt>

[**InkDisp Class**](/windows/win32/msinkaut/?branch=master)
</dt> <dt>

[**IInkGesture Interface**](/windows/win32/msinkaut/nn-msinkaut-iinkgesture?branch=master)
</dt> </dl>

 

 




