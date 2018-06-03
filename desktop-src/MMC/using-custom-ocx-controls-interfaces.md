---
title: Using Custom OCX Controls Interfaces
description: MMC provides snap-in developers with the following interface methods for working with OCX controls
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 226095cf-b606-4cdf-bb61-207902c774c2
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- custom OCX controls MMC , interfaces
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Custom OCX Controls: Interfaces

MMC provides snap-in developers with the following interface methods for working with OCX controls:

-   [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype)
-   [**IConsole2::QueryResultView**](https://www.bing.com/search?q=**IConsole2::QueryResultView**)

## Other Constructs

MMC defines the following additional constructs for working with OCX controls:

-   [**MMCN\_INITOCX**](mmcn-initocx.md) notification
-   [**MMCN\_BTN\_CLICK**](mmcn-btn-click.md) notification
-   [**MMCN\_RESTORE\_VIEW**](mmcn-restore-view.md) notification
-   MMC\_VIEW\_OPTIONS\_CREATENEW view option (see [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype))
-   [**IS\_SPECIAL\_DATAOBJECT**](/windows/desktop/api/Mmc/nf-mmc-is_special_dataobject) macro

## Related topics

<dl> <dt>

[Using Custom OCX Controls: Implementation Details](using-custom-ocx-controls-implementation-details.md)
</dt> </dl>

 

 




