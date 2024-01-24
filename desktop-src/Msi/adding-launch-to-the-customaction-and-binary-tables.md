---
description: Add a record to the CustomAction table for the Launch custom action.
ms.assetid: 010ce7cd-010b-4fac-90ad-5745c6a38630
title: Adding Launch to the CustomAction and Binary Tables
ms.topic: article
ms.date: 05/31/2018
---

# Adding Launch to the CustomAction and Binary Tables

Add a record to the [CustomAction table](customaction-table.md) for the Launch custom action. Enter the custom action's name in the Action column of the CustomAction table. Enter the total numeric type for Launch, 65, into the Type column of the Custom action table. The Source column of the CustomAction table specifies a key into the record of the [Binary Table](binary-table.md) that contains the binary data for the DLL. Enter Tutorial.dll into the Source column of the CustomAction table. The entry point specified in the Target field of the CustomAction table must match that exported from the DLL. Enter LaunchTutorial into the Target column of the CustomAction table.

[CustomAction Table](customaction-table.md)



| Action | Type | Source       | Target         |
|--------|------|--------------|----------------|
| Launch | 65   | Tutorial.dll | LaunchTutorial |



 

Add the Tutorial.dll you created from Tutorial.cpp as a binary stream to the Binary table.

[Binary Table](binary-table.md)



| Name         | Data                          |
|--------------|-------------------------------|
| Tutorial.dll | {*binary data added for DLL*} |



 

Continue to [Adding a Control Event at the End of the Installation to Run Launch](adding-a-control-event-at-the-end-of-the-installation-to-run-launch.md).

 

 



