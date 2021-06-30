---
title: IAgentCharacterEx GetLanguageID
description: IAgentCharacterEx GetLanguageID
ms.assetid: 4e4e5342-edf9-480b-a9c3-e2626fd89e76
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::GetLanguageID

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetLanguageID(
   long * plangID  // address of language ID setting
);
```

Retrieves the language ID set for the character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="plangID"></span><span id="plangid"></span><span id="PLANGID"></span>*plangID*
</dt> <dd>

Address of a variable that receives the language ID setting for the character.

</dd> </dl>

A Long integer specifying the language ID for the character. The language ID (LANGID) for a character is a 16-bit value defined by Windows, consisting of a primary language ID and a secondary language ID. The following examples are values for some languages. To determine the values other languages, see the Platform SDK documentation.



| Language              | ID     | Language              | ID     |
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



 

If you do not set this language ID for the character, the character's language ID will be the current system language ID.

This setting also determines the language for TTS output, word balloon text, the commands in the character's pop-up menu, and speech recognition engine. To determine if there is a compatible speech recognition engine available for the character's language, use [**IAgentCharacterEx::GetSRModeID**](iagentcharacterex--getsrmodeid.md) or [**IAgentCharacterEx::GetTTSModeID**](iagentcharacterex--getttsmodeid.md).

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

> [!Note]  
> If the language ID is set to a language that supports bidirectional text (such as Arabic or Hebrew), but the system running your application does not have bidirectional support installed, text will appear in the word balloon in logical rather than display order.

 

## See Also

[**IAgentCharacterEx:SetLanguageID**](iagentcharacterex--setlanguageid.md), [**IAgentCharacterEx::GetSRModeID**](iagentcharacterex--getsrmodeid.md), [**IAgentCharacterEx::GetTTSModeID**](iagentcharacterex--getttsmodeid.md)


 

 




