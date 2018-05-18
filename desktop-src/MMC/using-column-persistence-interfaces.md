---
title: Using Column Persistence Interfaces
description: MMC provides snap-in developers with the following interface for working with column persistence
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '66b876bc-f93c-4d7b-ab7e-2ccd8429f4f5'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["column persistence MMC , interfaces"]
---

# Using Column Persistence: Interfaces

MMC provides snap-in developers with the following interface for working with column persistence:

-   [**IColumnData**](icolumndata.md)

## Other Constructs

MMC defines the following notification and clipboard format for working with column persistence:

-   [**MMCN\_COLUMNS\_CHANGED**](mmcn-columns-changed.md) notification
-   [**CCF\_COLUMN\_SET\_ID**](ccf-column-set-id.md) clipboard format

MMC defines four structures to be used for accessing column configuration data:

-   [**MMC\_COLUMN\_DATA**](mmc-column-data.md)
-   [**MMC\_COLUMN\_SET\_DATA**](mmc-column-set-data.md)
-   [**MMC\_SORT\_DATA**](mmc-sort-data.md)
-   [**MMC\_SORT\_SET\_DATA**](mmc-sort-set-data.md)

MMC also defines the following structure for use with the [**MMCN\_COLUMNS\_CHANGED**](mmcn-columns-changed.md) notification:

-   [**MMC\_VISIBLE\_COLUMNS**](mmc-visible-columns.md)

## Related topics

<dl> <dt>

[Using Column Persistence](using-column-persistence.md)
</dt> <dt>

[Using Column Persistence: Implementation Details](using-column-persistence-implementation-details.md)
</dt> <dt>

[Using Column Persistence: Advanced Topics](using-column-persistence-advanced-topics.md)
</dt> </dl>

 

 




