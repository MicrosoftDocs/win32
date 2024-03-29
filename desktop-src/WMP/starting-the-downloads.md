---
title: Starting the Downloads
description: Starting the Downloads
ms.assetid: 0a830b11-f7e1-41da-a867-86f9ac361c0b
keywords:
- Windows Media Player online stores,Download Manager
- online stores,Download Manager
- type 2 online stores,Download Manager
- Windows Media Player online stores,starting downloads
- online stores,starting downloads
- type 2 online stores,starting downloads
- Windows Media Player,Download Manager
- Windows Media Player Download Manager
- Download Manager
- starting downloads
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Starting the Downloads

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The downloading starts when the user clicks **Download**. This button is named btnDownload in the code and the event handler function for the **onClick** event is named "OnDownload".

"OnDownload" first creates a new empty **DownloadCollection** object and assigns it to a local variable.


```C++
oDLC = g_oManager.createDownloadCollection();

```



Next, the function starts each of the five items downloading and stores the returned **DownloadItem** object in an array.


```C++
g_DLI[0] = oDLC.startDownload(g_sFiles[0], g_sDLType);
g_DLI[1] = oDLC.startDownload(g_sFiles[1], g_sDLType);
g_DLI[2] = oDLC.startDownload(g_sFiles[2], g_sDLType);
g_DLI[3] = oDLC.startDownload(g_sFiles[3], g_sDLType);
g_DLI[4] = oDLC.startDownload(g_sFiles[4], g_sDLType);

```



The code then updates the user interface elements with the information about the download collection and its download items.

## Related topics

<dl> <dt>

[**Using the Download Manager**](using-the-download-manager.md)
</dt> </dl>

 

 




