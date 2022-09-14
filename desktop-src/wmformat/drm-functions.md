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
ms.date: 05/31/2018
---

# Microsoft Windows Media DRM Client Functions

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

 

 




