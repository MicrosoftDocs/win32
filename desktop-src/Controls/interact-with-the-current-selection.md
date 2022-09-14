---
title: How to Interact with the Current Selection
description: The user can select text in a rich edit control by using the mouse or the keyboard.
ms.assetid: A529792C-DFA7-4BE1-8607-5A1556B64626
ms.topic: article
ms.date: 05/31/2018
---

# How to Interact with the Current Selection

The user can select text in a rich edit control by using the mouse or the keyboard. The *current selection* is the range of selected characters, or the position of the insertion point if no characters are selected. An application can get information about the current selection, set it, determine when it changes, and show or hide the selection highlight.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Interact with the Current Selection

To determine the current selection in a rich edit control, use the [**EM\_EXGETSEL**](em-exgetsel.md) message. To set the current selection, use the [**EM\_EXSETSEL**](em-exsetsel.md) message. The [**CHARRANGE**](/windows/desktop/api/Richedit/ns-richedit-charrange) structure is used with both messages and specifies a range of characters. To retrieve information about the contents of the current selection, you can use the [**EM\_SELECTIONTYPE**](em-selectiontype.md) message.

An application can detect when the current selection changes by processing the [EN\_SELCHANGE](en-selchange.md) notification code. The notification code specifies a [**SELCHANGE**](/windows/desktop/api/Richedit/ns-richedit-selchange) structure that contains information about the new selection. A rich edit control sends this notification code only if you enable it by using the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.

By default, a rich edit control shows and hides the selection highlight when it gains and loses the focus. You can show or hide the selection highlight at any time by using the [**EM\_HIDESELECTION**](em-hideselection.md) message. For example, an application might provide a Search dialog box to find text in a rich edit control. The application might select matching text without closing the dialog box, in which case it must use the **EM\_HIDESELECTION** message to highlight the selection.

As with edit controls, you can specify the [**ES\_NOHIDESEL**](edit-control-styles.md) window style to prevent a rich edit control from hiding the selection highlight when it loses the focus.

As an alternative to using the [**EM\_EXGETSEL**](em-exgetsel.md) and [**EM\_EXSETSEL**](em-exsetsel.md) messages, you can retrieve and set the current selection by using the [**EM\_GETSEL**](em-getsel.md) and [**EM\_SETSEL**](em-setsel.md) edit control messages. The **EM\_GETSEL** message packs two 16-bit character indexes into its 32-bit return value and therefore, works only for selections that fall entirely within the first 64K. However, a rich edit control will never contain more than 32K characters of text, unless you extend this limit by using the [**EM\_LIMITTEXT**](em-limittext.md) or [**EM\_EXLIMITTEXT**](em-exlimittext.md) message. For selections that extend beyond the first 64 KB of text, the **EM\_GETSEL** message returns –1. In such a case you can still use the values that are returned in *wParam* and *lParam* to find the start and end characters of the selection.

## Related topics

<dl> <dt>

[Using Rich Edit Controls](using-rich-edit-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 




