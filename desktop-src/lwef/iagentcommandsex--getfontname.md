---
title: IAgentCommandsEx GetFontName
description: IAgentCommandsEx GetFontName
ms.assetid: cd0d0d93-839e-471c-9cfa-9f47dcce841b
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandsEx::GetFontName

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetFontName(
   BSTR * pbszFontName  // address of variable for font displayed 
);                      // in character's pop-up menu
```

Retrieves the value for the font displayed in the character's pop-up menu.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbszFontName"></span><span id="pbszfontname"></span><span id="PBSZFONTNAME"></span>*pbszFontName*
</dt> <dd>

The address of a BSTR that receives the font name displayed in the character's pop-up menu.

</dd> </dl>

The font name returned corresponds to the font used to display text in the character's pop-up menu when your client application is input-active. The default value for the font setting is based on the menu font setting for the character's language ID setting, or if not set, the user default language ID setting.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

## See Also

[**IAgentCommandsEx::SetFontName**](iagentcommandsex--setfontname.md), [**IAgentCommandsEx::SetFontSize**](iagentcommandsex--setfontsize.md)


 

 




