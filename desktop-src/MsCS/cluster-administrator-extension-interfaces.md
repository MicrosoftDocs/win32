---
title: Failover Cluster Administrator Extension Interfaces
description: The Failover Cluster Administrator extension interfaces allow you to create custom property pages, wizard pages, and context menu items for the Failover Cluster Administrator user interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a2306e94-47c6-441f-b06d-70e3f633f78e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Failover Cluster Administrator Failover Cluster ,Failover Cluster Administrator Extension API,interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Failover Cluster Administrator Extension Interfaces

\[With the exception of [**IWEExtendPropertySheet**](/windows/previous-versions/cluadmex/nn-cluadmex-iweextendpropertysheet?branch=master), support for the Failover Cluster Administrator extension interfaces was removed in Windows Server 2008.\]

The Failover Cluster Administrator extension interfaces allow you to create custom property pages, wizard pages, and context menu items for the [Failover Cluster Administrator](cluster-administrator.md) user interface.



| Interface                                                           | Description                                                                                                             |
|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [**IWEExtendContextMenu**](/windows/previous-versions/cluadmex/nn-cluadmex-iweextendcontextmenu?branch=master)<br/>     | Allows you to create context menu items and add them to a Failover Cluster Administrator context menu.<br/>       |
| [**IWEExtendPropertySheet**](/windows/previous-versions/cluadmex/nn-cluadmex-iweextendpropertysheet?branch=master)<br/> | Allows you to create property sheet pages and add them to the Failover Cluster Administrator user interface.<br/> |
| [**IWEExtendWizard**](/windows/previous-versions/cluadmex/nn-cluadmex-iweextendwizard?branch=master)<br/>               | Allows you to create custom Failover Cluster Administrator wizard pages.<br/>                                     |
| [**IWEExtendWizard97**](/windows/previous-versions/cluadmex/nn-cluadmex-iweextendwizard97?branch=master)<br/>           | Allows you to create custom Failover Cluster Administrator Wizard 97 wizard pages.<br/>                           |
| [**IWEInvokeCommand**](/windows/previous-versions/cluadmex/nn-cluadmex-iweinvokecommand?branch=master)<br/>             | Allows you to respond when users select your context menu items.<br/>                                             |



 

## Related topics

<dl> <dt>

[Failover Cluster Administrator Extension Functions and Interfaces](cluster-administrator-extension-functions.md)
</dt> </dl>

 

 





