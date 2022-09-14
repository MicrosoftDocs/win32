---
title: How to Use Rich Edit Control Notification Codes
description: A rich edit control's parent window can process notification codes to monitor events that affect the control. Rich edit controls support all of the notification codes that are used with edit controls, as well as several additional ones.
ms.assetid: E045EADE-CB37-492A-85EC-6CF236677F08
ms.topic: article
ms.date: 05/31/2018
---

# How to Use Rich Edit Control Notification Codes

A rich edit control's parent window can process notification codes to monitor events that affect the control. Rich edit controls support all of the notification codes that are used with edit controls, as well as several additional ones.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Use a Rich Edit Control Notification Code

You can determine which notification codes a rich edit control sends its parent window by setting its event mask. To set the event mask for a rich edit control, use the [**EM\_SETEVENTMASK**](em-seteventmask.md) message. You can retrieve the current event mask for a rich edit control by using the [**EM\_GETEVENTMASK**](em-geteventmask.md) message. For a list of event mask flags, see [Rich Edit Control Event Mask Flags](rich-edit-control-event-mask-flags.md).

A rich edit control's parent window can filter all keyboard and mouse input to the control by processing the [EN\_MSGFILTER](en-msgfilter.md) notification code. The parent window can prevent the keyboard or mouse message from being processed or can change the message by modifying the specified [**MSGFILTER**](/windows/desktop/api/Richedit/ns-richedit-msgfilter) structure.

An application can process the [EN\_PROTECTED](en-protected.md) notification code to detect when the user attempts to modify protected text. To mark a range of text as protected, you can set the protected character effect.

You can enable the user to drop files in a rich edit control by processing the [EN\_DROPFILES](en-dropfiles.md) notification code. The specified [**ENDROPFILES**](/windows/desktop/api/Richedit/ns-richedit-endropfiles) structure contains information about the files that are being dropped.

## Related topics

<dl> <dt>

[Using Rich Edit Controls](using-rich-edit-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 




