---
title: How to Use Rich Edit Clipboard Operations
description: An application can paste the contents of the clipboard into a rich edit control by using either the best available clipboard format or a specific clipboard format.
ms.assetid: 1FEFFD95-839B-4A26-A26E-B8429D5FF4C0
ms.topic: article
ms.date: 05/31/2018
---

# How to Use Rich Edit Clipboard Operations

An application can paste the contents of the clipboard into a rich edit control by using either the best available clipboard format or a specific clipboard format. You can also determine whether a rich edit control is capable of pasting a clipboard format.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Use a Rich Edit Clipboard Operation

As with an edit control, you can copy or cut the contents of the current selection by using the [**WM\_COPY**](/windows/desktop/dataxchg/wm-copy) or [**WM\_CUT**](/windows/desktop/dataxchg/wm-cut) message. Similarly, you can paste the contents of the clipboard into a rich edit control by using the [**WM\_PASTE**](/windows/desktop/dataxchg/wm-paste) message. The control pastes the first available format that it recognizes, which presumably is the most descriptive format.

To paste a specific clipboard format, you can use the [**EM\_PASTESPECIAL**](em-pastespecial.md) message. This message is useful for applications with a **Paste Special** command that enables the user to select the clipboard format. You can use the [**EM\_CANPASTE**](em-canpaste.md) message to determine whether a given format is recognized by the control.

You can also use the [**EM\_CANPASTE**](em-canpaste.md) message to determine whether any available clipboard format is recognized by a rich edit control. This message is useful when processing the [**WM\_INITMENUPOPUP**](/windows/desktop/menurc/wm-initmenupopup) message. An application might enable or gray its **Paste** command depending on whether the control can paste any available format.

Rich edit controls register two clipboard formats:

-   Rich Text Format
-   Rich Text Format Without Objects
-   RichEdit Text and Objects

An application can register these formats by using the [**RegisterClipboardFormat**](/windows/desktop/api/winuser/nf-winuser-registerclipboardformata) function, specifying the CF\_RTF, CF\_RTFNOOBJS, and CF\_RETEXTOBJ values.

## Related topics

<dl> <dt>

[Using Rich Edit Controls](using-rich-edit-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 