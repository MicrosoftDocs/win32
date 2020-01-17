---
title: StringFileInfo BLOCK statement
description: Describes the form of the string information block.
ms.assetid: d5edf638-b70a-44d0-a43a-89d4d21e679f
keywords:
- StringFileInfo BLOCK statement Menus and Other Resources
topic_type:
- apiref
api_name:
- StringFileInfo BLOCK
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# StringFileInfo BLOCK statement

Defines a string information block.

``` syntax
BLOCK "StringFileInfo" { BLOCK "lang-charset" {VALUE "string-name", "value" . . . }}
```

## Parameters

<dl> <dt>

<span id="lang-charset"></span><span id="LANG-CHARSET"></span>*lang-charset*
</dt> <dd>

Language and character-set identifier pair. It is a hexadecimal string consisting of the concatenation of the language and character-set identifiers specified in the Remarks section.

</dd> <dt>

<span id="string-name"></span><span id="STRING-NAME"></span>*string-name*
</dt> <dd>

Name of a value in the block and can be one of the predefined names specified in the Remarks section.

</dd> <dt>

<span id="value"></span><span id="VALUE"></span>*value*
</dt> <dd>

Character string that specifies the value of the corresponding string name. More than one **VALUE** statement can be given.

</dd> </dl>

## Remarks

The *lang-charset* parameter specifies one of the following language codes.



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



 

The *lang-charset* parameter also specifies one of the following character-set identifiers.



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



 

The *string-name* parameter specifies one of the following predefined names.



| Name                 | Description                                                                                                                                                                                                                                                                                                 |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Comments**         | Additional information that should be displayed for diagnostic purposes.                                                                                                                                                                                                                                    |
| **CompanyName**      | Company that produced the file—for example, "Microsoft Corporation" or "Standard Microsystems Corporation, Inc." This string is required.                                                                                                                                                                   |
| **FileDescription**  | File description to be presented to users. This string may be displayed in a list box when the user is choosing files to install—for example, "Keyboard Driver for AT-Style Keyboards". This string is required.                                                                                            |
| **FileVersion**      | Version number of the file—for example, "3.10" or "5.00.RC2". This string is required.                                                                                                                                                                                                                      |
| **InternalName**     | Internal name of the file, if one exists—for example, a module name if the file is a dynamic-link library. If the file has no internal name, this string should be the original filename, without extension. This string is required.                                                                       |
| **LegalCopyright**   | Copyright notices that apply to the file. This should include the full text of all notices, legal symbols, copyright dates, and so on. This string is optional.                                                                                                                                             |
| **LegalTrademarks**  | Trademarks and registered trademarks that apply to the file. This should include the full text of all notices, legal symbols, trademark numbers, and so on. This string is optional.                                                                                                                        |
| **OriginalFilename** | Original name of the file, not including a path. This information enables an application to determine whether a file has been renamed by a user. The format of the name depends on the file system for which the file was created. This string is required.                                                 |
| **PrivateBuild**     | Information about a private version of the file—for example, "Built by TESTER1 on \\TESTBED". This string should be present only if **VS\_FF\_PRIVATEBUILD** is specified in the *fileflags* parameter of the root block.                                                                                   |
| **ProductName**      | Name of the product with which the file is distributed. This string is required.                                                                                                                                                                                                                            |
| **ProductVersion**   | Version of the product with which the file is distributed—for example, "3.10" or "5.00.RC2". This string is required.                                                                                                                                                                                       |
| **SpecialBuild**     | Text that specifies how this version of the file differs from the standard version—for example, "Private build for TESTER1 solving mouse problems on M250 and M250E computers". This string should be present only if **VS\_FF\_SPECIALBUILD** is specified in the *fileflags* parameter of the root block. |



 

 

 




