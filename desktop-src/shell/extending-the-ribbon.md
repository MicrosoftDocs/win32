---
description: Learn how to extend the Windows Explorer Ribbon.
title: Extending the Ribbon
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 0C043FF8-3862-4F02-8700-BB556C4F35B8
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Extending the Ribbon

In Windows Explorer, the Ribbon helps make common end-user file management activities easier and more discoverable, but there are changes afoot for app developers. For example, the old command bar was freely extensible but the Ribbon is more restricted at this time. Also, the Ribbon is not shown by default for all namespace extensions, so you have to opt in to get the Ribbon; otherwise, you get the older command bar.

Actions available to users on the Ribbon fall into three extensibility categories:

- Extensibility is not needed. Examples: Copy, Paste, Delete. Windows handles these verbs for you.
- Extensibility is not currently allowed: Examples: Zip, Close Session, and other custom actions. Use the context menu to cover these scenarios.
- Extensibility is built into the action itself. Examples: Search, Email, Print, New Item. You need to register for these verbs to include your app or file format in the Ribbon .

This document describes how you can opt-in to get the Ribbon, and how to register to handle specific Ribbon verbs.

## Opting in to the Ribbon

To opt in to the Ribbon, your [**IShellFolder2**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellfolder2) implementation should specify **EP\_Ribbon** in [**IExplorerPaneVisibility::GetPaneState**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iexplorerpanevisibility-getpanestate) and return **EPS\_FORCE** \| **EPS\_DEFAULT\_ON**.

## Extending the Ribbon for File Extensions

These Ribbon buttons are extensible based on file extensions:

- Extract All
- Mount \| Burn (an ISO)
- Play \| Play All \| Add to Playlist (verb: Enqueue)
- Open
- Edit
- Properties

When you register to statically handle the relevant verbs for new file types, the Ribbon handles the verbs appropriately. You register just as you would for context menu verbs. For more information about file associations and registering for verbs, see [Verbs and File Associations](fa-verbs.md) and [Creating Shortcut Menu Handlers](context-menu-handlers.md).

## Registering as a Default Handler for ActionIds

First, register your ProgId under the appropriate AssocActionId subkey. Each AssocActionId subkey represents a verb or action that users can invoke from the Ribbon. In this example, the app registers for the ZipSelection ActionID to extend the "Extract All" button on the Ribbon.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Classes
         Explorer.AssocActionId.ZipSelection
            shell
               open
                  command
                     (Default) = %SystemRoot%\[Your App].exe
      Microsoft
         Windows
            CurrentVersion
               Your App Name
                  Capabilities
                     URL Protocol
                     FriendlyTypeName = @%SystemRoot%\explorer.exe,-1234
```

Once that registration is complete, you must then register to handle protocols just as you normally would, as described in [Default Programs](default-programs.md).

 

 



