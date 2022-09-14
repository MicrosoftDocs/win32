---
title: Creating Licenses Locally
description: Creating Licenses Locally
ms.assetid: 151dd231-26a9-4203-84e1-446a07c1e07a
keywords:
- Windows Media Format SDK,creating licenses locally
- Windows Media Format SDK,licenses
- digital rights management (DRM),creating licenses locally
- DRM (digital rights management),creating licenses locally
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- DRM Client Extended APIs,creating licenses locally
- Client Extended APIs,creating licenses locally
- licenses,creating licenses locally
ms.topic: article
ms.date: 05/31/2018
---

# Creating Licenses Locally

In certain circumstances, such as during [DRM Import](drm-import.md), you can create your own licenses. Windows Media DRM licenses can be written a few different ways, but to make your own license, you must use the Extensible Media Rights (XMR) binary schema. For more information, see [Building an XMR License](building-an-xmr-license.md).

When you create a license, you can add it to the local license store by calling the [**IWMDRMLicenseManagement::StoreLicense**](iwmdrmlicensemanagement-storelicense.md) method.

## Related topics

<dl> <dt>

[**Acquiring Licenses**](acquiring-licenses.md)
</dt> <dt>

[**Building an XMR License**](building-an-xmr-license.md)
</dt> </dl>

 

 




