---
description: This topic defines terms that are important when working with NLS functionality.
ms.assetid: daf929b2-8ff9-4a17-b294-f2c0eaef5848
title: NLS Terminology
ms.topic: article
ms.date: 05/31/2018
---

# NLS Terminology

This topic defines terms that are important when working with NLS functionality.

## Locale and Language Terms

The following table summarizes locale and language terms. See also [Locales and Languages](locales-and-languages.md).



|                          | Language group                                                                                                                                                                                                                                                                   | Language for non-Unicode programs                                                                                                                                                                                                                | Standards and Formats                                                                                                                                                                                                                   |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Purpose**              | Provides all keyboard layouts, input method editors (IMEs), TrueType fonts, font links, license package files (LPKs), bitmap fonts, and code page translation tables needed by the operating system for a group of languages. Therefore affects all other settings in this list. | Determines which bitmap fonts, and OEM, ANSI, and Macintosh code pages are defaults for the operating system. This language only affects applications that are not fully Unicode. Prior to Windows XP, this language was called "system locale". | Determines which settings are used for formatting dates, times, currency, and numbers as a default for each user. Also determines the sort order for sorting text. Prior to Windows XP, Standards and Formats was called "user locale". |
| **First Set**            | Installation                                                                                                                                                                                                                                                                     | Installation                                                                                                                                                                                                                                     | Installation                                                                                                                                                                                                                            |
| **How users can change** | Regional Options (Control Panel item)<br/> **Windows XP:** Regional and Language Options<br/> (only administrators)<br/>                                                                                                                                       | Regional Options (Control Panel item)<br/> **Windows XP:** Regional and Language Options<br/> (only administrators)<br/>                                                                                                       | Regional Options (Control Panel item)<br/> **Windows XP:** Regional and Language Options<br/>                                                                                                                               |
| **Default**              | Western Europe and United States and language group required to display language of a localized version.                                                                                                                                                                         | Language of localized version.                                                                                                                                                                                                                   | Language of localized operating system.                                                                                                                                                                                                 |
| **Function**             | [**EnumSystemLanguageGroups**](/windows/desktop/api/Winnls/nf-winnls-enumsystemlanguagegroupsa)                                                                                                                                                                                                                     | [**GetSystemDefaultLangID**](/windows/desktop/api/Winnls/nf-winnls-getsystemdefaultlangid)                                                                                                                                                                                         | [**GetUserDefaultLCID**](/windows/desktop/api/Winnls/nf-winnls-getuserdefaultlcid), [**GetUserDefaultLocaleName**](/windows/desktop/api/Winnls/nf-winnls-getuserdefaultlocalename)                                                                                                                          |



 



|                          | Thread locale                                                                                                                                                 | Input language                                                                                            | System default UI language                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Purpose**              | Determines the settings that are used for formatting dates, times, currency, and large numbers for a thread. Also determines the sort order for sorting text. | Consists of a language and a method of input.                                                             | Determines the default language of menus and dialogs, messages, setup information (INF) files, and help files.<br/> **Windows Vista and later:** Known as install language. Plays a more limited role, largely superseded by system preferred UI languages.<br/> For more information, see [User Interface Language Management](user-interface-language-management.md)<br/> |
| **First Set**            | Default to Standards and Formats                                                                                                                              | Installation                                                                                              | Installation                                                                                                                                                                                                                                                                                                                                                                                   |
| **How users can change** | [**SetThreadLocale**](/windows/desktop/api/Winnls/nf-winnls-setthreadlocale)                                                                                                                    | Regional Options (Control Panel item)<br/> **Windows XP:** Regional and Language Options<br/> | No                                                                                                                                                                                                                                                                                                                                                                                             |
| **Default**              | Standards and Formats                                                                                                                                         | Language of localized version with default input method.                                                  | Language of localized version.                                                                                                                                                                                                                                                                                                                                                                 |
| **Function**             | [**GetThreadLocale**](/windows/desktop/api/Winnls/nf-winnls-getthreadlocale)                                                                                                                    | [**GetKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-getkeyboardlayout)                                                     | [**GetSystemDefaultUILanguage**](/windows/desktop/api/Winnls/nf-winnls-getsystemdefaultuilanguage)                                                                                                                                                                                                                                                                                                                               |



 



