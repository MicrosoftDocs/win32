---
title: DRM Versions
description: DRM Versions
ms.assetid: ac802547-a3cc-4b30-a8e6-62b679326486
keywords:
- Windows Media Format SDK,DRM versions
- digital rights management (DRM),versions
- DRM (digital rights management),versions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM Versions

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

There are several versions of Windows Media digital rights management (DRM). DRM version 1 is often set apart from the other versions in this documentation, because it is implemented using techniques that are different from the later versions. The second generation of Windows Media DRM is called DRM version 7 because it was introduced as part of the Windows Media Format 7 SDK. It is sometimes called DRM version 2. The later versions of Windows Media DRM, DRM version 9 and the new Windows Media DRM 10, are extensions of DRM version 7 and use the same procedures for implementation. All versions of Windows Media DRM use the same encryption routines; the differences between versions have to do with license features.

When you create protected files by using the objects of the Windows Media Format SDK, you should support both version 1 and the most current version. Files protected by DRM version 1 differ from files protected by later versions only in the contents of the header. Newer files that contain the additional header information can still be used on clients that render only version 1 content. While later versions of DRM offer a higher level of security and additional features, there are still many players that use only version 1.

For more information on DRM versions, see the Windows Media Rights Manager SDK documentation.

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> </dl>

 

 




