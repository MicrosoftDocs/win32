---
description: 'There are three functions that generate dialog boxes to handle errors: SetupCopyError, SetupDeleteError, and SetupRenameError.'
ms.assetid: 'fcb310e1-5db7-47f3-b3d6-d528eb17e19a'
title: Error Handling (Setup API)
ms.topic: article
ms.date: 05/31/2018
---

# Error Handling (Setup API)

There are three functions that generate dialog boxes to handle errors: [**SetupCopyError**](/windows/desktop/api/Setupapi/nf-setupapi-setupcopyerrora), [**SetupDeleteError**](/windows/desktop/api/Setupapi/nf-setupapi-setupdeleteerrora), and [**SetupRenameError**](/windows/desktop/api/Setupapi/nf-setupapi-setuprenameerrora).

Callback routines can use these functions to generate a user interface to handle [**SPFILENOTIFY\_COPYERROR**](spfilenotify-copyerror.md), [**SPFILENOTIFY\_DELETEERROR**](spfilenotify-deleteerror.md), and [**SPFILENOTIFY\_RENAMEERROR**](spfilenotify-renameerror.md) notifications.

Each of these error-handling functions generates a dialog box that asks the user for information on how to proceed. As with [**SetupPromptForDisk**](/windows/desktop/api/Setupapi/nf-setupapi-setuppromptfordiska), you can modify the dialog box's layout and behavior by specifying flags during the function call.

 

 



