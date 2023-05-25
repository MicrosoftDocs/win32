---
title: DRM Import
description: DRM Import
ms.assetid: 5e67a721-830b-4d99-9f90-4cb2d7c61104
keywords:
- Windows Media Format SDK,DRM Client Extended APIs
- Windows Media Format SDK,Client Extended APIs
- Windows Media Format SDK,Extended APIs
- Windows Media Format SDK,APIs
- Windows Media Format SDK,digital rights management (DRM)
- Windows Media Format SDK,DRM import
- Windows Media Format SDK,import
- Windows Media Format SDK,content protection system (CPS)
- digital rights management (DRM),Client Extended APIs
- DRM (digital rights management),Client Extended APIs
- digital rights management (DRM),Extended APIs
- DRM (digital rights management),Extended APIs
- digital rights management (DRM),APIs
- DRM (digital rights management),APIs
- digital rights management (DRM),import
- DRM (digital rights management),import
- digital rights management (DRM),content protection system (CPS)
- DRM (digital rights management),content protection system (CPS)
- DRM Client Extended APIs,import
- Client Extended APIs,import
- DRM Client Extended APIs,content protection system (CPS)
- Client Extended APIs,content protection system (CPS)
- content protection system (CPS)
- CPS (content protection system)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM Import

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following sections explain how to convert media content from a third-party content protection system (CPS) to Windows Media DRM. This process is known as DRM Import and consists essentially of the following steps:

1.  Creating the ASF file.
2.  Creating the license.
3.  Optionally deleting the license.

DRM Import is explained in the following sections.



| Section                                                                              | Description                                                                          |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [Importing License and Key Material](importing-license-and-key-material.md)         | Describes how to issue licenses locally and import them into Windows Media DRM.      |
| [Checking Certificate Revocation](checking-certificate-revocation.md)               | Describes how to check certificate revocation.                                       |
| [Building an XMR License](building-an-xmr-license.md)                               | Describes how to create an XMR license and pass it to the DRM subsystem.             |
| [Creating and Initializing a DRM Writer](creating-and-initializing-a-drm-writer.md) | Describes how to initialize an ASF writer object to prepare for DRM Import.          |
| [Encrypting and Importing Media Samples](encrypting-and-importing-media-samples.md) | Describes how to encrypt and import individual media samples into Windows Media DRM. |
| [License Deletion](license-deletion.md)                                             | Describes how to delete locally created licenses.                                    |



 

## Related topics

<dl> <dt>

[**Programming Guide**](drm-programming-guide.md)
</dt> </dl>

 

 




