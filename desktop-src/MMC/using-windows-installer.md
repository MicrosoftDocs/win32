---
title: Using Windows Installer
description: Describes the use of windows installer for deployment.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 39e54e73-7ef3-4519-a174-ce6b68558318
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using Windows Installer

Microsoft Windows Installer is a setup technology used in a number of Microsoft applications, including Microsoft Office. Directory services provide the ability to store a snap-in installation in the directory and to download it automatically when the user tries to open a console file that references that snap-in. This is the preferred methodology for distributing snap-ins. Windows Installer exists on all Windows operating systems and can be used for your setup even if you do not intend to use the directory for distribution.

Group policies enable administrators to grant access to tools and functionality on a group basis, for either computers or users. Directory services use these group policies to control access to application installations. You must provide a policy file (\*.adm) that sets the appropriate permissions for each snap-in to be distributed.

Snap-in users can distribute a saved console file to recipients who may not have installed all the snap-ins referenced in the console file. When a user performs an action that requires a snap-in that is not locally installed, MMC's integration with Windows Installer makes it possible for the snap-in to be downloaded automatically and installed on the user's local computer.

For more information about using Windows Installer for snap-in and saved console file installation, see [Distributing Your Snap-in](distributing-your-snap-in.md).

The following topic provides an overview of how to use Windows Installer to distribute saved console files: [Distributing Saved Console Files](distributing-saved-console-files.md).

 

 




