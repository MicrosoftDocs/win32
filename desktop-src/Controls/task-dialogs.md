---
title: Task Dialog
description: This section contains information about the programming elements used with a task dialog. A task dialog is similar to, while much more flexible than, a basic message box.
ms.assetid: 'vs|controls|~\controls\taskdialogs\taskdialogs.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Task Dialog

This section contains information about the programming elements used with a task dialog. A *task dialog* is similar to, while much more flexible than, a basic message box.

### Overviews



| Topic                                           | Contents                                            |
|-------------------------------------------------|-----------------------------------------------------|
| [About Task Dialogs](task-dialogs-overview.md) | Describes the elements of a task dialog.<br/> |



 

### Functions



| Topic                                                  | Contents                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TaskDialog**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialog)                       | Creates, displays, and operates a task dialog. The task dialog contains application-defined message text and title, icons, and any combination of predefined push buttons. This function does not support the registration of a callback function to receive notifications.<br/>                                                                                                                |
| [*TaskDialogCallbackProc*](/windows/win32/api/commctrl/nc-commctrl-pftaskdialogcallback) | An application-defined function used with the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) function. It receives messages from the task dialog when various events occur.<br/> The **PFTASKDIALOGCALLBACK** type defines a pointer to this callback function. [*TaskDialogCallbackProc*](/windows/win32/api/commctrl/nc-commctrl-pftaskdialogcallback) is a placeholder for the application defined function name.<br/> |
| [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect)       | Creates, displays, and operates a task dialog. The task dialog contains application-defined icons, messages, title, verification check box, command links, push buttons, and radio buttons. This function can register a callback function to receive notification messages.<br/>                                                                                                               |



 

### Messages



| Topic                                                                                           | Contents                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TDM\_CLICK\_BUTTON**](tdm-click-button.md)                                                  | Simulates the action of a button click in a task dialog.<br/>                                                                                                                                  |
| [**TDM\_CLICK\_RADIO\_BUTTON**](tdm-click-radio-button.md)                                     | Simulates the action of a radio button click in a task dialog.<br/>                                                                                                                            |
| [**TDM\_CLICK\_VERIFICATION**](tdm-click-verification.md)                                      | Simulates the action of a verification checkbox click in a task dialog.<br/>                                                                                                                   |
| [**TDM\_ENABLE\_BUTTON**](tdm-enable-button.md)                                                | Enables or disables a push button in a task dialog.<br/>                                                                                                                                       |
| [**TDM\_ENABLE\_RADIO\_BUTTON**](tdm-enable-radio-button.md)                                   | Enables or disables a radio button in a task dialog.<br/>                                                                                                                                      |
| [**TDM\_NAVIGATE\_PAGE**](tdm-navigate-page.md)                                                | Recreates a task dialog with new contents, simulating the functionality of a multi-page wizard.<br/>                                                                                           |
| [**TDM\_SET\_BUTTON\_ELEVATION\_REQUIRED\_STATE**](tdm-set-button-elevation-required-state.md) | Specifies whether a given task dialog button or command link should have a User Account Control (UAC) shield icon; that is, whether the action invoked by the button requires elevation. <br/> |
| [**TDM\_SET\_ELEMENT\_TEXT**](tdm-set-element-text.md)                                         | Updates a text element in a task dialog.<br/>                                                                                                                                                  |
| [**TDM\_SET\_MARQUEE\_PROGRESS\_BAR**](tdm-set-marquee-progress-bar.md)                        | Indicates whether the hosted progress bar should be displayed in marquee mode.<br/>                                                                                                            |
| [**TDM\_SET\_PROGRESS\_BAR\_MARQUEE**](tdm-set-progress-bar-marquee.md)                        | Starts and stops the marquee display of the progress bar, and sets the speed of the marquee.<br/>                                                                                              |
| [**TDM\_SET\_PROGRESS\_BAR\_POS**](tdm-set-progress-bar-pos.md)                                | Sets the current position for a progress bar.<br/>                                                                                                                                             |
| [**TDM\_SET\_PROGRESS\_BAR\_RANGE**](tdm-set-progress-bar-range.md)                            | Sets the minimum and maximum values for the hosted progress bar.<br/>                                                                                                                          |
| [**TDM\_SET\_PROGRESS\_BAR\_STATE**](tdm-set-progress-bar-state.md)                            | Sets the current state of the progress bar.<br/>                                                                                                                                               |
| [**TDM\_UPDATE\_ELEMENT\_TEXT**](tdm-update-element-text.md)                                   | Updates a text element in a task dialog. <br/>                                                                                                                                                 |
| [**TDM\_UPDATE\_ICON**](tdm-update-icon.md)                                                    | Refreshes the icon of a task dialog. <br/>                                                                                                                                                     |



 

