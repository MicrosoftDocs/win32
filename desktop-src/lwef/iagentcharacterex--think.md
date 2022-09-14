---
title: IAgentCharacterEx Think
description: IAgentCharacterEx Think
ms.assetid: 64bfa388-0db7-423c-a4af-64a9f7351e9a
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::Think

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Think(
   BSTR bszText,    // text to think
   long * pdwReqID  // address of a request ID
);
```

Displays the character's thought word balloon with the specified text.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszText"></span><span id="bsztext"></span><span id="BSZTEXT"></span>*bszText*
</dt> <dd>

The text to appear in the character's thought balloon.

</dd> <dt>

<span id="pdwReqID"></span><span id="pdwreqid"></span><span id="PDWREQID"></span>*pdwReqID*
</dt> <dd>

Address of a variable that receives the **Think** request ID.

</dd> </dl>

Like the [**IAgentCharacter::Speak**](iagentcharacter--speak.md) method, the **Think** method is a queued request that displays text in a word balloon, except that thoughts display in a special thought balloon. The thought balloon supports only the Bookmark speech control tag (**\\Mrk**) and ignores any other speech control tags. Unlike **IAgentCharacter::Speak**, the **Think** method does not change the character's animation state.

The [**IAgentBalloon**](/windows/desktop/lwef/iagentballoon) settings also apply to the appearance style of the thought balloon. For example, the balloon's [**Enabled**](enabled-property.md) property must also be **True** for the text to display.

Microsoft Agent's automatic word breaking in the word balloon breaks words using white-space characters (for example, space and tab). However, it may break a word to fit the balloon as well. In languages like Japanese, Chinese, and Thai, where spaces are not used to break words, insert a Unicode zero width space character (0x200B) between characters to define logical word breaks.

> [!Note]  
> Set the character's language ID (using [**IAgentCharacterEx::SetLanguageID**](iagentcharacterex--setlanguageid.md) before using the [**IAgentCharacter::Speak**](iagentcharacter--speak.md) method to ensure appropriate text display within the word balloon.

 

## See Also

[**IAgentBalloon::GetEnabled**](iagentballoon--getenabled.md), [**IAgentBalloonEx::SetStyle**](iagentballoonex--setstyle.md), [**IAgentCharacter::Speak**](iagentcharacter--speak.md)


 

 