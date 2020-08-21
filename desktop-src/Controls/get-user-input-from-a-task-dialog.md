---
title: How to Get User Input from a Task Dialog
description: To complete a task, users submit the task details to the application by configuring the controls within the task dialog, and then clicking a command button (usually OK).
ms.assetid: 73CD8FBF-95C9-43C8-B9D8-3823840C23A9
ms.topic: article
ms.date: 05/31/2018
---

# How to Get User Input from a Task Dialog

To complete a task, users submit the task details to the application by configuring the controls within the task dialog, and then clicking a command button (usually **OK**).

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Getting User Input from a Task Dialog

You can identify the button that was clicked by examining the *pnButton* parameter of the calling function. You can also identify the selected radio button from the *pnRadioButton* parameter of [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect), and the state of the verification check box from the *pfVerificationFlagChecked* parameter.

Clicks on buttons and hyperlinks are received by the [*TaskDialogCallbackProc*](/windows/win32/api/commctrl/nc-commctrl-pftaskdialogcallback) function in the form of [TDN\_BUTTON\_CLICKED](tdn-button-clicked.md) and [TDN\_HYPERLINK\_CLICKED](tdn-hyperlink-clicked.md) notifications. If your callback function returns S\_OK after handling a button notification, the task dialog closes and the command identifier of the button is returned in *pnButton*. If you return S\_FALSE, or do not have a callback function, the task dialog remains open.

## Related topics

<dl> <dt>

[Using Task Dialogs](using-task-dialogs.md)
</dt> </dl>

 

 