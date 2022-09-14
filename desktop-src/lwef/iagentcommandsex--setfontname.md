---
title: IAgentCommandsEx SetFontName
description: IAgentCommandsEx SetFontName
ms.assetid: c676ceb6-c098-4ac0-9103-ece469317ad6
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandsEx::SetFontName

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetFontName(
   BSTR bszFontName  // font to be displayed in character's pop-up menu
);
```

Sets the font displayed in the character's pop-up menu.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszFontName"></span><span id="bszfontname"></span><span id="BSZFONTNAME"></span>*bszFontName*
</dt> <dd>

A BSTR that sets the font displayed in the character's pop-up menu.

</dd> </dl>

This property determines the font used to display text in the character's pop-up menu. The default value for the font setting is based on the menu font setting for the character's language ID setting-or if that's not set-the user default language ID setting.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

## See Also

[**IAgentCommandsEx::GetFontName**](iagentcommandsex--getfontname.md), [**IAgentCommandsEx::GetFontSize**](iagentcommandsex--getfontsize.md), [**IAgentCommandsEx::SetFontSize**](iagentcommandsex--setfontsize.md)


 

 




