---
title: Discovery Pages
description: Discovery Pages
ms.assetid: deb0cbf9-b7e1-4ce6-8241-b9199129515a
keywords:
- Windows Media Player online stores,discovery pages
- online stores,discovery pages
- type 1 online stores,discovery pages
- Windows Media Player library,discovery pages
- library,discovery pages
- discovery pages
ms.topic: article
ms.date: 05/31/2018
---

# Discovery Pages

If the active online store is a type 1 store, Windows Media Player displays the store's content in its user interface. The library tree-view control has a node for the online store. When the user clicks that node or any of its subnodes, Windows Media Player displays content from the online store in the details pane.

As the user interacts with online store content in the tree-view control or in the details pane, Windows Media Player displays webpages, called *discovery pages*, provided by the online store. Discovery pages provide additional information about the music as the user browses the online store's catalog. Discovery pages communicate with Windows Media Player through the properties, methods, and events of the [External object](external-object-for-type-1-online-stores.md).

Whenever Windows Media Player changes its view of the online store's content, it calls [IWMPContentPartner::GetTemplate](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-gettemplate), implemented by the online store's plug-in, to get the URL of the discovery page to display with the new view.

The view of online store content in Windows Media Player is characterized by five pieces of information: task, location type, location ID, selected item type, and selected item ID. Windows Media Player supplies those five items to the **GetTemplate** method in the *task*, *location*, *pContext*, *clickLocation*, and *pClickContext* parameters. Windows Media Player makes those five items available to discovery pages in the *task*, *libraryLocationType*, *libraryLocationID*, *selectedItemType*, and *selectedItemID* properties of the **External** object. For more information about how Windows Media Player specifies its view of online store content, see [Location and Selected Item](location-and-selected-item.md).

In addition to enabling a discovery page to communicate with Windows Media Player, the **External** object enables a discovery page to communicate with the online store's plug-in. When that happens, Windows Media Player acts as a bridge between the discovery page and the plug-in. For example, the discovery page can call [External.sendMessage](external-sendmessage.md) to send a custom message to the plug-in. Windows Media Player receives this method call and in turn calls [IWMPContentPartner::SendMessage](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-sendmessage) to pass the message to the plug-in. When the plug-in has finished processing the message, it calls [IWMPContentPartnerCallback::SendMessageComplete](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartnercallback-sendmessagecomplete). Windows Media Player then notifies the discovery page by raising the [External.OnSendMessageComplete](external-onsendmessagecomplete-event.md) event.

The **External** object also provides a way for a discovery page to communicate with another discovery page. When script on a discovery page calls [External.changeView](external-changeview.md), the script can supply a string in the *ViewParams* parameter. Windows Media Player does not interpret the *ViewParams* string, but it makes the string available to the next discovery page in the [External.viewParameters](external-viewparameters.md) property.

## Related topics

<dl> <dt>

[**About Type 1 Online Stores**](about-type-1-online-stores.md)
</dt> <dt>

[**Location and Selected Item**](location-and-selected-item.md)
</dt> </dl>

 

 




