---
description: A MUI console application can support either system settings or application-specific settings for its user interface languages. This topic discusses the filtering of languages for this type of application.
ms.assetid: 6d3c491f-3f5e-4592-aada-49b8b415b497
title: Filtering Languages in a MUI Console Application
ms.topic: article
ms.date: 05/31/2018
---

# Filtering Languages in a MUI Console Application

A MUI console application can support either system settings or application-specific settings for its user interface languages. This topic discusses the filtering of languages for this type of application.

## Limit the Languages to Display

Unlike a graphical window, the Windows console cannot display [complex scripts](uniscribe-glossary.md), such as Arabic, Hebrew, Persian, Hindi, Urdu, Thai, and many others. Therefore, many user interface languages cannot be displayed by the console under any circumstances.

The console can display only characters from the single [OEM code page](code-pages.md) associated with the current language for non-Unicode applications. For each OEM code page, the console uses a particular font, and this might not provide full coverage for that code page.

These console-related limitations reduce the number of user interface languages that the console can display on a particular computer. For example, if the current language for non-Unicode applications is Japanese and the user tries to display German text in the console, characters with umlauts do not display correctly. If the current language for non-Unicode applications is German and the user wants to display Japanese text in the console, the results are much worse, rendering the text almost incomprehensible.

> [!Note]  
> When providing console support for your MUI applications, remember that the console provides only limited support for [input method editors](input-method-manager.md).

 

## Set the Language for Console Output

On Windows Vista and later, a console application sets the language to support the console display by calling [**SetThreadPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-setthreadpreferreduilanguages). In this call, the application passes MUI\_CONSOLE\_FILTER in the *dwFlags* parameter and **NULL** for *pwszLanguagesBuffer*. An alternative is to call [**SetThreadUILanguage**](/windows/win32/api/winnls/nf-winnls-setthreaduilanguage) with a language identifier of 0. This setting causes the function to select the language that best supports the console display.

On Windows XP, the application can only set the language for console output by calling [**SetThreadUILanguage**](/windows/win32/api/winnls/nf-winnls-setthreaduilanguage) with a language identifier of 0.

## Related topics

<dl> <dt>

[Setting Application Language Preferences](setting-application-language-preferences.md)
</dt> </dl>

 

 
