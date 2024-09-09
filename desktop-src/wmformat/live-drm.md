---
title: Live DRM
description: Live DRM
ms.assetid: 0af65f28-8c47-4827-b6d6-c32d75b00f2c
keywords:
- Windows Media Format SDK,Live DRM
- digital rights management (DRM),Live DRM
- DRM (digital rights management),Live DRM
- Live DRM
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Live DRM

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Starting with Windows Media 9 Series, the Windows Media Format SDK can be used to write DRM-protected files. This enables scenarios such as Live DRM, in which DRM protection is applied to a file or stream as it is being encoded, rather than as a post-processing step after encoding has been completed. Live DRM enables content owners to protect live broadcasts, such as pay-per-view concerts or sporting events. Live DRM also represents a simplified or streamlined way to create protected files. You can use Live DRM to apply any version of DRM protection. A protected file created using Live DRM is exactly the same as a file protected as a post-processing step.

**Note** DRM is not supported by the x64-based version of this SDK.

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**Protecting Files with DRM Version 7 or Later**](protecting-files-with-drm-version-7-or-later.md)
</dt> </dl>

 

 




