---
title: Creating Protected Files
description: Creating Protected Files
ms.assetid: 5237e797-72ec-402e-81ec-ab379747e464
keywords:
- Windows Media Format SDK,creating protected files
- Windows Media Format SDK,protected files
- Advanced Systems Format (ASF),creating protected files
- ASF (Advanced Systems Format),creating protected files
- Advanced Systems Format (ASF),protected files
- ASF (Advanced Systems Format),protected files
- Advanced Systems Format (ASF),WMStubDRM.lib
- ASF (Advanced Systems Format),WMStubDRM.lib
- WMStubDRM.lib,creating protected files
- WMStubDRM.lib,protected files
- digital rights management (DRM),WMStubDRM.lib
- DRM (digital rights management),WMStubDRM.lib
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating Protected Files

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To create protected digital media files using either DRM version 1 or DRM versions 7 and later, link to the WMStubDRM.lib file that you obtained from Microsoft, and create the writer object. For version 1 protection, use the [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo) interface to set the DRM attributes you want to apply. For versions 7 and later, use the [**IWMDRMWriter**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmwriter) interface methods.

The following topics describe in detail how to protect files.

-   [Protecting Files with DRM Version 1](protecting-files-with-drm-version-1.md)
-   [Protecting Files with DRM Version 7 or Later](protecting-files-with-drm-version-7-or-later.md)

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**DRM Attribute List**](drm-attribute-list.md)
</dt> <dt>

[**DRM Properties**](drm-properties.md)
</dt> <dt>

[**DRM Versions**](drm-versions.md)
</dt> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> <dt>

[**Obtaining the Required DRM Library**](obtaining-the-required-drm-library.md)
</dt> <dt>

[**Reading Protected Files**](reading-protected-files.md)
</dt> </dl>

 

 




