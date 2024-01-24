---
title: The OnCreate Method
description: The OnCreate Method
ms.assetid: b23546b3-968f-41d8-ba07-3d694152c3ed
keywords:
- Windows Media Player plug-ins,OnCreate method
- plug-ins,OnCreate method
- user interface plug-ins,OnCreate method
- UI plug-ins,OnCreate method
- OnCreate method
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# The OnCreate Method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The OnCreate method is called when the plug-in window is first created.

The following code is used to implement this method:


```C++
LRESULT OnCreate(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL& bHandled)
{
    HWND hCtrl = ::CreateWindowEx(0L, _T("BUTTON"), _T("Search"),
        WS_CHILD | BS_PUSHBUTTON, 10, 10, 100, 30, m_hWnd, 
        (HMENU)IDC_SEARCH, _Module.GetResourceInstance(), NULL);
    ::ShowWindow(hCtrl, SW_SHOW );
    return 0;
}

```



This method creates the **Search** button and associates it with the IDC\_SEARCH command ID, which is defined at the beginning of the file:


```C++
#define IDC_SEARCH 2000

```



This command ID is mapped to the OnSearch method in the message map section described previously.

## Related topics

<dl> <dt>

[**Implementing CPluginWindow**](implementing-cpluginwindow.md)
</dt> </dl>

 

 




