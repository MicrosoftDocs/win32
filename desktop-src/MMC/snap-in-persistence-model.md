---
title: Snap-in Persistence Model
description: MMC enables each snap-in to persist private configuration data in the console file. Snap-ins can persist their data by implementing either the IPersistStreamInit, the IPersistStream, or the IPersistStorage interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c850a7c7-b409-469c-9d31-f3028c8cc1a9'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["snap-in persistence model MMC"]
---

# Snap-in Persistence Model

MMC enables each snap-in to persist private configuration data in the console file. Snap-ins can persist their data by implementing either the [**IPersistStreamInit**](_com_ipersiststreaminit), the [**IPersistStream**](_com_ipersiststream), or the [**IPersistStorage**](_com_ipersiststorage) interface.

MMC will always query a snap-in for [**IPersistStream**](_com_ipersiststream). If it does not receive an **IPersistStream** interface pointer, it will query for [**IPersistStreamInit**](_com_ipersiststreaminit), then [**IPersistStorage**](_com_ipersiststorage). Snap-ins that do not persist their data should simply return with an appropriate error code when MMC queries them for any of these interfaces.

Snap-ins are encouraged to implement either the [**IPersistStream**](_com_ipersiststream) or [**IPersistStreamInit**](_com_ipersiststreaminit) interface to persist their data. Both interfaces are lightweight and easy to implement. In contrast, the [**IPersistStorage**](_com_ipersiststorage) interface requires the implementation of many features not required by snap-ins that simply want to persist their data.

Be aware that MMC supports both [**IComponentData**](icomponentdata.md) and [**IComponent**](icomponent.md) persistence. The snap-in's **IComponentData** object should persist view-independent data for each of its scope items. Each **IComponent** object should persist any view-specific data it requires to re-create its own view.

For snap-ins that support persistence, MMC calls the **Load** and **Save** methods when a user action initiates a console file load or save. Most often this occurs when a file is loaded, or when the user clicks **Save** or **Save As** on the **File** menu. The snap-in should be sure to accurately implement the **IsDirty** method.

Be aware that extension snap-ins in general cannot persist their data. The only exceptions to this rule are namespace and taskpad extensions. Namespace extensions must always implement [**IComponentData**](icomponentdata.md). Taskpad extensions that support persistence must also implement **IComponentData**. Namespace extensions can support **IComponentData** and [**IComponent**](icomponent.md) persistence. Taskpad extensions can only support **IComponentData** persistence.

 

 




