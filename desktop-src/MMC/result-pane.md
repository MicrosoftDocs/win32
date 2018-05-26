---
title: Testing the Result Pane
description: Provides guidelines for testing the result pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 78fc9d83-b50d-42a3-be13-a542727bf2c8
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Testing the Result Pane

The following tests involve interaction with the result pane in a snap-in:

-   Set a multicolumn list view in the result pane to **Details** and sort the list by clicking different column headers.
-   Change a result item in one view and confirm that the change is applied to the same result item in all views. Try several different items and use these actions: rename, delete, cut/copy/paste, menu commands provided by the snap-in, apply changes from a property page, and add new items.
-   Insert all columns for the result pane, including the columns that need to be hidden initially (these can be inserted as hidden columns). This makes it possible for the user to configure all inserted columns from the **Columns** dialog box and to choose which ones to display.
-   Check that appropriate toolbar buttons are enabled when the result pane background is selected.
-   Check that appropriate verbs are enabled in the **Action** menu when the result pane background is selected.
-   Check that appropriate verbs are enabled in the **Action** menu when an OCX control is selected in the result pane and when a taskpad is selected in the result pane.
-   Check that appropriate toolbar buttons are enabled when an OCX control is selected in the result pane and when a taskpad is selected in the result pane.

 

 




