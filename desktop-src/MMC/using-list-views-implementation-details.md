---
title: Using List Views Implementation Details
description: Using List Views Implementation Details
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 418a74bc-7ac1-42ae-9a19-1456b9f4ad89
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- list views MMC , implementation details
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using List Views: Implementation Details

**To implement a list view**

1.  Implement the [**IComponent::GetResultViewType**](/windows/win32/Mmc/nf-mmc-icomponent-getresultviewtype?branch=master) method. The *ppViewType* parameter specifies the view type. For standard list views, the value of the parameter should be **NULL**, indicating that MMC should display the default view type (list view). Specify the view options with the *pViewOptions* parameter. Use the **MMC\_VIEW\_OPTIONS\_NONE** option to specify no view options.

    Alternately, if [**IComponent::GetResultViewType**](/windows/win32/Mmc/nf-mmc-icomponent-getresultviewtype?branch=master) returns **S\_FALSE**, MMC will automatically set the view type to list view and the view options to **MMC\_VIEW\_OPTIONS\_NONE**.

2.  Handle the [**MMCN\_ADD\_IMAGES**](mmcn-add-images.md) notification message, which MMC sends to the snap-in's [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) implementation to request images for the result pane.
3.  Handle the [**MMCN\_SHOW**](mmcn-show.md) notification message, which MMC sends to the snap-in's [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) implementation to indicate that the result pane has the focus. In response to the notification, the snap-in should:

    -   If necessary, obtain interface pointers to the [**IHeaderCtrl2**](/windows/win32/Mmc/nn-mmc-iheaderctrl2?branch=master) and [**IResultData**](/windows/win32/Mmc/nn-mmc-iresultdata?branch=master) interfaces by querying the [**IConsole2**](/windows/win32/Mmc/nn-mmc-iconsole2?branch=master) interface for them. Make sure to use the **IConsole2** interface associated with the snap-in's [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) implementation, and not with its [**IComponentData**](/windows/win32/Mmc/nn-mmc-icomponentdata?branch=master) implementation.
    -   Add columns to the result pane using the [**IHeaderCtrl2::InsertColumn**](iheaderctrl2-insertcolumn.md) method.
    -   Enumerate the result data items for the result pane using the [**IResultData::InsertItem**](/windows/win32/Mmc/nf-mmc-iresultdata-insertitem?branch=master) method.
    -   If necessary, set the view mode and view style for the list view using [**IResultData::SetViewMode**](/windows/win32/Mmc/nf-mmc-iresultdata-setviewmode?branch=master) and [**IResultData::ModifyViewStyle**](/windows/win32/Mmc/nf-mmc-iresultdata-modifyviewstyle?branch=master), respectively. One of the view modes you can set is filtered view. For more information about this mode, see [Adding Filtered Views](adding-filtered-views.md).

4.  Implement the [**IComponent::GetDisplayInfo**](/windows/win32/Mmc/nf-mmc-icomponent-getdisplayinfo?branch=master) method. After the snap-in returns from the [**MMCN\_SHOW**](mmcn-show.md) notification handler, MMC calls its **IComponent::GetDisplayInfo** implementation once for each item in the result pane to request the item's display information.
5.  Handle the [**MMCN\_SELECT**](mmcn-select.md) notification message, which MMC sends after [**MMCN\_SHOW**](mmcn-show.md) to indicate which item in the scope pane is currently selected. In the notification handler, the snap-in has the opportunity to update the standard verbs for the scope item. See [Enabling MMC Standard Verbs](enabling-mmc-standard-verbs.md) for details.

    [**MMCN\_SELECT**](mmcn-select.md) is also sent when a result item is selected, at which time the snap-in can update the standard verbs for the selected item in the result pane.

## Related topics

<dl> <dt>

[Using List Views: Interfaces](using-list-views-interfaces.md)
</dt> </dl>

 

 




