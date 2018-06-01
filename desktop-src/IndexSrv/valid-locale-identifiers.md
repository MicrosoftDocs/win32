---
Description: Valid Locale Identifiers
ms.assetid: f082512e-f2dc-4e1f-83bf-c05b57402eee
title: Valid Locale Identifiers
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Valid Locale Identifiers

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following table shows the International Organization of Standards (ISO) language identifiers recognized by Indexing Service in CiLocale:



| Language                             | CiLocale String | Win32 Equivalent                                   |
|--------------------------------------|-----------------|----------------------------------------------------|
| Afrikaans                            | AF              | LANG\_AFRIKAANS \| SUBLANG\_DEFAULT                |
| Arabic                               | AR              | LANG\_ARABIC \| SUBLANG\_DEFAULT                   |
| Basque (Basque)                      | EU              | LANG\_BASQUE \| SUBLANG\_DEFAULT                   |
| Belarusian                           | BE              | LANG\_BELARUSIAN \| SUBLANG\_DEFAULT               |
| Bulgarian                            | BG              | LANG\_BULGARIAN \| SUBLANG\_DEFAULT                |
| Catalan                              | CA              | LANG\_CATALAN \| SUBLANG\_DEFAULT                  |
| Chinese (China)                      | ZH, ZH-CN       | LANG\_CHINESE \| SUBLANG\_CHINESE\_SIMPLIFIED      |
| Chinese (Taiwan)                     | ZH-TW           | LANG\_CHINESE \| SUBLANG\_CHINESE\_TRADITIONAL     |
| Croatian                             | HR              | LANG\_CROATIAN \| SUBLANG\_DEFAULT                 |
| Czech                                | CS              | LANG\_CZECH \| SUBLANG\_DEFAULT                    |
| Danish                               | DA              | LANG\_DANISH \| SUBLANG\_DEFAULT                   |
| Dutch                                | NL              | LANG\_DUTCH \| SUBLANG\_DUTCH                      |
| English (Great Britain)              | EN-GB           | LANG\_ENGLISH \| SUBLANG\_ENGLISH\_UK              |
| English (United States)              | EN, EN-US       | LANG\_ENGLISH \| SUBLANG\_ENGLISH\_US              |
| Estonian                             | ET              | LANG\_ESTONIAN \| SUBLANG\_DEFAULT                 |
| Faeroese                             | FO              | LANG\_FAEROESE \| SUBLANG\_DEFAULT                 |
| Finnish                              | FI              | LANG\_FINNISH \| SUBLANG\_DEFAULT                  |
| French                               | FR, FR-FR       | LANG\_FRENCH \| SUBLANG\_FRENCH                    |
| French (Canadian)                    | FR-CA           | LANG\_FRENCH \| SUBLANG\_FRENCH\_CANADIAN          |
| German                               | DE              | LANG\_GERMAN \| SUBLANG\_GERMAN                    |
| Greek                                | EL              | LANG\_GREEK \| SUBLANG\_DEFAULT                    |
| Hebrew                               | HE, IW          | LANG\_HEBREW \| SUBLANG\_DEFAULT                   |
| Hungarian                            | HU              | LANG\_HUNGARIAN \| SUBLANG\_DEFAULT                |
| Icelandic                            | IS              | LANG\_ICELANDIC \| SUBLANG\_DEFAULT                |
| Indonesian                           | ID, IN          | LANG\_INDONESIAN \| SUBLANG\_DEFAULT               |
| Italian                              | IT              | LANG\_ITALIAN \| SUBLANG\_ITALIAN                  |
| Japanese                             | JA              | LANG\_JAPANESE \| SUBLANG\_DEFAULT                 |
| Korean                               | KO              | LANG\_KOREAN \| SUBLANG\_DEFAULT                   |
| Latvian                              | LV              | LANG\_LATVIAN \| SUBLANG\_DEFAULT                  |
| Lithuanian                           | LT              | LANG\_LITHUANIAN \| SUBLANG\_DEFAULT               |
| Neutral (use built-in word breaking) | NEUTRAL         | LANG\_NEUTRAL \| SUBLANG\_NEUTRAL                  |
| Norwegian                            | NO              | LANG\_NORWEGIAN \| SUBLANG\_DEFAULT                |
| Polish                               | PL              | LANG\_POLISH \| SUBLANG\_DEFAULT                   |
| Portuguese                           | PT              | LANG\_PORTUGUESE \| SUBLANG\_DEFAULT               |
| Portuguese (Brazil)                  | PT-BR           | LANG\_PORTUGUESE \| SUBLANG\_PORTUGUESE\_BRAZILIAN |
| Romanian                             | RO              | LANG\_ROMANIAN \| SUBLANG\_DEFAULT                 |
| Russian                              | RU              | LANG\_RUSSIAN \| SUBLANG\_DEFAULT                  |
| Serbian                              | SR              | LANG\_SERBIAN \| SUBLANG\_DEFAULT                  |
| Slovak                               | SK              | LANG\_SLOVAK \| SUBLANG\_DEFAULT                   |
| Slovenian                            | SL              | LANG\_SLOVENIAN \| SUBLANG\_DEFAULT                |
| Spanish                              | ES, ES-ES       | LANG\_SPANISH \| SUBLANG\_SPANISH                  |
| Swedish                              | SV              | LANG\_SWEDISH \| SUBLANG\_DEFAULT                  |
| Thai                                 | TH              | LANG\_THAI \| SUBLANG\_DEFAULT                     |
| Turkish                              | TR              | LANG\_TURKISH \| SUBLANG\_DEFAULT                  |
| Ukrainian                            | UK              | LANG\_UKRAINIAN \| SUBLANG\_DEFAULT                |
| Vietnamese                           | VI              | LANG\_VIETNAMESE \| SUBLANG\_DEFAULT               |



 

Indexing Service in Microsoft Windows XP uses Component Object Model (COM) objects and interfaces available through the Mlang APIs to provide support for 150 locales.

CiLocale can be specified in the .idq or .ida file. It can also be specified by the browser as the HTTP\_ACCEPT\_LANGUAGE variable. Values entered in the .idq and .ida files supersede those sent in HTTP\_ACCEPT\_LANGUAGE. If no value is found in the .idq or .ida file, the value of HTTP\_ACCEPT\_LANGUAGE is read from left to right to find a supported language.

For example:


```
HTTP_ACCEPT_LANGUAGE=EN, FR, CZ
```



> [!Note]  
> Values are separated by commas.

 

 

 



