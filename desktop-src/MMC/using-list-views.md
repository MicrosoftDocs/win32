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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using List Views

The default result pane view type is a list view. A list view displays a collection of items, each consisting of an icon and a label, and provides several ways to display and arrange the items. For example, additional information about each item can be displayed in columns to the right of the icon and label.

MMC implements list views using a list-view control. The control supports a number of view type modes, and the user can choose a mode by selecting a scope item and clicking **View** on the context menu. Be aware that snap-ins can programmatically set all view type modes.

Many of the features associated with list views are provided by MMC interfaces. For example, [**IResultData**](/windows/win32/Mmc/nn-mmc-iresultdata?branch=master) allows snap-ins to manipulate items and the view style associated with the list view. **IResultData** methods include [**InsertItem**](/windows/win32/Mmc/nf-mmc-iresultdata-insertitem?branch=master) and [**DeleteItem**](/windows/win32/Mmc/nf-mmc-iresultdata-deleteitem?branch=master), which are used by snap-ins to insert or delete single items in the result pane. [**DeleteAllRsltItems**](/windows/win32/Mmc/nf-mmc-iresultdata-deleteallrsltitems?branch=master) allows deletion of all items in the pane. Snap-ins can find items or subitems by using [**FindItemByLParam**](/windows/win32/Mmc/nf-mmc-iresultdata-finditembylparam?branch=master). Single items can be set or retrieved using [**SetItem**](/windows/win32/Mmc/nf-mmc-iresultdata-setitem?branch=master) and [**GetItem**](/windows/win32/Mmc/nf-mmc-iresultdata-getitem?branch=master). The next item can be retrieved by using [**GetNextItem**](/windows/win32/Mmc/nf-mmc-iresultdata-getnextitem?branch=master). The view mode can be set or retrieved by using [**SetViewMode**](/windows/win32/Mmc/nf-mmc-iresultdata-setviewmode?branch=master) and [**GetViewMode**](/windows/win32/Mmc/nf-mmc-iresultdata-getviewmode?branch=master). The state of a particular item can be modified with [**ModifyItemState**](/windows/win32/Mmc/nf-mmc-iresultdata-modifyitemstate?branch=master) and the result pane's view style can be set with [**ModifyViewStyle**](/windows/win32/Mmc/nf-mmc-iresultdata-modifyviewstyle?branch=master). Snap-ins can sort all items in the result pane with [**Sort**](/windows/win32/Mmc/nf-mmc-iresultdata-sort?branch=master) and, after changing an item being displayed, update the item using [**UpdateItem**](/windows/win32/Mmc/nf-mmc-iresultdata-updateitem?branch=master). The text for the result pane's description bar can be set by using [**SetDescBarText**](/windows/win32/Mmc/nf-mmc-iresultdata-setdescbartext?branch=master).

The [**IConsoleVerb**](/windows/win32/Mmc/nn-mmc-iconsoleverb?branch=master) interface allows snap-ins to enable standard verbs including cut, copy, paste, delete, properties, rename, refresh, and print. [**SetVerbState**](/windows/win32/Mmc/nf-mmc-iconsoleverb-setverbstate?branch=master) enables a snap-in to set a given verb's button state, while [**GetVerbState**](/windows/win32/Mmc/nf-mmc-iconsoleverb-getverbstate?branch=master) is used to retrieve a verb's button state. The [**SetDefaultVerb**](/windows/win32/Mmc/nf-mmc-iconsoleverb-setdefaultverb?branch=master) and [**GetDefaultVerb**](/windows/win32/Mmc/nf-mmc-iconsoleverb-getdefaultverb?branch=master) methods allow a snap-in to set and retrieve the default action on an object.

[**IHeaderCtrl2**](/windows/win32/Mmc/nn-mmc-iheaderctrl2?branch=master) methods manipulate the number of columns and their text labels for the list view. With [**InsertColumn**](iheaderctrl2-insertcolumn.md), a snap-in can add a column to a list view; with [**DeleteColumn**](iheaderctrl2-deletecolumn.md) it can remove one. You can set the width of a column with [**SetColumnWidth**](iheaderctrl2-setcolumnwidth.md) and retrieve the current width with [**GetColumnWidth**](iheaderctrl2-getcolumnwidth.md). The [**SetColumnText**](iheaderctrl2-setcolumntext.md) method is available to set text in a specified column, and [**GetColumnText**](iheaderctrl2-getcolumntext.md) to retrieve current text.

Other [**IHeaderCtrl2**](/windows/win32/Mmc/nn-mmc-iheaderctrl2?branch=master) methods include [**SetChangeTimeOut**](/windows/win32/Mmc/nf-mmc-iheaderctrl2-setchangetimeout?branch=master), [**SetColumnFilter**](/windows/win32/Mmc/nf-mmc-iheaderctrl2-setcolumnfilter?branch=master), and [**GetColumnFilter**](/windows/win32/Mmc/nf-mmc-iheaderctrl2-getcolumnfilter?branch=master). These methods provide support for users to filter list views based on filters set on each column in the result view.

The [**IColumnData**](/windows/win32/Mmc/nn-mmc-icolumndata?branch=master) interface allows snap-ins to access column configuration data that MMC persists in memory when the user customizes list view columns. Specifically, the user can:

-   Change the width of a column.
-   Reorder columns.
-   Hide or display columns.
-   Sort columns.

[**GetColumnConfigData**](/windows/win32/Mmc/nf-mmc-icolumndata-getcolumnconfigdata?branch=master) enables a snap-in to retrieve the current width, order, and hidden status of a set of columns in a list view. [**SetColumnConfigData**](/windows/win32/Mmc/nf-mmc-icolumndata-setcolumnconfigdata?branch=master) allows the snap-in to set this information. The [**GetColumnSortData**](/windows/win32/Mmc/nf-mmc-icolumndata-getcolumnsortdata?branch=master) and [**SetColumnSortData**](/windows/win32/Mmc/nf-mmc-icolumndata-setcolumnsortdata?branch=master) methods allow a snap-in to retrieve and set the sorted column and sorting direction for a column set.

With the [**IImageList**](/windows/win32/Mmc/nn-mmc-iimagelist?branch=master) interface, the snap-in can insert images to be used as icons for items in the result pane. [**ImageListSetIcon**](/windows/win32/Mmc/nf-mmc-iimagelist-imagelistseticon?branch=master) is used to set an icon in an image list, and [**ImageListSetStrip**](/windows/win32/Mmc/nf-mmc-iimagelist-imagelistsetstrip?branch=master) enables a snap-in to set a strip of icons in an image list.

A snap-in adds support for virtual lists by implementing the [**IResultOwnerData**](/windows/win32/Mmc/nn-mmc-iresultownerdata?branch=master) interface. For more information, see [Owner Data/Virtual Lists](owner-data-virtual-lists.md).

The [**RESULTDATAITEM**](/windows/win32/Mmc/ns-mmc-_resultdataitem?branch=master) structure is used frequently to accomplish much of the work associated with the result pane.

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

 

 




