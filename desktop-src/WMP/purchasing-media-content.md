---
title: Purchasing Media Content
description: Purchasing Media Content
ms.assetid: df4a3152-f9e3-4a97-b021-6d5e8de9c184
keywords:
- Windows Media Player online stores,purchasing media content
- online stores,purchasing media content
- type 1 online stores,purchasing media content
- Windows Media Player online stores,media content purchases
- online stores,media content purchases
- type 1 online stores,media content purchases
- media content,purchasing
- purchasing media content
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Purchasing Media Content

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When Windows Media Player displays music content in the library tree view, the user interface includes elements that the user can click to buy the content. For example, the user might click a button to buy an individual song or to buy an entire album.

If the active online store is a Type 1 store, Windows Media Player has access to track, album, and list prices in the online store's catalog. Those prices in the catalog are strings that have a format understood only by the online store. Windows Media Player does not interpret price strings; it merely displays them in user interface elements like Buy buttons.

When Windows Media Player sets up a purchase for a set of media items, it passes the IDs and prices of the media items to the content partner plug-in by calling [IWMPContentPartner::CanBuySilent](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-canbuysilent). At that point, the plug-in can inspect the prices provided by the Player. These are the prices that the user expects to pay; that is, the prices that the Player displayed to the user. Based on the media IDs and prices provided by the Player, the plug-in calculates a total price, which it returns to the Player in the *bstrTotalPrice* parameter. The prices that the Player passes to **CanBuySilent** provide the plug-in with information, but they do not obligate the plug-in to return a certain total price. The plug-in can calculate the total price as it sees fit.

In addition to calculating the total price of a purchase, **CanBuySilent** determines whether the purchace can proceed silently; that is, without displaying a dialog box. If **CanBuySilent** returns **True**, Windows Media Player simply changes the text on the Buy button to prompt the user to confirm the purchase. If **CanBuySilent** returns **False**, Windows Media Player displays a dialog box that prompts the user to confirm the purchase. The dialog box provides the user with information that summarizes the purchase like number of albums, number of individual tracks, and the total price (as returned by the plug-in).

After the user confirms the purchase, the Player calls [IWMPContentPartner::Buy](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-buy). This method call provides the plug-in with the same content container list as **CanBuySilent**. When calling **Buy**, Windows Media Player also provides a cookie (simply a **DWORD** value, unique for the session) that the plug-in can use to identify the transaction. When the transaction is completed, the plug-in must call [IWMPContentPartnerCallback::BuyComplete](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartnercallback-buycomplete), passing the original cookie value for the *dwBuyCookie* parameter, to notify the Player that the transaction is finished.

## Related topics

<dl> <dt>

[**Programming Guide for Type 1 Online Stores**](programming-guide-for-type-1-online-stores.md)
</dt> </dl>

 

 




