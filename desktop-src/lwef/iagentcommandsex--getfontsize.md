---
title: IAgentCommandsEx GetFontSize
description: IAgentCommandsEx GetFontSize
ms.assetid: 8173e026-d28f-43d8-a8b4-96d1d97a8b68
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandsEx::GetFontSize

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetFontSize(
   long * plFontSize  // address of variable for font size 
);                    // for font displayed in character's pop-up menu
```

Retrieves the value for the size of the font displayed in the character's pop-up menu.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="plFontSize"></span><span id="plfontsize"></span><span id="PLFONTSIZE"></span>*plFontSize*
</dt> <dd>

The address of a value that receives the size of the font.

</dd> </dl>

The point size of the font returned corresponds to the size defined to display text in the character's pop-up menu when your client is input-active. The default value for the font setting is based on the menu font setting for the character's language ID setting, or if not set, the user default language setting.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

## See Also

[**IAgentCommandsEx::SetFontSize**](iagentcommandsex--setfontsize.md), [**IAgentCommandsEx::SetFontName**](iagentcommandsex--setfontname.md)


 

 




