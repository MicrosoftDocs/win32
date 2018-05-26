---
title: How to Automatically Resize Rich Edit Controls
description: An application can resize a rich edit control as needed so that it is always the same size as its contents.
ms.assetid: CCAFC039-AC9E-4BC4-ABE1-8C56FA9DD3F5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

When processing the [EN\_REQUESTRESIZE](en-requestresize.md) notification code, an application should resize the control to the dimensions in the specified [**REQRESIZE**](/windows/win32/Richedit/ns-richedit-_reqresize?branch=master) structure. An application might also move any information that is near the control to accommodate the control's change in height. To resize the control, you can use the [**SetWindowPos**](https://msdn.microsoft.com/library/windows/desktop/ms633545) function.

You can force a bottomless rich edit control to send an [EN\_REQUESTRESIZE](en-requestresize.md) notification code by using the [**EM\_REQUESTRESIZE**](em-requestresize.md) message. This message can be useful when processing the [**WM\_SIZE**](https://msdn.microsoft.com/library/windows/desktop/ms632646) message.

## Remarks

To receive [EN\_REQUESTRESIZE](en-requestresize.md) notification codes, you must enable the notification by using the [EM\_SETEVENTMASK](em-seteventmask.md) message.

## Related topics

<dl> <dt>

[Using Rich Edit Controls](using-rich-edit-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](http://go.microsoft.com/fwlink/p/?linkid=214295)
</dt> </dl>

 

 




