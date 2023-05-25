---
title: Protected Files
description: Protected Files
ms.assetid: '29f70339-8350-43ed-be65-3c8f42d94e50'
keywords:
- Windows Media Format SDK,digital rights management (DRM)
- Windows Media Format SDK,DRM licenses
- Windows Media Format SDK,licenses for DRM
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- digital rights management (DRM),protected file licensing
- DRM (digital rights management),protected file licensing
- licenses,DRM
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Protected Files

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When a file is protected by using Windows Media DRM, the data section of the file is encrypted. The process of protecting a file is also called packaging the file. The Windows Media DRM Client Extended APIs do not enable you to package files. You can package files using the objects of the Windows Media Rights Manager SDK or the Windows Media Format SDK.

A user cannot access the data in a protected file without first obtaining a license for that file.

## Related topics

<dl> <dt>

[**Concepts**](drmconcepts.md)
</dt> </dl>

 

 




