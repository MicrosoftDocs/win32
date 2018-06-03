---
title: Using List Views Interfaces
description: The MMC SDK specifies a number of interfaces and other language constructs for working with list views.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3b97ae4e-c8a1-4793-b4e5-b3823288b85d
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- list views MMC , interfaces
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using List Views: Interfaces

The MMC SDK specifies a number of interfaces and other language constructs for working with list views. The following interfaces are available:

-   [**IColumnData**](/windows/desktop/api/Mmc/nn-mmc-icolumndata)
-   [**IConsoleVerb**](/windows/desktop/api/Mmc/nn-mmc-iconsoleverb)
-   [**IHeaderCtrl2**](/windows/desktop/api/Mmc/nn-mmc-iheaderctrl2)
-   [**IImageList**](/windows/desktop/api/Mmc/nn-mmc-iimagelist)
-   [**IResultData**](/windows/desktop/api/Mmc/nn-mmc-iresultdata)
-   [**IResultDataCompare**](/windows/desktop/api/Mmc/nn-mmc-iresultdatacompare)
-   [**IResultDataCompareEx**](/windows/desktop/api/Mmc/nn-mmc-iresultdatacompareex)
-   [**IResultOwnerData**](/windows/desktop/api/Mmc/nn-mmc-iresultownerdata) (for virtual list views)

For more information about these interfaces, see [Using List Views](using-list-views.md) and refer to their detailed descriptions in the Reference section of the MMC SDK.

## Other Constructs

The MMC SDK specifies a number of notifications for working with list views. Here is a list of the most common notifications. For a complete listing of all notifications, see [MMC Notifications](mmc-notifications.md) in the Reference section of the MMC SDK.

-   [**MMCN\_ADD\_IMAGES**](mmcn-add-images.md)
-   [**MMCN\_COLUMN\_CLICK**](mmcn-column-click.md)
-   [**MMCN\_RENAME**](mmcn-rename.md)
-   [**MMCN\_RESTORE\_VIEW**](mmcn-restore-view.md)
-   [**MMCN\_SELECT**](mmcn-select.md)
-   [**MMCN\_SHOW**](mmcn-show.md)
-   [**MMCN\_VIEW\_CHANGE**](mmcn-view-change.md)

The following enumeration types are the most common types used with list views. For a complete listing of all enumeration types, see [MMC Enumerations](mmc-enumerations.md) in the Reference section of the MMC SDK.

-   [**MMC\_BUTTON\_STATE**](/windows/desktop/api/Mmc/ne-mmc-_mmc_button_state)
-   [**MMC\_CONSOLE\_VERB**](/windows/desktop/api/Mmc/ne-mmc-_mmc_console_verb)
-   [**MMC\_FILTER\_CHANGE\_CODE**](/windows/desktop/api/Mmc/ne-mmc-_mmc_filter_change_code)
-   [**MMC\_FILTER\_TYPE**](/windows/desktop/api/Mmc/ne-mmc-_mmc_filter_type)
-   [**MMC\_NOTIFY\_TYPE**](/windows/desktop/api/Mmc/ne-mmc-_mmc_notify_type)
-   [**MMC\_RESULT\_VIEW\_STYLE**](/windows/desktop/api/Mmc/ne-mmc-_mmc_result_view_style)

The following structures are the most common ones used with list views. See [MMC Structures](console-structures.md) in the Reference section of the MMC SDK for a complete listing.

-   [**MMC\_RESTORE\_VIEW**](/windows/desktop/api/Mmc/ns-mmc-_mmc_restore_view)
-   [**RESULTDATAITEM**](/windows/desktop/api/Mmc/ns-mmc-_resultdataitem)

## Related topics

<dl> <dt>

[Using List Views: Implementation Details](using-list-views-implementation-details.md)
</dt> </dl>

 

 




