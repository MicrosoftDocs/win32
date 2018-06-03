---
title: Using Column Persistence Interfaces
description: MMC provides snap-in developers with the following interface for working with column persistence
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 66b876bc-f93c-4d7b-ab7e-2ccd8429f4f5
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- column persistence MMC , interfaces
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Column Persistence: Interfaces

MMC provides snap-in developers with the following interface for working with column persistence:

-   [**IColumnData**](/windows/desktop/api/Mmc/nn-mmc-icolumndata)

## Other Constructs

MMC defines the following notification and clipboard format for working with column persistence:

-   [**MMCN\_COLUMNS\_CHANGED**](mmcn-columns-changed.md) notification
-   [**CCF\_COLUMN\_SET\_ID**](ccf-column-set-id.md) clipboard format

MMC defines four structures to be used for accessing column configuration data:

-   [**MMC\_COLUMN\_DATA**](/windows/desktop/api/Mmc/ns-mmc-_mmc_column_data)
-   [**MMC\_COLUMN\_SET\_DATA**](/windows/desktop/api/Mmc/ns-mmc-_mmc_column_set_data)
-   [**MMC\_SORT\_DATA**](/windows/desktop/api/Mmc/ns-mmc-_mmc_sort_data)
-   [**MMC\_SORT\_SET\_DATA**](/windows/desktop/api/Mmc/ns-mmc-_mmc_sort_set_data)

MMC also defines the following structure for use with the [**MMCN\_COLUMNS\_CHANGED**](mmcn-columns-changed.md) notification:

-   [**MMC\_VISIBLE\_COLUMNS**](/windows/desktop/api/Mmc/ns-mmc-_mmc_visible_columns)

## Related topics

<dl> <dt>

[Using Column Persistence](using-column-persistence.md)
</dt> <dt>

[Using Column Persistence: Implementation Details](using-column-persistence-implementation-details.md)
</dt> <dt>

[Using Column Persistence: Advanced Topics](using-column-persistence-advanced-topics.md)
</dt> </dl>

 

 




