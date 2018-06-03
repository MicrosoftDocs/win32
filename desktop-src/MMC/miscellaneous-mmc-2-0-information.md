---
title: Miscellaneous MMC 2.0 Information
description: The following information is provided for developers programming for MMC 2.0
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 31b8c6ee-be02-403f-b5ac-04e7c34c4bc3
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Microsoft Management Console 2.0 MMC , miscellaneous information
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Miscellaneous MMC 2.0 Information

The following information is provided for developers programming for MMC 2.0:

-   The Active Template Library (ATL) Snap-in Wizard does not support the new MMC 2.0 features. The ATL Snap-in Wizard is no longer supported, and new snap-ins, even those targeting MMC 1.1 or MMC 1.2, should not be written with this wizard.
-   Custom icons in taskpad views are now supported when using the New Task Wizard.
-   The "Enable context menus on taskpads in this console" option has been removed from the **File+Options** property page; the context menus will always be enabled.
-   In MMC 2.0, the [**IConsoleVerb**](/windows/desktop/api/Mmc/nn-mmc-iconsoleverb) methods fully support the [**MMC\_BUTTON\_STATE**](/windows/desktop/api/Mmc/ne-mmc-_mmc_button_state) enumeration values. In MMC 1.2, MMC\_BUTTON\_STATE's INDETERMINATE, BUTTONPRESSED, and CHECKED values were not used.
-   MMC 2.0 removes the ability to create a new window by dragging a node to the main window background. This feature is allowed in MMC 1.2, but it is removed from MMC 2.0 to facilitate the expanded drag-and-drop functionality for snap-ins. An MMC 2.0 user can still achieve the new window effect by invoking the **New Window from Here** menu command.
-   The Visual Basic Snap-in Designer does not support MMC 2.0 features.

 

 




