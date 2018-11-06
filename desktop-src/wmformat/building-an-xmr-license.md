---
title: Building an XMR License
description: Building an XMR License
ms.assetid: c43e4913-82a6-4dd0-9d1f-1fb237ecbb30
keywords:
- Windows Media Format SDK,DRM import
- Windows Media Format SDK,import
- Windows Media Format SDK,XMR licenses
- Windows Media Format SDK,licenses
- Windows Media Format SDK,Extensible Media Rights (XMR)
- digital rights management (DRM),import
- DRM (digital rights management),import
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- digital rights management (DRM),XMR licenses
- DRM (digital rights management),XMR licenses
- digital rights management (DRM),Extensible Media Rights (XMR)
- DRM (digital rights management),Extensible Media Rights (XMR)
- DRM Client Extended APIs,import
- Client Extended APIs,import
- DRM Client Extended APIs,XMR licenses
- Client Extended APIs,XMR licenses
- DRM Client Extended APIs,licenses
- Client Extended APIs,licenses
- DRM Client Extended APIs,Extensible Media Rights (XMR)
- Client Extended APIs,Extensible Media Rights (XMR)
- licenses,XMR
- Extensible Media Rights (XMR)
- XMR (Extensible Media Rights)
ms.topic: article
ms.date: 05/31/2018
---

# Building an XMR License

To generate a license for Windows Media DRM to process, you must use the Extensible Media Rights (XMR) binary schema. XMR is a schema for conveying media usage rights and restrictions and needs to be licensed separately.

The important material in a license is encrypted using the public key in the Windows Media DRM certificate collection, so it is visible only to the Windows Media DRM Client Extended API subsystem. .

It is your responsibility to ensure that the license structure and policy settings are valid and consistent with the license issuer's intent, and that they conform to the compliance rules.

You should read the Windows Media DRM import compliance rules to learn the complete set of XMR objects that must be present in the license.

To pass the XMR license to the DRM subsystem, call the [**IWMDRMLicenseManagement::StoreLicense**](iwmdrmlicensemanagement-storelicense.md) method. Use the following format to pass the license in the *bstrLicenseResponse* parameter:


```C++
<LICENSERESPONSE>
    <LICENSE version="3.0.0.0">insert base64-encoded XMR license here</LICENSE>
</LICENSERESPONSE>
```



This string must be in Unicode format (UTF-16).

## Related topics

<dl> <dt>

[**DRM Import**](drm-import.md)
</dt> </dl>

 

 




