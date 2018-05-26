---
Description: There are three functions that generate dialog boxes to handle errors SetupCopyError, SetupDeleteError, and SetupRenameError.
ms.assetid: 0bff17a6-590d-4410-9ed1-0a655d94caad
title: Error Handling
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Error Handling

There are three functions that generate dialog boxes to handle errors: [**SetupCopyError**](/windows/win32/Setupapi/nf-setupapi-setupcopyerrora?branch=master), [**SetupDeleteError**](/windows/win32/Setupapi/nf-setupapi-setupdeleteerrora?branch=master), and [**SetupRenameError**](/windows/win32/Setupapi/nf-setupapi-setuprenameerrora?branch=master).

Callback routines can use these functions to generate a user interface to handle [**SPFILENOTIFY\_COPYERROR**](spfilenotify-copyerror.md), [**SPFILENOTIFY\_DELETEERROR**](spfilenotify-deleteerror.md), and [**SPFILENOTIFY\_RENAMEERROR**](spfilenotify-renameerror.md) notifications.

Each of these error-handling functions generates a dialog box that asks the user for information on how to proceed. As with [**SetupPromptForDisk**](/windows/win32/Setupapi/nf-setupapi-setuppromptfordiska?branch=master), you can modify the dialog box's layout and behavior by specifying flags during the function call.

 

 



