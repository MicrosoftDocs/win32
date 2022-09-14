---
title: IAgentCharacterEx GetAutoPopupMenu
description: IAgentCharacterEx GetAutoPopupMenu
ms.assetid: c29bfd6e-c7eb-426e-be38-2fa0bdb13211
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::GetAutoPopupMenu

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetAutoPopupMenu(
   long * pbAutoPopupMenu  // address of auto pop-up menu display setting
);
```

Retrieves whether the server automatically displays the character's pop-up menu.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbAutoPopupMenu"></span><span id="pbautopopupmenu"></span><span id="PBAUTOPOPUPMENU"></span>*pbAutoPopupMenu*
</dt> <dd>

Address of a variable that receives **True** if the Microsoft Agent server automatically handles displaying the character's pop-up menu and **False** if not.

</dd> </dl>

When this property is set to **False**, your application must display the pop-up menu using [**IAgentCharacterEx::ShowPopupMenu**](iagentcharacterex--showpopupmenu.md) method.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

## See Also

[**IAgentCharacterEx::SetAutoPopupMenu**](iagentcharacterex--setautopopupmenu.md), [**IAgentCharacterEx::ShowPopupMenu**](iagentcharacterex--showpopupmenu.md)


 

 




