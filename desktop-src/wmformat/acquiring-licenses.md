---
title: Acquiring Licenses
description: Acquiring Licenses
ms.assetid: dde33d57-6c63-4e1a-8398-5db466fb22fa
keywords:
- Windows Media Format SDK,DRM Client Extended APIs
- Windows Media Format SDK,Client Extended APIs
- Windows Media Format SDK,Extended APIs
- Windows Media Format SDK,APIs
- Windows Media Format SDK,digital rights management (DRM)
- Windows Media Format SDK,acquiring licenses
- Windows Media Format SDK,licenses
- digital rights management (DRM),Client Extended APIs
- DRM (digital rights management),Client Extended APIs
- digital rights management (DRM),Extended APIs
- DRM (digital rights management),Extended APIs
- digital rights management (DRM),APIs
- DRM (digital rights management),APIs
- digital rights management (DRM),acquiring licenses
- DRM (digital rights management),acquiring licenses
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- DRM Client Extended APIs,acquiring licenses
- Client Extended APIs,acquiring licenses
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Acquiring Licenses

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A common scenario for acquiring licenses is when a user has a protected Windows Media file and tries to access the content for the first time. Because the Windows Media DRM Client Extended APIs are separate from ASF file handling routines, the basic license acquisition scenario, while supported, requires more API calls than using the Windows Media Format SDK and the Media Foundation SDK.

This section describes how to use the Windows Media DRM Client Extended APIs to acquire licenses that are stored in the local license store on a client computer. It contains the following topics.



| Topic                                                                | Description                                                                                                                                |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [Silent License Acquisition](silent-license-acquisition.md)         | Describes how to acquire licenses without user intervention.                                                                               |
| [Non-Silent License Acquisition](non-silent-license-acquisition.md) | Describes how to acquire licenses when user intervention (such as paying for the content) is required.                                     |
| [License Pre-Delivery](license-pre-delivery.md)                     | Describes how to pull licenses from a license server to a client computer.                                                                 |
| [Creating Licenses Locally](creating-licenses-locally.md)           | Describes how to create your own licenses without downloading them from a license server and how to store them in the local license store. |



 

## Related topics

<dl> <dt>

[**Programming Guide**](drm-programming-guide.md)
</dt> </dl>

 

 




