---
title: License Pre-Delivery
description: License Pre-Delivery
ms.assetid: 184d9118-5b60-4871-a1e3-75c45153460d
keywords:
- Windows Media Format SDK,pre-delivery of licenses
- Windows Media Format SDK,licenses
- digital rights management (DRM),pre-delivery of licenses
- DRM (digital rights management),pre-delivery of licenses
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- DRM Client Extended APIs,pre-delivery of licenses
- Client Extended APIs,pre-delivery of licenses
- pre-delivery of licenses
- licenses,pre-delivery of licenses
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# License Pre-Delivery

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

License pre-delivery is the process used to pull licenses to a client computer preemptively. A common scenario for using pre-delivery is when a user subscribes to a music service. Without delivering licenses before they are needed, the user would have to wait for license acquisition for each new song.

Because pre-delivery is not done as a response to attempted access, it is typically performed only by the content owner. That is, you can only pre-deliver licenses for content that you control. The pre-delivery process is a coordination between a client component and a license server built by using the objects of the Windows Media Digital Rights Management SDK.

License pre-delivery is similar to [Non-Silent License Acquisition](non-silent-license-acquisition.md). Follow the same steps, except that you don't have a DRM header to pass to [**IWMDRMLicenseManagement::AcquireLicense**](iwmdrmlicensemanagement-acquirelicense.md). The method will generate a challenge that is not content-specific that you can send to your license server.

Alternatively you can use the [Windows Media Rights Manager](/previous-versions//bb676133(v=technet.10)) to pre-deliver licenses.

## Related topics

<dl> <dt>

[**Acquiring Licenses**](acquiring-licenses.md)
</dt> <dt>

[**Using the Media Foundation Event Model**](using-the-media-foundation-model.md)
</dt> </dl>

 

 