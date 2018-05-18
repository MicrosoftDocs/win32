---
Description: 'There are three functions that generate dialog boxes to handle errors: SetupCopyError, SetupDeleteError, and SetupRenameError.'
ms.assetid: '0bff17a6-590d-4410-9ed1-0a655d94caad'
title: Error Handling
---

# Error Handling

There are three functions that generate dialog boxes to handle errors: [**SetupCopyError**](setupcopyerror.md), [**SetupDeleteError**](setupdeleteerror.md), and [**SetupRenameError**](setuprenameerror.md).

Callback routines can use these functions to generate a user interface to handle [**SPFILENOTIFY\_COPYERROR**](spfilenotify-copyerror.md), [**SPFILENOTIFY\_DELETEERROR**](spfilenotify-deleteerror.md), and [**SPFILENOTIFY\_RENAMEERROR**](spfilenotify-renameerror.md) notifications.

Each of these error-handling functions generates a dialog box that asks the user for information on how to proceed. As with [**SetupPromptForDisk**](setuppromptfordisk.md), you can modify the dialog box's layout and behavior by specifying flags during the function call.

 

 



