---
description: This section contains Properties belonging to the InkEdit Control.
ms.assetid: 6aa476b3-97ad-4289-836b-f46fe4d04280
title: InkEdit Properties
ms.topic: article
ms.date: 05/31/2018
---

# InkEdit Properties

This section contains Properties belonging to the InkEdit Control.



| Property                                                 | Description                                                                                                                                                                                            |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Appearance**](/windows/desktop/api/inked/nf-inked-iinkedit-get_appearance)                 | Gets or sets a value that determines whether the [InkEdit](inkedit-control-reference.md) control appears flat or 3-D.<br/>                                                                      |
| [**BackColor**](/windows/desktop/api/inked/nf-inked-iinkedit-get_backcolor)                   | Gets or sets the background color for the [InkEdit](inkedit-control-reference.md) control.<br/>                                                                                                 |
| [**BorderStyle**](/windows/desktop/api/inked/nf-inked-iinkedit-get_borderstyle)               | Gets or sets a value that determines whether the [InkEdit](inkedit-control-reference.md) control has a border.<br/>                                                                             |
| [**DisableNoScroll**](/windows/desktop/api/inked/nf-inked-iinkedit-get_disablenoscroll)       | Gets or sets a value that determines whether scroll bars in the [InkEdit](inkedit-control-reference.md) control are disabled.<br/>                                                              |
| [**DrawingAttributes**](/windows/desktop/api/inked/nf-inked-iinkedit-get_drawingattributes)   | Gets or sets the drawing attributes for ink that is yet to be drawn on the [InkEdit](inkedit-control-reference.md) control.<br/>                                                                |
| [**Enabled**](/windows/desktop/api/inked/nf-inked-iinkedit-get_enabled)                       | Gets or sets a value that determines whether the [InkEdit](inkedit-control-reference.md) control can respond to user-generated events.<br/>                                                     |
| [**Factoid**](/windows/desktop/api/inked/nf-inked-iinkedit-get_factoid)                       | Gets or sets the [Factoid](factoid-constants.md) constant that a [**IInkRecognizer**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognizer) object uses to constrain its search for the recognition result.<br/>                  |
| [**Font**](/windows/desktop/api/inked/nf-inked-iinkedit-get_font)                             | Gets or sets the font of the text that the [InkEdit](inkedit-control-reference.md) control displays.<br/>                                                                                       |
| [**hWnd**](/windows/desktop/api/inked/nf-inked-iinkedit-get_hwnd)                             | Gets the window handle to which the [**InkDisp**](inkdisp-class.md) control is bound.<br/>                                                                                                      |
| [**InkInsertMode**](/windows/desktop/api/inked/nf-inked-iinkedit-get_inkinsertmode)           | Gets or sets a value that specifies how ink is inserted onto the [InkEdit](inkedit-control-reference.md) control, either as text or as ink.<br/>                                                |
| [**InkMode**](/windows/desktop/api/inked/nf-inked-iinkedit-get_inkmode)                       | Gets or sets a value that specifies whether ink collection is disabled, ink is collected, or ink and gestures are collected.<br/>                                                                |
| [**Locked**](/windows/desktop/api/inked/nf-inked-iinkedit-get_locked)                         | Gets or sets a value that specifies whether the [InkEdit](inkedit-control-reference.md) control is read-only or not.<br/>                                                                       |
| [**MaxLength**](/windows/desktop/api/inked/nf-inked-iinkedit-get_maxlength)                   | Gets or sets a value indicating whether an [InkEdit](inkedit-control-reference.md) control can hold a maximum number of characters and, if so, specifies the maximum number of characters.<br/> |
| [**MouseIcon**](/windows/desktop/api/inked/nf-inked-iinkedit-get_mouseicon)                   | Gets or sets the current custom mouse icon.<br/>                                                                                                                                                 |
| [**MousePointer**](/windows/desktop/api/inked/nf-inked-iinkedit-get_mousepointer)             | Gets or sets a value that indicates the type of mouse pointer that appears when the mouse is over a particular part of the [InkEdit](inkedit-control-reference.md) control.<br/>                |
| [**MultiLine**](/windows/desktop/api/inked/nf-inked-iinkedit-get_multiline)                   | Gets or sets a value that indicates whether this is a multiline [InkEdit](inkedit-control-reference.md) control.<br/>                                                                           |
| [**RecognitionTimeout**](/windows/desktop/api/inked/nf-inked-iinkedit-get_recognitiontimeout)        | Gets or sets the length of time, in milliseconds, between the last [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) object collected and the beginning of text recognition.<br/>                         |
| [**Recognizer**](/windows/desktop/api/inked/nf-inked-iinkedit-get_recognizer)                 | Gets or sets the [**IInkRecognizer**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognizer) object to use for recognition.<br/>                                                                                                    |
| [**ScrollBars**](/windows/desktop/api/inked/nf-inked-iinkedit-get_scrollbars)                 | Gets or sets the type of scroll bars that appear in the [InkEdit](inkedit-control-reference.md) control.<br/>                                                                                   |
| [**SelAlignment**](/windows/desktop/api/inked/nf-inked-iinkedit-get_selalignment)             | Gets or sets the alignment to apply to the current selection or insertion point (run time only).<br/>                                                                                            |
| [**SelBold**](/windows/desktop/api/inked/nf-inked-iinkedit-get_selbold)                       | Gets or sets a value that specifies whether the font style of the currently selected text in the [InkEdit](inkedit-control-reference.md) control is bold (run time only).<br/>                  |
| [**SelCharOffset**](/windows/desktop/api/inked/nf-inked-iinkedit-get_selcharoffset)           | Gets or sets whether text in the [InkEdit](inkedit-control-reference.md) control appears on the baseline, as a superscript, or as a subscript (run time only).<br/>                             |
| [**SelColor**](/windows/desktop/api/inked/nf-inked-iinkedit-get_selcolor)                     | Gets or sets the text color of the current text selection or insertion point (run time only).<br/>                                                                                               |
| [**SelFontName**](/windows/desktop/api/inked/nf-inked-iinkedit-get_selfontname)               | Gets or sets the font name of the selected text within the [InkEdit](inkedit-control-reference.md) control (run time only).<br/>                                                                |
| [**SelFontSize**](/windows/desktop/api/inked/nf-inked-iinkedit-get_selfontsize)               | Gets or sets the font size of the selected text within the [InkEdit](inkedit-control-reference.md) control (run time only).<br/>                                                                |
| [**SelInks**](/windows/desktop/api/inked/nf-inked-iinkedit-get_selinks)                       | Gets or sets the array of embedded [**InkDisp**](inkdisp-class.md) objects (if displayed as ink) that the current selection contains.<br/>                                                      |
| [**SelInksDisplayMode**](/windows/desktop/api/inked/nf-inked-iinkedit-get_selinksdisplaymode) | Gets or sets a value that allows toggling the appearance of the selection between ink and text.<br/>                                                                                             |
| [**SelItalic**](/windows/desktop/api/inked/nf-inked-iinkedit-get_selitalic)                   | Gets or sets a value that specifies whether the font style of the currently selected text in the [InkEdit](inkedit-control-reference.md) control is italic (run time only).<br/>                |
| [**SelLength**](/windows/desktop/api/inked/nf-inked-iinkedit-get_sellength)                   | Gets or sets the number of characters that are selected in the [InkEdit](inkedit-control-reference.md) control (run time only).<br/>                                                            |
| [**SelRTF**](/windows/desktop/api/inked/nf-inked-iinkedit-get_selrtf)                         | Gets or sets the currently selected Rich Text Format (RTF) formatted text in the [InkEdit](inkedit-control-reference.md) control (run time only).<br/>                                          |
| [**SelStart**](/windows/desktop/api/inked/nf-inked-iinkedit-get_selstart)                     | Gets or sets the starting point of the text that is selected in the text box (run time only).<br/>                                                                                               |
| [**SelText**](/windows/desktop/api/inked/nf-inked-iinkedit-get_seltext)                       | Gets or sets the selected text within the [InkEdit](inkedit-control-reference.md) control (run time only).<br/>                                                                                 |
| [**SelUnderline**](/windows/desktop/api/inked/nf-inked-iinkedit-get_selunderline)             | Gets or sets a value that specifies whether the font style of the currently selected text in the [InkEdit](inkedit-control-reference.md) control is underlined (run time only).<br/>            |
| [**Status**](/windows/desktop/api/inked/nf-inked-iinkedit-get_status)                         | Gets a value that specifies whether the [InkEdit](inkedit-control-reference.md) control is idle, collecting ink, or recognizing ink (run time only).<br/>                                       |
| [**Text**](/windows/desktop/api/inked/nf-inked-iinkedit-get_text)                             | Gets or sets the current text in the text box.<br/>                                                                                                                                              |
| [**TextRTF**](/windows/desktop/api/inked/nf-inked-iinkedit-get_textrtf)                       | Gets or sets the text of the [InkEdit](inkedit-control-reference.md) control, including all RTF codes.<br/>                                                                                     |
| [**UseMouseForInput**](/windows/desktop/api/inked/nf-inked-iinkedit-get_usemouseforinput)     | Gets or sets a value that indicates whether the mouse can be used as an input device.<br/>                                                                                                       |



 

 

 




