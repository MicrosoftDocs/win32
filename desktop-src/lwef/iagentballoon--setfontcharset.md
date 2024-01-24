---
title: IAgentBalloon SetFontCharSet
description: IAgentBalloon SetFontCharSet
ms.assetid: ce1b152d-c8af-47ec-9e6b-5768dbcf3566
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::SetFontCharSet

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetFontCharSet(
   short sFontCharSet  // character set displayed in word balloon
); 
```

Sets the character set of the font displayed in the word balloon.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="sFontCharSet"></span><span id="sfontcharset"></span><span id="SFONTCHARSET"></span>*sFontCharSet*
</dt> <dd>

The character set of the font. The following are some common settings for value:



| Value    | Character set                                                                                       |
|-----|----------------------------------------------------------------------------------------|
| 0   | Standard Windows characters (ANSI).                                                    |
| 1   | Default character set.                                                                 |
| 2   | The symbol character set.                                                              |
| 128 | Double-byte character set (DBCS) unique to the Japanese version of Windows.            |
| 129 | Double-byte character set (DBCS) unique to the Korean version of Windows.              |
| 134 | Double-byte character set (DBCS) unique to the Simplified Chinese version of Windows.  |
| 136 | Double-byte character set (DBCS) unique to the Traditional Chinese version of Windows. |
| 255 | Extended characters usually displayed by MS-DOS applications.                          |



 

</dd> </dl>

For other character set values, consult the Platform SDK documentation.

The default character set used in a character's word balloon is defined in the Microsoft Agent Character Editor. You can change it with [**IAgentBalloon::SetFontCharSet**](https://www.bing.com/search?q=**IAgentBalloon::SetFontCharSet**). However, the user can override the character set setting for all characters using the Microsoft Agent property sheet. This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

## See Also

[**IAgentBalloon::GetFontCharSet**](iagentballoon--getfontcharset.md)


 

 




