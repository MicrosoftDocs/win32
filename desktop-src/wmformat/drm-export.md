---
title: DRM Export
description: DRM Export
ms.assetid: 0b44f2e5-e63c-4bdb-8123-097a5d5e3756
keywords:
- Windows Media Format SDK,DRM Client Extended APIs
- Windows Media Format SDK,Client Extended APIs
- Windows Media Format SDK,Extended APIs
- Windows Media Format SDK,APIs
- Windows Media Format SDK,digital rights management (DRM)
- Windows Media Format SDK,DRM export
- Windows Media Format SDK,export
- digital rights management (DRM),Client Extended APIs
- DRM (digital rights management),Client Extended APIs
- digital rights management (DRM),Extended APIs
- DRM (digital rights management),Extended APIs
- digital rights management (DRM),APIs
- DRM (digital rights management),APIs
- digital rights management (DRM),export
- DRM (digital rights management),export
- DRM Client Extended APIs,export
- Client Extended APIs,export
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM Export

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media DRM export functionality enables you to create licensed applications that decrypt content protected by Windows Media DRM, and re-encrypt in an output content protection scheme (CPS) explicitly specified by the associated license issuer. The license issuer explicitly authorizes the export of content to a specific CPS through an inclusion list.

> [!Note]  
> To access export functionality, you must apply for an [Export Application Certificate](export-application-certificate.md) from Microsoft.

 

Windows Media DRM export functionality is explained in the following sections.



| Section                                                                                      | Description                                                                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [Export Application Certificate](export-application-certificate.md)                         | Describes an export application certificate.                                                        |
| [Explicit Authorization and Inclusion Lists](explicit-authorization-and-inclusion-lists.md) | Explains the process of explicit authorization, and how inclusions lists work.                      |
| [Exporting Compressed Content](exporting-compressed-content.md)                             | Describes how to export compressed content from Windows Media DRM protected audio or video content. |



 

## Related topics

<dl> <dt>

[**Explicit Authorization and Inclusion Lists**](explicit-authorization-and-inclusion-lists.md)
</dt> <dt>

[**Programming Guide**](drm-programming-guide.md)
</dt> </dl>

 

 




