---
description: MUI allows your applications to manage user interface languages in two ways.
ms.assetid: ae8ab98f-dc3b-414d-85c9-6bf204c2f776
title: User Interface Language Management
ms.topic: article
ms.date: 05/31/2018
---

# User Interface Language Management

MUI allows your applications to manage user interface languages in two ways. An application can use a simple approach to language management by defaulting to the operating system language settings. Alternatively, the application can support its own languages from which the user can select. The MUI API also allows your application direct access to languages and language lists supported by the operating system and maintained by the resource loader. The remainder of this topic defines the system-supported languages and the language fallback mechanism.

## Languages Maintained by the Operating System

### System Default UI Language/Install Language

The system default UI language is the language of the localized version used to set up Windows. All menus, dialog boxes, error messages, and help files are represented in this language, except when the user selects a different language.

On Windows Vista and later, the system default UI language is known as the "install language" and plays a more limited role. For most purposes, it is superseded by the system preferred UI languages. However, in certain contexts it is useful to have a single install language that is always known to be fully supported.

No MUI function is available to set the system default UI language. To retrieve this language, the application can call [**GetSystemDefaultUILanguage**](/windows/desktop/api/Winnls/nf-winnls-getsystemdefaultuilanguage).

### System UI Language

The operating system defines the system UI language as a user interface language that can be set by an administrator in the **Advanced** tab of the regional and language options portion of Control Panel. The operating system uses this language if the current user has not made specific language settings or if no active account is logged in. The language can be changed only if more than one user interface language is installed on the computer.

> [!Note]  
> The operating system must be rebooted for all users and services to see the effect of the language change.

 

No MUI function is available to set the system UI language. To retrieve this value, an application targeted at Windows Vista and later can call [**GetSystemPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-getsystempreferreduilanguages) and obtain the first language in the system preferred UI languages list. Applications targeted at pre-Windows Vista operating systems cannot use [**GetSystemPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-getsystempreferreduilanguages) and should be based on the assumption that the system UI language is always the same as the system default UI language.

### User UI Language

The user UI language determines the user interface language used for menus, dialog boxes, help files, and so forth. It can be set by the current user in the **Language** tab of the regional and language options portion of Control Panel. This language can be changed only if more than one user interface language is installed on the computer. Note that the user will have to log off and then log back on to see the effect. For example, a multinational corporation wants to deploy Windows in all of its subsidiaries. The company creates a global install job, which installs the English language version of Windows on all clients, regardless of location. At the same time, it installs specific language modules depending on the organizational unit of which a computer is a member. When the user logs on the first time to a newly installed operating system, Windows appears as a localized version.

On Windows Vista and later, the user UI language is the first language in the user preferred UI languages list. Note that fallback languages can be used if particular resources are not available in this language.

On pre-Windows Vista operating systems, the user UI language is usually the same as the system default UI language. However, for Windows MUI, the two languages can be different.

To retrieve the user UI language, an application can call [**GetUserDefaultUILanguage**](/windows/desktop/api/Winnls/nf-winnls-getuserdefaultuilanguage) or [**GetUserPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-getuserpreferreduilanguages). The application cannot change the user UI language, as there is no function to set it.

## Language Lists Maintained by the Operating System

### System Preferred UI Languages List

The resource loader maintains a system preferred UI languages list. Included in this list are languages preferred by the operating system for its own resources, such as menus and dialogs, messages, INF files, and help files. The list is made up of the system default UI language and the system UI language and their fallbacks. An application can retrieve system preferred UI languages by calling [**GetSystemPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-getsystempreferreduilanguages).

### User Preferred UI Languages List

The resource loader uses a user preferred UI languages list that includes languages that the user prefers. The resource loader uses resources matching languages from this list, if available, for a particular application thread. These languages take precedence over any system preferences. To retrieve user preferred UI languages, your application can call [**GetUserPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-getuserpreferreduilanguages).

