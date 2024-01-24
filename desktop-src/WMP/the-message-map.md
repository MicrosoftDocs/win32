---
title: The Message Map
description: The Message Map
ms.assetid: 4640b0f5-625e-4a9e-86f5-3e75d0afb40d
keywords:
- Windows Media Player plug-ins,message map
- plug-ins,message map
- user interface plug-ins,message map
- UI plug-ins,message map
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# The Message Map

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The plug-in window responds to various events by calling methods that are mapped to corresponding event messages. The wizard provides a mapping so that OnPaint and OnEraseBackground will be called at the appropriate times. To create the **Search** button and to respond to clicks from it, the message map section is modified as follows:


```C++
BEGIN_MSG_MAP(CPluginWindow)
    MESSAGE_HANDLER(WM_PAINT, OnPaint)
    MESSAGE_HANDLER(WM_ERASEBKGND, OnEraseBackground)
    MESSAGE_HANDLER(WM_CREATE, OnCreate)
    COMMAND_ID_HANDLER(IDC_SEARCH, OnSearch)
END_MSG_MAP()

```



## Related topics

<dl> <dt>

[**Implementing CPluginWindow**](implementing-cpluginwindow.md)
</dt> </dl>

 

 