|                          | System UI language, system preferred UI languages                                                                                                                                                                  | User UI language, user preferred UI languages                                                                                                                                               | Thread preferred UI languages                                                                                                                                                                 |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Purpose**              | Determine the language of menus and dialogs, messages, INF files, and help files for the operating system. For more information, see [User Interface Language Management](user-interface-language-management.md). | Determine the language of menus and dialogs, messages, and help files for the user. For more information, see [User Interface Language Management](user-interface-language-management.md). | **Windows Vista and later:** Specify the preferred languages for application threads. For more information, see [User Interface Language Management](user-interface-language-management.md). |
| **First Set**            | Default to NULL                                                                                                                                                                                                    | Default to NULL                                                                                                                                                                             | Default to NULL                                                                                                                                                                               |
| **How users can change** | Regional and Language Options<br/> (only administrators)<br/>                                                                                                                                          | Regional Options (Control Panel item)<br/> **Windows XP:** Regional and Language Options<br/>                                                                                   | [**SetThreadPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-setthreadpreferreduilanguages)                                                                                                                        |
| **Default**              | **Windows Vista and later:** Language of localized version, followed by any fallbacks.                                                                                                                             | **Prior to Windows Vista:** Language of localized version.<br/> **Windows Vista and later:** Language of localized version, followed by any fallbacks.<br/>                     | Null list                                                                                                                                                                                     |
| **Function**             | [**GetSystemPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-getsystempreferreduilanguages)                                                                                                                                             | [**GetUserDefaultUILanguage**](/windows/desktop/api/Winnls/nf-winnls-getuserdefaultuilanguage), [**GetUserPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-getuserpreferreduilanguages)                                                            | [**GetThreadPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-getthreadpreferreduilanguages)                                                                                                                        |



 



|                          | Process preferred UI languages                                                                                                                                                                 |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Purpose**              | **Windows 7 and later:** Determine the preferred languages for an application process. For more information, see [User Interface Language Management](user-interface-language-management.md). |
| **First Set**            | Default to NULL                                                                                                                                                                                |
| **How users can change** | Regional and Language Options (only administrators)                                                                                                                                            |
| **Default**              | **Windows 7 and later:** Language of localized version, followed by any fallbacks.                                                                                                             |
| **Function**             | [**GetProcessPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-getprocesspreferreduilanguages), [**SetProcessPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-setprocesspreferreduilanguages)                                             |



 

## Code Page

The inability of 256-code point code pages to support mixing of scripts in a single text was one of the main reasons for the rise of Unicode. Code pages remain important for writing console code, for maintaining legacy applications or running on older versions of Windows, and for interfacing with some non-Microsoft software that is not Unicode-enabled.

## Input Language

The input language is represented by a per-process data variable that describes a language (for example, Greek) and an input method (for example, the keyboard). Multiple input languages can be installed and the user can switch between them.

To set and retrieve the input language value, the application calls [**LoadKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-loadkeyboardlayouta) and [**GetKeyboardLayout**](/windows/win32/api/winuser/nf-winuser-getkeyboardlayout), respectively. Users can add and remove input languages through the **Languages** tab in the regional and language options portion of the Control Panel.

The default input language is the localized language of the operating system, and it is the setting that is active when a new application is started (or when a new window is opened for some applications). Switching to a different input language is done on a per-application basis. In other words, two different input languages can be used in two different applications. For example, a user can type German using the international United States keyboard layout, English using voice input (with non-Microsoft software), and Spanish using an IME in three different applications.

## Language for Non-Unicode Programs

The language for non-Unicode programs (formerly called "system locale") determines the code page that is used on the operating system by default. The language for non-Unicode programs setting affects only non-Unicode applications, that is, ANSI applications. Setting the language instructs Windows to emulate a non-Unicode-based operating system, localized to this language. Changing the language for non-Unicode programs installs the necessary bitmap font files to support non-Unicode applications in the specified language. To allow the user to select a language for non-Unicode programs, the appropriate language group must be installed. Your application needs the script support to select a language for non-Unicode programs. The language for non-Unicode programs is a per-system setting and requires a restart to be implemented.

Sometimes there is no noticeable difference between two languages for non-Unicode programs. For example, this is the case with the German (Neutral) and German (Austria) locales. In general, the settings of one language group are very similar and differ only in the OEM or MAC code page.

An ANSI application should check the language for non-Unicode programs setting during installation. It uses [**GetACP**](/windows/desktop/api/Winnls/nf-winnls-getacp) or [**GetOEMCP**](/windows/desktop/api/Winnls/nf-winnls-getoemcp) to retrieve the value. No function is supported to set the language for non-Unicode programs. However, users can change it by using the **Advanced** tab in the regional and language options portion of the Control Panel. The following are some examples of language for non-Unicode programs settings:

1.  A German user who wants to run a Japanese application that was designed for Japanese Windows 95 must select Japanese as the language for non-Unicode programs. After this selection, non-Unicode German applications have problems. For example, German umlauts (¨) are not displayed correctly.
2.  A German user who wants to type Japanese text in a non-Unicode German application must select Japanese as the language for non-Unicode programs. As in the first example, this causes problems in entering German text in non-Unicode applications.
3.  An Arabic user who wants to type Arabic, French, and English in a non-Unicode Arabic application should select Arabic as a language for non-Unicode programs, because the Arabic ANSI code page contains most French characters and all English characters.

## Language Group

The language group controls the language for non-Unicode programs, Standards and Formats, input languages, and user interface languages that can be selected. For each localized version, the specified language group is the default and cannot be removed. For example, Windows installs the Western Europe and United States language group by default. Thus, if the English version of Windows is installed in a non-English speaking country/region, the user will typically install another language group.