### Process Preferred UI Languages List

On Windows Vista and later, the resource loader maintains a process preferred UI languages list consisting of up to five valid languages set by a running process for a MUI application. The languages can be set by the application with a call to [**SetProcessPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-setprocesspreferreduilanguages). The application can retrieve the languages by calling [**GetProcessPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-getprocesspreferreduilanguages).

### Thread Preferred UI Languages List

On Windows Vista and later, the resource loader uses a thread preferred UI languages list that consists of up to five valid languages set by a thread in a running process for a MUI application. These languages are used to customize the application user interface languages and make them different from the operating system language. The thread preferred UI languages list is based on the user preferred UI languages, the system preferred UI languages, and the system default UI language.

To set the thread preferred UI languages, the application should call [**SetThreadPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-setthreadpreferreduilanguages). To retrieve these languages, the application calls [**GetThreadPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-getthreadpreferreduilanguages).

## Neutral Language Representation

A neutral language is represented as the language alone, without region or locale. For example, the neutral representation of the English (Canada) language, en-CA, is represented as "en". Even though a neutral language is not associated with the aspects of a region or locale, you can associate it with a resource set. Typically, a neutral language resource is based on the use in the most prevalent region for the language.

As an illustration, suppose that your MUI application localizes German language resources for German (Switzerland) represented as de-CH and German (Austria) represented as de-AT, while building a full set of resources for German (Germany) represented as de-DE. You must make decisions for this application considering entire resource files. If the application duplicates the de-DE resources as neutral language resources, it must provide a fallback language for the resource loader. If the loader does not find a particular language-specific resource file for de-CH or for de-AT, it falls back to the language-neutral "de" resources. These resources are most likely more appropriate than resources for a completely different language, for example, English (United States), which are the only other possible fallbacks.

As another example, an application might not localize at all for Belize. However, support of a language preference of English (Belize), represented as en-BZ, allows the application to fall back to "en" resources.

## Language Fallback in the Resource Loader

Windows Vista and later arrange user interface language settings in a preordered fallback language list used by the resource loader. To form the list, the operating system combines several languages, in the order shown:

-   Thread preferred UI languages, consisting of thread user interface language and its neutral form. Examples are fr-FR for French (France) and its neutral form "fr" and es-ES for Spanish (Spain) and its neutral form "es".
-   Process preferred UI languages, consisting of process user interface language and its neutral form. An example is de-DE for German (Germany) and its neutral form "de".
-   User UI language and its neutral form. An example is ja-JP for Japanese (Japan) and its neutral form "ja".
-   System UI language and its neutral form. An example is it-IT for Italian (Italy) and its neutral form "it".
    > [!Note]  
    > This language is only included in the fallback list when the user UI language is not set.

     

-   System default UI language and its neutral form. An example is es-ES for Spanish (Spain) and its neutral form "es".

The following shows the merged fallback list. Note that the duplication of languages, for example, es-ES and es, is eliminated. Since the example sets the user UI language to ja-JP, the system UI language does not appear in the merged fallback list.

fr-FR, fr, es-ES, es, de-DE, de, ja-JP, ja

When loading resources for a MUI application, the resource loader tries to select one of the files matching the thread preferred UI languages list for the currently running application thread. If the resource loader cannot find a direct match between a selected language and the first language-specific resource in the merged fallback list, it checks the subsequent languages in the list until it finds an acceptable fallback.

If the resource loader finds no file that it needs, it must use a "guaranteed good" fallback language. For the MUI resource technology, the resource loader determines the fallback language from the provided resource configuration data. For more information, see [MUI Resource Management](mui-resource-management.md).

## Related topics

<dl> <dt>

[About Multilingual User Interface](about-multilingual-user-interface.md)
</dt> <dt>

[Locales and Languages](locales-and-languages.md)
</dt> <dt>

[NLS Terminology](nls-terminology.md)
</dt> </dl>

 

 



