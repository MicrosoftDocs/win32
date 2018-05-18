---
title: Adding Filtered Views
description: A filtered view is an MMC standard list view.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4be29e44-7e64-4c2c-820b-26c6cfea0661'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["filtered views MMC", "filtered views MMC"]
---

# Adding Filtered Views

A filtered view is an MMC standard list view. MMC allows users to filter a list view in the result pane of a scope item based on filters set on each list view column. Filtered views can be set as an option on standard (non-virtual) list views or on virtual list views. Filtered views cannot be set for custom views (views implemented by an OCX control or a webpage).

When the user clicks the Filtered menu item (or the snap-in programmatically sets the view mode to filtered view), MMC turns on the filtered view and sends the snap-in an [**MMCN\_FILTER\_CHANGE**](mmcn-filter-change.md) notification, indicating that filtering has been enabled. MMC takes care of creating the filter header controls on each column of the result list. Each filter header control has a text box (for the filter value) and a filter button that enables the user to change the filter operator.

After the view mode has been set to filtered view, the snap-in is responsible for hiding or adding items in the result list based on the filter values and filter operators set on the columns. Be aware that the filter value is the value that the snap-in compares with the values in that column to determine whether an item should be added or removed in the list. The filter operator is the comparison operator that is used to compare the filter value against the column value of each item. The filter operators supported are determined by the snap-in.

The snap-in should update the filtered result view (based on the column filters) in the snap-in's notification handler for [**MMCN\_FILTER\_CHANGE**](mmcn-filter-change.md) when the arg value is MFCC\_VALUE\_CHANGE.

The snap-in is also responsible for the menu that enables the user to change the filter operator. The user clicks the filter button on the header control to force MMC to send an [**MMCN\_FILTERBTN\_CLICK**](mmcn-filterbtn-click.md) notification to the snap-in. The snap-in must handle the **MMCN\_FILTERBTN\_CLICK** notification and display a menu that enables the user to change the filter operator.

Be aware that the filtered view mode does not affect the sort settings on the result list.

## Related topics

<dl> <dt>

[Adding Filtered Views: Interfaces](adding-filtered-views-interfaces.md)
</dt> <dt>

[Adding Filtered Views: Implementation Details](adding-filtered-views-implementation-details.md)
</dt> </dl>

 

 




