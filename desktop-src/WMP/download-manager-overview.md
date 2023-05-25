---
title: Download Manager Overview
description: Download Manager Overview
ms.assetid: a13435ac-3784-4d4c-ba49-a51e373a2874
keywords:
- Windows Media Player online stores,Download Manager
- online stores,Download Manager
- type 2 online stores,Download Manager
- Windows Media Player online stores,real-time downloading
- online stores,real-time downloading
- type 2 online stores,real-time downloading
- Windows Media Player online stores,background downloading
- online stores,background downloading
- type 2 online stores,background downloading
- Windows Media Player,Download Manager
- Windows Media Player Download Manager
- Download Manager
- real-time downloading
- background downloading
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Download Manager Overview

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Microsoft Windows Media Player provides online store task panes that contain a hosted browser window. Through the online stores, users can interact with online store webpages across the Internet.

The Windows Media Player Download Manager provides an object model that you can use to handle the tasks associated with downloading content to the user's computer from Microsoft Internet Information Services (IIS) using Hypertext Transfer Protocol (HTTP). With the Download Manager, you can:

-   Manage multiple downloads simultaneously as a collection.
-   Specify a URL for a file and start it downloading using HTTP.
-   Query for the download state and progress.
-   Pause, resume, or cancel a download.
-   Specify whether a download occurs in the background or in real time. (Background downloading is only available on the Microsoft Windows XP operating system.) See [About Background and Real-time Downloading](#about-background-and-real-time-downloading).
-   Specify how content is displayed in the library. See [About Library Integration](#about-library-integration).

The Download Manager is the solution for downloading content from script code in hosted webpages. To download content using C++ code, use the Windows XP Background Intelligent Transfer Service (BITS). For more information, see [BITS](bits.md).

## About Background and Real-time Downloading

The Download Manager offers two types of downloading: background and real-time. Which type you use is up to you, and it is possible to allow the user to select the download type as well. If you choose to allow the user to select the download type, be sure to explain the differences between the two available types.

Real-time downloading occurs all at once. When the user starts a file download, the entire file is transferred to the user's computer in a single, continuous stream. The user cannot pause or otherwise interrupt the download. If the user chooses to close Windows Media Player before the download is finished, he or she loses any incomplete files and must download them from the beginning to acquire the content.

The main advantage of real-time downloading is that it allows the user to acquire the content faster than background downloading. Real-time downloading is available to users of Windows XP, but it is the only type of downloading available on versions of the Windows operating system prior to Windows XP.

Background downloading happens in a piecemeal fashion. When the user starts a background download, parts of the file are transferred to the user's computer when processor time is available. It is possible to pause and resume a background download. If the user chooses to close Windows Media Player before background downloading is finished, the condition of any incomplete files is saved and the downloading can continue in the background, even after restarting the computer.

Background downloading can take longer than real-time downloading because the download process only happens when the processor is not performing other tasks.

Background downloading is only available when using Windows XP.

## About Library Integration

Windows Media Player can automatically organize online store content in the library. To enable this, you must specify a value for the **WM/ContentDistributor** attribute for each digital media file. When a digital media file is added to the library, which happens automatically when using the Download Manager, the file is listed in the **Purchased Music** or **Purchased Videos** node automatically. For example, if the value for **WM/ContentDistributor** is "Proseware" and the digital media file contains music, the content would appear in the library in the following location:

All Music/Purchased Music/Proseware

## Related topics

<dl> <dt>

[**Download Manager**](download-manager.md)
</dt> <dt>

[**DownloadCollection.startDownload**](downloadcollection-startdownload.md)
</dt> </dl>

 

 




