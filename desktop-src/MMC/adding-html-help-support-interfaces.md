---
title: Adding HTML Help Support Interfaces
description: HTML Help requires the implementation or use of the following interfaces and methods
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7e5fc48b-7192-4db9-b110-cf7fdb59b57f
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- adding HTML Help support interfaces MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding HTML Help Support: Interfaces

HTML Help requires the implementation or use of the following interfaces and methods:

-   [**ISnapinHelp2**](/windows/desktop/api/Mmc/nn-mmc-isnapinhelp2)
    -   [**ISnapinHelp2::GetHelpTopic**](https://www.bing.com/search?q=**ISnapinHelp2::GetHelpTopic**)
    -   [**ISnapinHelp2::GetLinkedTopics**](/windows/desktop/api/Mmc/nf-mmc-isnapinhelp2-getlinkedtopics)
-   [**IDisplayHelp**](/windows/desktop/api/Mmc/nn-mmc-idisplayhelp)
    -   [**IDisplayHelp::ShowTopic**](/windows/desktop/api/Mmc/nf-mmc-idisplayhelp-showtopic)

## Other Additions

MMC sends the following notification in response to the user's request for context-sensitive (F1) Help:

-   [**MMCN\_CONTEXTHELP**](mmcn-contexthelp.md)

The following function enables you to call an HTML Help topic from a property sheet:

-   [**MMCPropertyHelp**](/windows/desktop/api/Mmc/nf-mmc-mmcpropertyhelp)

MMC sends the following notification in response to the user's request for Help to snap-ins that do not provide HTML Help by implementing [**ISnapinHelp2**](/windows/desktop/api/Mmc/nn-mmc-isnapinhelp2):

-   [**MMCN\_SNAPINHELP**](mmcn-snapinhelp.md)

Be aware that snap-ins are strongly encouraged to provide HTML Help.

## Related topics

<dl> <dt>

[Adding HTML Help Support: Implementation Details](adding-html-help-support-implementation-details.md)
</dt> </dl>

 

 




