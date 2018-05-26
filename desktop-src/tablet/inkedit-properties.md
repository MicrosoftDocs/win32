---
Description: This section contains Properties belonging to the InkEdit Control.
ms.assetid: 6aa476b3-97ad-4289-836b-f46fe4d04280
title: InkEdit Properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InkEdit Properties

This section contains Properties belonging to the InkEdit Control.



| Property                                                 | Description                                                                                                                                                                                            |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Appearance**](/windows/win32/inked/?branch=master)                 | Gets or sets a value that determines whether the [InkEdit](inkedit-control-reference.md) control appears flat or 3-D.<br/>                                                                      |
| [**BackColor**](/windows/win32/inked/?branch=master)                   | Gets or sets the background color for the [InkEdit](inkedit-control-reference.md) control.<br/>                                                                                                 |
| [**BorderStyle**](/windows/win32/inked/?branch=master)               | Gets or sets a value that determines whether the [InkEdit](inkedit-control-reference.md) control has a border.<br/>                                                                             |
| [**DisableNoScroll**](/windows/win32/inked/?branch=master)       | Gets or sets a value that determines whether scroll bars in the [InkEdit](inkedit-control-reference.md) control are disabled.<br/>                                                              |
| [**DrawingAttributes**](/windows/win32/inked/?branch=master)   | Gets or sets the drawing attributes for ink that is yet to be drawn on the [InkEdit](inkedit-control-reference.md) control.<br/>                                                                |
| [**Enabled**](/windows/win32/inked/?branch=master)                       | Gets or sets a value that determines whether the [InkEdit](inkedit-control-reference.md) control can respond to user-generated events.<br/>                                                     |
| [**Factoid**](/windows/win32/inked/?branch=master)                       | Gets or sets the [Factoid](factoid-constants.md) constant that a [**IInkRecognizer**](/windows/win32/msinkaut/nn-msinkaut-iinkrecognizer?branch=master) object uses to constrain its search for the recognition result.<br/>                  |
| [**Font**](/windows/win32/inked/?branch=master)                             | Gets or sets the font of the text that the [InkEdit](inkedit-control-reference.md) control displays.<br/>                                                                                       |
| [**hWnd**](/windows/win32/inked/?branch=master)                             | Gets the window handle to which the [**InkDisp**](/windows/win32/msinkaut/?branch=master) control is bound.<br/>                                                                                                      |
| [**InkInsertMode**](/windows/win32/inked/?branch=master)           | Gets or sets a value that specifies how ink is inserted onto the [InkEdit](inkedit-control-reference.md) control, either as text or as ink.<br/>                                                |
| [**InkMode**](/windows/win32/inked/?branch=master)                       | Gets or sets a value that specifies whether ink collection is disabled, ink is collected, or ink and gestures are collected.<br/>                                                                |
| [**Locked**](/windows/win32/inked/?branch=master)                         | Gets or sets a value that specifies whether the [InkEdit](inkedit-control-reference.md) control is read-only or not.<br/>                                                                       |
| [**MaxLength**](/windows/win32/inked/?branch=master)                   | Gets or sets a value indicating whether an [InkEdit](inkedit-control-reference.md) control can hold a maximum number of characters and, if so, specifies the maximum number of characters.<br/> |
| [**MouseIcon**](/windows/win32/inked/?branch=master)                   | Gets or sets the current custom mouse icon.<br/>                                                                                                                                                 |
| [**MousePointer**](/windows/win32/inked/?branch=master)             | Gets or sets a value that indicates the type of mouse pointer that appears when the mouse is over a particular part of the [InkEdit](inkedit-control-reference.md) control.<br/>                |
| [**MultiLine**](/windows/win32/inked/?branch=master)                   | Gets or sets a value that indicates whether this is a multiline [InkEdit](inkedit-control-reference.md) control.<br/>                                                                           |
| [**RecognitionTimeout**](/windows/win32/inked/?branch=master)        | Gets or sets the length of time, in milliseconds, between the last [**IInkStrokeDisp**](/windows/win32/msinkaut/nn-msinkaut-iinkstrokedisp?branch=master) object collected and the beginning of text recognition.<br/>                         |
| [**Recognizer**](/windows/win32/inked/?branch=master)                 | Gets or sets the [**IInkRecognizer**](/windows/win32/msinkaut/nn-msinkaut-iinkrecognizer?branch=master) object to use for recognition.<br/>                                                                                                    |
| [**ScrollBars**](/windows/win32/inked/?branch=master)                 | Gets or sets the type of scroll bars that appear in the [InkEdit](inkedit-control-reference.md) control.<br/>                                                                                   |
| [**SelAlignment**](/windows/win32/inked/?branch=master)             | Gets or sets the alignment to apply to the current selection or insertion point (run time only).<br/>                                                                                            |
| [**SelBold**](/windows/win32/inked/?branch=master)                       | Gets or sets a value that specifies whether the font style of the currently selected text in the [InkEdit](inkedit-control-reference.md) control is bold (run time only).<br/>                  |
| [**SelCharOffset**](/windows/win32/inked/?branch=master)           | Gets or sets whether text in the [InkEdit](inkedit-control-reference.md) control appears on the baseline, as a superscript, or as a subscript (run time only).<br/>                             |
| [**SelColor**](/windows/win32/inked/?branch=master)                     | Gets or sets the text color of the current text selection or insertion point (run time only).<br/>                                                                                               |
| [**SelFontName**](/windows/win32/inked/?branch=master)               | Gets or sets the font name of the selected text within the [InkEdit](inkedit-control-reference.md) control (run time only).<br/>                                                                |
| [**SelFontSize**](/windows/win32/inked/?branch=master)               | Gets or sets the font size of the selected text within the [InkEdit](inkedit-control-reference.md) control (run time only).<br/>                                                                |
| [**SelInks**](/windows/win32/inked/?branch=master)                       | Gets or sets the array of embedded [**InkDisp**](/windows/win32/msinkaut/?branch=master) objects (if displayed as ink) that the current selection contains.<br/>                                                      |
| [**SelInksDisplayMode**](/windows/win32/inked/?branch=master) | Gets or sets a value that allows toggling the appearance of the selection between ink and text.<br/>                                                                                             |
| [**SelItalic**](/windows/win32/inked/?branch=master)                   | Gets or sets a value that specifies whether the font style of the currently selected text in the [InkEdit](inkedit-control-reference.md) control is italic (run time only).<br/>                |
| [**SelLength**](/windows/win32/inked/?branch=master)                   | Gets or sets the number of characters that are selected in the [InkEdit](inkedit-control-reference.md) control (run time only).<br/>                                                            |
| [**SelRTF**](/windows/win32/inked/?branch=master)                         | Gets or sets the currently selected Rich Text Format (RTF) formatted text in the [InkEdit](inkedit-control-reference.md) control (run time only).<br/>                                          |
| [**SelStart**](/windows/win32/inked/?branch=master)                     | Gets or sets the starting point of the text that is selected in the text box (run time only).<br/>                                                                                               |
| [**SelText**](/windows/win32/inked/?branch=master)                       | Gets or sets the selected text within the [InkEdit](inkedit-control-reference.md) control (run time only).<br/>                                                                                 |
| [**SelUnderline**](/windows/win32/inked/?branch=master)             | Gets or sets a value that specifies whether the font style of the currently selected text in the [InkEdit](inkedit-control-reference.md) control is underlined (run time only).<br/>            |
| [**Status**](/windows/win32/inked/?branch=master)                         | Gets a value that specifies whether the [InkEdit](inkedit-control-reference.md) control is idle, collecting ink, or recognizing ink (run time only).<br/>                                       |
| [**Text**](/windows/win32/inked/?branch=master)                             | Gets or sets the current text in the text box.<br/>                                                                                                                                              |
| [**TextRTF**](/windows/win32/inked/?branch=master)                       | Gets or sets the text of the [InkEdit](inkedit-control-reference.md) control, including all RTF codes.<br/>                                                                                     |
| [**UseMouseForInput**](/windows/win32/inked/?branch=master)     | Gets or sets a value that indicates whether the mouse can be used as an input device.<br/>                                                                                                       |



 

 

 




