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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Viewing Attributes of Protected Files

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




