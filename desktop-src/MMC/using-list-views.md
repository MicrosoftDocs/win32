---
title: Using List Views
description: The default result pane view type is a list view.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bb484872-05ff-48b5-bad4-17dbdc1815f7
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- list views MMC
- list views MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using List Views

The default result pane view type is a list view. A list view displays a collection of items, each consisting of an icon and a label, and provides several ways to display and arrange the items. For example, additional information about each item can be displayed in columns to the right of the icon and label.

MMC implements list views using a list-view control. The control supports a number of view type modes, and the user can choose a mode by selecting a scope item and clicking **View** on the context menu. Be aware that snap-ins can programmatically set all view type modes.

Many of the features associated with list views are provided by MMC interfaces. For example, [**IResultData**](/windows/desktop/api/Mmc/nn-mmc-iresultdata) allows snap-ins to manipulate items and the view style associated with the list view. **IResultData** methods include [**InsertItem**](/windows/desktop/api/Mmc/nf-mmc-iresultdata-insertitem) and [**DeleteItem**](/windows/desktop/api/Mmc/nf-mmc-iresultdata-deleteitem), which are used by snap-ins to insert or delete single items in the result pane. [**DeleteAllRsltItems**](/windows/desktop/api/Mmc/nf-mmc-iresultdata-deleteallrsltitems) allows deletion of all items in the pane. Snap-ins can find items or subitems by using [**FindItemByLParam**](/windows/desktop/api/Mmc/nf-mmc-iresultdata-finditembylparam). Single items can be set or retrieved using [**SetItem**](/windows/desktop/api/Mmc/nf-mmc-iresultdata-setitem) and [**GetItem**](/windows/desktop/api/Mmc/nf-mmc-iresultdata-getitem). The next item can be retrieved by using [**GetNextItem**](/windows/desktop/api/Mmc/nf-mmc-iresultdata-getnextitem). The view mode can be set or retrieved by using [**SetViewMode**](/windows/desktop/api/Mmc/nf-mmc-iresultdata-setviewmode) and [**GetViewMode**](/windows/desktop/api/Mmc/nf-mmc-iresultdata-getviewmode). The state of a particular item can be modified with [**ModifyItemState**](/windows/desktop/api/Mmc/nf-mmc-iresultdata-modifyitemstate) and the result pane's view style can be set with [**ModifyViewStyle**](/windows/desktop/api/Mmc/nf-mmc-iresultdata-modifyviewstyle). Snap-ins can sort all items in the result pane with [**Sort**](/windows/desktop/api/Mmc/nf-mmc-iresultdata-sort) and, after changing an item being displayed, update the item using [**UpdateItem**](/windows/desktop/api/Mmc/nf-mmc-iresultdata-updateitem). The text for the result pane's description bar can be set by using [**SetDescBarText**](/windows/desktop/api/Mmc/nf-mmc-iresultdata-setdescbartext).

The [**IConsoleVerb**](/windows/desktop/api/Mmc/nn-mmc-iconsoleverb) interface allows snap-ins to enable standard verbs including cut, copy, paste, delete, properties, rename, refresh, and print. [**SetVerbState**](/windows/desktop/api/Mmc/nf-mmc-iconsoleverb-setverbstate) enables a snap-in to set a given verb's button state, while [**GetVerbState**](/windows/desktop/api/Mmc/nf-mmc-iconsoleverb-getverbstate) is used to retrieve a verb's button state. The [**SetDefaultVerb**](/windows/desktop/api/Mmc/nf-mmc-iconsoleverb-setdefaultverb) and [**GetDefaultVerb**](/windows/desktop/api/Mmc/nf-mmc-iconsoleverb-getdefaultverb) methods allow a snap-in to set and retrieve the default action on an object.

