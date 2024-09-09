---
title: DRM Transcryptor Object
description: DRM Transcryptor Object
ms.assetid: 50c041b3-6621-4618-843f-6ef9b8e741ab
keywords:
- Windows Media Format SDK,DRM transcryptor objects
- Advanced Systems Format (ASF),DRM transcryptor objects
- ASF (Advanced Systems Format),DRM transcryptor objects
- objects,DRM transcryptor objects
- DRM transcryptor objects
- Windows Media Format SDK,transcryptor objects
- Advanced Systems Format (ASF),transcryptor objects
- ASF (Advanced Systems Format),transcryptor objects
- objects,transcryptor objects
- transcryptor objects
- digital rights management (DRM),transcryptor objects
- DRM (digital rights management),transcryptor objects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM Transcryptor Object

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The DRM transcryptor object converts DRM-protected ASF files into data streams ready to be sent to network devices that use Windows Media DRM 10 for Network Devices.

The DRM transcryptor object is created by the [**WMCreateDRMTranscryptor**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatedrmtranscryptor) function, which sets a pointer to the [**IWMDRMTranscryptor**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmtranscryptor) interface. **IUnknown** and **IWMDRMTranscryptor** are the only interfaces supported by this object.

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> </dl>

 

 




