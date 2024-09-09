---
title: Microsoft Secure Audio Path (deprecated)
description: Microsoft Secure Audio Path (deprecated)
ms.assetid: 55833ca4-b25b-408c-af66-f89e9b6110c9
keywords:
- Windows Media Format SDK,Microsoft Secure Audio Path (SAP)
- digital rights management (DRM),Microsoft Secure Audio Path (SAP)
- DRM (digital rights management),Microsoft Secure Audio Path (SAP)
- Windows Media Format SDK,Secure Audio Path (SAP)
- digital rights management (DRM),Secure Audio Path (SAP)
- DRM (digital rights management),Secure Audio Path (SAP)
- Microsoft Secure Audio Path (SAP),about
- Secure Audio Path (SAP),about
- SAP (Secure Audio Path),about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Microsoft Secure Audio Path (deprecated)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This page documents a feature that will be supported with a different technical solution in future versions of Windows.

Content creators and distributors can specify in a DRM license that an audio file is only allowed to be played on a system with Microsoft Secure Audio Path (SAP) components. Secure Audio Path provides a much higher degree of protection to audio content by making it virtually impossible for untrusted applications or audio drivers to access the unencrypted audio bits. Secure Audio Path is supported on Microsoft Windows® Me and Windows XP. It secures digital music in the operating system kernel. In addition, the Digital Millennium Copyright Act makes circumventing antipiracy measures in software a crime.

Secure Audio Path is activated and implemented completely automatically by the Microsoft DRM component when a DRM license requires SAP. For applications running on Windows® XP Service Pack 1, you can enable SAP encryption to any audio content, outside the context of the Microsoft DRM solution, by using the Secure Audio Path SDK. For more information on the Secure Audio Path SDK, see the [Microsoft Web site](/docs/).

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> </dl>

 

 
