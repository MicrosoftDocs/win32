---
title: IAgentCharacterEx SetLanguageID
description: IAgentCharacterEx SetLanguageID
ms.assetid: 064f4c3c-1871-4372-9796-5b53f05c6d9a
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::SetLanguageID

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetLanguageID(
   long langID  // language ID setting of character
); 
```

Sets the language ID set for the character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="langID"></span><span id="langid"></span><span id="LANGID"></span>*langID*
</dt> <dd>

The language ID setting for the character.

</dd> </dl>

A Long integer specifying the language ID for the character. The language ID (LANGID) for a character is a 16-bit value defined by Windows, consisting of a primary language ID and a secondary language ID. You can use the following values for the specified languages. For more information, see the Platform SDK documentation.



| Language              | ID     |  Language             | ID     |
|-----------------------|--------|-----------------------|--------|
| Arabic (Saudi)        | 0x0401 | Italian               | 0x0410 |
| Basque                | 0x042d | Japanese              | 0x0411 |
| Chinese (Simplified)  | 0x0804 | Korean                | 0x0412 |
| Chinese (Traditional) | 0x0404 | Norwegian             | 0x0414 |
| Croatian              | 0x041A | Polish                | 0x0415 |
| Czech                 | 0x0405 | Portuguese (Portugal) | 0x0816 |
| Danish                | 0x0406 | Portuguese (Brazil)   | 0x0416 |
| Dutch                 | 0x0413 | Romanian              | 0x0418 |
| English (British)     | 0x0809 | Russian               | 0x0419 |
| English (US)          | 0x0409 | Slovakian             | 0x041B |
| Finnish               | 0x040B | Slovenian             | 0x0424 |
| French                | 0x040C | Spanish               | 0x0C0A |
| German                | 0x0407 | Swedish               | 0x041D |
| Greek                 | 0x0408 | Thai                  | 0x041E |
| Hebrew                | 0x040D | Turkish               | 0x041F |
| Hungarian             | 0x040E |                       |        |



 

If you do not set the language ID for the character, its language ID will be the current system language ID if the corresponding Agent language DLL is installed; otherwise, the character's language will be English (US).

This property also determines the language for the word balloon text, the commands in the character's pop-up menu, and the speech recognition engine. It also determines the default language for TTS output. To determine if there is a compatible speech engine available for the character's language, use [**IAgentCharacterEx::GetSRModeID**](iagentcharacterex--getsrmodeid.md) or [**IAgentCharacterEx::GetTTSModeID**](iagentcharacterex--getttsmodeid.md).

If you try to set the language ID for a character and the Agent language resources, the code page, or a display font for the language ID is not available, Agent returns an error and the character's language ID remains at its last setting. Setting this property does not return an error if there are no matching speech engines for the language.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

> [!Note]  
> If you set the character's language ID to a language that supports bidirectional text (such as Arabic or Hebrew), but the system running your application does not have bidirectional support installed, text will appear in the word balloon in logical rather than display order.

 

## See Also

[**IAgentCharacterEx:GetLanguageID**](iagentcharacterex--getlanguageid.md), [**IAgentCharacterEx::GetSRModeID**](iagentcharacterex--getsrmodeid.md), [**IAgentCharacterEx::GetTTSModeID**](iagentcharacterex--getttsmodeid.md)


 

 




