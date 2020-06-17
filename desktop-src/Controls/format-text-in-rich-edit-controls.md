---
title: How to Format Text in Rich Edit Controls
description: An application can send messages to a rich edit control in order to format characters and paragraphs and retrieve formatting information.
ms.assetid: 19A4F0D1-88C5-407D-A70F-CB486DAD352E
ms.topic: article
ms.date: 05/31/2018
---

# How to Format Text in Rich Edit Controls

An application can send messages to a rich edit control in order to format characters and paragraphs and retrieve formatting information. Paragraph formatting attributes include alignment, tabs, indents, numbering, and simple tables. For characters, you can specify font name, size, color, and effects such as bold, italic, and protected.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Format Text in a Rich Edit Control

You can apply paragraph formatting by using the [**EM\_SETPARAFORMAT**](em-setparaformat.md) message. To determine the current paragraph formatting for the selected text, use the [**EM\_GETPARAFORMAT**](em-getparaformat.md) message. The [**PARAFORMAT**](/windows/desktop/api/Richedit/ns-richedit-paraformat) or [**PARAFORMAT2**](/windows/desktop/api/Richedit/ns-richedit-paraformat2) structure is used with both messages to specify paragraph formatting attributes.

You can apply character formatting by using the [**EM\_SETCHARFORMAT**](em-setcharformat.md) message. To determine the current character formatting for the selected text, you can use the [**EM\_GETCHARFORMAT**](em-getcharformat.md) message. The [**CHARFORMAT**](/windows/win32/api/richedit/ns-richedit-charformata) or [**CHARFORMAT2**](/windows/desktop/api/Richedit/ns-richedit-charformat2a) structure is used with both messages to specify character attributes.

You can also use [**EM\_SETCHARFORMAT**](em-setcharformat.md) and [**EM\_GETCHARFORMAT**](em-getcharformat.md) messages to set and retrieve the character formatting of the insertion point, which is the formatting that is applied to any subsequently inserted characters. For example, if an application sets the default character formatting to bold and the user then types a character, that character is bold.

The character formatting of the insertion point is applied to newly inserted text only if the current selection is empty (if the current selection is an insertion point). Otherwise, the new text assumes the character formatting of the text it replaces. If the selection changes, the default character formatting changes to match the first character in the new selection.

The protected character effect is unique in that it does not change the appearance of text. If the user attempts to modify protected text, a rich edit control sends its parent window an [EN\_PROTECTED](en-protected.md) notification code, allowing the parent window to allow or prevent the change. To receive this notification code, you must enable it by using the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.

Foreground color is always a character attribute. In Microsoft Rich Edit 1.0, background color is only a property of the rich edit control. To set the default background color, use the [**EM\_SETBKGNDCOLOR**](em-setbkgndcolor.md) message. Note that Rich Edit does not support the [**WM\_CTLCOLOREDIT**](wm-ctlcoloredit.md) message.

## Related topics

<dl> <dt>

[Using Rich Edit Controls](using-rich-edit-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 