### Notifications



| Topic                                                           | Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [TDN\_BUTTON\_CLICKED](tdn-button-clicked.md)                  | Sent by a task dialog when the user selects a button or command link in the task dialog. This notification code is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method.<br/>                                                                                                                                                                                                   |
| [TDN\_CREATED](tdn-created.md)                                 | Sent by a task dialog after the task dialog has been created and before it is displayed. This notification code is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method. <br/>                                                                                                                                                                                                  |
| [TDN\_DESTROYED](tdn-destroyed.md)                             | Sent by a task dialog when it is destroyed and its window handle is no longer valid. This notification code is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method.<br/>                                                                                                                                                                                                       |
| [TDN\_DIALOG\_CONSTRUCTED](tdn-dialog-constructed.md)          | Sent by a task dialog after the task dialog has been created and before it is displayed. This notification code is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method. <br/>                                                                                                                                                                                                  |
| [TDN\_EXPANDO\_BUTTON\_CLICKED](tdn-expando-button-clicked.md) | Sent by a task dialog when the user clicks on the task dialog's expando button. This notification code is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method.<br/>                                                                                                                                                                                                            |
| [TDN\_HELP](tdn-help.md)                                       | Sent by a task dialog when the user presses F1 on the keyboard while the task dialog has focus. This notification code is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method.<br/>                                                                                                                                                                                            |
| [TDN\_HYPERLINK\_CLICKED](tdn-hyperlink-clicked.md)            | Sent by a task dialog when the user clicks a hyperlink in the task dialog content. This notification code is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method. <br/>                                                                                                                                                                                                        |
| [TDN\_NAVIGATED](tdn-navigated.md)                             | Sent by a task dialog when a navigation has occurred. This notification code is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method. <br/>                                                                                                                                                                                                                                     |
| [TDN\_RADIO\_BUTTON\_CLICKED](tdn-radio-button-clicked.md)     | Sent by a task dialog when the user selects a button or command link in the task dialog. This notification code is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method. <br/>                                                                                                                                                                                                  |
| [TDN\_TIMER](tdn-timer.md)                                     | Sent by a task dialog approximately every 200 milliseconds. This notification code is sent when the TDF\_CALLBACK\_TIMER flag has been set in the **dwFlags** member of the [**TASKDIALOGCONFIG**](/windows/desktop/api/Commctrl/ns-commctrl-taskdialogconfig) structure that was passed to the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) function. This notification code is received only through the task dialog callback function, which can be registered using the **TaskDialogIndirect** method.<br/> |
| [TDN\_VERIFICATION\_CLICKED](tdn-verification-clicked.md)      | Sent by the task dialog when the user clicks the task dialog verification check box. This notification code is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method.<br/>                                                                                                                                                                                                       |



 

### Structures



| Topic                                           | Contents                                                                                                                                                   |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TASKDIALOG\_BUTTON**](/windows/desktop/api/Commctrl/ns-commctrl-taskdialog_button) | Contains information used to display a button in a task dialog. The [**TASKDIALOGCONFIG**](/windows/desktop/api/Commctrl/ns-commctrl-taskdialogconfig) structure uses this structure.<br/> |
| [**TASKDIALOGCONFIG**](/windows/desktop/api/Commctrl/ns-commctrl-taskdialogconfig)    | Contains information used to display a task dialog. The [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) function uses this structure.<br/>          |



 

 

