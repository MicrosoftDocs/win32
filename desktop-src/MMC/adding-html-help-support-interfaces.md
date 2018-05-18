---
title: Adding HTML Help Support Interfaces
description: HTML Help requires the implementation or use of the following interfaces and methods
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7e5fc48b-7192-4db9-b110-cf7fdb59b57f'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["adding HTML Help support interfaces MMC"]
---

# Adding HTML Help Support: Interfaces

HTML Help requires the implementation or use of the following interfaces and methods:

-   [**ISnapinHelp2**](isnapinhelp2.md)
    -   [**ISnapinHelp2::GetHelpTopic**](isnapinhelp2-gethelptopic.md)
    -   [**ISnapinHelp2::GetLinkedTopics**](isnapinhelp2-getlinkedtopics.md)
-   [**IDisplayHelp**](idisplayhelp.md)
    -   [**IDisplayHelp::ShowTopic**](idisplayhelp-showtopic.md)

## Other Additions

MMC sends the following notification in response to the user's request for context-sensitive (F1) Help:

-   [**MMCN\_CONTEXTHELP**](mmcn-contexthelp.md)

The following function enables you to call an HTML Help topic from a property sheet:

-   [**MMCPropertyHelp**](mmcpropertyhelp.md)

MMC sends the following notification in response to the user's request for Help to snap-ins that do not provide HTML Help by implementing [**ISnapinHelp2**](isnapinhelp2.md):

-   [**MMCN\_SNAPINHELP**](mmcn-snapinhelp.md)

Be aware that snap-ins are strongly encouraged to provide HTML Help.

## Related topics

<dl> <dt>

[Adding HTML Help Support: Implementation Details](adding-html-help-support-implementation-details.md)
</dt> </dl>

 

 




