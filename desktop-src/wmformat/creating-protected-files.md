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
ms.date: 05/31/2018
---

# Creating Protected Files

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

 

 




