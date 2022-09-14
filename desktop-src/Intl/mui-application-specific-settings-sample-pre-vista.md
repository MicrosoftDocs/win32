---
description: 'MUI: Application-Specific Settings Sample (Pre-Windows Vista)'
ms.assetid: 932aa981-ddd9-4a5b-9003-7dafd98e3ae4
title: 'MUI: Application-Specific Settings Sample (Pre-Windows Vista)'
ms.topic: article
ms.date: 05/31/2018
---

# MUI: Application-Specific Settings Sample (Pre-Windows Vista)

The sample application described in this topic is similar to the one shown in [MUI: Application-Specific Settings Sample (Windows Vista)](mui-application-specific-settings-sample-vista.md), except that this application will run on Windows 2000 and later. The main difference from the other sample is that language fallback has to be customized to run on multiple operating systems.

This application first parses a delimited language list in a text file and converts it to a multi-string language list to define the application-specific language preferences. The delimiters supported in the sample are ",", ";", ":", and " ". After parsing the list, the code finds and loads the resources in the identified language. In contrast to the other application-specific settings sample, this code loads and releases resource files using calls to the MUI functions [**LoadMUILibrary**](/windows/desktop/api/Muiload/nf-muiload-loadmuilibrarya) and [**FreeMUILibrary**](/windows/desktop/api/Muiload/nf-muiload-freemuilibrary).


