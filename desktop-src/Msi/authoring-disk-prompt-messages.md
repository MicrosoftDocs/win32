---
description: Use the following guidelines to author a Windows Installer installation that displays a message box prompting the user to insert a disk.
ms.assetid: 8b53a490-921f-4d89-83b7-dbc62231ef92
title: Authoring Disk Prompt Messages
ms.topic: article
ms.date: 05/31/2018
---

# Authoring Disk Prompt Messages

Use the following guidelines to author a Windows Installer installation that displays a message box prompting the user to insert a disk.

**To display a message box prompting the user to insert a disk**

1.  Use the authoring capabilities of the installer to set the [**DiskPrompt**](diskprompt.md) property string in the [Property](property-table.md) table. This should include the name of the product being installed and a placeholder parameter within the string for the title printed on the disk. For example, for Microsoft Publisher the **DiskPrompt** property could be "Microsoft Publisher: Disk \[1\]", where \[1\] is the placeholder for the disk title.
2.  Enter the titles of each of the disks being prompted for into separate rows of the DiskPrompt column of the [Media](media-table.md) table. For example, the first and only entry into the Media table could be "1–Install."
3.  During the [InstallFiles](installfiles-action.md) action the value from the DiskPrompt column of the [Media](media-table.md) table is substituted for the placeholder in the string of the [**DiskPrompt**](diskprompt.md) property.
4.  The message displayed by the message box is created from a built-in template string in the [Error table](error-table.md). This is Error 1302 and the template string is: "Please insert the disk: \[2\]", and the \[2\] represents a placeholder for the [**DiskPrompt**](diskprompt.md) property.

The example displays the following message to the user: "Please insert the disk: Microsoft Publisher: Disk 1 – Install."

Note that disk prompt messages get displayed by all [User Interface Levels](user-interface-levels.md) except None.

 

 



