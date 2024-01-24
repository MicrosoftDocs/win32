---
title: License Revocation (Windows Media Format SDK)
description: License Revocation
ms.assetid: '15917bce-d89e-41eb-904d-7ee290ba545e'
keywords:
- Windows Media Format SDK,license revocation
- digital rights management (DRM),license revocation
- DRM (digital rights management),license revocation
- Windows Media Format SDK,revoking content licenses
- digital rights management (DRM),revoking content licenses
- DRM (digital rights management),revoking content licenses
- license revocation,about
- revoking content licenses
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# License Revocation (Windows Media Format SDK)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Format SDK provides methods by which an application can interact with a license issuer's Web site to revoke a content license.

A typical scenario for license revocation is when a user gives an old computer to someone else. In this case, the original user may have many licenses for protected content stored on the computer even though that user no longer uses the computer. License revocation enables the original user to remove the licenses from the computer.

The license revocation process involves messages being passed back and forth between the client application and a Web-based application created by the license issuer.

**Note** DRM is not supported by the x64-based version of this SDK.

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**Implementing License Revocation**](implementing-license-revocation.md)
</dt> </dl>

 

 




