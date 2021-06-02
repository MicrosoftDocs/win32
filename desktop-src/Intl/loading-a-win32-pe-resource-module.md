---
description: This topic describes how the application loads a Win32 PE resource module on either Windows Vista and later or on an earlier operating system. Calls are included for releasing the resource module.
ms.assetid: c9f126a7-315a-4856-80b3-aec02402a80e
title: Loading a Win32 PE Resource Module
ms.topic: article
ms.date: 05/31/2018
---

# Loading a Win32 PE Resource Module

This topic describes how the application loads a Win32 PE resource module on either Windows Vista and later or on an earlier operating system. Calls are included for releasing the resource module.

## Load the Resource Module on Windows Vista and Later

On Windows Vista and later, the application loads the resource module using a call to [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**LoadLibraryEx**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryexa). The recommended operation is to call this function with both flags specified. The following is an example of application code that loads a module based on system language settings.


```C++
HMODULE hResModule = LoadLibraryEx(TEXT("Mymodule.dll"), 0,
                                   LOAD_LIBRARY_AS_DATAFILE | LOAD_LIBRARY_AS_IMAGE_RESOURCE);
// ... insert code here to call resource loading functions ...
FreeLibrary(hResModule);
```



## Load the Resource Module on Pre-Windows Vista Operating Systems

On pre-Windows Vista operating systems, the application loads a resource module based on a language setting that is compatible with the target operating system, as well as Windows Vista and later. For this type of module loading, the application must call the MUI functions [**LoadMUILibrary**](/windows/desktop/api/Muiload/nf-muiload-loadmuilibrarya) and [**FreeMUILibrary**](/windows/desktop/api/Muiload/nf-muiload-freemuilibrary).


```C++
#include "MuiLoad.h"
HMODULE hResModule = LoadMUILibrary(TEXT("Mymodule.dll"), MUI_LANGUAGE_NAME, 0);
// ... insert code here to call resource loading functions ...
FreeMUILibrary(hResModule);
```



## Related topics

<dl> <dt>

[Locating Win32 PE Resources](locating-win32-pe-resources.md)
</dt> <dt>

[MUI: Application-Specific Settings Sample (Windows Vista)](mui-application-specific-settings-sample-vista.md)
</dt> <dt>

[MUI: Application-Specific Settings Sample (Pre-Windows Vista)](mui-application-specific-settings-sample-pre-vista.md)
</dt> </dl>

 

 