[**IHeaderCtrl2**](/windows/desktop/api/Mmc/nn-mmc-iheaderctrl2) methods manipulate the number of columns and their text labels for the list view. With [**InsertColumn**](https://www.bing.com/search?q=**InsertColumn**), a snap-in can add a column to a list view; with [**DeleteColumn**](https://www.bing.com/search?q=**DeleteColumn**) it can remove one. You can set the width of a column with [**SetColumnWidth**](https://www.bing.com/search?q=**SetColumnWidth**) and retrieve the current width with [**GetColumnWidth**](https://www.bing.com/search?q=**GetColumnWidth**). The [**SetColumnText**](https://www.bing.com/search?q=**SetColumnText**) method is available to set text in a specified column, and [**GetColumnText**](https://www.bing.com/search?q=**GetColumnText**) to retrieve current text.

Other [**IHeaderCtrl2**](/windows/desktop/api/Mmc/nn-mmc-iheaderctrl2) methods include [**SetChangeTimeOut**](/windows/desktop/api/Mmc/nf-mmc-iheaderctrl2-setchangetimeout), [**SetColumnFilter**](/windows/desktop/api/Mmc/nf-mmc-iheaderctrl2-setcolumnfilter), and [**GetColumnFilter**](/windows/desktop/api/Mmc/nf-mmc-iheaderctrl2-getcolumnfilter). These methods provide support for users to filter list views based on filters set on each column in the result view.

The [**IColumnData**](/windows/desktop/api/Mmc/nn-mmc-icolumndata) interface allows snap-ins to access column configuration data that MMC persists in memory when the user customizes list view columns. Specifically, the user can:

-   Change the width of a column.
-   Reorder columns.
-   Hide or display columns.
-   Sort columns.

[**GetColumnConfigData**](/windows/desktop/api/Mmc/nf-mmc-icolumndata-getcolumnconfigdata) enables a snap-in to retrieve the current width, order, and hidden status of a set of columns in a list view. [**SetColumnConfigData**](/windows/desktop/api/Mmc/nf-mmc-icolumndata-setcolumnconfigdata) allows the snap-in to set this information. The [**GetColumnSortData**](/windows/desktop/api/Mmc/nf-mmc-icolumndata-getcolumnsortdata) and [**SetColumnSortData**](/windows/desktop/api/Mmc/nf-mmc-icolumndata-setcolumnsortdata) methods allow a snap-in to retrieve and set the sorted column and sorting direction for a column set.

With the [**IImageList**](/windows/desktop/api/Mmc/nn-mmc-iimagelist) interface, the snap-in can insert images to be used as icons for items in the result pane. [**ImageListSetIcon**](/windows/desktop/api/Mmc/nf-mmc-iimagelist-imagelistseticon) is used to set an icon in an image list, and [**ImageListSetStrip**](/windows/desktop/api/Mmc/nf-mmc-iimagelist-imagelistsetstrip) enables a snap-in to set a strip of icons in an image list.

A snap-in adds support for virtual lists by implementing the [**IResultOwnerData**](/windows/desktop/api/Mmc/nn-mmc-iresultownerdata) interface. For more information, see [Owner Data/Virtual Lists](owner-data-virtual-lists.md).

The [**RESULTDATAITEM**](/windows/desktop/api/Mmc/ns-mmc-_resultdataitem) structure is used frequently to accomplish much of the work associated with the result pane.

## For more information, see:

-   [Using List Views: Interfaces](using-list-views-interfaces.md)
-   [Using List Views: Implementation Details](using-list-views-implementation-details.md)
-   [Owner Data/Virtual Lists](owner-data-virtual-lists.md)
-   [Exporting List Views to a File](exporting-list-views-to-a-file.md)
-   [Dynamically Updating List Views](dynamically-updating-list-views.md)

## Related topics

<dl> <dt>

[Owner Data/Virtual Lists](owner-data-virtual-lists.md)
</dt> <dt>

[Dynamically Updating List Views](dynamically-updating-list-views.md)
</dt> <dt>

[Exporting List Views to a File](exporting-list-views-to-a-file.md)
</dt> <dt>

[Using List Views: Interfaces](using-list-views-interfaces.md)
</dt> <dt>

[Using List Views: Implementation Details](using-list-views-implementation-details.md)
</dt> <dt>

[Adding Filtered Views](adding-filtered-views.md)
</dt> <dt>

[Using Column Persistence](using-column-persistence.md)
</dt> </dl>

 

 




