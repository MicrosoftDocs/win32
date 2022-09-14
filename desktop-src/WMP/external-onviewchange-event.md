---
title: External.OnViewChange Event
description: Note This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The OnViewChange event occurs when the view changes in Windows Media Player.
ms.assetid: aa1378ad-8b84-4592-85c5-5e284be05ea6
keywords:
- External.OnViewChange Event Windows Media Player
topic_type:
- apiref
api_name:
- External.OnViewChange Event
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# External.OnViewChange Event

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **OnViewChange** event occurs when the view changes in Windows Media Player.

``` syntax
window.external.OnViewChange = FunctionName
```

## Possible Values

This is a write-only property that specifies the name of the function in script that Windows Media Player calls when the event occurs.

## Parameters

The function that handles this event takes no parameters.

## Remarks

The view in Windows Media Player can change for any of the following reasons:

-   The user interacts with the Windows Media Player user interface.
-   The user interacts with a discovery page, and script on the discovery page calls [External.changeView](external-changeview.md).
-   The user interacts with a discovery page, and script on the discovery page calls [External.changeViewOnlineList](external-changeviewonlinelist.md).

When the view changes in Windows Media Player, the Player calls [IWMPContentPartner::GetTemplate](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-gettemplate) to get the URL of the next discovery page to display. However, before the Player displays the new discovery page, it raises the **OnViewChange** event. If the **OnViewChange** event handler calls [External.cancelNavigate](external-cancelnavigate.md), Windows Media Player does not display the new discovery page. Instead, it continues to display the current discovery page.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11<br/>                                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.changeView**](external-changeview.md)
</dt> <dt>

[**External.changeViewOnlineList**](external-changeviewonlinelist.md)
</dt> </dl>

 

 





