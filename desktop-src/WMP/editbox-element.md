---
title: EDITBOX Element
description: EDITBOX Element
ms.assetid: 9ad4abab-e448-4fcf-9451-2476a603e401
keywords:
- Windows Media Player skins,EDITBOX element
- skins,EDITBOX element
- EDITBOX element
- reference for skins,EDITBOX element
- elements,EDITBOX
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EDITBOX Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **EDITBOX** element provides a way for users to enter text within a skin.

The **EDITBOX** element supports the following attributes.



| Attribute                                      | Description                                                                                                   |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [backgroundColor](editbox-backgroundcolor.md) | Specifies or retrieves the background color for the edit box control.                                         |
| [border](editbox-border.md)                   | Specifies or retrieves a value indicating whether the edit box control has a border.                          |
| [editStyle](editbox-editstyle.md)             | Specifies or retrieves the style of the edit box control.                                                     |
| [fontFace](editbox-fontface.md)               | Specifies or retrieves the font used for text in the edit box control.                                        |
| [fontSize](editbox-fontsize.md)               | Specifies or retrieves the font size for the edit box control.                                                |
| [fontStyle](editbox-fontstyle.md)             | Specifies or retrieves the font style for the edit box control.                                               |
| [foregroundColor](editbox-foregroundcolor.md) | Specifies or retrieves the text color in the edit box control.                                                |
| [justification](editbox-justification.md)     | Specifies or retrieves the alignment of the text within the edit box control.                                 |
| [lineCount](editbox-linecount.md)             | Retrieves the number of lines in the edit box control.                                                        |
| [readOnly](editbox-readonly.md)               | Specifies or retrieves a value indicating whether text in the edit box control is read-only or can be edited. |
| [textLimit](editbox-textlimit.md)             | Specifies or retrieves the maximum number of characters that the user can type in the edit box control.       |
| [value](editbox-value.md)                     | Specifies or retrieves the text that is displayed in the edit box control.                                    |
| [wordWrap](editbox-wordwrap.md)               | Specifies or retrieves a value indicating whether word wrap is enabled in the edit box control.               |



 

The **EDITBOX** element supports the following methods.



| Method                                             | Description                                                                                         |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [getLine](editbox-getline.md)                     | Retrieves the text for the line with the specified index.                                           |
| [getLineFromChar](editbox-getlinefromchar.md)     | Retrieves the line index for the specified character index.                                         |
| [getLineIndex](editbox-getlineindex.md)           | Retrieves the character index for the specified line index.                                         |
| [getSelectionEnd](editbox-getselectionend.md)     | Retrieves the ending position of the selected text in the edit box control.                         |
| [getSelectionStart](editbox-getselectionstart.md) | Retrieves the starting position of the selected text in the edit box control.                       |
| [replaceSelection](editbox-replaceselection.md)   | Replaces the current selection with the specified text.                                             |
| [setSelection](editbox-setselection.md)           | Selects the text in the edit box control from the specified start index to the specified end index. |



 

The **EDITBOX** element supports the ambient attributes and can implement all ambient event handlers with the exception of **onclick**. For more information, see [Ambient Attributes](ambient-attributes.md) and [Ambient Event Handlers](ambient-event-handlers.md).

> [!Note]  
> This element requires Windows Media Player for Windows XP or later.

 

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




