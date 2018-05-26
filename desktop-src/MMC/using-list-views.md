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

Many of the features associated with list views are provided by MMC interfaces. For example, [**IResultData**](iresultdata.md) allows snap-ins to manipulate items and the view style associated with the list view. **IResultData** methods include [**InsertItem**](iresultdata-insertitem.md) and [**DeleteItem**](iresultdata-deleteitem.md), which are used by snap-ins to insert or delete single items in the result pane. [**DeleteAllRsltItems**](iresultdata-deleteallrsltitems.md) allows deletion of all items in the pane. Snap-ins can find items or subitems by using [**FindItemByLParam**](iresultdata-finditembylparam.md). Single items can be set or retrieved using [**SetItem**](iresultdata-setitem.md) and [**GetItem**](iresultdata-getitem.md). The next item can be retrieved by using [**GetNextItem**](iresultdata-getnextitem.md). The view mode can be set or retrieved by using [**SetViewMode**](iresultdata-setviewmode.md) and [**GetViewMode**](iresultdata-getviewmode.md). The state of a particular item can be modified with [**ModifyItemState**](iresultdata-modifyitemstate.md) and the result pane's view style can be set with [**ModifyViewStyle**](iresultdata-modifyviewstyle.md). Snap-ins can sort all items in the result pane with [**Sort**](iresultdata-sort.md) and, after changing an item being displayed, update the item using [**UpdateItem**](iresultdata-updateitem.md). The text for the result pane's description bar can be set by using [**SetDescBarText**](iresultdata-setdescbartext.md).

The [**IConsoleVerb**](iconsoleverb.md) interface allows snap-ins to enable standard verbs including cut, copy, paste, delete, properties, rename, refresh, and print. [**SetVerbState**](iconsoleverb-setverbstate.md) enables a snap-in to set a given verb's button state, while [**GetVerbState**](iconsoleverb-getverbstate.md) is used to retrieve a verb's button state. The [**SetDefaultVerb**](iconsoleverb-setdefaultverb.md) and [**GetDefaultVerb**](iconsoleverb-getdefaultverb.md) methods allow a snap-in to set and retrieve the default action on an object.

[**IHeaderCtrl2**](iheaderctrl2.md) methods manipulate the number of columns and their text labels for the list view. With [**InsertColumn**](iheaderctrl2-insertcolumn.md), a snap-in can add a column to a list view; with [**DeleteColumn**](iheaderctrl2-deletecolumn.md) it can remove one. You can set the width of a column with [**SetColumnWidth**](iheaderctrl2-setcolumnwidth.md) and retrieve the current width with [**GetColumnWidth**](iheaderctrl2-getcolumnwidth.md). The [**SetColumnText**](iheaderctrl2-setcolumntext.md) method is available to set text in a specified column, and [**GetColumnText**](iheaderctrl2-getcolumntext.md) to retrieve current text.

Other [**IHeaderCtrl2**](iheaderctrl2.md) methods include [**SetChangeTimeOut**](iheaderctrl2-setchangetimeout.md), [**SetColumnFilter**](iheaderctrl2-setcolumnfilter.md), and [**GetColumnFilter**](iheaderctrl2-getcolumnfilter.md). These methods provide support for users to filter list views based on filters set on each column in the result view.

The [**IColumnData**](icolumndata.md) interface allows snap-ins to access column configuration data that MMC persists in memory when the user customizes list view columns. Specifically, the user can:

-   Change the width of a column.
-   Reorder columns.
-   Hide or display columns.
-   Sort columns.

[**GetColumnConfigData**](icolumndata-getcolumnconfigdata.md) enables a snap-in to retrieve the current width, order, and hidden status of a set of columns in a list view. [**SetColumnConfigData**](icolumndata-setcolumnconfigdata.md) allows the snap-in to set this information. The [**GetColumnSortData**](icolumndata-getcolumnsortdata.md) and [**SetColumnSortData**](icolumndata-setcolumnsortdata.md) methods allow a snap-in to retrieve and set the sorted column and sorting direction for a column set.

With the [**IImageList**](iimagelist.md) interface, the snap-in can insert images to be used as icons for items in the result pane. [**ImageListSetIcon**](iimagelist-imagelistseticon.md) is used to set an icon in an image list, and [**ImageListSetStrip**](iimagelist-imagelistsetstrip.md) enables a snap-in to set a strip of icons in an image list.

A snap-in adds support for virtual lists by implementing the [**IResultOwnerData**](iresultownerdata.md) interface. For more information, see [Owner Data/Virtual Lists](owner-data-virtual-lists.md).

The [**RESULTDATAITEM**](resultdataitem.md) structure is used frequently to accomplish much of the work associated with the result pane.

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

 

 




