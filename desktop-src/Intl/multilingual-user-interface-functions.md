---
Description: The following functions are used with Multilingual User Interface (MUI).
ms.assetid: 918d1f04-78fe-4b60-bee7-08d2f131437e
title: Multilingual User Interface Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Multilingual User Interface Functions

The following functions are used with Multilingual User Interface (MUI).



| Function                                                                 | Description                                                                                                             |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [**EnumUILanguages**](/windows/win32/Winnls/nf-winnls-enumuilanguagesa?branch=master)                               | Enumerates the user interface languages that are available on the operating system.                                     |
| [**EnumUILanguagesProc**](/windows/win32/Winnls/?branch=master)                       | An application-defined function used with the [**EnumUILanguages**](/windows/win32/Winnls/nf-winnls-enumuilanguagesa?branch=master) function.                      |
| [**FreeMUILibrary**](/windows/win32/Muiload/nf-muiload-freemuilibrary?branch=master)                                 | Decrements the reference count of a resource module loaded by [**LoadMUILibrary**](/windows/win32/Muiload/nf-muiload-loadmuilibrarya?branch=master)                  |
| [**GetFileMUIInfo**](/windows/win32/Winnls/nf-winnls-getfilemuiinfo?branch=master)                                 | Retrieves resource-related information about a file.                                                                    |
| [**GetFileMUIPath**](/windows/win32/Winnls/nf-winnls-getfilemuipath?branch=master)                                 | Retrieves the path to a language-specific resource file associated with the supplied LN file.                           |
| [**GetProcessPreferredUILanguages**](/windows/win32/Winnls/nf-winnls-getprocesspreferreduilanguages?branch=master) | Retrieves the process preferred UI languages.                                                                           |
| [**GetSystemDefaultUILanguage**](/windows/win32/Winnls/nf-winnls-getsystemdefaultuilanguage?branch=master)         | Retrieves the language identifier for the system default UI language, known as the "install language" on Windows Vista. |
| [**GetSystemPreferredUILanguages**](/windows/win32/Winnls/nf-winnls-getsystempreferreduilanguages?branch=master)   | Retrieves the system preferred UI languages.                                                                            |
| [**GetThreadPreferredUILanguages**](/windows/win32/Winnls/nf-winnls-getthreadpreferreduilanguages?branch=master)   | Retrieves the thread preferred UI languages for the current thread.                                                     |
| [**GetThreadUILanguage**](/windows/win32/Winnls/nf-winnls-getthreaduilanguage?branch=master)                       | Returns the language identifier of the first user interface language for the current thread.                            |
| [**GetUILanguageFallbackList**](/windows/win32/Muiload/nf-muiload-getuilanguagefallbacklist?branch=master)           | Gets a fallback list of user interface languages represented as language names.                                         |
| [**GetUILanguageInfo**](/windows/win32/Winnls/nf-winnls-getuilanguageinfo?branch=master)                           | Retrieves a variety of information about a user interface language.                                                     |
| [**GetUserDefaultUILanguage**](/windows/win32/Winnls/nf-winnls-getuserdefaultuilanguage?branch=master)             | Returns the language identifier for the user UI language for the current user.                                          |
| [**GetUserPreferredUILanguages**](/windows/win32/Winnls/nf-winnls-getuserpreferreduilanguages?branch=master)       | Retrieves the user preferred UI languages.                                                                              |
| [**LoadMUILibrary**](/windows/win32/Muiload/nf-muiload-loadmuilibrarya?branch=master)                                 | Returns a handle to the language-specific resources associated with a particular language-neutral (LN) file.            |
| [**SetProcessPreferredUILanguages**](/windows/win32/Winnls/nf-winnls-setprocesspreferreduilanguages?branch=master) | Sets the process preferred UI languages for the application process.                                                    |
| [**SetThreadPreferredUILanguages**](/windows/win32/Winnls/nf-winnls-setthreadpreferreduilanguages?branch=master)   | Sets the thread preferred UI languages.                                                                                 |
| [**SetThreadUILanguage**](/windows/win32/Winnls/nf-winnls-setthreaduilanguage?branch=master)                       | Sets the preferred user interface language for the current thread.                                                      |



 

 

 



