---
title: Viewing Attributes of Protected Files
description: Viewing Attributes of Protected Files
ms.assetid: fbfa1a1b-afd0-4f61-86ae-488716e16355
keywords:
- Windows Media Format SDK,viewing attributes of protected files
- Windows Media Format SDK,attributes of protected files
- Windows Media Format SDK,protected files
- Advanced Systems Format (ASF),viewing attributes of protected files
- ASF (Advanced Systems Format),viewing attributes of protected files
- Advanced Systems Format (ASF),attributes of protected files
- ASF (Advanced Systems Format),attributes of protected files
- Advanced Systems Format (ASF),protected files
- ASF (Advanced Systems Format),protected files
- digital rights management (DRM),viewing attributes of protected files
- DRM (digital rights management),viewing attributes of protected files
- digital rights management (DRM),attributes of protected files
- DRM (digital rights management),attributes of protected files
- digital rights management (DRM),protected files
- DRM (digital rights management),protected files
ms.topic: article
ms.date: 05/31/2018
---

# Viewing Attributes of Protected Files

In some scenarios, you may need to retrieve certain DRM attributes in a file without actually accessing the contents of the file. This capability is useful, for example, in applications that process batches of files in different ways based on information in the file header. In previous versions of the Windows Media Format SDK, applications were required to link to the DRM static library in order to open any protected file. Applications that do not have the DRM library can use the [**IWMDRMEditor::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmeditor-getdrmproperty) interface on the metadata editor object to examine certain DRM attributes.

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**DRM Attribute List**](drm-attribute-list.md)
</dt> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> <dt>

[**IWMDRMEditor Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmeditor)
</dt> </dl>

 

 




