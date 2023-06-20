---
title: Checking Certificate Revocation
description: Checking Certificate Revocation
ms.assetid: 498bd2a5-4336-4fc4-9718-6c5fe2db9066
keywords:
- Windows Media Format SDK,DRM import
- Windows Media Format SDK,import
- Windows Media Format SDK,certificate revocation
- Windows Media Format SDK,revocation of certificates
- digital rights management (DRM),import
- DRM (digital rights management),import
- digital rights management (DRM),certificate revocation
- DRM (digital rights management),certificate revocation
- digital rights management (DRM),revocation of certificates
- DRM (digital rights management),revocation of certificates
- DRM Client Extended APIs,import
- Client Extended APIs,import
- DRM Client Extended APIs,certificate revocation
- Client Extended APIs,certificate revocation
- DRM Client Extended APIs,revocation of certificates
- Client Extended APIs,revocation of certificates
- certificates,revocation
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Checking Certificate Revocation

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When importing content into Windows Media DRM, you must ensure that no certificate in a certificate collection has been revoked by verifying that no certificate in the collection is in the revocation list. The revocation list is extracted by using the [**IWMDRMSecurity::GetRevocationData**](iwmdrmsecurity-getrevocationdata.md) method.

You then use the [**IWMDRMSecurity::CheckCertForRevocation**](iwmdrmsecurity-checkcertforrevocation.md) method to verify that the certificate is not revoked.

## Related topics

<dl> <dt>

[**DRM Import**](drm-import.md)
</dt> </dl>

 

 




