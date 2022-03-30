---
description: The Windows UI provides users with access to a wide variety of objects necessary to run applications and manage the operating system.
title: Shell Developer's Guide
ms.topic: article
ms.date: 03/30/2022
ms.assetid: 8f88ef25-3645-4f54-9453-41f919c0fc0a
topic_type: 
 - kbArticle
---

# Shell Developer's Guide

> [!NOTE]
> This guide provides information about using the Windows Shell with the Win32 api. For information about the Windows Shell for other languages or with frameworks like UWP use [the corresponding documentation](/windows/apps/design/shell/).

> [!CAUTION]
> These docs got updated recently to match Windows 10 and Windows 11. If you want to develop for older versions of Windows please view the [legacy documentation](previous-versions/windows/desktop/legacy/bb776778\(v=vs.85\)).

The Windows UI provides users with access to a wide variety of objects necessary to run applications and manage the operating system. The most numerous and familiar of these objects are the folders and files that reside on computer disk drives. There are also a number of virtual objects that allow the user to do tasks such as sending files to remote printers or accessing the Recycle Bin. The Shell organizes these objects into a hierarchical namespace, and provides users and applications with a consistent and efficient way to access and manage objects.

## In this section

- [Security Considerations: Microsoft Windows Shell](sec-shell.md)
- [Guidance for Implementing In-Process Extensions](shell-and-managed-code.md)
- [Shell and Common Controls Versions](versions.md)
- [Implementing the Basic Folder Object Interfaces](nse-implement.md)
- [Implementing a Custom File Format](customizing-file-types-bumper.md)
- [Shell Extensibility (Creating a Data Source)](shell-extensibility-bumper.md)
- [Implementing Control Panel Items](control-panel-applications.md)
- [Supporting Shell Applications](application-support-bumper.md)
- [Legacy Shell Topics](miscellaneous-topics-bumper.md)

## Document Conventions

The Shell Developers's Guide follows the usual Windows Software Development Kit (SDK) document conventions. Two conventions in particular should be noted:

- Sample code omits normal error-correction code. This code has been removed only to make the code more readable. You should include all appropriate error-correction code in your own applications.
- To make sample registry entries clear, key, subkey, and entry names as well as values are displayed with a standard font. User or application-defined item names are italicized.
