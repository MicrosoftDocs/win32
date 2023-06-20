---
title: Microsoft Windows Media DRM Client Functions
description: Microsoft Windows Media DRM Client Functions
ms.assetid: 5d726c56-d0f3-4eb8-829f-3a0c1a0e0802
keywords:
- Windows Media Format SDK,functions
- digital rights management (DRM),functions
- DRM (digital rights management),functions
- DRM Client Extended APIs,functions
- Client Extended APIs,functions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Microsoft Windows Media DRM Client Functions

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following functions are implemented as part of the Microsoft Windows Media DRM Client Extended APIs.



| Function                                                             | Description                                                                                                                                                                                     |
|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WMDRMCreateProvider**](wmdrmcreateprovider.md)                   | Creates a class factory that can create the other DRM objects. This function does not require a stub library from Microsoft and creates objects that do not support the protected DRM features. |
| [**WMDRMCreateProtectedProvider**](wmdrmcreateprotectedprovider.md) | Creates a class factory that can create the other DRM objects. This function requires a stub library from Microsoft and creates objects that support the protected DRM features.                |
| [**WMDRMShutdown**](wmdrmshutdown.md)                               | Releases resources used by the APIs.                                                                                                                                                            |
| [**WMDRMStartup**](wmdrmstartup.md)                                 | Initializes resources used by the APIs.                                                                                                                                                         |



 

## Related topics

<dl> <dt>

[**Programming Reference**](drm-programming-reference.md)
</dt> </dl>

 

 




