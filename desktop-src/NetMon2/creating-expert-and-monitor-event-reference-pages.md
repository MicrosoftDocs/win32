---
description: This section describes how to plan, develop, and test event reference pages (ERPs) and how to deploy them in an expert or monitor. For information about ERPs and how to use them with Network Monitor, see Event Reference Page.
ms.assetid: 78d6e8cf-785e-4d5f-a78d-9ef9da9bc3e0
title: Creating Expert and Monitor Event Reference Pages
ms.topic: article
ms.date: 05/31/2018
---

# Creating Expert and Monitor Event Reference Pages

This section describes how to plan, develop, and test event reference pages (ERPs) and how to deploy them in an expert or monitor. For information about ERPs and how to use them with Network Monitor, see [Event Reference Page](event-reference-page.md).

To develop a new ERP, the first step is determining the events that require individual ERPs for your custom [expert](experts.md) or [monitor](monitors.md). You must create separate ERPs for each event you wish to display in the Network Monitor Event Viewer. For example, suppose that:

-   You develop a monitor named Game Monitor and Stock Watcher.
-   The monitor is located in a file called Gamemon.dll.
-   The monitor generates two events, Game Running and My Internet Stock Soars.
-   You plan to develop two ERPs, Gamemon1.htm and Gamemon2.htm.

> [!Note]  
> It's not necessary to have a one-to-one correspondence of ERPs to monitor or expert events.

 

After you have established a list of unique ERPs, follow these steps to create each ERP.

-   [Write the HTML source document](writing-an-event-reference-page.md).
-   [Save and name](naming-an-event-reference-page.md) the HTML source file as an .htm file.
-   [Test the ERP](testing-an-event-reference-page.md) with the completed expert or monitor.

 

 



