---
title: External.cancelNavigate method
description: Note This topic describes functionality designed for use by online stores. | External.cancelNavigate method
ms.assetid: e65d64fb-292c-4413-9727-b24609e78d68
keywords:
- cancelNavigate method Windows Media Player
- cancelNavigate method Windows Media Player , External class
- External class Windows Media Player , cancelNavigate method
topic_type:
- apiref
api_name:
- External.cancelNavigate
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# External.cancelNavigate method

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **cancelNavigate** method informs Windows Media Player that it should not display a new discovery page even though the view has changed in the Player.

## Syntax


```JScript
External.cancelNavigate()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

When the view changes in Windows Media Player, the Player calls the online store's plug-in to determine which discovery page to display next. In some cases, however, the online store might want the Player to continue displaying the existing discovery page. The following process determines whether the Player displays a new discovery page:

1.  An action by the user, either in the Player's user interface or on the discovery page, requests that the Player change its view.
2.  The Player calls the plug-in's [GetTemplate](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-gettemplate) method to determine which discovery page to display next. The Player stores the URL of the new discovery page but does not display the new discovery page at this time.
3.  The Player raises the [OnViewChange](external-onviewchange-event.md) event.
4.  If the **OnViewChange** event handler on the discovery page calls **cancelNavigate**, the Player does not display the new discovery page (determined in step 2). Instead, it continues to display the existing discovery page. If the **OnViewChange** event handler does not call **cancelNavigate**, the Player does display the new discovery page.

For example, suppose the Player is currently displaying the view of an album with a certain track selected. Also assume that the current discovery page is the page that represents the entire album. If the user clicks a different track from the same album, the Player's view changes slightly to show that the new track is selected. But there is no need to display a new discovery page. The discovery page that represents the entire album is still the appropriate page for the Player to display.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.changeViewOnlineList**](external-changeviewonlinelist.md)
</dt> <dt>

[**External.OnViewChange**](external-onviewchange-event.md)
</dt> </dl>

 

 





