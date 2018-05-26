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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Adding Filtered Views: Interfaces

MMC provides snap-in developers with the following interface and methods for working with filtered views:

-   [**IHeaderCtrl2**](/windows/win32/Mmc/nn-mmc-iheaderctrl2?branch=master)
    -   [**IHeaderCtrl2::SetColumnFilter**](/windows/win32/Mmc/nf-mmc-iheaderctrl2-setcolumnfilter?branch=master)
    -   [**IHeaderCtrl2::GetColumnFilter**](/windows/win32/Mmc/nf-mmc-iheaderctrl2-getcolumnfilter?branch=master)
    -   [**IHeaderCtrl2::SetChangeTimeOut**](/windows/win32/Mmc/nf-mmc-iheaderctrl2-setchangetimeout?branch=master)

## Other Additions

MMC defines the following notifications for working with filtered views:

-   [**MMCN\_FILTER\_CHANGE**](mmcn-filter-change.md)
-   [**MMCN\_FILTERBTN\_CLICK**](mmcn-filterbtn-click.md)

Furthermore, MMC defines the following additional constructs to be used for working with filtered views:

-   [**MMC\_FILTER\_TYPE**](/windows/win32/Mmc/ne-mmc-_mmc_filter_type?branch=master) enumeration
-   [**MMC\_FILTER\_CHANGE\_CODE**](/windows/win32/Mmc/ne-mmc-_mmc_filter_change_code?branch=master) enumeration
-   [**MMC\_FILTERDATA**](/windows/win32/Mmc/ns-mmc-_mmc_filterdata?branch=master) structure

## Related topics

<dl> <dt>

[Adding Filtered Views: Implementation Details](adding-filtered-views-implementation-details.md)
</dt> </dl>

 

 




