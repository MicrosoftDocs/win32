---
title: Initializing the Page
description: Initializing the Page
ms.assetid: 66bd3810-01a3-4413-9dad-12cf71e72ed1
keywords:
- Windows Media Player online stores,Download Manager
- online stores,Download Manager
- type 2 online stores,Download Manager
- Windows Media Player online stores,initializing pages
- online stores,initializing pages
- type 2 online stores,initializing pages
- Windows Media Player,Download Manager
- Windows Media Player Download Manager
- Download Manager
- initializing pages
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Initializing the Page

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When the webpage loads, the **Init** function runs. This code first retrieves any data stored in a previous session. For details, see [Maintaining Session Information](maintaining-session-information.md). It then creates the **DownloadManager** object and stores it in the global variable named g\_oManager.


```C++
g_oManager = external.DownloadManager;

```



Next, the function connects the **OnColorChange** event to the function named **OnAppColor** and then calls the function directly to initialize the background color. See [Matching the Windows Media Player Colors](matching-the-windows-media-player-colors.md).

Finally, the function starts a timer with a one-second interval and initializes the list boxes that display the pending download collections and download items. This is important because there may have been sessions in progress the last time the online store closed and this information needs to be displayed again.

## Related topics

<dl> <dt>

[**Using the Download Manager**](using-the-download-manager.md)
</dt> </dl>

 

 




