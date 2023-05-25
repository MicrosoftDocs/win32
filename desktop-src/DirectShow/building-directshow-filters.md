---
description: Building DirectShow Filters
ms.assetid: fb907263-e7f3-42d6-80f9-a9f16fc21033
title: Building DirectShow Filters
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Building DirectShow Filters

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The DirectShow base classes are recommended for implementing DirectShow filters. To build with the base classes, perform the following steps, in addition to the steps listed in [Setting Up the Build Environment](setting-up-the-build-environment.md):

- Build the base class library, located in the directory Samples\\Multimedia\\DirectShow\\BaseClasses, under the SDK root directory. There are two versions of the library: a retail version (Strmbase.lib) and a debug version (Strmbasd.lib).
- Include the header file Streams.h.
- Use the \_\_stdcall calling convention.
- Use the multithreaded C run-time library (debug or retail, as appropriate).
- Include a definition (.def) file that exports the DLL functions. The following is an example of a definition file. It assumes that the output file is named MyFilter.dll.

```C++
LIBRARY MYFILTER.DLL
EXPORTS 
    DllMain             PRIVATE
    DllGetClassObject   PRIVATE
    DllCanUnloadNow     PRIVATE
    DllRegisterServer   PRIVATE
    DllUnregisterServer PRIVATE
```

- Link to the following lib files.

| Label | Value |
    |--------------|--------------------------------------|
    | Debug Build  | Strmbasd.lib, Msvcrtd.lib, Winmm.lib |
    | Retail Build | Strmbase.lib, Msvcrt.lib, Winmm.lib  |

- Choose the "ignore default libraries" option in the linker settings.
- Declare the DLL entry point in your source code, as follows:

```C++
extern "C" BOOL WINAPI DllEntryPoint(HINSTANCE, ULONG, LPVOID);
BOOL APIENTRY DllMain(HANDLE hModule, DWORD dwReason, LPVOID lpReserved)
{
    return DllEntryPoint((HINSTANCE)(hModule), dwReason, lpReserved);
}
```

Previous Versions

For versions of the base class library before DirectShow 9.0, you must also do the following:

- For debug builds, define the preprocessor flag DEBUG.

This step is not required for the version of the base class library that is available in DirectShow 9.0 and later.

## Related topics

<dl> <dt>

[DirectShow Base Classes](directshow-base-classes.md)
</dt> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>
