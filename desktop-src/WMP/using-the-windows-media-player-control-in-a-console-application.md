---
title: Using the Windows Media Player Control in a Console Application
description: Using the Windows Media Player Control in a Console Application
ms.assetid: e5162aad-69d5-4253-83d1-46735336e6da
keywords:
- Windows Media Player,embedding ActiveX control
- Windows Media Player object model,embedding ActiveX control
- object model,embedding ActiveX control
- Windows Media Player Mobile,embedding ActiveX control
- Windows Media Player ActiveX control,embedding
- Windows Media Player Mobile ActiveX control,embedding
- ActiveX control,embedding
- Windows Media Player,console applications
- Windows Media Player object model,console applications
- object model,console applications
- Windows Media Player Mobile,console applications
- Windows Media Player ActiveX control,console applications
- Windows Media Player Mobile ActiveX control,console applications
- ActiveX control,console applications
- console application embedding
- embedding,console applications
ms.topic: article
ms.date: 05/31/2018
---

# Using the Windows Media Player Control in a Console Application

You can create an instance of the Windows Media Player COM object directly by using **CoCreateInstance**. When you do this, the **Player** object displays no user interface. However, the object is still useful for tasks that don't require the user interface, such as working with the library, playing digital audio files, or accessing properties of the Player.

The following example code shows a simple console program that displays the Windows Media Player version in a message box. The example code uses ATL to take advantage of smart pointers and the **CComBSTR** string class.


```C++
#include "atlbase.h"
#include "atlwin.h"
#include "wmp.h"

int _tmain(int argc, _TCHAR* argv[])
{
    CoInitialize(NULL);

    HRESULT hr = S_OK;
    CComBSTR bstrVersionInfo; // Contains the version string.
    CComPtr<IWMPPlayer> spPlayer;  // Smart pointer to IWMPPlayer interface.

    hr = spPlayer.CoCreateInstance( __uuidof(WindowsMediaPlayer), 0, CLSCTX_INPROC_SERVER );

    if(SUCCEEDED(hr))
    {
        hr = spPlayer->get_versionInfo(&bstrVersionInfo);
    }

    if(SUCCEEDED(hr))
    {
        // Show the version in a message box.
        COLE2T pStr(bstrVersionInfo);
        MessageBox( NULL, (LPCSTR)pStr, _T("Windows Media Player Version"), MB_OK );
    }

    // Clean up.
    spPlayer.Release();
    CoUninitialize();

    return 0;
}

```



## Related topics

<dl> <dt>

[**Using the Windows Media Player Control in a C++ Program**](using-the-windows-media-player-control-in-a-c---program.md)
</dt> </dl>

 

 




