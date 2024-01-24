---
title: DRM Protection and Content License Distribution
description: DRM Protection and Content License Distribution
ms.assetid: 147fef8c-7298-450d-a1a9-345c03c49bec
keywords:
- Windows Media Format SDK,DRM content protection
- Windows Media Format SDK,DRM licenses
- Advanced Systems Format (ASF),DRM content protection
- ASF (Advanced Systems Format),DRM content protection
- Advanced Systems Format (ASF),DRM license distribution
- ASF (Advanced Systems Format),DRM license distribution
- digital rights management (DRM),content protection
- DRM (digital rights management),content protection
- digital rights management (DRM),license distribution
- DRM (digital rights management),license distribution
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM Protection and Content License Distribution

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

On the creation side, digital rights management technology involves two main processes: (1) protecting the content and (2) providing licenses for the content. Protecting a file basically involves encrypting the content, and including a URL in the file header that specifies where a license for the content may be obtained. If you want to protect files with and then distribute the files to other computers or devices, you can use either the Windows Media Format SDK or the Windows Media Rights Manager SDK to protect the file. For live-DRM scenarios, you must use the Windows Media Format SDK to protect the content as it is being encoded.

To create and issue licenses for protected content, you can create your own custom solution using the objects of the Windows Media Rights Manager SDK, or you can use a service run by a third party.

Whichever method you use, the protected files that you create will contain, in the DRM header object, a URL that tells client applications where to obtain a license for the content.

> [!Note]  
> The Windows Media Format SDK does not provide support for creating or issuing licenses.

 

On the playback side, a DRM-enabled application must be able to obtain licenses for protected content, to decrypt that content using the key contained in the license, and to enforce the license restrictions, such as the number of times a file may be played, or whether the file can be copied to another device. The Windows Media Format SDK provides all the support required to create a fully enabled DRM playback application.

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> </dl>

 

 




