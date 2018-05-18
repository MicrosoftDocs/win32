---
title: Adding Filtered Views Interfaces
description: MMC provides snap-in developers with the following interface and methods for working with filtered views
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9ea27f86-b50f-4cf6-b00c-874ecdc3e3e9'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["filtered views MMC , interfaces"]
---

# Adding Filtered Views: Interfaces

MMC provides snap-in developers with the following interface and methods for working with filtered views:

-   [**IHeaderCtrl2**](iheaderctrl2.md)
    -   [**IHeaderCtrl2::SetColumnFilter**](iheaderctrl2-setcolumnfilter.md)
    -   [**IHeaderCtrl2::GetColumnFilter**](iheaderctrl2-getcolumnfilter.md)
    -   [**IHeaderCtrl2::SetChangeTimeOut**](iheaderctrl2-setchangetimeout.md)

## Other Additions

MMC defines the following notifications for working with filtered views:

-   [**MMCN\_FILTER\_CHANGE**](mmcn-filter-change.md)
-   [**MMCN\_FILTERBTN\_CLICK**](mmcn-filterbtn-click.md)

Furthermore, MMC defines the following additional constructs to be used for working with filtered views:

-   [**MMC\_FILTER\_TYPE**](mmc-filter-type.md) enumeration
-   [**MMC\_FILTER\_CHANGE\_CODE**](mmc-filter-change-code.md) enumeration
-   [**MMC\_FILTERDATA**](mmc-filterdata.md) structure

## Related topics

<dl> <dt>

[Adding Filtered Views: Implementation Details](adding-filtered-views-implementation-details.md)
</dt> </dl>

 

 




