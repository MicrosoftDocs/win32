---
title: IAgentCommandsEx SetFontSize
description: IAgentCommandsEx SetFontSize
ms.assetid: 095f78d2-ef91-4880-ad49-dd9a94f02891
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandsEx::SetFontSize

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetFontSize(
   long lFontSize  // font size displayed in character's pop-up menu
);
```

Sets the size of the font displayed in the character's pop-up menu.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="lFontSize"></span><span id="lfontsize"></span><span id="LFONTSIZE"></span>*lFontSize*
</dt> <dd>

The size of the font.

</dd> </dl>

This property determines the point size of the font used to display text in the character's pop-up menu when your client application is input-active. The default value for the font setting is based on the menu font setting for the character's language ID setting-or if that's not set-the user default language setting. If not input-active, your client application's [**Command**](/windows/desktop/lwef/the-command-object) [**Caption**](caption-property.md) text appears in the point size specified for the input-active client.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

## See Also

[**IAgentCommandsEx::GetFontSize**](iagentcommandsex--getfontsize.md), [**IAgentCommandsEx::GetFontName**](iagentcommandsex--getfontname.md), [**IAgentCommandsEx::SetFontName**](iagentcommandsex--setfontname.md)


 

 