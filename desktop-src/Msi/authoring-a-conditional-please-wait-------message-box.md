---
description: The following example illustrates how to author a conditional message box that pops up and warns the user that a background task is still running whenever the user activates a displayed control prematurely.
ms.assetid: 4a99a96b-50c2-42eb-82ad-acdfa186a71f
title: Authoring a "Please Wait . . ." Message Box
ms.topic: article
ms.date: 05/31/2018
---

# Authoring a Conditional "Please Wait..." Message Box

The following example illustrates how to author a conditional message box that pops up and warns the user that a background task is still running whenever the user activates a displayed control prematurely.

The example also illustrates how the [SpawnWaitDialog ControlEvent](spawnwaitdialog-controlevent.md) can generally be used to protect a control that triggers an action dependent upon the completion of a background task.

In this example, a [Selection Dialog](selection-dialog.md) containing three push button controls labeled **Install Now**, **Next**, and **Disk Cost** is displayed to the user during the installation process. However, the installer also carries out a disk space costing task in the background while displaying this dialog box. The author wishes to protect these buttons from activation and wants a "Please wait" message box to pop up if the user clicks any of the buttons before the costing has completed. The author also wants this message box to contain a **Cancel** button and to disappear as soon as the background task is finished.

**To display a dialog box asking the user to wait while background disk costing is completed**

1.  Use the authoring capabilities of the installer to add a new modal dialog box, named **WaitForCosting**, into the [Dialog table](dialog-table.md). The dialog box should display a text string that says "Please wait while disk space costing is completed."
2.  Add a single push button control to this dialog box, labeled **Cancel**, by authoring it into the [Control table](control-table.md).
3.  Link the **Cancel** push button to a ControlEvent that closes the **WaitForCosting** dialog box by authoring an [EndDialog ControlEvent](enddialog-controlevent.md) into the [ControlEvent table](controlevent-table.md). Set the argument of the EndDialog Control event to be Exit.
4.  Link a [SpawnWaitDialog ControlEvent](spawnwaitdialog-controlevent.md) to the existing **Install Now**, **Next**, and **Disk Cost** push button controls displayed in the [Selection Dialog](selection-dialog.md) box. Set the argument of this ControlEvent in the ControlEvent table to be the **WaitForCosting** dialog box and set the expression in the Condition column of the table to be: [**CostingComplete**](costingcomplete.md) =1.

 

 



