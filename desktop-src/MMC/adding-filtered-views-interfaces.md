---
title: Adding Filtered Views Interfaces
description: MMC provides snap-in developers with the following interface and methods for working with filtered views
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9ea27f86-b50f-4cf6-b00c-874ecdc3e3e9
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- filtered views MMC , interfaces
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding Filtered Views: Interfaces

MMC provides snap-in developers with the following interface and methods for working with filtered views:

-   [**IHeaderCtrl2**](/windows/desktop/api/Mmc/nn-mmc-iheaderctrl2)
    -   [**IHeaderCtrl2::SetColumnFilter**](/windows/desktop/api/Mmc/nf-mmc-iheaderctrl2-setcolumnfilter)
    -   [**IHeaderCtrl2::GetColumnFilter**](/windows/desktop/api/Mmc/nf-mmc-iheaderctrl2-getcolumnfilter)
    -   [**IHeaderCtrl2::SetChangeTimeOut**](/windows/desktop/api/Mmc/nf-mmc-iheaderctrl2-setchangetimeout)

## Other Additions

MMC defines the following notifications for working with filtered views:

-   [**MMCN\_FILTER\_CHANGE**](mmcn-filter-change.md)
-   [**MMCN\_FILTERBTN\_CLICK**](mmcn-filterbtn-click.md)

Furthermore, MMC defines the following additional constructs to be used for working with filtered views:

-   [**MMC\_FILTER\_TYPE**](/windows/desktop/api/Mmc/ne-mmc-_mmc_filter_type) enumeration
-   [**MMC\_FILTER\_CHANGE\_CODE**](/windows/desktop/api/Mmc/ne-mmc-_mmc_filter_change_code) enumeration
-   [**MMC\_FILTERDATA**](/windows/desktop/api/Mmc/ns-mmc-_mmc_filterdata) structure

## Related topics

<dl> <dt>

[Adding Filtered Views: Implementation Details](adding-filtered-views-implementation-details.md)
</dt> </dl>

 

 




