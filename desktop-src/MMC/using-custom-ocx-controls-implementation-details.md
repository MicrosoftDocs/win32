---
title: Using Custom OCX Controls Implementation Details
description: Using Custom OCX Controls Implementation Details
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cefe4fae-8660-424d-89fb-faa702ddaa20'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["custom OCX controls MMC , implementation details"]
---

# Using Custom OCX Controls: Implementation Details

## To start a custom OCX control in the result pane

1.  Implement a mechanism for storing the selected view type (for example, standard list view or OCX view) and the user's view preference. This allows a standard list view or the OCX view to be loaded when MMC calls [**IComponent::GetResultViewType**](icomponent-getresultviewtype.md) to display the result pane for a particular scope item in your snap-in.
2.  Handle selection of the OCX view in the [**IComponent::GetResultViewType**](icomponent-getresultviewtype.md) method.

    For a custom view provided by an OLE custom control (OCX), the ppViewType parameter should point to the address of a string that contains the string representation of the custom control's CLSID. The string must begin with an open brace ({) and end with a close brace (}). [**GetResultViewType**](icomponent-getresultviewtype.md) expects a CLSID for the OCX control when the first character of the string is a brace. Be aware that the snap-in must allocate the string with the [**CoTaskMemAlloc**](_com_cotaskmemalloc) Windows API function.

    The following string represents the Calendar control and could be returned in the ppViewType parameter to display the Calendar control in the result view pane:

    {8E27C92B-1264-101C-8A2F-040224009C02}

    MMC allows a single instance of each OCX type per snap-in instance per view. If the MMC\_VIEW\_OPTIONS\_CREATENEW option is selected for the pViewOptions parameter, MMC will destroy the cached OCX control and create a new one every time an item requests the OCX view. Otherwise, MMC will display the cached OCX control instance for any of the snap-in's items that request this OCX view.

3.  Handle the [**MMCN\_SHOW**](mmcn-show.md) notification message sent to the snap-in's [**IComponent::Notify**](icomponent-notify.md) implementation. In particular, keep the following things in mind:

    -   Your snap-in can interact with the OCX control placed in the result pane. To do so, during MMCN\_SHOW, call [**IConsole2::QueryResultView**](iconsole2-queryresultview.md) to query for the OCX control object's IUnknown interface pointer.
    -   During [**MMCN\_SHOW**](mmcn-show.md), the snap-in should cache the cookie (of the scope item) passed in the call to [**IComponent::Notify**](icomponent-notify.md) in the lpDataObject argument. The snap-in needs the cookie to identify the correct scope item when MMC sends it an [**MMCN\_SELECT**](mmcn-select.md) or MMCN\_DESELECTALL notification message with a special data object (DOBJ\_CUSTOMOCX or DOBJ\_CUSTOMWEB).

        For snap-ins that have a custom result pane (OCX or web), MMC sends the [**MMCN\_SELECT**](mmcn-select.md) or MMCN\_DESELECTALL notification with a special data object when the result pane is selected or deselected. The only way for snap-ins to identify the corresponding scope item is to use the cookie cached during MMCN\_SHOW.

        Be aware that, to make sure that the data object is DOBJ\_CUSTOMOCX (for OCX views), the snap-in should check the data object using the [**IS\_SPECIAL\_DATAOBJECT**](is-special-dataobject.md) macro before dereferencing it.

    -   Upon deselection of the result pane with the OCX view, the arg parameter of [**MMCN\_SHOW**](mmcn-show.md) is set to **FALSE**, indicating that the OCX view is going out of focus. At this time, the snap-in can do any necessary clean-up.

4.  MMC sends the snap-in's [**IComponent**](icomponent.md) implementation an [**MMCN\_INITOCX**](mmcn-initocx.md) notification message when its OCX control is initialized for the first time. During MMCN\_INITOCX, the snap-in can perform any initialization procedures required by the OCX control.

    The param parameter passed in the call to [**IComponent::Notify**](icomponent-notify.md) (with MMCN\_INITOCX) contains the same IUnknown interface pointer obtained by calling [**IConsole2::QueryResultView**](iconsole2-queryresultview.md) during the handling of the [**MMCN\_SHOW**](mmcn-show.md) notification.

5.  If necessary, implement a mechanism by which the OCX control can communicate with the snap-in. One method is for the snap-in to expose a COM interface that the OCX control can call. Be aware that the OCX control runs in the same thread as the snap-in, so you only need to deal with threading issues if the OCX control is multithreaded.
6.  If necessary, handle the [**MMCN\_RESTORE\_VIEW**](mmcn-restore-view.md) notification message. The notification is sent to the snap-in's [**IComponent::Notify**](icomponent-notify.md) method when the result pane for a scope item must be restored by the snap-in after the user has navigated the view history using the **Back** or **Forward** buttons.

    By handling the notification, the snap-in can find out what the view type and view options were the last time the result pane was displayed. This is particularly important if, for example, the [**IComponent**](icomponent.md) associated with the corresponding scope item supports multiple view types. Say the result pane supports two view types: list view and OCX view. The default view type is list view. The user selects another scope item and then presses the **Back** button to return to the same item. The user expects the OCX view, but the snap-in's default behavior is to display the list view. By looking at the [**MMCN\_RESTORE\_VIEW**](mmcn-restore-view.md) notification, the snap-in can find out what the view type and the view options were the last time the result pane was displayed and perform the necessary Steps to return the result pane to its previous state.

7.  If the snap-in adds items to the Action menu when the OCX view is displayed in the result pane, MMC calls the [**IExtendContextMenu::AddMenuItems**](iextendcontextmenu-addmenuitems.md) method of the corresponding [**IComponent**](icomponent.md) implementation with a special data object for the OCX view. To make sure that the data object is DOBJ\_CUSTOMOCX (for OCX views), the snap-in should check the data object using the [**IS\_SPECIAL\_DATAOBJECT**](is-special-dataobject.md) macro before dereferencing it. Furthermore, using the cookie cached during [**MMCN\_SHOW**](mmcn-show.md) in Step 3, the snap-in can identify the scope item corresponding to the OCX view and then add menu items accordingly.
8.  If necessary, handle the [**MMCN\_BTN\_CLICK**](mmcn-btn-click.md) notification. For an OCX view for which the MMC\_VERB\_PROPERTIES verb is enabled, when the user clicks the **Properties** button on the console toolbar, MMC sends the snap-in an **MMCN\_BTN\_CLICK** notification message. The notification's param argument contains the MMC\_VERB\_PROPERTIES enumerator value, and its lpDataObject argument contains a special data object (DOBJ\_CUSTOMOCX). If required, the snap-in can identify the scope item that corresponds to the OCX view by using the cookie it cached during [**MMCN\_SHOW**](mmcn-show.md) as described in Step 3 above.

## Related topics

<dl> <dt>

[Using Custom OCX Controls: Interfaces](using-custom-ocx-controls-interfaces.md)
</dt> </dl>

 

 




