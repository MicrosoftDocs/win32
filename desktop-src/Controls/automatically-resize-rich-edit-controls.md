---
title: How to Automatically Resize Rich Edit Controls
description: An application can resize a rich edit control as needed so that it is always the same size as its contents.
ms.assetid: CCAFC039-AC9E-4BC4-ABE1-8C56FA9DD3F5
ms.topic: article
ms.date: 05/31/2018
---

# How to Automatically Resize Rich Edit Controls

An application can resize a rich edit control as needed so that it is always the same size as its contents. A rich edit control supports this so-called *bottomless* functionality by sending its parent window an [EN\_REQUESTRESIZE](en-requestresize.md) notification code whenever the size of the control's content changes.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Automatically Resize a Rich Edit Control

When processing the [EN\_REQUESTRESIZE](en-requestresize.md) notification code, an application should resize the control to the dimensions in the specified [**REQRESIZE**](/windows/desktop/api/Richedit/ns-richedit-reqresize) structure. An application might also move any information that is near the control to accommodate the control's change in height. To resize the control, you can use the [**SetWindowPos**](/windows/desktop/api/winuser/nf-winuser-setwindowpos) function.

You can force a bottomless rich edit control to send an [EN\_REQUESTRESIZE](en-requestresize.md) notification code by using the [**EM\_REQUESTRESIZE**](em-requestresize.md) message. This message can be useful when processing the [**WM\_SIZE**](/windows/desktop/winmsg/wm-size) message.

## Remarks

To receive [EN\_REQUESTRESIZE](en-requestresize.md) notification codes, you must enable the notification by using the [EM\_SETEVENTMASK](em-seteventmask.md) message.

## Related topics

<dl> <dt>

[Using Rich Edit Controls](using-rich-edit-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 