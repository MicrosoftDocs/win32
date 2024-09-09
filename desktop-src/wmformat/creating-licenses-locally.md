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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating Licenses Locally

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

In certain circumstances, such as during [DRM Import](drm-import.md), you can create your own licenses. Windows Media DRM licenses can be written a few different ways, but to make your own license, you must use the Extensible Media Rights (XMR) binary schema. For more information, see [Building an XMR License](building-an-xmr-license.md).

When you create a license, you can add it to the local license store by calling the [**IWMDRMLicenseManagement::StoreLicense**](iwmdrmlicensemanagement-storelicense.md) method.

## Related topics

<dl> <dt>

[**Acquiring Licenses**](acquiring-licenses.md)
</dt> <dt>

[**Building an XMR License**](building-an-xmr-license.md)
</dt> </dl>

 

 




