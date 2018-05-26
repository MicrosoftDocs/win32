---
title: Working with Context Menus
description: MMC generates default context menus for the items in the scope and result panes, and snap-ins can extend these default context menus by providing context menu items of their own.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b76b40da-1ab7-4b43-9c7e-03b901a6db3f
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- context menus MMC
- context menus MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Working with Context Menus

MMC generates default context menus for the items in the scope and result panes, and snap-ins can extend these default context menus by providing context menu items of their own. The default context menus contain items, for example, for the **New** and **All Tasks** menus. These default menus are integral to the usability of the console, because they provide lists of the methods (or tasks) that can be invoked on a given item or a list of the objects that can be created within a given container.

Snap-ins add their own items to the default context menus by implementing the [**IExtendContextMenu**](/windows/win32/Mmc/nn-mmc-iextendcontextmenu?branch=master) interface. The snap-in's implementation of **IExtendContextMenu** calls methods in [**IContextMenuCallback**](/windows/win32/Mmc/nn-mmc-icontextmenucallback?branch=master), which is implemented by MMC. Some snap-ins also call methods in [**IContextMenuProvider**](/windows/win32/Mmc/nn-mmc-icontextmenuprovider?branch=master) (also implemented by MMC) when they need to build a context menu from scratch.

[**IContextMenuCallback**](/windows/win32/Mmc/nn-mmc-icontextmenucallback?branch=master) is a callback mechanism that has one method, [**AddItem**](/windows/win32/Mmc/nf-mmc-icontextmenucallback-additem?branch=master), for adding single items to a context menu. MMC provides the snap-in with an instance of **IContextMenuCallback** when one is required. Snap-ins should not call **QueryInterface** for an instance of **IContextMenuCallback**, nor should they keep the instance of [**IContextMenuProvider**](/windows/win32/Mmc/nn-mmc-icontextmenuprovider?branch=master) beyond the scope in which it is provided.

The [**IExtendContextMenu**](/windows/win32/Mmc/nn-mmc-iextendcontextmenu?branch=master) interface is implemented by the snap-in and allows items to be added using the callback mechanism just mentioned. MMC calls the [**IExtendContextMenu::AddMenuItems**](/windows/win32/Mmc/nf-mmc-iextendcontextmenu-addmenuitems?branch=master) method to give the extension an opportunity to add menu items. The snap-in typically calls the [**IContextMenuCallback::AddItem**](/windows/win32/Mmc/nf-mmc-icontextmenucallback-additem?branch=master) method zero or more times to add items to the context menu. MMC calls the [**IExtendContextMenu::Command**](/windows/win32/Mmc/nf-mmc-iextendcontextmenu-command?branch=master) method if the user selects an item added by the snap-in in the **AddMenuItems** method call.

Most snap-ins do not need to use the [**IContextMenuProvider**](/windows/win32/Mmc/nn-mmc-icontextmenuprovider?branch=master) interface. This interface allows snap-ins to add extensible context menus to result pane views other than the default list view. For example, if the view is an OCX, the snap-in itself can create the context menu using the Windows API. However, using the Windows API does not allow other snap-ins to extend this context menu as they can on other items. Instead, the OCX should call **QueryInterface** for a pointer to the **IContextMenuProvider** interface, and generate the context menu using its COM methods. This context menu can then be extended by other snap-ins. Incidentally, **IContextMenuProvider** derives from [**IContextMenuCallback**](/windows/win32/Mmc/nn-mmc-icontextmenucallback?branch=master), so it implicitly contains the [**IContextMenuCallback::AddItem**](/windows/win32/Mmc/nf-mmc-icontextmenucallback-additem?branch=master) method.

[**IContextMenuProvider**](/windows/win32/Mmc/nn-mmc-icontextmenuprovider?branch=master) methods include [**EmptyMenuList**](/windows/win32/Mmc/nf-mmc-icontextmenuprovider-emptymenulist?branch=master), which clears the context menu, and [**ShowContextMenu**](/windows/win32/Mmc/nf-mmc-icontextmenuprovider-showcontextmenu?branch=master), which displays the menu. Its two remaining methods, [**AddPrimaryExtensionItems**](/windows/win32/Mmc/nf-mmc-icontextmenuprovider-addprimaryextensionitems?branch=master) and [**AddThirdPartyExtensionItems**](/windows/win32/Mmc/nf-mmc-icontextmenuprovider-addthirdpartyextensionitems?branch=master), give other snap-ins the opportunity to extend the context menu.

The snap-in that has added an item to the scope or result pane is always considered to "extend" the item's context menu. MMC always calls its implementation of the [**IExtendContextMenu::AddMenuItems**](/windows/win32/Mmc/nf-mmc-iextendcontextmenu-addmenuitems?branch=master) method if that snap-in implements the [**IExtendContextMenu**](/windows/win32/Mmc/nn-mmc-iextendcontextmenu?branch=master) interface. Snap-ins that wish to extend the context menus of items that they did not add must explicitly register themselves as being context menu extensions for items (scope or result) of that particular node type. For more information, see [Extending the Context Menu of a Primary Snap-in](extending-a-primary-snap-ins-context-menu.md).

When a snap-in adds a menu item, it must specify an insertion point in the context menu where that item should be located. The default context menus created by MMC contain a set of insertion points where snap-ins can add items. To maintain consistency, snap-ins can only add items at these predefined insertion points. Snap-ins creating context menus from scratch using the [**IContextMenuProvider**](/windows/win32/Mmc/nn-mmc-icontextmenuprovider?branch=master) interface must provide these insertion points to allow other extensions to add items to their context menus.

The [**CONTEXTMENUITEM**](/windows/win32/Mmc/ns-mmc-_contextmenuitem?branch=master) structure provides a variety of flags that can be set to manage MMC context menus, even when they are nested deeply and items are to be inserted in specific positions on the menu. MMC enforces menu integrity.

## Related topics

<dl> <dt>

[Working with Context Menus: Interfaces](working-with-context-menus-interfaces.md)
</dt> <dt>

[Working with Context Menus: Implementation Details](working-with-context-menus-implementation-details.md)
</dt> <dt>

[Extending a Primary Snap-in's Context Menu](extending-a-primary-snap-ins-context-menu.md)
</dt> <dt>

Extending the Context Menu of a Primary Snap-in
</dt> </dl>

 

 




