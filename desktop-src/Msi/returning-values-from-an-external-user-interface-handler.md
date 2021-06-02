---
description: An external user interface (UI) handler can return any number of values to Windows Installer depending on the button type provided in the message type parameter the installer passes to the handler.
ms.assetid: a918082d-709d-4b4f-ae3b-5f16ed0ca910
title: Returning Values from an External User Interface Handler
ms.topic: article
ms.date: 05/31/2018
---

# Returning Values from an External User Interface Handler

An external user interface (UI) handler can return any number of values to Windows Installer depending on the button type provided in the message type parameter the installer passes to the handler.

The external UI handler can return the values –1 and 0 at any time because these are not related to the button types. A return value of –1 indicates that an internal error occurred in the external UI handler. A return value of 0 indicates that the external UI handler has not handled the installer message and the installer must handle the message instead.

For messages that do not include a button type, such as INSTALLMESSAGE\_ACTIONDATA and INSTALLMESSAGE\_PROGRESS, returning IDCANCEL cancels the installation. Returning IDOK notifies the installer that the message was handled by the external UI handler.

The remaining return values, as described below, are directly related to the button types that are included with the message type.



| External UI return value | Meaning                                                                                                |
|--------------------------|--------------------------------------------------------------------------------------------------------|
| IDOK                     | The **OK** button was pressed by the user. The message information was understood.                     |
| IDCANCEL                 | The **CANCEL** button was pressed. Cancel the installation.                                            |
| IDABORT                  | The **ABORT** button was pressed. Abort the installation.                                              |
| IDRETRY                  | The **RETRY** button was pressed. Try the action again.                                                |
| IDIGNORE                 | The **IGNORE** button was pressed. Ignore the error and continue.                                      |
| IDYES                    | The **YES** button was pressed. The affirmative response, continue with current sequence of events..   |
| IDNO                     | The **NO** button was pressed. The negative response, do not continue with current sequence of events. |



 

For example, if the external UI handler is sent a message with the MB\_ABORTRETRYIGNORE message box styles flag, the external UI handler can return one of the following values:

-   –1 (error in external UI handler)
-   0 (no action taken in external UI handler, let Windows Installer handle it)
-   IDABORT (**ABORT** button pressed)
-   IDRETRY (**RETRY** button pressed)
-   IDIGNORE (**IGNORE** button pressed)

 

 



