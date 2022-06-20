---
description: This topic describes how Windows Search supports multiple languages.
ms.assetid: a800d2ac-3aee-4e74-a29a-a70355138ebc
title: Languages Supported by Windows Search
ms.topic: article
ms.date: 05/31/2018
---

# Languages Supported by Windows Search

This topic describes how Windows Search supports multiple languages.

## Tokenization, Wordbreakers, and Language Resources

Windows Search is language-independent, but the accuracy of search across languages may vary because of the way wordbreakers tokenize text. Wordbreakers implement various tokenization rules for languages and break text into individual tokens, or words, to be indexed or searched.

Both the language of the indexed text and the query string are broken into tokens. Because tokenization rules vary by language, there are separate wordbreakers for each language or family of languages. If there is a mismatch between the query language and the indexed language, the results can be unpredictable.

Windows Search ships with a well defined set of wordbreakers. Classic wordbreaker and stemmer components are supported in Windows Vista and later. If the language of a document cannot be determined, Windows Search attempts to detect the language to identify the most appropriate wordbreaker. Windows Search attempts to detect the language by calling the [**GetSystemPreferredUILanguages**](/windows/win32/api/winnls/nf-winnls-getsystempreferreduilanguages) function to determine the first Multiple User Interface (MUI) language (which is typically the system UI language unless MUI language packs are installed). If that call succeeds, the wordbreaker for the first MUI language is used. If the call to **GetSystemPreferredUILanguages** fails, Windows Search retrieves the system locale by calling the [**GetSystemDefaultLCID**](/windows/win32/api/winnls/nf-winnls-getsystemdefaultlcid) function and uses the wordbreaker associated with that locale.

If no wordbreaker is installed for a language, Windows Search breaks on white space by using the **Neutral** wordbreaker.

You can remove a language through the registry, as illustrated in the following example.

```
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         Control
            ContentIndex
               Language
                  Dutch_Dutch
                     (Default)
                     Locale
                     NoiseFile
                     StemmerClass = CLSID
                     WBreakerClass = CLSID
```

> [!TIP]
> If you make changes to the registry, restart Windows Search.

 

When Windows Search requires a new wordbreaker, the class identifier (CLSID) is read, and the instantiated wordbreaker is cached.

You can create a custom wordbreaker for a language by implementing the [**IWordBreaker**](/windows/desktop/api/Indexsrv/nn-indexsrv-iwordbreaker) interface. Windows Search then calls the **IWordBreaker** methods when it builds content indexes and runs queries.

Locale information for indexed content is retrieved from the source of the content. If the source implementer does not know the locale of the indexed content, it should set the locale to [**LOCALE\_NEUTRAL**](../intl/locale-neutral.md).

