---
description: Your application can support a different set of user interface languages from those supported by the target operating system. This topic discusses this type of support, using snippets from complete samples.
ms.assetid: cb9f2a5f-3bb8-4287-a542-c71d20b37194
title: Supporting Application-Specific Language Settings
ms.topic: article
ms.date: 05/31/2018
---

# Supporting Application-Specific Language Settings

Your application can support a different set of user interface languages from those supported by the target operating system. This topic discusses this type of support, using snippets from complete samples.

## Interpret User's Language Preference

Your application must first determine which user interface language to display, based on user preference. The code can read the settings from a configuration file or from registry settings.

The following example defines two functions used to interpret the user's language preference. The first function illustrates the reading of a delimited list of languages from a file, represented in the code as "langs.txt". The delimiters supported in the sample are ",",";";"." and " ". The second function converts the string read from the file to a multi-string value. This operation is necessary because the MUI functions used to set languages only accept multi-string values.


```C++
BOOL GetMyUserDefinedLanguages(WCHAR * langStr, DWORD langStrSize)
{
    BOOL rtnVal = FALSE;
    // Very simple implementation - assumes that first 'langStrSize' characters of the
    // L".\\langs.txt" file comprises a string of one or more languages.
    HANDLE langConfigFileHandle = CreateFileW(L".\\langs.txt", GENERIC_READ, 0,
                                    NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    if(langConfigFileHandle != INVALID_HANDLE_VALUE)
    {
        // Clear the input variables.
        DWORD bytesActuallyRead = 0;
        if(ReadFile(langConfigFileHandle, langStr, langStrSize*sizeof(WCHAR), &bytesActuallyRead, NULL)
           && bytesActuallyRead > 0)
        {
            rtnVal = TRUE;
            DWORD nullIndex = (bytesActuallyRead/sizeof(WCHAR) < langStrSize)
                              ? bytesActuallyRead/sizeof(WCHAR) : langStrSize;
            langStr[nullIndex] = L'\0';
        }
        CloseHandle(langConfigFileHandle);
    }
    return rtnVal;
}
BOOL ConvertMyLangStrToMultiLangStr(WCHAR * langStr, WCHAR * langMultiStr, DWORD langMultiStrSize)
{
    BOOL rtnVal = FALSE;
    size_t strLen = 0;
    rtnVal = SUCCEEDED(StringCchLengthW(langStr, USER_CONFIGURATION_STRING_BUFFER*2, &strLen));
    if(rtnVal && strLen > 0 && langMultiStr && langMultiStrSize > 0)
    {
        WCHAR * langMultiStrPtr = langMultiStr;
        WCHAR * last = langStr + (langStr[0] == 0xFEFF ? 1 : 0);
        WCHAR * context = last;
        WCHAR * next = wcstok_s(last,L",; :",&context);
        while(next && rtnVal)
        {
            // Make sure you validate the user input.
            if(SUCCEEDED(StringCchLengthW(last, LOCALE_NAME_MAX_LENGTH, &strLen))
               && IsValidLocaleName(next))
            {
                langMultiStrPtr[0] = L'\0';
                rtnVal &= SUCCEEDED(StringCchCatW(langMultiStrPtr,
                                    (langMultiStrSize - (langMultiStrPtr - langMultiStr)), next));
                langMultiStrPtr += strLen + 1;
            }
            next = wcstok_s(NULL, L",; :", &context);
            if(next)
                last = next;
        }
        // Make sure there is a double null term for the multi-string.
        if(rtnVal && (langMultiStrSize - (langMultiStrPtr - langMultiStr)))
        {
            langMultiStrPtr[0] = L'\0';
        }
        else // Fail and guard anyone whom might use the multi-string.
        {
            langMultiStr[0] = L'\0';
            langMultiStr[1] = L'\0';
        }
    }
    return rtnVal;
}
```



## Set the Application Language

After reading the language preference information, the application code must use the retrieved setting to set the application language. On Windows 7 and later, the application can set the language at the process level by calling the [**SetProcessPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-setprocesspreferreduilanguages) function.


```C++
DWORD langCount = 0;
// Using SetProcessPreferredUILanguages is recommended for new applications (esp. multi-threaded applications).
if(!SetProcessPreferredUILanguages(MUI_LANGUAGE_NAME, userLanguagesMultiString, &langCount) || langCount == 0)
{
    swprintf_s(displayBuffer, SUFFICIENTLY_LARGE_ERROR_BUFFER,
               L"FAILURE: Unable to set the user defined languages, last error = %d.", GetLastError());
    MessageBoxW(NULL, displayBuffer, L"HelloMUI ERROR!", MB_OK | MB_ICONERROR);
    return 1; // Exit.
}
```



On Windows Vista and later, the application language is set at the thread level by calling the [**SetThreadPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-setthreadpreferreduilanguages) function.


```C++
DWORD langCount = 0;
// The following line of code is supported on Windows Vista and later.
if(!SetThreadPreferredUILanguages(MUI_LANGUAGE_NAME, userLanguagesMultiString, &langCount) || langCount == 0)
{
    swprintf_s(displayBuffer, SUFFICIENTLY_LARGE_ERROR_BUFFER,
               L"FAILURE: Unable to set the user defined languages, last error = %d.", GetLastError());
    MessageBoxW(NULL, displayBuffer, L"HelloMUI ERROR!", MB_OK | MB_ICONERROR);
    return 1; // Exit.
}
return 1;
```



## Related topics

<dl> <dt>

[Setting Application Language Preferences](setting-application-language-preferences.md)
</dt> <dt>

[MUI: Application-Specific Settings Sample (Windows Vista)](mui-application-specific-settings-sample-vista.md)
</dt> <dt>

[MUI: Application-Specific Settings Sample (Pre-Windows Vista)](mui-application-specific-settings-sample-pre-vista.md)
</dt> </dl>

 

 



