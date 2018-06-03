---
title: Adding Context Menu Items
description: When an administrator pulls up a context menu for the object you are extending, Failover Cluster Administrator calls your implementation of the IWEExtendContextMenu AddContextMenuItems method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3914b482-33a7-4532-bb86-18f0dc253013
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- context menus Failover Cluster
- context menus Failover Cluster ,adding items
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding Context Menu Items

\[Support for Failover Cluster Administrator extension DLLs was removed in Windows Server 2008.\]

When an administrator pulls up a context menu for the object you are extending, [Failover Cluster Administrator](cluster-administrator.md) calls your implementation of the [**IWEExtendContextMenu::AddContextMenuItems**](/previous-versions/windows/desktop/api/cluadmex/nf-cluadmex-iweextendcontextmenu-addcontextmenuitems) method. Your implementation should:

1.  Create the context menu items to be added to the context menu.
2.  Call the Failover Cluster Administrator information interfaces as needed. See [Using the Information Interfaces](using-the-information-interfaces.md).
3.  Call [**IWCContextMenuCallback::AddExtensionMenuItem**](/previous-versions/windows/desktop/api/cluadmex/nf-cluadmex-iwccontextmenucallback-addextensionmenuitem) for each item to be added. This causes the item to appear in the context menu seen by the administrator.

When an administrator selects a context menu item created by your extension, Failover Cluster Administrator calls your implementation of [**IWEInvokeCommand::InvokeCommand**](/previous-versions/windows/desktop/api/cluadmex/nf-cluadmex-iweinvokecommand-invokecommand). Your implementation should perform the action you want to associate with the context menu item.

 

 




