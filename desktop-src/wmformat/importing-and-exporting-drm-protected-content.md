---
title: Importing and Exporting DRM Protected Content
description: Importing and Exporting DRM Protected Content
ms.assetid: 1c0520dd-b698-4174-a70e-32f43e2395b1
keywords:
- Windows Media Format SDK,DRM Client Extended APIs
- Windows Media Format SDK,Client Extended APIs
- Windows Media Format SDK,Extended APIs
- Windows Media Format SDK,APIs
- Windows Media Format SDK,digital rights management (DRM)
- Windows Media Format SDK,import
- Windows Media Format SDK,export
- digital rights management (DRM),Client Extended APIs
- DRM (digital rights management),Client Extended APIs
- digital rights management (DRM),Extended APIs
- DRM (digital rights management),Extended APIs
- digital rights management (DRM),APIs
- DRM (digital rights management),APIs
- digital rights management (DRM),importing protected content
- DRM (digital rights management),importing protected content
- digital rights management (DRM),exporting protected content
- DRM (digital rights management),exporting protected content
- DRM Client Extended APIs,about
- Client Extended APIs,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Importing and Exporting DRM Protected Content

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

One of the primary roles of the new Windows Media DRM Client Extended APIs is to enable the import and export of DRM-protected content to third-party rights management systems.

The primary challenge of importing and exporting protected data in your application is to robustly share ASF data samples between your system and the DRM subsystem. When your application handles data samples it has to assure that certain robustness standards are met to avoid the potential for the protection mechanism to be circumvented. These standards are outlined in the robustness and compliance rules that you agree to when you license DRM.

## Related topics

<dl> <dt>

[**About the Windows Media DRM Client Extended APIs**](about-the-windows-media-drm-client-extended-apis.md)
</dt> </dl>

 

 




