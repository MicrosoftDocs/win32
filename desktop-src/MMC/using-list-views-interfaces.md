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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using List Views: Interfaces

The MMC SDK specifies a number of interfaces and other language constructs for working with list views. The following interfaces are available:

-   [**IColumnData**](/windows/win32/Mmc/nn-mmc-icolumndata?branch=master)
-   [**IConsoleVerb**](/windows/win32/Mmc/nn-mmc-iconsoleverb?branch=master)
-   [**IHeaderCtrl2**](/windows/win32/Mmc/nn-mmc-iheaderctrl2?branch=master)
-   [**IImageList**](/windows/win32/Mmc/nn-mmc-iimagelist?branch=master)
-   [**IResultData**](/windows/win32/Mmc/nn-mmc-iresultdata?branch=master)
-   [**IResultDataCompare**](/windows/win32/Mmc/nn-mmc-iresultdatacompare?branch=master)
-   [**IResultDataCompareEx**](/windows/win32/Mmc/nn-mmc-iresultdatacompareex?branch=master)
-   [**IResultOwnerData**](/windows/win32/Mmc/nn-mmc-iresultownerdata?branch=master) (for virtual list views)

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

-   [**MMC\_BUTTON\_STATE**](/windows/win32/Mmc/ne-mmc-_mmc_button_state?branch=master)
-   [**MMC\_CONSOLE\_VERB**](/windows/win32/Mmc/ne-mmc-_mmc_console_verb?branch=master)
-   [**MMC\_FILTER\_CHANGE\_CODE**](/windows/win32/Mmc/ne-mmc-_mmc_filter_change_code?branch=master)
-   [**MMC\_FILTER\_TYPE**](/windows/win32/Mmc/ne-mmc-_mmc_filter_type?branch=master)
-   [**MMC\_NOTIFY\_TYPE**](/windows/win32/Mmc/ne-mmc-_mmc_notify_type?branch=master)
-   [**MMC\_RESULT\_VIEW\_STYLE**](/windows/win32/Mmc/ne-mmc-_mmc_result_view_style?branch=master)

The following structures are the most common ones used with list views. See [MMC Structures](console-structures.md) in the Reference section of the MMC SDK for a complete listing.

-   [**MMC\_RESTORE\_VIEW**](/windows/win32/Mmc/ns-mmc-_mmc_restore_view?branch=master)
-   [**RESULTDATAITEM**](/windows/win32/Mmc/ns-mmc-_resultdataitem?branch=master)

## Related topics

<dl> <dt>

[Using List Views: Implementation Details](using-list-views-implementation-details.md)
</dt> </dl>

 

 




