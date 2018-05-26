---
title: Dynamically Updating List Views
description: You might want to implement a list view with items whose status changes over time and which should be dynamically updated to reflect the changes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5baf8753-d17b-4b0b-b3f3-c449dd0c2566
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- list views MMC , dynamically updating
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Dynamically Updating List Views

You might want to implement a list view with items whose status changes over time and which should be dynamically updated to reflect the changes.

For example, suppose your snap-in displays a list view that shows the real-time status of resources that it manages. The snap-in should dynamically update the list view as the resource status values change.

Be aware that snap-ins are not allowed to call any MMC interfaces from a thread other than the main thread, so snap-ins must use thread-safe techniques to perform the updates.

## Related topics

<dl> <dt>

[Using List Views](using-list-views.md)
</dt> </dl>

 

 




