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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DRM Transcryptor Object

The DRM transcryptor object converts DRM-protected ASF files into data streams ready to be sent to network devices that use Windows Media DRM 10 for Network Devices.

The DRM transcryptor object is created by the [**WMCreateDRMTranscryptor**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatedrmtranscryptor?branch=master) function, which sets a pointer to the [**IWMDRMTranscryptor**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmdrmtranscryptor?branch=master) interface. **IUnknown** and **IWMDRMTranscryptor** are the only interfaces supported by this object.

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> </dl>

 

 




