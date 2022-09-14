---
title: IAgentCharacterEx ShowPopupMenu
description: IAgentCharacterEx ShowPopupMenu
ms.assetid: f93c4c9e-5ef8-42d1-8f22-d6625af7978f
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::ShowPopupMenu

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT ShowPopupMenu(
   short x,  // x-coordinate of pop-up menu
   short y   // y-coordinate of pop-up menu
);
```

Displays the pop-up menu for the character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="x"></span><span id="X"></span>*x*
</dt> <dd>

The x-coordinate of the character's pop-up menu in pixels, relative to the screen origin (upper left).

</dd> <dt>

<span id="y"></span><span id="Y"></span>*y*
</dt> <dd>

The y-coordinate of the character's pop-up menu in pixels, relative to the screen origin (upper left).

</dd> </dl>

When you set [**IAgentCharacterEx::SetAutoPopupMenu**](iagentcharacterex--setautopopupmenu.md) to **False**, the server no longer automatically displays the menu when the character or its taskbar icon is right-clicked. You can use this method to display the menu.

The menu displays until the user selects a command or displays another menu. Only one pop-up menu can be displayed at a time; therefore, calls to this method will cancel (remove) the former menu.

This method should only be called when your client application is the active client of the character; otherwise it fails.

[**IAgentCharacterEx::SetAutoPopupMenu**](iagentcharacterex--setautopopupmenu.md)

 

 




