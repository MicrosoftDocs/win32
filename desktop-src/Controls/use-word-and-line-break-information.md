---
title: How to Use Word and Line Break Information
description: A rich edit control calls a function called a word-break procedure to find breaks between words and to determine where it can break lines.
ms.assetid: DDCE9814-0D39-494C-953A-FB6A98100EEA
ms.topic: article
ms.date: 05/31/2018
---

# How to Use Word and Line Break Information

A rich edit control calls a function called a word-break procedure to find breaks between words and to determine where it can break lines. The control uses this information when performing word-wrap operations and when processing CTRL+LEFT ARROW key and CTRL+RIGHT ARROW key combinations. An application can send messages to a rich edit control to replace the default word-break procedure, to retrieve word-break information, and to determine what line a given character falls on.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Use Word and Line Break Information

Word-break procedures for rich edit controls are similar to those for edit controls, but they have additional capabilities: word-break procedures for both kinds of controls can determine whether a character is a delimiter and can find the nearest word break before or after the specified position. A delimiter is a character that marks the end of a word, such as a space. Usually, in an edit control, a word break occurs only after delimiters. However, different rules apply to most Asian languages.

Word-break procedures for rich edit controls also group characters into character classes, each identified by a value in the range 0x00 through 0x0F. Breaks occur either after delimiters or between characters of different classes. Thus, a word-break procedure with different classes for alphanumeric and punctuation characters would find two word breaks in the string "Win.doc" (before and after the period).

A character's class can be combined with zero or more word-break flags to form an 8-bit value. When performing word-wrap operations, a rich edit control uses word-break flags to determine where it can break lines. Rich Edit uses the following word-break flags.



| Flag            | Description                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| WBF\_BREAKAFTER | Lines may be broken after the character.                                                                                          |
| WBF\_BREAKLINE  | The character is a delimiter. Delimiters mark the ends of words. Lines may be broken after delimiters.                            |
| WBF\_ISWHITE    | The character is a white-space character. Trailing white-space characters are not included in the length of a line when wrapping. |



 

The WBF\_BREAKAFTER value is used to allow wrapping after a character that does not mark the end of a word, such as a hyphen.

You can replace the default word-break procedure for a rich edit control with your own procedure by using the [**EM\_SETWORDBREAKPROC**](em-setwordbreakproc.md) message. For more information about word-break procedures, see the description of the [*EditWordBreakProc*](/windows/win32/api/winuser/nc-winuser-editwordbreakproca) function.

> [!Note]  
> This replacement is not recommended for Microsoft Rich Edit 2.0 and later, due to the complexity of multilingual word breaking.

 

For Microsoft Rich Edit 1.0, you can use the [**EM\_SETWORDBREAKPROCEX**](em-setwordbreakprocex.md) message to replace the default extended word-break procedure with an [*EditWordBreakProcEx*](/windows/desktop/api/Richedit/nc-richedit-editwordbreakprocex) function. This function provides additional information about the text, such as the character set. You can use the [**EM\_GETWORDBREAKPROCEX**](em-getwordbreakprocex.md) message to retrieve the address of the current extended word-break procedure. Note that Microsoft Rich Edit 2.0 and later do not support *EditWordBreakProcEx*, **EM\_GETWORDBREAKPROCEX**, and **EM\_SETWORDBREAKPROCEX**.

You can use the [**EM\_FINDWORDBREAK**](em-findwordbreak.md) message to find word breaks or to determine a character's class and word-break flags. In turn, the control calls its word-break procedure to get the requested information.

To determine which line a given character falls on, you can use the [**EM\_EXLINEFROMCHAR**](em-exlinefromchar.md) message.

## Related topics

<dl> <dt>

[Using Rich Edit Controls](using-rich-edit-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 