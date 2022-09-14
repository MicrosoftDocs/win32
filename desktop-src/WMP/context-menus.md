---
title: Context Menus
description: Context Menus
ms.assetid: d1ea899a-9087-4502-8825-5cef1a87ef03
keywords:
- Windows Media Player online stores,context menus
- online stores,context menus
- type 1 online stores,context menus
- Windows Media Player online stores,custom context menus
- online stores,custom context menus
- type 1 online stores,custom context menus
- context menus
- custom context menus
ms.topic: article
ms.date: 05/31/2018
---

# Context Menus

Online stores can provide custom context menus. To do this, the online store plug-in implements the [IWMPContentPartner::GetCommands](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getcommands) method. Windows Media Player calls this method to provide information about the location in the user interface where the context menu is displayed (where the user right-clicked). The plug-in returns an array of [WMPContextMenuInfo](/previous-versions/windows/desktop/api/contentpartner/ns-contentpartner-wmpcontextmenuinfo) structures that describe each context menu item, including a command ID for each.

After Windows Media Player has retrieved the array, the Player uses the array to build the context menu the user sees. When the user clicks an item in the context menu, the Player calls [IWMPContentPartner::InvokeCommand](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-invokecommand), passing the command ID associated with the menu item through the *dwCommandID* parameter. The Player also passes a library location value and an array of IDs that represents the items the menu was invoked upon, such as an array of track IDs. By using this information, the plug-in can start any appropriate process in response to the user's mouse click.

## Related topics

<dl> <dt>

[**About Type 1 Online Stores**](about-type-1-online-stores.md)
</dt> </dl>

 

 




