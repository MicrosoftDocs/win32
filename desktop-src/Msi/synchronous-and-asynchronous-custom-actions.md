---
Description: The Windows Installer processes custom actions as a separate thread from the main installation.
ms.assetid: 6451029c-87f4-44ee-aa2b-cc9a1c25bcc0
title: Synchronous and Asynchronous Custom Actions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Synchronous and Asynchronous Custom Actions

The Windows Installer processes custom actions as a separate thread from the main installation. During synchronous execution of a custom action, the installer waits for the thread of the custom action to complete before continuing the main installation. During asynchronous execution, the installer runs the custom action simultaneously as the current installation continues. Authors of custom actions must therefore be aware of any asynchronous threads that may be making changes to the installation database between function calls.

In particular, calls to [**MsiGetTargetPath**](/windows/win32/Msiquery/nf-msiquery-msigettargetpatha?branch=master) and [**MsiSetTargetPath**](/windows/win32/Msiquery/nf-msiquery-msisettargetpatha?branch=master) should be avoided in asynchronous custom actions. Instead use [**MsiGetProperty**](/windows/win32/Msiquery/nf-msiquery-msigetpropertya?branch=master) to obtain a target path. Bulk database operations such as import, export, and transform operations should be avoided in any type of custom action.

Option flags can be set in the Type field of the [CustomAction table](customaction-table.md) to specify that the main and custom action threads run synchronously or asynchronously. See [Custom Action Return Processing Options](custom-action-return-processing-options.md).

The installer can only execute [Rollback Custom Actions](rollback-custom-actions.md) and [Concurrent Installation](concurrent-installations.md) actions as synchronous custom actions.

 

 



