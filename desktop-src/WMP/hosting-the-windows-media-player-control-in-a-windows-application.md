---
title: Hosting the Windows Media Player Control in a Windows Application
description: Hosting the Windows Media Player Control in a Windows Application
ms.assetid: 8da04160-b9db-4082-aeff-b0107189e33e
keywords:
- Windows Media Player,embedding ActiveX control
- Windows Media Player object model,embedding ActiveX control
- object model,embedding ActiveX control
- Windows Media Player Mobile,embedding ActiveX control
- Windows Media Player ActiveX control,embedding
- Windows Media Player Mobile ActiveX control,embedding
- ActiveX control,embedding
- Windows Media Player,Windows-based programs
- Windows Media Player object model,Windows-based programs
- object model,Windows-based programs
- Windows Media Player Mobile,Windows-based programs
- Windows Media Player ActiveX control,Windows-based programs
- Windows Media Player Mobile ActiveX control,Windows-based programs
- ActiveX control,Windows-based programs
- Windows-based program embedding
- embedding,Windows-based programs
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Hosting the Windows Media Player Control in a Windows Application

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To use the Windows Media Player ActiveX control (including the user interface) in a Windows-based program, you must provide an ActiveX control container. ATL provides the **CAxWindow** class to provide ActiveX host window functionality.

To host the Windows Media Player control using the **CAxWindow** class, follow these steps:

1.  Include the following headers:
    ```C++
    #include "wmp.h"
    #include <atlbase.h>
    #include <atlcom.h>
    #include <atlhost.h>
    #include <atlctl.h>
    ```

    

2.  Declare member variables, as follows:
    ```C++
    CAxWindow  m_wndView;  // ActiveX host window class.
    CComPtr<IWMPPlayer>  m_spWMPPlayer;  // Smart pointer to IWMPPlayer interface.
    
    ```

    

3.  When your application window is created, call **AtlAxWinInit**, which is required when using the ATL ActiveX host window.
    ```C++
    AtlAxWinInit();
    
    ```

    

4.  Declare local variables for return codes and to contain the pointer to the host window interface:
    ```C++
    CComPtr<IAxWinHostWindow>  spHost;
    HRESULT  hr;
    
    ```

    

5.  Create the host window:
    ```C++
    GetClientRect(&rcClient);
    m_wndView.Create(m_hWnd, rcClient, NULL, WS_CHILD | WS_VISIBLE | WS_CLIPCHILDREN, WS_EX_CLIENTEDGE);
    
    ```

    

6.  Retrieve the host window interface pointer:
    ```C++
    hr = m_wndView.QueryHost(&spHost);
    
    ```

    

7.  Create the Windows Media Player control in the host window using the class ID:
    ```C++
    hr = spHost->CreateControl(CComBSTR(_T("{6BF52A52-394A-11d3-B153-00C04F79FAA6}")), m_wndView, 0);
    
    ```

    

8.  Retrieve the **IWMPPlayer** interface pointer:
    ```C++
    hr = m_wndView.QueryControl(&m_spWMPPlayer);
    
    ```

    

When you write your own code, be sure to check each **HRESULT** return code for errors.

For a complete sample that illustrates how to host the Windows Media Player ActiveX control by using the **CAxWindow** class, see the WMPHost sample.

## Hosting the Windows Media Player 10 Mobile control in Windows CE

Microsoft eMbedded Visual C++ 4.0 and the Pocket PC 2003 SDK or the Smartphone 2003 SDK must be installed when developing Windows CE-based applications that host a Windows Media Player 10 Mobile control. Also, unlike ATL for Windows, ATL for Windows CE does not support the apartment threading model. Therefore, you must find all instances of apartment threading in your ATL project and change them to use free threading.

## Related topics

<dl> <dt>

[**Samples**](samples.md)
</dt> <dt>

[**Using the Windows Media Player Control in a C++ Program**](using-the-windows-media-player-control-in-a-c---program.md)
</dt> </dl>

 

 




