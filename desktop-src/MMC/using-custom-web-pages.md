---
title: Using Custom Webpages
description: The result pane of an MMC console can host HTML pages that are located either locally on the computer with MMC or on an external Web server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d0c25ed9-60ff-4790-8e10-9962e7f77cb4
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- custom webpages MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Custom Webpages

The result pane of an MMC console can host HTML pages that are located either locally on the computer with MMC or on an external Web server.

This section discusses how to start a custom webpage in a snap-in.

**To start a custom webpage**

1.  Implement a mechanism for storing the selected view type (for example, standard list view or Web view) and the user's view preference. This allows a standard list view or the Web view to be loaded when MMC calls [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) to display the result pane for a particular scope item in your snap-in.
2.  Handle selection of the Web view in the [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) method.

    For a custom view provided by a webpage, ppViewType should point to the address of a string that contains the URL for the page. The following string represents the URL for the Microsoft website and could be returned in the *ppViewType* parameter to display the website in the result view pane.

    ``` syntax
    www.microsoft.com
    ```

3.  Handle the [**MMCN\_SHOW**](mmcn-show.md) notification message sent to the snap-in's [**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify) implementation. Also, consider the following:
    -   During MMCN\_SHOW, the snap-in should cache the cookie (of the scope item) passed in the call to [**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify) in the lpDataObject argument. The snap-in needs the cookie to identify the correct scope item when MMC sends it an MMCN\_SELECT or MMCN\_DESELECTALL notification message with a special data object (DOBJ\_CUSTOMOCX or DOBJ\_CUSTOMWEB).

        For snap-ins that have a custom result pane (OCX or web), MMC sends the MMCN\_SELECT or MMCN\_DESELECTALL notification with a special data object when the result pane is selected or deselected. The only way for snap-ins to identify the corresponding scope item is to use the cookie cached during MMCN\_SHOW.

        Be aware that, to make sure that the data object is DOBJ\_CUSTOMWEB (for web views), the snap-in should check the data object using the [**IS\_SPECIAL\_DATAOBJECT**](/windows/desktop/api/Mmc/nf-mmc-is_special_dataobject) macro before dereferencing it.

    -   Upon deselection of the result pane with the web view, the arg parameter of MMCN\_SHOW is set to **FALSE**, indicating that the view is going out of focus. At this time, the snap-in can do any necessary clean-up.

4.  If necessary, handle the [**MMCN\_RESTORE\_VIEW**](mmcn-restore-view.md) notification message. The notification is sent to the snap-in's [**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify) method when the result pane for a scope item must be restored by the snap-in after the user has navigated the view history using the **Back** or **Forward** buttons.

    By handling the notification, the snap-in can find out what the view type and view options were the last time the result pane was displayed. This is particularly important if, for example, the [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) associated with the corresponding scope item supports multiple view types. Say the result pane supports two view types: list view and web view. The default view type is list view. The user selects another scope item and then presses the **Back** button to return to the same item. The user expects the web view, but the snap-in's default behavior is to display the list view. By looking at the [**MMCN\_RESTORE\_VIEW**](mmcn-restore-view.md) notification, the snap-in can find out what the view type and the view options were the last time the result pane was displayed and perform the necessary Steps to return the result pane to its previous state.

5.  If the snap-in adds items to the Action menu when the web view is displayed in the result pane, MMC calls the [**IExtendContextMenu::AddMenuItems**](/windows/desktop/api/Mmc/nf-mmc-iextendcontextmenu-addmenuitems) method of the corresponding [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) implementation with a special data object for the web view. To make sure that the data object is DOBJ\_CUSTOMWEB (for web views), the snap-in should check the data object using the [**IS\_SPECIAL\_DATAOBJECT**](/windows/desktop/api/Mmc/nf-mmc-is_special_dataobject) macro before dereferencing it. The snap-in can then determine what is selected on the web view and add menu items accordingly.

 

 




