---
title: Owner Data/Virtual Lists
description: Virtual list views, also known as owner data, appear to the user as any other list view but the underlying code to populate them is optimized for large data sets.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f02a4045-977a-4e52-93bd-7defa4fd1d89
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- owner data/virtual lists MMC
- virtual lists MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Owner Data/Virtual Lists

Virtual list views, also known as *owner data*, appear to the user as any other list view but the underlying code to populate them is optimized for large data sets. List views that contain more than several hundred items generally achieve significant performance improvement as virtual lists. The decision to use a virtual list view should be based on the cost of fetching the data as well as the volume of data. In the case of a remote database query with a huge result set a virtual list view would be an obvious choice. In other less clear-cut circumstances the snap-in developer should try both list view types before making a final choice.

A virtual list-view control maintains very little item state information itself. Except for the item selection and focus information, all item information must be managed by the snap-in. MMC requests item information from the snap-in by calling the snap-in's [**IComponent::GetDisplayInfo**](icomponent-getdisplayinfo.md) implementation.

A snap-in adds support for virtual lists by implementing the [**IResultOwnerData**](iresultownerdata.md) interface. MMC calls the snap-in's [**FindItem**](iresultownerdata-finditem.md) implementation to find the next item in a virtual list matching a user-specified string. The [**SortItems**](iresultownerdata-sortitems.md) method sorts the items of a virtual list. MMC calls the snap-in's implementation of this method when the user clicks the header item of a virtual list or when the snap-in calls [**IResultData::Sort**](iresultdata-sort.md).

Because a virtual list control is intended for large data sets, it is recommended that you cache requested item data to improve retrieval performance. The list view provides a cache-hinting mechanism to assist in optimizing the cache. MMC calls the [**CacheHint**](iresultownerdata-cachehint.md) method when it is about to request display information by successfully calling the snap-in's [**IComponent::GetDisplayInfo**](icomponent-getdisplayinfo.md) method for a range of items in a virtual list. **CacheHint** allows the snap-in to collect the information ahead of time in cases where an optimization can be made.

The [**IResultData**](iresultdata.md) interface handles virtual lists as well. Because of the nature of virtual lists, not all methods apply and some methods have limited functionality. The primary difference in handling virtual lists it that because MMC does not maintain any storage for virtual items, it does not provide item IDs. Instead virtual list items are identified by their list position (index).

Virtual list views are implemented in much the same way as standard list views, with a few notable differences.

**To implement a virtual list view**

1.  Implement the [**IComponent::GetResultViewType**](icomponent-getresultviewtype.md) method. The *ppViewType* parameter specifies the view type. For standard list views, the value of the parameter should be **NULL**, indicating that MMC should display the default view type (list view). Specify the view options with the *pViewOptions* parameter. Use the MMC\_VIEW\_OPTIONS\_OWNERDATALIST option to specify a virtual list view.
2.  Follow all instructions except for Step 1 in [Using List Views: Implementation Details](using-list-views-implementation-details.md).
3.  Implement the [**IResultOwnerData**](iresultownerdata.md) interface. If necessary, develop a mechanism for caching the requested items in the virtual list view to improve performance. Implement the [**CacheHint**](iresultownerdata-cachehint.md) method for optimizing retrievals.

## Related topics

<dl> <dt>

[Using List Views](using-list-views.md)
</dt> </dl>

 

 




