---
description: The installer runs the sample's installation wizard sequence only if the full UI level is used to install the application.
ms.assetid: 323d62ae-333b-49fd-96a1-55b228c8ab2c
title: Adding a Control Event at the End of the Installation to Run Launch
ms.topic: article
ms.date: 05/31/2018
---

# Adding a Control Event at the End of the Installation to Run Launch

The installer runs the sample's installation wizard sequence only if the [*full UI*](f-gly.md) level is used to install the application. The last dialog box of the sample dialog sequence is an [Exit Dialog](exit-dialog.md) named ExitDialog. When a user interacts with the OK button on ExitDialog, this first publishes an [EndDialog ControlEvent](enddialog-controlevent.md) that returns control to the installer. The control then publishes a [DoAction ControlEvent](doaction-controlevent.md) that runs the Launch custom action. Each control event requires a record in the [ControlEvent table](controlevent-table.md). See [ControlEvent Overview](controlevent-overview.md).

[ControlEvent Table](controlevent-table.md)



| Dialog     | Control\_ | Event     | Argument | Condition                     | Ordering |
|------------|-----------|-----------|----------|-------------------------------|----------|
| ExitDialog | OK        | EndDialog | Return   | 1                             | 1        |
| ExitDialog | OK        | DoAction  | Launch   | NOT Installed AND $Tutorial=3 | 2        |



 

The condition on the DoAction control ensures the custom action only runs during the first installation of the application and that it is being installed locally. The phrase $Tutorial=3 means the action state of the Tutorial component is set to local. See [Conditional Statement Syntax](conditional-statement-syntax.md).

This completes the sample.

 

 



