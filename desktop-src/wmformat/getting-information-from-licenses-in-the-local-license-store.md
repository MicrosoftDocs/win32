---
title: Getting Information from Licenses in the Local License Store
description: Getting Information from Licenses in the Local License Store
ms.assetid: dd1abd5e-6536-4d8f-9607-b800c5a16d04
keywords:
- Windows Media Format SDK,DRM Client Extended APIs
- Windows Media Format SDK,Client Extended APIs
- Windows Media Format SDK,Extended APIs
- Windows Media Format SDK,APIs
- Windows Media Format SDK,digital rights management (DRM)
- Windows Media Format SDK,local license store
- Windows Media Format SDK,licenses
- digital rights management (DRM),Client Extended APIs
- DRM (digital rights management),Client Extended APIs
- digital rights management (DRM),Extended APIs
- DRM (digital rights management),Extended APIs
- digital rights management (DRM),APIs
- DRM (digital rights management),APIs
- digital rights management (DRM),local license store
- DRM (digital rights management),local license store
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- DRM Client Extended APIs,local license store
- Client Extended APIs,local license store
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Getting Information from Licenses in the Local License Store

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media DRM Client Extended APIs provide multiple ways to get information about the rights granted by licenses in the local license store. The following topics describe how to get these various types of information.



| Topic                                                                                                  | Description                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Querying for Simple Rights Information](querying-for-simple-rights-information.md)                   | Describes how to get simple information about whether specific actions are allowed for protected content. For example, can an application play a media file.                    |
| [Querying for Detailed Rights Information](querying-for-detailed-rights-information.md)               | Describes how to get detailed aggregated information about the rights granted by all the licenses in the local license store for a piece of protected content using the key ID. |
| [Enumerating Licenses in the Local License Store](enumerating-licenses-in-the-local-license-store.md) | Describes how to get individual licenses from the local license store.                                                                                                          |



 

## Related topics

<dl> <dt>

[**Programming Guide**](drm-programming-guide.md)
</dt> </dl>

 

 




