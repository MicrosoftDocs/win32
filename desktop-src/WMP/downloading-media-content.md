---
title: Downloading Media Content
description: Downloading Media Content
ms.assetid: 0a057e13-6e0c-4a8f-9cab-051183e6b222
keywords:
- Windows Media Player online stores,downloading media content
- online stores,downloading media content
- type 1 online stores,downloading media content
- Windows Media Player online stores,media content downloading
- online stores,media content downloading
- type 1 online stores,media content downloading
- media content,downloading
- downloading media content
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Downloading Media Content

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player handles music file downloads for the online store. A download can be initiated when the discovery page calls [External.download](external-download.md) or when the user chooses, in the Player, to download a set of tracks. In either case, Windows Media Player calls [IWMPContentPartner::Download](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-download), passing a content container list that describes the set of tracks to be downloaded and a cookie that represents the download transaction. The content partner plug-in must then call [IWMPContentPartnerCallback::DownloadTrack](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartnercallback-downloadtrack) once for each track in the set. When the plug-in calls **DownloadTrack**, it passes an **HRESULT** in the *hrDownload* parameter. If the plug-in passes a success code in *hrDownload*, Windows Media Player downloads the track. If the plug-in passes a failure code in *hrDownload*, the Player does not download the track. For each call to **Download**, the plug-in must supply the transaction cookie and the ID of the track in question. For tracks that will actually be downloaded, the plug-in must also supply the URL of the track.

After a file is downloaded, Windows Media Player automatically updates the library to reflect the newly purchased music. The Player provides status information to the plug-in about the download operation by calling [IWMPContentPartner::DownloadTrackComplete](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-downloadtrackcomplete). In this method, the Player provides an **HRESULT** to indicate success or failure of the download, the track ID, and the custom parameters string that the online store provided when it called **DownloadTrack**.

## Related topics

<dl> <dt>

[**Programming Guide for Type 1 Online Stores**](programming-guide-for-type-1-online-stores.md)
</dt> </dl>

 

 




