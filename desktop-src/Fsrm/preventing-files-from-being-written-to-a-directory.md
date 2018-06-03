---
title: Preventing Files From Being Written to a Directory
description: A file screen restricts the types of files that the system or any user can store in a specific directory and its subdirectories.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f5c4fe49-5cea-4f4a-ba12-e1b8f2361534
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , preventing files from being written to a directory
- file screens File Server Resource Manager
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Preventing Files From Being Written to a Directory

A file screen restricts the types of files that the system or any user can store in a specific directory and its subdirectories. For each file screen there is a list of blocked file groups that define a set of file name based patterns that will be restricted. When a file is created or renamed, the server evaluates whether the file name matches a pattern in any file groups configured on the path.

If a match is found, the file is blocked and a set of actions are initiated. For example, you can request that email is sent to one or more recipients. If audit logging is turned on (logging is off by default), FSRM logs an event to the audit log, and not the system event log, which can be done with an event log action.

You can also define a file screen exception. The exception defines a list of file groups that are allowed in the directory and its subdirectories. Files with names that match the name patterns are not blocked. Typically, you apply an exception to a subdirectory of the directory that contains the file screen.

The file screen applies to future files only; a file screen is not applied retroactively to existing files in the directory. To list the files that currently exist in the directory that violate the screen, create a report job that lists files by type.

You can create file screens directly but typically you create file screen templates from which file screens derive. The template is used to modify properties in bulk by applying the changes to file screens that derive from the file screen template.

For details on file screens, templates, exceptions, groups, and actions, see the following topics:

-   [Using Templates to Define File Screens](using-templates-to-define-file-screens.md)
-   [Defining a File Screen](defining-a-file-screen.md)
-   [Defining a File Screen Exception](defining-a-file-screen-exception.md)
-   [Creating File Groups to Specify the Files to Restrict](creating-file-groups-to-specify-the-files-to-restrict.md)
-   [Performing Actions Based on File Screen Violations](performing-actions-based-on-file-screen-violations.md)
-   [Updating a File Screen](updating-a-file-screen.md)

 

 




