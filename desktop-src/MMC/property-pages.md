---
title: Testing the Property Pages
description: MMC property pages differ in some ways from standard Windows property pages.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e07f576a-5907-4a35-ba8a-7c1c95fdf33d
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Testing the Property Pages

MMC property pages differ in some ways from standard Windows property pages. Perform the following tests on your snap-in property pages:

-   Display pages using both small and large fonts in both low and high resolutions.
-   Display a page for a list item, click a different node in the scope pane, and then click **Apply** on the property sheet.
-   Display a page for a list item, click a different node in the scope pane, return to the original node, and then display properties for the same list item again. MMC should simply set the focus to the existing sheet. Click **Apply** on the property sheet.
-   If your snap-in supports multiselection property pages, then perform the preceding tests using a multiple selection.
-   If your snap-in supports multiselection property pages, then display a property sheet for a large number of selected items.
-   For a node in the scope pane, open a property page for its result items in different views. Ensure that the same property page is opened in each view.
-   Open the property pages for several different nodes. Ensure that the property page is the correct one for each node and that no two nodes share the same property sheet.
-   Delete an item that has a property page open, and then apply changes from that property page. Ensure this situation is handled gracefully.
-   Ensure that changes to the properties of an item are correctly updated in all views.
-   Check that extension snap-in property pages are the same size as their parent's property pages.

 

 




