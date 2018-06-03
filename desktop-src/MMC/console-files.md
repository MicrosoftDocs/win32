---
title: Testing the Console Files
description: Provides guidelines for testing console files.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 398c69eb-018b-49ee-a35c-e71c60bca8d2
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Testing the Console Files

Because anyone can save a console file in author mode, the following tests should be performed by a wide range of administrators, developers, and testers:

-   Save a console file with each of the snap-in nodes selected and ensure that the node is still selected when the console file is reopened.
-   Save a console file with each of the snap-in nodes at the root of a view.
-   Add multiple instances of your snap-in to the same console file and ensure all functionality remains intact.
-   Save a console file that contains your snap-in for each of the MMC user modes. Ensure that no major functionality of your snap-in is blocked when the user cannot gain access to toolbars or the scope pane.
-   Ensure that the icon for a saved console file is not the default MMC icon.
-   Close a view after opening a property page, and then apply changes. Then, open the view to see if the changes were applied.
-   Perform drag-and-drop operations between different instances of your snap-in within the same console file to ensure that no problems occur.
-   Shut down console windows with your snap-in selected in the following ways: each node in the scope pane selected, result pane background selected, any OCX control your snap-in uses selected, and with multiple result items selected. Be especially careful of nodes that display toolbars or menu buttons. Ensure that no problems occur.
-   Ensure that your saved console file title agrees with the name in the **Start** menu.
-   If your snap-in implements asynchronous insertion into the namespace, try saving a console file with a scope item at the bottom of the expanded tree selected.
-   If your snap-in modifies the display name of its static node, ensure that this text is does not change when the snap-in is saved into a console file.

 

 




