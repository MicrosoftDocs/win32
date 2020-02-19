---
title: Displaying Dialog Boxes
description: Displaying Dialog Boxes
ms.assetid: 637555af-0a36-4aee-908f-496b52f7bd78
keywords:
- Windows Media Player online stores,displaying dialog boxes
- online stores,displaying dialog boxes
- type 1 online stores,displaying dialog boxes
- Windows Media Player online stores,dialog boxes
- online stores,dialog boxes
- type 1 online stores,dialog boxes
- displaying dialog boxes
ms.topic: article
ms.date: 05/31/2018
---

# Displaying Dialog Boxes

The online store can invoke dialog boxes through Windows Media Player. To do this, call [External.showPopup](external-showpopup.md) from the discovery page script code, providing a custom index value that represents the dialog box to display. This index value has meaning only to the online store code; Windows Media Player does not interpret this value. Windows Media Player then calls [IWMPContentPartner::GetItemInfo](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getiteminfo), passing g\_szItemInfo\_PopupURL for the *bstrInfoName* parameter and the index number for the *pContext* parameter. The plug-in then returns a **BSTR** containing the URL of the webpage to display in the dialog box and the Player shows the dialog box.

## Related topics

<dl> <dt>

[**Programming Guide for Type 1 Online Stores**](programming-guide-for-type-1-online-stores.md)
</dt> </dl>

 

 




