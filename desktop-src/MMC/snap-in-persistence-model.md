---
title: Snap-in Persistence Model
description: MMC enables each snap-in to persist private configuration data in the console file. Snap-ins can persist their data by implementing either the IPersistStreamInit, the IPersistStream, or the IPersistStorage interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c850a7c7-b409-469c-9d31-f3028c8cc1a9
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- snap-in persistence model MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Snap-in Persistence Model

MMC enables each snap-in to persist private configuration data in the console file. Snap-ins can persist their data by implementing either the [**IPersistStreamInit**](https://www.bing.com/search?q=**IPersistStreamInit**), the [**IPersistStream**](https://www.bing.com/search?q=**IPersistStream**), or the [**IPersistStorage**](https://www.bing.com/search?q=**IPersistStorage**) interface.

MMC will always query a snap-in for [**IPersistStream**](https://www.bing.com/search?q=**IPersistStream**). If it does not receive an **IPersistStream** interface pointer, it will query for [**IPersistStreamInit**](https://www.bing.com/search?q=**IPersistStreamInit**), then [**IPersistStorage**](https://www.bing.com/search?q=**IPersistStorage**). Snap-ins that do not persist their data should simply return with an appropriate error code when MMC queries them for any of these interfaces.

Snap-ins are encouraged to implement either the [**IPersistStream**](https://www.bing.com/search?q=**IPersistStream**) or [**IPersistStreamInit**](https://www.bing.com/search?q=**IPersistStreamInit**) interface to persist their data. Both interfaces are lightweight and easy to implement. In contrast, the [**IPersistStorage**](https://www.bing.com/search?q=**IPersistStorage**) interface requires the implementation of many features not required by snap-ins that simply want to persist their data.

Be aware that MMC supports both [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) and [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) persistence. The snap-in's **IComponentData** object should persist view-independent data for each of its scope items. Each **IComponent** object should persist any view-specific data it requires to re-create its own view.

For snap-ins that support persistence, MMC calls the **Load** and **Save** methods when a user action initiates a console file load or save. Most often this occurs when a file is loaded, or when the user clicks **Save** or **Save As** on the **File** menu. The snap-in should be sure to accurately implement the **IsDirty** method.

Be aware that extension snap-ins in general cannot persist their data. The only exceptions to this rule are namespace and taskpad extensions. Namespace extensions must always implement [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata). Taskpad extensions that support persistence must also implement **IComponentData**. Namespace extensions can support **IComponentData** and [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) persistence. Taskpad extensions can only support **IComponentData** persistence.

 

 




