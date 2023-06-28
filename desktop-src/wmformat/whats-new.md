---
title: What's New (Windows Media Format 11 SDK)
description: What's New
ms.assetid: af04b99a-4653-4c82-944a-7005cf1181fe
keywords:
- Windows Media Format SDK,what's new
- Windows Media Format SDK,features
- Windows Media Format SDK,new features
- Windows Media Format SDK,Client Extended APIs
- Windows Media Format SDK,DRM updates
- Windows Media Format SDK,codec updates
- Windows Media Format SDK,thumbnail images
- digital rights management (DRM),new features
- DRM (digital rights management),new features
- thumbnail images
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# What's New (Windows Media Format 11 SDK)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Format 11 SDK introduces new digital rights management (DRM) features. The following changes have been made to the SDK since the 9.5 release.

## Windows Media DRM Client Extended APIs

The Windows Media Format 11 SDK ships with a new set of DRM APIs. These APIs are implemented in their own library. Many of the DRM features supported by the objects of the Windows Media Format SDK are also supported by the Windows Media DRM Client Extended APIs. The primary difference in the new APIs is that they do not rely on having an ASF file to work. Instead, the new APIs deal with the local license store directly, often using the key ID to identify licenses.

For more information, see the [Windows Media DRM Client Extended APIs](windows-media-drm-client-extended-apis.md) documentation.

## Updated Codecs

The Windows Media Video 9 Advanced Profile codec has been updated to produce a compressed bit stream that is compliant with the published SMPTE VC-1 standard.

The Windows Media Audio 10 Professional codec is also included in this release of the SDK. The new audio codec features improved quality at lower bit rates.

## Thumbnail Right

Applications can request a new DRM action to read from video to create a thumbnail image. This enables applications to create and display thumbnail images for video files without opening the file for playback.

## Related topics

<dl> <dt>

[**About the Windows Media Format SDK**](about-the-windows-media-format-sdk.md)
</dt> </dl>

 

 




