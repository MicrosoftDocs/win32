---
title: IAgentBalloon GetFontCharSet
description: IAgentBalloon GetFontCharSet
ms.assetid: 1ab5767a-31e3-449c-b242-f20b11336ca0
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::GetFontCharSet

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetFontCharSet(
   short * psFontCharSet  // character set displayed in word balloon
); 
```

Indicates the character set of the font displayed in a word balloon.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="psFontCharSet"></span><span id="psfontcharset"></span><span id="PSFONTCHARSET"></span>*psFontCharSet*
</dt> <dd>

The address of a value that receives the font's character set. The following are some common settings for value:



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

The default character set used in a character's word balloon is defined in the Microsoft Agent Character Editor. You can change it using [**IAgentBalloon::SetFontCharSet**](iagentballoon--setfontcharset.md). However, the user can override the character set setting for all characters using the Microsoft Agent property sheet.

## See Also

[**IAgentBalloon::SetFontCharSet**](iagentballoon--setfontcharset.md)


 

 




