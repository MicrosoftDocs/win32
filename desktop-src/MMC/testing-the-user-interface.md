---
title: Testing the User Interface
description: Provides test guidelines for the GUI.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8a8f802a-36de-4a09-926b-24ea504d3dfa
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- snap-in testing MMC , testing the UI
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Testing the User Interface

Most of the items in this section relate to navigation within the namespace; a few are more general in nature.

Testing tasks that should be performed on the user interface for a snap-in are:

-   Check for duplication of keyboard shortcuts.
-   Double-click each node in the scope pane and each result item and ensure that an appropriate default verb is applied.
-   With **Console Root** selected, right-click each node in the scope pane and select each of the node's context menu items to test the navigation.
-   Click the **Back** and **Forward** buttons to navigate between nodes that display different view types such as list view, OCX, and taskpad. The most important task is the navigation between different view types on a single node in the scope pane. Be sure that such navigation does not cause problems.
-   Add items from each node of the scope pane and from each view of each node to the **Favorites** list. Add these items as navigation tasks to a console taskpad. This tests both the functionality of the **Favorites** list and the use of taskpads for navigation.
-   Expand your entire tree without selecting any nodes. Click **Console Root** and press the asterisk (\*) key.
-   Run your snap-in with the desktop set to different color depths. Ensure that all of the toolbar buttons, console tree icons, result item large icons, and result item small icons appear correctly.
-   Ensure that the appropriate toolbar buttons are enabled when selecting nodes in the scope pane, result items, and multiple items. If a toolbar is never appropriate for a selection, it should be hidden. If a toolbar button is not appropriate for the current state of the selection, it should appear dimmed.
-   If your snap-in supports multiselection, select several result items and verify that the proper context menu appears for each item. Repeat this procedure for scope items in the result pane and for a mixture of scope and result items in the result pane.
-   Verify that the text in the status bar and description bar is correct while selecting different nodes in the scope pane, result items, and context menu items.
-   If your snap-in is MMC 1.1-compatible, run tests with both Internet Explorer 4.0 and Internet Explorer 5. Pay particular attention to property pages, wizards, snap-in Help, and taskpads.
-   When dragging a node, ensure that the "prohibited" icon is correctly displayed for invalid drop targets.
-   If your snap-in uses the same OCX control for multiple nodes in the scope pane, ensure that the OCX control's state is correct when navigating between the different nodes and when the OCX control is displayed in multiple views.

 

 




