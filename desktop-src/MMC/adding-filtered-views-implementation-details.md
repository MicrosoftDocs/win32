---
title: Adding Filtered Views Implementation Details
description: Adding Filtered Views Implementation Details
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 05541da0-47c4-452e-a7b3-adcc54ac2e7d
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- filtered views MMC , implementation details
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Adding Filtered Views: Implementation Details

## To implement a filtered view

1.  Notify MMC that the snap-in supports filtered view by setting the **MMC\_VIEW\_OPTIONS\_FILTERED** flag in the *pViewOptions* parameter returned by [**IComponent::GetResultViewType**](/windows/win32/Mmc/nf-mmc-icomponent-getresultviewtype?branch=master).

    A Filtered menu item is added to the **View** menu when the snap-in notifies MMC that it supports filtered view.

2.  Turn on filtered view. There are two ways to do this:

    -   The user can click Filtered on the **View** menu.
    -   The snap-in can programmatically set the view mode to filtered view by calling [**IResultData::SetViewMode**](/windows/win32/Mmc/nf-mmc-iresultdata-setviewmode?branch=master) with **MMCLV\_VIEWSTYLE\_FILTERED** passed in the *lViewMode* parameter. For a scenario where you could use **IResultData::SetViewMode**, see [Using List Views: Implementation Details](using-list-views-implementation-details.md).

    When the user clicks the Filtered menu item or the snap-in programmatically sets the view mode to filtered view, MMC turns on the filtered view and sends the snap-in an [**MMCN\_FILTER\_CHANGE**](mmcn-filter-change.md) notification, indicating that filtering has been enabled.

    MMC takes care of creating the filter header controls on each column of the result view. Each filter header control has a text box (for the filter value) and a filter button that enables the user to change the filter operator.

3.  Handle the [**MMCN\_FILTER\_CHANGE**](mmcn-filter-change.md) notification in the [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) method.

    MMC calls [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) with [**MMCN\_FILTER\_CHANGE**](mmcn-filter-change.md) as the event parameter when filtering has been enabled or disabled, or when a filter value has changed. The arg parameter is a value of enumerated type [**MMC\_FILTER\_CHANGE\_CODE**](/windows/win32/Mmc/ne-mmc-_mmc_filter_change_code?branch=master) that specifies the type of change.

    Here are the values for [**MMC\_FILTER\_CHANGE\_CODE**](/windows/win32/Mmc/ne-mmc-_mmc_filter_change_code?branch=master) and how the snap-in should handle them:

    <dl> <dt>

<span id="MFCC_ENABLE"></span><span id="mfcc_enable"></span>**MFCC\_ENABLE**
</dt> <dd>

    Indicates that filtered view was turned on.

    If this is the first time the snap-in has switched to filtered view, the snap-in can initialize its column filters and filtering mechanisms here. The snap-in can use the [**IHeaderCtrl2::SetColumnFilter**](/windows/win32/Mmc/nf-mmc-iheaderctrl2-setcolumnfilter?branch=master) method to set the filter value and its maximum character length for each column. It can use the [**IHeaderCtrl2::SetChangeTimeOut**](/windows/win32/Mmc/nf-mmc-iheaderctrl2-setchangetimeout?branch=master) method to set the filter change notification time-out. This time-out value is applied to all columns in the filtered list. The snap-in could also set the default filter operator for each column at this point. Be aware that the snap-in is responsible for storing, setting, and enabling the user to change the filter operator on each column.

    Be aware that if the snap-in does not call [**IHeaderCtrl2::SetColumnFilter**](/windows/win32/Mmc/nf-mmc-iheaderctrl2-setcolumnfilter?branch=master) to set the filter data for a column, MMC sets the filter type to string filter and specifies no default value for the filter.

    If a filtered view has been restored after switching to another view type or another scope item, the snap-in can either restore the last filtered view state or reinitialize the filters.

    </dd> <dt>

<span id="MFCC_DISABLE"></span><span id="mfcc_disable"></span>**MFCC\_DISABLE**
</dt> <dd>

    Indicates that filtered view was turned off.

    The snap-in can store the current filter settings so that it can restore them when the filtered view is enabled again.

    </dd> <dt>

<span id="MFCC_VALUE_CHANGE"></span><span id="mfcc_value_change"></span>**MFCC\_VALUE\_CHANGE**
</dt> <dd>

    Indicates that the filter value for a column in a result view list has changed. The param parameter of the [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) method contains the column ID.

    The snap-in can apply the filter for the specified column here. The snap-in must implement its own mechanism to filter the result list (see the next Step).

    MMC sends this notification in the following cases:

    -   If the user edits a column filter and either presses ENTER to apply the filter or switches to another column.
    -   If text has been typed and the filter change interval elapses with no further keystrokes. The filter change interval can be set using [**IHeaderCtrl2::SetChangeTimeOut**](/windows/win32/Mmc/nf-mmc-iheaderctrl2-setchangetimeout?branch=master).
    -   If the snap-in returns **S\_OK** in response to an [**MMCN\_FILTERBTN\_CLICK**](mmcn-filterbtn-click.md) notification.

    </dd> </dl>

4.  Implement one or more methods to filter the result list.

    The snap-in is responsible for hiding or adding items in the result list based on the filter values and filter operators set on the columns. Be aware that the filter value of a column is the value that the snap-in compares with the values in that column to determine whether an item should be added or removed in the list. The filter operator is the comparison operator that is used to compare the filter value against the column value of each item. The filter operators supported are determined by the snap-in.

    The snap-in uses [**IHeaderCtrl2::GetColumnFilter**](/windows/win32/Mmc/nf-mmc-iheaderctrl2-getcolumnfilter?branch=master) to get the filter value set on the specified column. The snap-in is responsible for setting, storing, and maintaining the filter operator for each column. The snap-in can implement a method that completely rebuilds the result list by removing all items and re-adding them appropriately, or the snap-in can manipulate the existing items in the result list.

5.  Handle the [**MMCN\_FILTERBTN\_CLICK**](mmcn-filterbtn-click.md) notification in the [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) method.

    MMC calls [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) with [**MMCN\_FILTERBTN\_CLICK**](mmcn-filterbtn-click.md) as the event parameter when the user clicks the filter button in a filter header control. The *arg* parameter is the column ID of the column whose filter button was clicked.

    The snap-in is responsible for the user interface that enables the user to change the filter operator. Usually, a menu is a sufficient user interface to make filter operator changes.

    Therefore, the snap-in must handle the [**MMCN\_FILTERBTN\_CLICK**](mmcn-filterbtn-click.md) notification by presenting some user interface to enable the user to specify a new filter operator. The *param* value points to the coordinates of the filter button. The snap-in can use those coordinates to calculate the placement of the user interface used to change the filter operator.

    After the snap-in has handled the filter operator changes, it can return **S\_OK** to generate an [**MMCN\_FILTER\_CHANGE**](mmcn-filter-change.md) notification with *arg* set to **MFCC\_VALUE\_CHANGE** and *param* set to the column ID.

## Related topics

<dl> <dt>

[Adding Filtered Views: Interfaces](adding-filtered-views-interfaces.md)
</dt> </dl>

 

 