For example, if you implement a filter handler (an implementation of the [**IFilter**](https://www.bing.com/search?q=**IFilter**) interface), property handler, or protocol handler, you should set the locale for indexed content to [**LOCALE\_NEUTRAL**](../intl/locale-neutral.md) unless you have specific locale information and are confident of its accuracy.

> [!TIP]
> If an index query is based on user input, the locale should match the language in which the user is typing. You can determine this locale by calling the [**GetKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-getkeyboardlayout) function.

 

## Languages Supported by Wordbreakers

Windows Search includes wordbreakers to support the following languages.



| Registry key             | Language (sublanguage)                            | LCID   |
|--------------------------|---------------------------------------------------|--------|
| **Arabic\_SaudiArabia**  | Arabic (Neutral)                                  | 0x0001 |
| **Bengali\_Default**     | Bangla (Neutral)                                  | 0x0045 |
| **Bulgarian\_Default**   | Bulgarian (Bulgaria)                              | 0x0402 |
| **Catalan\_Default**     | Catalan (Catalan)                                 | 0x0403 |
| **Chinese\_HongKong**    | Chinese (Hong Kong SAR, PRC)                      | 0x0C04 |
| **Chinese\_Simplified**  | Chinese (Simplified)                              | 0x0804 |
| **Chinese\_Traditional** | Chinese (Traditional)                             | 0x0404 |
| **Croatian\_Default**    | Croatian (Croatia)                                | 0x041A |
| **Czech\_Default**       | Czech (Czech Republic)                            | 0x0405 |
| **Danish\_Default**      | Danish (Denmark)                                  | 0x0406 |
| **Dutch\_Dutch**         | Dutch (Netherlands)                               | 0x0413 |
| **English\_UK**          | English (United Kingdom)                          | 0x0809 |
| **English\_US**          | English (United States)                           | 0x0409 |
| **Finnish\_Default**     | Finnish (Finland)                                 | 0x040B |
| **French\_French**       | French (France)                                   | 0x040C |
| **German\_German**       | German (Germany)                                  | 0x0407 |
| **Greek\_Default**       | Greek (Greece)                                    | 0x0408 |
| **Gujarati\_Default**    | Gujarati (India)                                  | 0x0447 |
| **Hebrew\_Default**      | Hebrew (Neutral)                                  | 0x000D |
| **Hindi\_Default**       | Hindi (India)                                     | 0x0439 |
| **Hungarian\_Default**   | Hungarian (Hungary)                               | 0x040E |
| **Icelandic\_Default**   | Icelandic (Iceland)                               | 0x040F |
| **Indonesian\_Default**  | Indonesian (Indonesia)                            | 0x0421 |
| **Italian\_Italian**     | Italian (Italy)                                   | 0x0410 |
| **Japanese\_Default**    | Japanese (Japan)                                  | 0x0411 |
| **Kannada\_Default**     | Kannada (India)                                   | 0x044B |
| **Korean\_Default**      | Korean (Korea)                                    | 0x0412 |
| **Latvian\_Default**     | Latvian (Latvia)                                  | 0x0426 |
| **Lithuanian\_Default**  | Lithuanian (Lithuanian)                           | 0x0427 |
| **Malay\_Malaysia**      | Malay (Malaysia)                                  | 0x043E |
| **Malayalam\_Default**   | Malayalam (Neutral)                               | 0x004C |
| **Marathi\_Default**     | Marathi (India)                                   | 0x044E |
| **Norwegian\_Bokmal**    | Norwegian (Bokmål, Norway)                        | 0x0414 |
| **Polish\_Default**      | Polish (Poland)                                   | 0x0415 |
| **Portuguese\_Portugal** | Portuguese (Portugal)                             | 0x0816 |
| **Portuguese\_Brazil**   | Portuguese (Brazil)                               | 0x0416 |
| **Punjabi\_Default**     | Punjabi (India)                                   | 0x0446 |
| **Romanian\_Default**    | Romanian (Romania)                                | 0x0418 |
| **Russian\_Default**     | Russian (Neutral)                                 | 0x0019 |
| **Serbian\_Cyrillic**    | Serbian (Serbia and Montenegro, Former, Cyrillic) | 0x0C1A |
| **Serbian\_Latin**       | Serbian (Serbia and Montenegro, Former, Latin)    | 0x081A |
| **Slovak\_Default**      | Slovak (Slovakia)                                 | 0x041B |
| **Slovenian\_Default**   | Slovenian (Slovenia)                              | 0x0424 |
| **Spanish\_Modern**      | Spanish (Spain, Modern Sort)                      | 0x0C0A |
| **Swedish\_Default**     | Swedish (Sweden)                                  | 0x041D |
| **Tamil\_Default**       | Tamil (India)                                     | 0x0449 |
| **Telugu\_Default**      | Telugu (India)                                    | 0x044A |
| **Thai\_Default**        | Thai (Thailand)                                   | 0x041E |
| **Turkish\_Default**     | Turkish (Turkey)                                  | 0x041F |
| **Ukrainian\_Default**   | Ukrainian (Ukraine)                               | 0x0422 |
| **Urdu\_Default**        | Urdu (Pakistan)                                   | 0x0420 |
| **Vietnamese\_Default**  | Vietnamese (Vietnam)                              | 0x042A |



 

> [!Note]  
> LCIDs for some languages in the table are generated using the language identifier, sublanguage identifier, and sort identifier.

 

For more information about languages and associated identifiers, see [Language Identifier Constants and Strings](../intl/language-identifier-constants-and-strings.md).

> [!Note]  
> There is no guarantee that all of these language registry keys will be present on any given machine. The wordbreaker for any given language may or may not be installed in the machine depending on user settings.

 

**Beginning in Windows 8.1**, the preferred way to use wordbreakers is via the WinRT API [**WordsSegmenter class**](/uwp/api/Windows.Data.Text.WordsSegmenter).

## Additional Resources

-   For information on how to implement and use custom word breakers and stemmers for additional languages and locales, see [Extending Language Resources in Windows Search](extending-language-resources-in-windows-search.md).
-   If you need to identify the language of a piece of text, you can use Language Auto-Detection (LAD), which is available in Windows 7 and later. For more information, see [Extended Linguistic Services](../intl/extended-linguistic-services.md) (ELS).
-   For information on managing, querying, and extending the index, see the [Windows Search Developer's Guide](-search-developers-guide-entry-page.md).

## Related topics

<dl> <dt>

[Windows Search Overview](-search-3x-wds-overview.md)
</dt> <dt>

[Windows Search as a Development Platform](-search-3x-wds-development-ovr.md)
</dt> <dt>

[Using Managed Code with Shell Data and Windows Search](-search-3x-wds-managed-code.md)
</dt> </dl>

 

 
