---
title: DRM Support in DirectShow
description: DRM Support in DirectShow
ms.assetid: f464d4a4-3478-489a-b9ce-8ab1acabc3c8
keywords:
- Windows Media Format SDK,DRM support in DirectShow
- Windows Media Format SDK,DirectShow
- Windows Media Format SDK,digital rights management (DRM)
- Advanced Systems Format (ASF),DRM support in DirectShow
- ASF (Advanced Systems Format),DRM support in DirectShow
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- Advanced Systems Format (ASF),digital rights management (DRM)
- ASF (Advanced Systems Format),digital rights management (DRM)
- DirectShow,DRM support
- digital rights management (DRM),DirectShow
- DRM (digital rights management),DirectShow
ms.topic: article
ms.date: 05/31/2018
---

# DRM Support in DirectShow

Reading and writing DRM-protected files in DirectShow is done in basically the same way as when you use the Windows Media Format SDK directly. To begin with, you need the wmstubdrm static library, which is obtained separately from Microsoft. In addition, you must implement the **IKeyProvider** interface to enable your application to access the Windows Media Format SDK run-time objects when DRM is enabled.

When applying DRM version 1 protection, use the [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo) interface, which is obtained as described in [Reading ASF Files in DirectShow](reading-asf-files-in-directshow.md). When applying DRM version 7 protection, obtain the [**IWMDRMWriter**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmwriter) interface by calling **QueryService** on the [WM ASF Writer](wm-asf-writer-filter.md) filter, as shown in the code snippet later in this topic.

All other DRM-specific configuration is exactly the same as described in [Enabling DRM Support](enabling-drm-support.md). Use **QueryService** to obtain the [**IWMDRMReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmreader) interface from the [WM ASF Reader](wm-asf-reader-filter.md) filter.

DirectX 9.0 contains a sample, PlayWndASF, a DRM-enabled DirectShow player application that demonstrates DRM version 1 and version 7 license acquisition. This sample also includes an implementation of the **CKeyProvider** class, which supports the **IKeyProvider** interface.

 

 




