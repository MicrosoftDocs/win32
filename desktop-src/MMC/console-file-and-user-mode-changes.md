---
title: Console File and User Mode Changes
description: In MMC 2.0, a significant advantage to using a user mode console is that the user can change settings at will, and not be prompted to save changes when exiting (the changes will be saved automatically).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'da632889-eb1a-421d-a466-39f768760e7d'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Console File and User Mode Changes

In MMC 2.0, a significant advantage to using a user mode console is that the user can change settings at will, and not be prompted to save changes when exiting (the changes will be saved automatically). This change was implemented to make the MMC tool easier to use without requiring user interface responses to save settings. The automatic saving feature applies to user mode console files created with the "Do not save changes to this console" check box cleared.

The MMC recommendation (for MMC 2.0 and previous versions) is to distribute user mode console files instead of author mode console files. Author mode is not required for most management tasks.

In addition to automatically saving the user settings, another feature of MMC 2.0 user mode console files is that they require less storage space than MMC 1.x user mode console files.

Additionally, the main (non-user) console file can be a read-only file; the changes to the user's portion of the console are still saved. The user state and console state are maintained separately, which allows the main console file to be read-only and the user settings to be saved automatically.

Users can delete the user portion of their user mode console files by executing **Disk Cleanup** through the MMC 2.0 **File+Options** menu.

 

 




