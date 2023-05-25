---
title: Viewing DRM Attributes in the Metadata Editor
description: Viewing DRM Attributes in the Metadata Editor
ms.assetid: e25fb8c8-8f4d-40fd-aa6f-675921e0ccdd
keywords:
- Windows Media Format SDK,DRM attribute viewing
- digital rights management (DRM),attribute viewing
- DRM (digital rights management),attribute viewing
- Windows Media Format SDK,Metadata Editor
- digital rights management (DRM),Metadata Editor
- DRM (digital rights management),Metadata Editor
- Windows Media Format SDK,IWMDRMEditor interface
- digital rights management (DRM),IWMDRMEditor interface
- DRM (digital rights management),IWMDRMEditor interface
- Metadata Editor,DRM attribute viewing
- Metadata Editor,IWMDRMEditor interface
- IWMDRMEditor
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Viewing DRM Attributes in the Metadata Editor

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Metadata Editor exposes the IWMDRMEditor interface, which enables editing applications to examine certain attributes of a DRM header in a protected ASF file, and attributes in the content license, if one is present, even if the application doesn't have the DRM-specific static library (wmstubdrm.lib) that is required for fully-enabled DRM player and writer applications.

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**IWMDRMEditor Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmeditor)
</dt> </dl>

 

 




