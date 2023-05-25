---
title: Digital Rights Management Features
description: Digital Rights Management Features
ms.assetid: c3c1e59f-8ff9-496c-8e63-0c1cf4ce7092
keywords:
- Windows Media Format SDK,DRM features
- digital rights management (DRM),features
- DRM (digital rights management),features
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Digital Rights Management Features

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[The Windows Media DRM feature is deprecated and should not be used. Use [Microsoft PlayReady](/windows/uwp/audio-video-camera/playready-client-sdk) instead.\]

Digital rights management (DRM) is a technology that content owners can use to protect digital media files by encrypting them with a key (a piece of data that locks and unlocks the content). To play a protected ASF file, a consumer must obtain a separate license containing the key. Each license also contains rights, determined by the content owner or license issuer, which specify how the consumer can use the file. Using DRM technology, content owners can deliver songs, videos, and other digital media files over the Internet in a protected file format and control the use of their digital content. Microsoft DRM technology is also supported by the Windows Media Rights Manager, the Windows Media Encoder, and Windows Media Player. For more background information on Microsoft's DRM technology, see the [Microsoft Windows Media Web site](https://support.microsoft.com/help/17946/windows-media).

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

The following sections discuss the main DRM-related features of the Windows Media Format SDK.



| Section                                                                                            | Description                                                                                                                          |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [DRM Basics](drm-basics.md)                                                                       | Provides a brief overview of the DRM functionality provided by the Windows Media Format SDK.                                         |
| [DRM Versions](drm-versions.md)                                                                   | Describes the main differences between the versions of DRM protection available to applications.                                     |
| [Live DRM](live-drm.md)                                                                           | Describes the scenarios made possible by "on the fly" DRM protection.                                                                |
| [DRM Individualization](drm-individualization.md)                                                 | Describes the application security upgrade that DRM content owners or license issuers can require.                                   |
| [Backing Up and Restoring of DRM Licenses](backing-up-and-restoring-of-drm-licenses.md)           | Describes the pros and cons of permitting users to back up and restore their content licenses.                                       |
| [Viewing DRM Attributes in the Metadata Editor](viewing-drm-attributes-in-the-metadata-editor.md) | Describes the capabilities of this DRM helper object and the scenarios it was designed to support.                                   |
| [Output Protection Levels](output-protection-levels.md)                                           | Describes how Output Protection Levels make DRM version 10 licenses more flexible.                                                   |
| [License Revocation](license-revocation.md)                                                       | Describes license revocation.                                                                                                        |
| [Windows Media DRM 10 for Network Devices](windows-media-drm-10-for-network-devices.md)           | Introduces Windows Media DRM 10 for Network Devices and its implementation in this SDK.                                              |
| [Microsoft Secure Audio Path](microsoft-secure-audio-path--deprecated.md)                         | Describes the Microsoft Secure Audio Path architecture, which provides the highest degree of protection for protected audio content. |
| [Playlist Burning](playlist-burning.md)                                                           | Describes the playlist-burning feature of DRM and how it is supported in the Windows Media Format SDK.                               |



 

## Related topics

<dl> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> <dt>

[**Features**](features.md)
</dt> </dl>

 

 