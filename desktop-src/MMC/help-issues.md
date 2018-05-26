---
title: Help Issues
description: Ensures that Help is available for the end users.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 84bdf3f8-0eaf-428d-8fa6-61fdc0e8c13f
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Help Issues

Perform these tests to ensure that Help is available for your end users:

-   Call the MMC [**IDisplayHelp**](/windows/win32/Mmc/nn-mmc-idisplayhelp?branch=master) interface to properly display context-sensitive Help in the merged MMC HTML Help collections file.
-   Start Help to ensure that [**ISnapInHelp2**](/windows/win32/Mmc/nn-mmc-isnapinhelp2?branch=master) is implemented to give MMC the name of your Help file.
-   For Microsoft Visual Basic developers, test Help by pressing F1 on a scope item and on a list item. If you are using merged Help, ensure that your ShowHelpTopic calls display the correct topics.
-   Turn on the "autosync" option in Help. (This option is automatically set on Windows Server, but is not set on clients.)
-   Ensure that an extension snap-in provides its own Help file and exposes all fields of the About information.
-   In **About Help**, ensure that all the fields are exposed and that their text is not longer than the allotted space (that is, ensure that the text is not truncated).
-   Test F1 Help on each of your scope pane nodes, result nodes, result pane background, OCX views, multi-selected result items, and property pages to ensure that all of these items have context-sensitive Help implemented.
-   If context-sensitive Help does not work, ensure that the HTML Help file table of contents is a binary file. Snap-in context-sensitive Help does not work without a binary table of contents.

 

 




