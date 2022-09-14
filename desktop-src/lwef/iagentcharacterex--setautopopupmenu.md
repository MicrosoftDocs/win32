---
title: IAgentCharacterEx SetAutoPopupMenu
description: IAgentCharacterEx SetAutoPopupMenu
ms.assetid: f2402b1f-a39b-4fd5-a046-c0a3245d2af9
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::SetAutoPopupMenu

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetAutoPopupMenu(
   long bAutoPopupMenu,  // auto pop-up menu display setting
);
```

Sets whether the server automatically displays the character's pop-up menu.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bAutoPopupMenu"></span><span id="bautopopupmenu"></span><span id="BAUTOPOPUPMENU"></span>*bAutoPopupMenu*
</dt> <dd>

The automatic pop-up menu display flag. If this parameter is **True**, Microsoft Agent automatically displays the character's pop-up menu when the user right-clicks the character or character's taskbar icon.

</dd> </dl>

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

By setting this property to **False**, you can create your own menu-handling behavior. To display the menu after setting this property to **False**, use the [**IAgentCharacterEx::ShowPopupMenu**](iagentcharacterex--showpopupmenu.md) method.

## See Also

[**IAgentCharacterEx::GetAutoPopupMenu**](iagentcharacterex--getautopopupmenu.md), [**IAgentCharacterEx::ShowPopupMenu**](iagentcharacterex--showpopupmenu.md)


 

 




