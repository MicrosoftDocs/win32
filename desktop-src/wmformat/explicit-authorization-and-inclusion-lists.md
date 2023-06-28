---
title: Explicit Authorization and Inclusion Lists
description: Explicit Authorization and Inclusion Lists
ms.assetid: b2e1cdd4-ea3c-4b05-a53a-2cdc12440645
keywords:
- Windows Media Format SDK,DRM export
- Windows Media Format SDK,export
- Windows Media Format SDK,explicit authorization and inclusion lists
- Windows Media Format SDK,authorization lists
- Windows Media Format SDK,inclusion lists
- digital rights management (DRM),export
- DRM (digital rights management),export
- digital rights management (DRM),explicit authorization and inclusion lists
- DRM (digital rights management),explicit authorization and inclusion lists
- digital rights management (DRM),authorization lists
- DRM (digital rights management),authorization lists
- digital rights management (DRM),inclusion lists
- DRM (digital rights management),inclusion lists
- DRM Client Extended APIs,explicit authorization and inclusion lists
- Client Extended APIs,explicit authorization and inclusion lists
- DRM Client Extended APIs,authorization lists
- Client Extended APIs,authorization lists
- DRM Client Extended APIs,inclusion lists
- Client Extended APIs,inclusion lists
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Explicit Authorization and Inclusion Lists

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Licenses can contain an inclusion list to explicitly authorize the exporting of content protected by Windows Media DRM to other content protection schemes (CPS). As per the terms of the license agreement you enter into with Microsoft to enable DRM Export you can export only to a valid CPS that is identified in the inclusion list of a license.

An inclusion list is a bounded array of globally unique identifiers (GUIDs) that each represents a specific authorized CPS to which the content can be exported. The GUIDs listed in an inclusion list are independent of the output protection levels (OPL) and content protection levels (CPL). Enforcing these restrictions is the responsibility of your application.

> [!Note]  
> When performing Windows Media DRM Export on compressed content, you access the inclusion list through the [**IWMDRMLicense::GetInclusionList**](iwmdrmlicense-getinclusionlist.md) method. When performing Windows Media DRM Export on uncompressed content, use the [**IWMDRMReader3::GetInclusionList**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader3-getinclusionlist) method.

 

To register a new content protection system as a Windows Media DRM Permitted Export in the Windows Media DRM export compliance rules, please contact wmla@microsoft.com.

## Related topics

<dl> <dt>

[**DRM Export**](drm-export.md)
</dt> </dl>

 

 




