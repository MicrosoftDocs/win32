---
title: Recent Items
description: The Recent Items list is a pane in the Application Menu that displays the most recently used (MRU) items for an application.
ms.assetid: fdead358-d303-46de-9f8e-6fc2832d8e94
ms.topic: article
ms.date: 05/31/2018
---

# Recent Items

The Recent Items list is a pane in the [Application Menu](windowsribbon-controls-applicationmenu.md) that displays the most recently used (MRU) items for an application.

-   [Details](#details)
-   [Recent Items Properties](#recent-items-properties)
-   [Remarks](#remarks)
-   [Related topics](#related-topics)

## Details

The following screen shot illustrates a Recent Items list from WordPad for Windows 7).

![screen shot of the recent items list in the microsoft paint ribbon.](images/controls/recentitems.png)

The [Application Menu](windowsribbon-controls-applicationmenu.md) can have at most one [**ApplicationMenu.RecentItems**](windowsribbon-element-applicationmenu-recentitems.md) list, represented by an **ApplicationMenu.RecentItems** element, for displaying recent documents, pictures, movies, and other projects a user has been working on. The number of listed items ranges from zero to the maximum number specified in markup, with a default value of ten. The recent items are displayed as a numbered list of strings indicating file names. It is recommended that the [**Command.LabelDescription**](windowsribbon-element-command-labeldescription.md) property be used to give the full path for the file location, as shown in the following screen shot .

![screen shot of a recent items list in an application menu.](images/overviews/applicationmenu-menurecentitems.png)

The [**RecentItems**](windowsribbon-element-recentitems.md) element has an *EnablePinning* attribute that, if set to `true`, displays a pin icon to the right of each item in the list, as shown in the following screen shot.

> [!Note]  
> Pinning is enabled by default if the *EnablePinning* attribute is not specified.

 

![screen shot of recent items pinning in an application menu.](images/overviews/applicationmenu-menurecentitemspinned.png)

The pinning algorithm is intended to keep items from falling off the **Recent items** list. The algorithm produces the following behavior:

-   A new item is always added at the top of the **Recent items** list.
-   Items will move down in the list over time. Once the list is full (reaches the maximum number of items specified in markup), older items fall off the bottom of the list as new items are added to the top of the list.
-   If an item already appears somewhere in the list but is accessed again, it moves back to the top of the list.
-   If an item is pinned, it will still travel down the list, but it will not fall off the bottom. Instead, once the list is full, the first unpinned item above the pinned item will fall off when a new item is added to the list.
-   If the number of pinned items ever reaches the maximum number of items, then no new items will get added to the list until an item is unpinned.

## Recent Items Properties

The Ribbon framework defines a collection of [property keys](windowsribbon-reference-properties.md) for the Recent Items control.

Typically, a Recent Items property is updated in the ribbon UI by invalidating the Command associated with the control through a call to the [**IUIFramework::InvalidateUICommand**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand) method. The invalidation event is handled, and the property updates defined, by the [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method.

The [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method is not executed, and the application queried for an updated property value, until the property is required by the framework. For example, when a tab is activated and a control revealed in the ribbon UI, or when a tooltip is displayed.

> [!Note]  
> In some cases, a property can be retrieved through the [**IUIFramework::GetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty) method and set with the [**IUIFramework::SetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty) method.

 

The following table lists the property keys that are associated with the Recent Items control.



| Property Key                                                                       | Notes                                     |
|------------------------------------------------------------------------------------|-------------------------------------------|
| [UI\_PKEY\_Keytip](windowsribbon-reference-properties-uipkey-keytip.md)           | Can only be updated through invalidation. |
| [UI\_PKEY\_RecentItems](windowsribbon-reference-properties-uipkey-recentitems.md) | Can only be updated through invalidation. |



 

## Remarks

The [IApplicationDocumentLists::GetList](/windows/win32/api/shobjidl_core/nf-shobjidl_core-iapplicationdocumentlists-getlist) method can be used to retrieve the Windows Shell MRU list for the Ribbon application. The object retrieved by this method can then be used by the application to create the data required by the Ribbon framework to populate the **Recent items** list of the [Application Menu](windowsribbon-controls-applicationmenu.md).

> [!Note]  
> When using this method, *listtype* should have the value `ADLT_RECENT`.

 

For an example of how to implement an MRU items list in a Ribbon framework application, see the [HTMLEditRibbon Sample](windowsribbon-htmleditribbonsample.md).

## Related topics

<dl> <dt>

[Windows Ribbon Framework Control Library](windowsribbon-controls-entry.md)
</dt> <dt>

[**Recent items markup element**](windowsribbon-element-recentitems.md)
</dt> </dl>

 

 