---
description: A Cancel dialog box confirms that the user wants to terminate the installation. This is a modal dialog box.
ms.assetid: 5dab4315-721e-417d-91e0-b38653a65c23
title: Cancel Dialog
ms.topic: article
ms.date: 05/31/2018
---

# Cancel Dialog

A **Cancel** dialog box confirms that the user wants to terminate the installation. This is a modal dialog box.

This type of dialog box commonly contains a [Text control](text-control.md) and two [PushButtons](pushbutton-control.md). The two buttons give the user the choice of either returning to the last dialog box or confirming the termination of the installation.

The [EndDialog](enddialog-controlevent.md) ControlEvent is linked to these two buttons in the [ControlEvent table](controlevent-table.md). The *Return* parameter of the EndDialog ControlEvent is linked to one of the buttons and causes the **Cancel** dialog box to be terminated and the focus to return to the previous dialog box. The *Exit* parameter is linked to the other button and causes the user interface to return control to the installer with the appropriate code indicating that the user wants to exit. The installer then shuts down and displays the [UserExit Dialog](userexit-dialog.md).

 

 



