---
title: Working with Context Menus Implementation Details
description: Working with Context Menus Implementation Details
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9432592c-9d24-462c-9d33-819f4ed5171f
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- context menus MMC , implementation details
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Working with Context Menus: Implementation Details

## To add context menu items using IExtendContextMenu

1.  Implement the [**IExtendContextMenu**](iextendcontextmenu.md) interface and its two methods, [**AddMenuItems**](iextendcontextmenu-addmenuitems.md) and [**Command**](iextendcontextmenu-command.md).

    To add context menu items to the context menu of a scope item, the snap-in's [**IComponentData**](icomponentdata.md) implementation should implement and expose the [**IExtendContextMenu**](iextendcontextmenu.md) interface.

    To add context menu items to the context menu of a result item, the snap-in's [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) implementation responsible for that result item and its result pane should implement and expose the [**IExtendContextMenu**](iextendcontextmenu.md) interface.

    Also, if the user selects a scope item and then displays its context menu, MMC will give both the snap-in's [**IComponentData**](icomponentdata.md) and [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) (that owns the current view) implementations the opportunity to add menu items. MMC calls the [**IExtendContextMenu::AddMenuItems**](iextendcontextmenu-addmenuitems.md) method implemented by the snap-in's **IComponent** to allow the snap-in to add menu items to the **View** menu. MMC calls the **IExtendContextMenu::AddMenuItems** method implemented by the snap-in's **IComponentData** to allow the snap-in to add menu items to all other menus. Only the snap-in's **IComponent** implementation can add items to the **View** menu.

    If the user displays a scope item's context menu without first selecting the scope item, MMC will only give the snap-in's [**IComponentData**](icomponentdata.md) implementation the opportunity to add menu items to all menus except the **View** menu. Consequently, the **View** menu only appears for a scope item if the user first selects an item.

2.  In the snap-in's implementation of [**AddMenuItems**](iextendcontextmenu-addmenuitems.md):

    -   MMC specifies in the *pInsertionAllowed* parameter passed in the call to [**AddMenuItems**](iextendcontextmenu-addmenuitems.md) the insertion points at which the snap-in can add context menu items. The snap-in should check the *pInsertionAllowed* flags for permission before attempting to add menu items at the MMC-defined insertion points. For example, a snap-in should not add menu items to **CCM\_INSERTIONPOINTID\_PRIMARY\_NEW** or **CCM\_INSERTIONPOINTID\_3RDPARTY\_NEW** unless the **CCM\_INSERTIONALLOWED\_NEW** flag is set.

        A primary snap-in is permitted to reset any of the insertion flags in its [**AddMenuItems**](iextendcontextmenu-addmenuitems.md) method as a way of restricting the kinds of menu items that a third-party extension can add. For example, the primary snap-in can clear the **CCM\_INSERTIONALLOWED\_NEW** flag to prevent extensions from adding their own New menu items.

        The primary snap-in should not attempt to set bits in *pInsertionAllowed* that were originally cleared. This is because future versions of MMC may use bits that are not currently defined. Third-party extensions should not attempt to change *pInsertionAllowed* at all.

    -   For each item that the snap-in must add at an MMC-defined insertion point or at another insertion point determined by the snap-in, fill a [**CONTEXTMENUITEM**](contextmenuitem.md) structure. For more information, see **CONTEXTMENUITEM**.
    -   For each item, add the item (its [**CONTEXTMENUITEM**](contextmenuitem.md) structure) to the context menu of the selected scope or result item by calling [**AddItem**](icontextmenucallback-additem.md) on the [**IContextMenuCallback**](icontextmenucallback.md) interface passed in the *piCallback* parameter in the call to the snap-in's [**IExtendContextMenu::AddMenuItems**](iextendcontextmenu-addmenuitems.md) method.

3.  In the snap-in's implementation of [**Command**](iextendcontextmenu-command.md):

    -   MMC calls [**Command**](iextendcontextmenu-command.md) with the same command identifier (*lCommandID*) that the snap-in assigned to the item in its [**CONTEXTMENUITEM**](contextmenuitem.md) structure when it added the item. The snap-in can process the command and then return **S\_OK**.
    -   MMC reserves negative-valued command IDs for predefined menu command IDs that it sends to a snap-in's [**Command**](iextendcontextmenu-command.md) method. The –1 command ID is the **MMCC\_STANDARD\_VIEW\_SELECT** enumerator value defined in mmc.h. This is sent to **Command** when the user clicks a standard view command on the **View** menu (Large, Small, List, or Detail). This notifies the snap-in that the user is switching away from a custom view (OCX, HTML). After getting an **MMCC\_STANDARD\_VIEW\_SELECT** command, the snap-in should request a standard view the next time its [**IComponent::GetResultViewType**](icomponent-getresultviewtype.md) method is called and not request a custom view until one of its custom view menu items is selected. If the snap-in only uses standard views or only uses custom views, it can ignore the **MMCC\_STANDARD\_VIEW\_SELECT** command.

## Related topics

<dl> <dt>

[Working with Context Menus](working-with-context-menus.md)
</dt> <dt>

[Working with Context Menus: Interfaces](working-with-context-menus-interfaces.md)
</dt> </dl>

 

 




