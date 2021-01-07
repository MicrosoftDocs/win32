---
description: An installer function may display an error message dialog box returning any of the following errors. An error box is displayed only if the user interface level is at the full, reduced, or basic level. For more information, see User Interface Levels.
ms.assetid: 0153a21f-9b26-4088-b12b-96c9e6918cc3
title: Displayed Error Messages
ms.topic: article
ms.date: 05/31/2018
---

# Displayed Error Messages

An [installer function](installer-function-reference.md) may display an error message dialog box returning any of the following errors. An error box is displayed only if the user interface level is at the full, reduced, or basic level. For more information, see [User Interface Levels](user-interface-levels.md).

The installer functions only display error messages that are in the following table. For errors not in this list, the caller of the function is responsible for handling the display of error messages.



| Error code               | Error                        |
|--------------------------|------------------------------|
| ERROR\_INSTALL\_SUSPEND  | The install was suspended.   |
| ERROR\_INSTALL\_USEREXIT | The user exited the install. |
| ERROR\_INSTALL\_FAILURE  | Install failed.              |



 

 

 



