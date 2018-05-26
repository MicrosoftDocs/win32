---
title: How to Create Task Dialogs
description: A task dialog is created and shown by using either the TaskDialog function or the TaskDialogIndirect function.
ms.assetid: CCEFF52F-D501-4145-9799-0A9C529017E1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to Create Task Dialogs

A task dialog is created and shown by using either the [**TaskDialog**](/windows/win32/Commctrl/nf-commctrl-taskdialog?branch=master) function or the [**TaskDialogIndirect**](/windows/win32/Commctrl/nf-commctrl-taskdialogindirect?branch=master) function.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### TaskDialog

The **TaskDialog** function is suitable for simple dialog boxes that present textual information and ask for a standard choice. This creation function does not support progress bars, check boxes, footers, expand/collapse buttons, custom buttons, or radio buttons.

### TaskDialogIndirect

The **TaskDialogIndirect** function is more powerful, supporting all available interface elements and also enabling you to capture events in a callback procedure so that your application can update a progress bar or respond to a click of a hyperlink or button.

## Related topics

<dl> <dt>

[Using Task Dialogs](using-task-dialogs.md)
</dt> </dl>

 

 




