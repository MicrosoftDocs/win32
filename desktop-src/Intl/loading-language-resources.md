---
Description: Loading Language Resources
ms.assetid: 2655b2a3-2926-43f6-aef4-8b756c02a162
title: Loading Language Resources
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Loading Language Resources

Your application loads all user interface language resources, other than certain redirected registry strings, using calls to standard resource loading functions, for example, [**FormatMessage**](base.formatmessage), [**LoadString**](_win32_LoadString_cpp), and [**LoadImage**](_win32_LoadImage_cpp). Many resource loading functions have been modified to load resources from language-specific resource files automatically, treating resources as if they are contained in the LN file. The following example illustrates the use of **LoadString** to load language strings for an application that follows system language settings.


```C++
HMODULE hResModule = LoadLibraryEx(TEXT("Mymodule.dll"), 0,
                                   LOAD_LIBRARY_AS_DATAFILE | LOAD_LIBRARY_AS_IMAGE_RESOURCE);
// ...
LoadString(hResModule, myID, lpBuffer, cbBufferSize);
// ...
FreeLibrary(hResModule);
```



## Related topics

<dl> <dt>

[Locating Win32 PE Resources](locating-win32-pe-resources.md)
</dt> </dl>

 

 



