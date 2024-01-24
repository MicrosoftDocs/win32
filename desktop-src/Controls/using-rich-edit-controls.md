---
title: Using Rich Edit Controls
description: This section contains topics that demonstrate how to create and use rich edit controls.
ms.assetid: 2c4717c9-3257-42d5-9c36-89b7e524e788
ms.topic: article
ms.date: 05/31/2018
---

# Using Rich Edit Controls

This section contains topics that demonstrate how to create and use rich edit controls.

## In this section




| Topic | Description | 
|-------|-------------|
| <a href="create-rich-edit-controls.md">How to Create Rich Edit Controls</a><br /> | To create a rich edit control, call the <a href="/windows/desktop/api/winuser/nf-winuser-createwindowexa"><strong>CreateWindowEx</strong></a> function, specifying the rich edit window class. For Microsoft Rich Edit 4.1 (Msftedit.dll), specify MSFTEDIT_CLASS as the window class. For all previous versions, specify RICHEDIT_CLASS. For more information, see <a href="about-rich-edit-controls.md">Versions of Rich Edit</a>. <br /> Rich edit controls support most of the window styles used with edit controls as well as additional styles. You should specify the <a href="edit-control-styles.md"><strong>ES_MULTILINE</strong></a> window style if you want to allow more than one line of text in the control. For more information, see <a href="rich-edit-control-styles.md">Rich Edit Control Styles</a>. <br /> | 
| <a href="format-text-in-rich-edit-controls.md">How to Format Text in Rich Edit Controls</a><br /> | An application can send messages to a rich edit control in order to format characters and paragraphs and retrieve formatting information. Paragraph formatting attributes include alignment, tabs, indents, numbering, and simple tables. For characters, you can specify font name, size, color, and effects such as bold, italic, and protected. <br /> | 
| <a href="interact-with-the-current-selection.md">How to Interact with the Current Selection</a><br /> | The user can select text in a rich edit control by using the mouse or the keyboard. The <em>current selection</em> is the range of selected characters, or the position of the insertion point if no characters are selected. An application can get information about the current selection, set it, determine when it changes, and show or hide the selection highlight. <br /> | 
| <a href="use-rich-edit-text-operations.md">How to Use Rich Edit Text Operations</a><br /> | An application can send messages to retrieve or find text in a rich edit control. You can retrieve either the selected text or a specified range of text. <br /> | 
| <a href="use-word-and-line-break-information.md">How to Use Word and Line Break Information</a><br /> | A rich edit control calls a function called a word-break procedure to find breaks between words and to determine where it can break lines. The control uses this information when performing word-wrap operations and when processing CTRL+LEFT ARROW key and CTRL+RIGHT ARROW key combinations. An application can send messages to a rich edit control to replace the default word-break procedure, to retrieve word-break information, and to determine what line a given character falls on. <br /> | 
| <a href="use-rich-edit-clipboard-operations.md">How to Use Rich Edit Clipboard Operations</a><br /> | An application can paste the contents of the clipboard into a rich edit control by using either the best available clipboard format or a specific clipboard format. You can also determine whether a rich edit control is capable of pasting a clipboard format. <br /> | 
| <a href="use-streams.md">How to Use Streams</a><br /> | You can use streams to transfer data into or out of a rich edit control. A stream is defined by an <a href="/windows/desktop/api/Richedit/ns-richedit-editstream"><strong>EDITSTREAM</strong></a> structure, which specifies a buffer and an application-defined callback function. <br /> | 
| <a href="automatically-resize-rich-edit-controls.md">How to Automatically Resize Rich Edit Controls</a><br /> | An application can resize a rich edit control as needed so that it is always the same size as its contents. A rich edit control supports this so-called <em>bottomless</em> functionality by sending its parent window an <a href="en-requestresize.md">EN_REQUESTRESIZE</a> notification code whenever the size of the control's content changes. <br /> | 
| <a href="use-rich-edit-control-notification-codes.md">How to Use Rich Edit Control Notification Codes</a><br /> | A rich edit control's parent window can process notification codes to monitor events that affect the control. Rich edit controls support all of the notification codes that are used with edit controls, as well as several additional ones. <br /> | 
| <a href="use-font-binding-in-rich-edit-controls.md">How to Use Font Binding in Rich Edit Controls</a><br /> | Microsoft Rich Edit 3.0 assigns a character set to plain-text characters depending on their context. Some examples are: <br /><ul><li>Greek characters are assigned <strong>GREEK_CHARSET</strong>.</li><li>Hangul symbols are assigned <strong>HANGUL_CHARSET</strong>.</li><li>Chinese characters are assigned <strong>SHIFTJIS_CHARSET</strong> if kana characters are found nearby, or <strong>GB2312_CHARSET</strong> if no kana are found nearby.</li><li>Non-neutral ANSI characters are assigned <strong>ANSI_CHARSET</strong> in any event.</li></ul> | 
| <a href="using-rich-edit-com.md">How to Use OLE in Rich Edit Controls</a><br /> | This section contains information about using object linking and embedding (OLE) in rich edit controls. <br /> | 
| <a href="printing-rich-edit-controls.md">How to Print the Contents of Rich Edit Controls</a><br /> | This section contains information about how to print the contents of rich edit controls. <br /> | 




 

 

