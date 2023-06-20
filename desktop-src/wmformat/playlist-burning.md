---
title: Playlist Burning
description: Playlist Burning
ms.assetid: f34f3ea5-d921-4bfb-a8ea-cf8714b7b21d
keywords:
- Windows Media Format SDK,Windows Media DRM 10
- digital rights management (DRM),Windows Media DRM 10
- DRM (digital rights management),Windows Media DRM 10
- Windows Media Format SDK,playlist burning
- digital rights management (DRM),playlist burning
- DRM (digital rights management),playlist burning
- Windows Media DRM 10
- playlist burning
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Playlist Burning

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media DRM 10 licenses can support copying playlists of protected files to Red Book audio CD. License issuers can limit the number of times content can be copied to CD in a playlist by a total number of times and by the number of times a specific playlist can be copied. For more information about playlist burning rights in licenses, see the Windows Media Rights Manager 10 SDK documentation.

The Windows Media Format SDK provides the ability to quickly check all of the files in a playlist to ensure that they are licensed for playlist burning.

**Note** DRM is not supported by the x64-based version of this SDK.

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**IWMReaderPlaylistBurn Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderplaylistburn)
</dt> </dl>

 

 