When adding a language group, Windows copies (but does not activate) the necessary keyboard files, Input Method Editors (IMEs), TrueType font files, bitmap font files, and National Language Support (.nls) files. Adding a language group also adds registry values for font linking and installs scripting engines for complex script languages (Arabic, Hebrew, Indic, and Thai).

In addition to the Western Europe and United States language group, there are 16 other language groups:



<table>
<tbody>
<tr class="odd">
<td><dl> Arabic<br />
Armenian<br />
Baltic<br />
Central Europe<br />
Cyrillic<br />
Georgian<br />
Greek<br />
Hebrew<br />
</dl></td>
<td><dl> Indic<br />
Japanese<br />
Korean<br />
Simplified Chinese<br />
Traditional Chinese<br />
Thai<br />
Turkic<br />
Vietnamese<br />
</dl></td>
</tr>
</tbody>
</table>



 

Any number and combination of language groups can be installed on any operating system. For example, a Spanish user can install the Cyrillic language group to work on Russian texts. In this case, a word processing application needs to support the Cyrillic language group also.

> [!Note]  
> Adding the appropriate language group does not automatically enable an application to accept text. Testing is recommended. For example, non-Unicode applications might require the language for non-Unicode programs to be changed.

 

## Location

**Windows XP:** A location is a geographic identifier. It is represented by a per-user data variable that defines the country/region where the user lives.

To set the value, the application calls [**SetUserGeoID**](/windows/desktop/api/Winnls/nf-winnls-setusergeoid). To retrieve the value, the application calls [**GetUserGeoID**](/windows/desktop/api/Winnls/nf-winnls-getusergeoid).

## Standards and Formats

Standards and Formats (formerly "user locale") is a per-user variable that determines default sort order and the default settings for formatting dates, times, currency, and numbers. The variable is presented as a language (sometimes in combination with a country/region), but it is not a language itself. For example, setting the Standards and Formats variable to Hebrew indicates that the user wants to use the formatting conventions of Hebrew, not necessarily the Hebrew language. In addition, the Standards and Formats variable determines the string that is used for the names of days and months. For example, if a user displays "November 25, 1998", the "November" string can change based on the Standards and Formats variable. Changing the variable automatically adds an input locale with the default settings for the language.

To get the Standards and Formats variable setting, the application calls [**GetUserDefaultLCID**](/windows/desktop/api/Winnls/nf-winnls-getuserdefaultlcid) or [**GetUserDefaultLocaleName**](/windows/desktop/api/Winnls/nf-winnls-getuserdefaultlocalename). No NLS function is available to set the variable. However, users can change it through the **Region Options** tab in the regional and language options portion of the Control Panel.

An application should typically use the Standards and Formats variable settings to display data. However, an application that uses a fixed locale to display data should pass a specific locale identifier instead of using LOCALE\_USER\_DEFAULT.

## Thread Locale

The thread locale is represented by a per-thread locale data variable that determines the formatting of dates, times, currency, and large numbers for the thread. It defaults to the value for the locale currently selected for Standards and Formats. To set the thread locale, the application calls [**SetThreadLocale**](/windows/desktop/api/Winnls/nf-winnls-setthreadlocale). To retrieve the thread locale, the application calls [**GetThreadLocale**](/windows/desktop/api/Winnls/nf-winnls-getthreadlocale).

In most cases the thread locale should not be overwritten. Normally it should only be used to synchronize the thread locale of a server application with the Standards and Formats variable of a client machine. For example, a financial stock trading application for the New York Stock Exchange, which is used in banks worldwide, has to display the time, date, and stock prices in United States formats. This application uses [**SetThreadLocale**](/windows/desktop/api/Winnls/nf-winnls-setthreadlocale) to set the thread locale to English (United States) then uses the NLS functions to format dates, times, and stock prices.

Changing thread locale does not affect all API functions. Thus it is not always a reliable way to override the Standards and Formats variable. Instead, applications that control standards and formats should use a fixed locale to display data, passing a specific locale identifier instead of using LOCALE\_USER\_DEFAULT.

## NLS Example

The following example shows the interplay among Standards and Formats, the language for non-Unicode programs, location, and the user UI language.

A user who is a native of Chile but is living in the United States has a computer running Windows XP English. The user sets the location to United States to use an Internet service provider (ISP) to get the weather for the United States. However the Standards and Formats variable is set to Spanish (Chile) so that the information is formatted according to Chilean standards. In addition, the user uses a Korean word processor, which is an ANSI application, so that the language for non-Unicode programs is set to Korean (Korea). To use the application, the user has an English keyboard and also installs a Korean IME to support a second input language. The user's coworker, who shares the computer but is not comfortable with English, can set the user UI language to Spanish (Spain) when using the computer.

## Related topics

<dl> <dt>

[About National Language Support](about-national-language-support.md)
</dt> <dt>

[Locales and Languages](locales-and-languages.md)
</dt> <dt>

[Multilingual User Interface](multilingual-user-interface.md)
</dt> </dl>

 

 
