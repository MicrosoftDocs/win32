---
title: VarFileInfo BLOCK statement
description: Describes the form of the variable information block.
ms.assetid: 81c7f5df-78fa-4571-9dad-a6c3e932471e
keywords:
- VarFileInfo BLOCK statement Menus and Other Resources
topic_type:
- apiref
api_name:
- VarFileInfo BLOCK
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# VarFileInfo BLOCK statement

Defines a variable information block.

``` syntax
BLOCK "VarFileInfo" { VALUE "Translation", langID, charsetID . . . }
```

## Parameters

<dl> <dt>

<span id="langID"></span><span id="langid"></span><span id="LANGID"></span>*langID*
</dt> <dd>

One of the language identifiers specified in the Remarks section.

</dd> <dt>

<span id="charsetID"></span><span id="charsetid"></span><span id="CHARSETID"></span>*charsetID*
</dt> <dd>

One of the character-set identifiers specified in the Remarks section.

</dd> </dl>

## Remarks

More than one identifier pair can be given, but each pair must be separated from the preceding pair with a comma.

The *langID* parameter specifies one of the following language codes.



| Code   | Language            | Code   | Language                  |
|--------|---------------------|--------|---------------------------|
| 0x0401 | Arabic              | 0x0415 | Polish                    |
| 0x0402 | Bulgarian           | 0x0416 | Portuguese (Brazil)       |
| 0x0403 | Catalan             | 0x0417 | Rhaeto-Romanic            |
| 0x0404 | Traditional Chinese | 0x0418 | Romanian                  |
| 0x0405 | Czech               | 0x0419 | Russian                   |
| 0x0406 | Danish              | 0x041A | Croato-Serbian (Latin)    |
| 0x0407 | German              | 0x041B | Slovak                    |
| 0x0408 | Greek               | 0x041C | Albanian                  |
| 0x0409 | U.S. English        | 0x041D | Swedish                   |
| 0x040A | Castilian Spanish   | 0x041E | Thai                      |
| 0x040B | Finnish             | 0x041F | Turkish                   |
| 0x040C | French              | 0x0420 | Urdu                      |
| 0x040D | Hebrew              | 0x0421 | Bahasa                    |
| 0x040E | Hungarian           | 0x0804 | Simplified Chinese        |
| 0x040F | Icelandic           | 0x0807 | Swiss German              |
| 0x0410 | Italian             | 0x0809 | U.K. English              |
| 0x0411 | Japanese            | 0x080A | Spanish (Mexico)          |
| 0x0412 | Korean              | 0x080C | Belgian French            |
| 0x0413 | Dutch               | 0x0C0C | Canadian French           |
| 0x0414 | Norwegian – Bokmal  | 0x100C | Swiss French              |
| 0x0810 | Swiss Italian       | 0x0816 | Portuguese (Portugal)     |
| 0x0813 | Belgian Dutch       | 0x081A | Serbo-Croatian (Cyrillic) |
| 0x0814 | Norwegian – Nynorsk | ?      | ?                         |



 

The *charsetID* parameter specifies one of the following character-set identifiers:



| Identifier | Character Set              |
|------------|----------------------------|
| 0          | 7-bit ASCII                |
| 932        | Japan (Shift – JIS X-0208) |
| 949        | Korea (Shift – KSC 5601)   |
| 950        | Taiwan (Big5)              |
| 1200       | Unicode                    |
| 1250       | Latin-2 (Eastern European) |
| 1251       | Cyrillic                   |
| 1252       | Multilingual               |
| 1253       | Greek                      |
| 1254       | Turkish                    |
| 1255       | Hebrew                     |
| 1256       | Arabic                     |



 

 

 




