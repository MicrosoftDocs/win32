---
title: MMC Property Sheets
description: Describes the addition of property pages.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 61293c6c-178c-42a3-8802-5c0ec252d17a
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMC
- MMC, property sheets
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMC Property Sheets

When a user right-clicks a scope node or a result pane item and then clicks **Properties**, MMC allows the primary snap-in to add property pages to it. MMC then gives any extension snap-ins the same opportunity. If any snap-ins add property pages, MMC displays a property sheet with each property page as a tab on the property sheet. Any user action made on a particular property page is forwarded to the snap-in that added that page.

A stand-alone snap-in can also display a property page independent of the **Properties** command. In this case, the snap-in that requests the property sheet must explicitly tell MMC to allow extension snap-ins to add their own property pages.

There are several options regarding how to implement snap-in Help on property sheets. For more information, see [Adding HTML Help Support](adding-html-help-support.md).

 

 