```C++
// Down-Level enabled application that will work with Windows 2000 and later

#include <windows.h>
#include <wchar.h>
#include <strsafe.h>
#include <Nlsdl.h>
#include <MUILoad.h>
#include "resource.h"

#define SUFFICIENTLY_LARGE_STRING_BUFFER (MAX_PATH*2)
#define USER_CONFIGURATION_STRING_BUFFER (((LOCALE_NAME_MAX_LENGTH+1)*5)+1)
#define SUFFICIENTLY_LARGE_ERROR_BUFFER (1024*2)

BOOL GetMyUserDefinedLanguages(WCHAR * langStr, DWORD langStrSize);
BOOL ConvertMyLangStrToMultiLangStr(WCHAR * langStr, WCHAR * langMultiStr, DWORD langMultiStrSize);

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
    UNREFERENCED_PARAMETER(hInstance);
    UNREFERENCED_PARAMETER(hPrevInstance);
    UNREFERENCED_PARAMETER(lpCmdLine);
    UNREFERENCED_PARAMETER(nCmdShow);

    // The following code presents a hypothetical, yet common use pattern of MUI technology
    WCHAR displayBuffer[SUFFICIENTLY_LARGE_ERROR_BUFFER];

    // 1. Application starts by applying any user defined language preferences
    // (language setting is potentially optional for an application that wishes to strictly use OS system language fallback)
    // 1a. Application looks in pre-defined location for user preferences (registry, file, web, etc.)
    WCHAR userLanguagesString[USER_CONFIGURATION_STRING_BUFFER*2];
    if(!GetMyUserDefinedLanguages(userLanguagesString,USER_CONFIGURATION_STRING_BUFFER*2))
    {
        swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to find the user defined language configuration, last error = %d.",GetLastError());
        MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
        return 1; // exit
    }
    // 1b. Application converts the user defined 'readable' languages to the proper multi-string 'less readable' language name format
    WCHAR userLanguagesMultiString[USER_CONFIGURATION_STRING_BUFFER];
    if(!ConvertMyLangStrToMultiLangStr(userLanguagesString,userLanguagesMultiString,USER_CONFIGURATION_STRING_BUFFER))
    {
        swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to convert the user defined language configuration to multi-string, last error = %d.",GetLastError());
        MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
        return 1; // exit
    }
    // 1c. Application now attempts to set the fallback list - this is much different for a down-level 
    // shipping application when compared to a Vista or Windows 7  only shipping application    
    BOOL setSuccess = FALSE;
    DWORD setLangCount = 0;
    HMODULE hDLL = GetModuleHandleW(L"kernel32.dll");
    if( hDLL )
    {
        typedef BOOL (* SET_PREFERRED_UI_LANGUAGES_PROTOTYPE ) ( DWORD, PCWSTR, PULONG );
        SET_PREFERRED_UI_LANGUAGES_PROTOTYPE fp_SetPreferredUILanguages = (SET_PREFERRED_UI_LANGUAGES_PROTOTYPE)NULL;
        fp_SetPreferredUILanguages = (SET_PREFERRED_UI_LANGUAGES_PROTOTYPE) GetProcAddress(hDLL,"SetProcessPreferredUILanguages");
        if( fp_SetPreferredUILanguages )
        {
            // call SetProcessPreferredUILanguages if it is available in Kernel32.dll's export table - Windows 7 and later
            setSuccess = fp_SetPreferredUILanguages(MUI_LANGUAGE_NAME,userLanguagesMultiString,&setLangCount);
        }
        else
        {
            fp_SetPreferredUILanguages = (SET_PREFERRED_UI_LANGUAGES_PROTOTYPE) GetProcAddress(hDLL,"SetThreadPreferredUILanguages");
            // call SetThreadPreferredUILanguages if it is available in Kernel32.dll's export table - Windows Vista and later
            if(fp_SetPreferredUILanguages)
                setSuccess = fp_SetPreferredUILanguages(MUI_LANGUAGE_NAME,userLanguagesMultiString,&setLangCount);
        }
    }

    // 2. Application obtains access to the proper resource container 
    // for standard Win32 resource loading this is normally a PE module
    // LoadMUILibrary is the preferred alternative for loading of resource modules
    // when the application is potentially run on OS versions prior to Vista
    // LoadMUILibrary is available via Windows SDK releases in Vista and later
    // When available, it is advised to get the most up-to-date Windows SDK (e.g., Windows 7)
    HMODULE resContainer = NULL;
    if(setSuccess) // Vista and later OS scenario
    {
        resContainer = LoadMUILibraryW(HELLO_MODULE_CONTRIVED_FILE_PATH,MUI_LANGUAGE_NAME,0);
    }
    else // this block should only be hit on XP and earlier OS platforms as setSuccess will be TRUE on Vista and later
    {
        // need to provide your own fallback mechanism such as the implementation below
        // in essence the application will iterate through the user configured language list
        WCHAR * next = userLanguagesMultiString;
        while(!resContainer && *next != L'\0')
        {
            // convert the language name to an appropriate LCID
            // DownlevelLocaleNameToLCID is available via standalone download package 
            // and is contained in Nlsdl.h / Nlsdl.lib
            LCID nextLcid = DownlevelLocaleNameToLCID(next,DOWNLEVEL_LOCALE_NAME);
            // then have LoadMUILibrary attempt to probe for the right .mui module
            resContainer = LoadMUILibraryW(HELLO_MODULE_CONTRIVED_FILE_PATH,MUI_LANGUAGE_NAME,(LANGID)nextLcid);
            // increment to the next language name in our list
            size_t nextStrLen = 0;
            if(SUCCEEDED(StringCchLengthW(next,LOCALE_NAME_MAX_LENGTH,&nextStrLen)))
                next += (nextStrLen + 1);
            else
                break; // string is invalid - need to exit
        }
        // if the user configured list did not locate a module then try the languages associated with the system
        if(!resContainer)
            resContainer = LoadMUILibraryW(HELLO_MODULE_CONTRIVED_FILE_PATH,MUI_LANGUAGE_NAME,0);
    }
    if(!resContainer)
    {
        swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to load the resource container module, last error = %d.",GetLastError());
        MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
        return 1; // exit
    }

    // 3. Application parses the resource container to find the appropriate item
    WCHAR szHello[SUFFICIENTLY_LARGE_STRING_BUFFER];
    if(LoadStringW(resContainer,HELLO_MUI_STR_0,szHello,SUFFICIENTLY_LARGE_STRING_BUFFER) == 0)
    {
        swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to load the resource string, last error = %d.",GetLastError());
        MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
        FreeLibrary(resContainer);
        return 1; // exit
    }

    // 4. Application presents the discovered resource to the user via UI
    swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"%s MUI",szHello);
    MessageBoxW(NULL,displayBuffer,L"HelloMUI",MB_OK | MB_ICONINFORMATION);

    // 5. Application cleans up memory associated with the resource container after this item is no longer needed.
    if(!FreeMUILibrary(resContainer))
    {
        swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to unload the resource container, last error = %d.",GetLastError());
        MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
        return 1; // exit
    }

    return 0;
}

BOOL GetMyUserDefinedLanguages(WCHAR * langStr, DWORD langStrSize)
{
    BOOL rtnVal = FALSE;
    // very simple implementation - assumes that first 'langStrSize' characters of the 
    // L".\\langs.txt" file comprises a string of one or more languages
    HANDLE langConfigFileHandle = CreateFileW(L".\\langs.txt", GENERIC_READ, 0, 
        NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    if(langConfigFileHandle != INVALID_HANDLE_VALUE)
    {
        // clear out the input variables
        DWORD bytesActuallyRead = 0;
        if(ReadFile(langConfigFileHandle,langStr,langStrSize*sizeof(WCHAR),&bytesActuallyRead,NULL) && bytesActuallyRead > 0)
        {
            rtnVal = TRUE;
            DWORD nullIndex = (bytesActuallyRead/sizeof(WCHAR) < langStrSize) ? bytesActuallyRead/sizeof(WCHAR) : langStrSize;
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
    rtnVal = SUCCEEDED(StringCchLengthW(langStr,USER_CONFIGURATION_STRING_BUFFER*2,&strLen));
    if(rtnVal && strLen > 0 && langMultiStr && langMultiStrSize > 0)
    {
        WCHAR * langMultiStrPtr = langMultiStr;
        WCHAR * last = langStr + (langStr[0] == 0xFEFF ? 1 : 0);
        WCHAR * context = last;
        WCHAR * next = wcstok_s(last,L",; :",&context);
        while(next && rtnVal)
        {
            // make sure you validate the user input
            if(SUCCEEDED(StringCchLengthW(last,LOCALE_NAME_MAX_LENGTH,&strLen)) 
                && DownlevelLocaleNameToLCID(next,0) != 0)
            {
                langMultiStrPtr[0] = L'\0';
                rtnVal &= SUCCEEDED(StringCchCatW(langMultiStrPtr,(langMultiStrSize - (langMultiStrPtr - langMultiStr)),next));
                langMultiStrPtr += strLen + 1;
            }
            next = wcstok_s(NULL,L",; :",&context);
            if(next)
                last = next;
        }
        if(rtnVal && (langMultiStrSize - (langMultiStrPtr - langMultiStr))) // make sure there is a double null term for the multi-string 
        {
            langMultiStrPtr[0] = L'\0';
        }
        else // fail and guard anyone whom might use the multi-string
        {
            langMultiStr[0] = L'\0';
            langMultiStr[1] = L'\0';
        }
    }
    return rtnVal;
}
```



 

 



