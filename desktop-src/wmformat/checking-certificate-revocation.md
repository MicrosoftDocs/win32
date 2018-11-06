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
ms.date: 05/31/2018
---

# Checking Certificate Revocation

When importing content into Windows Media DRM, you must ensure that no certificate in a certificate collection has been revoked by verifying that no certificate in the collection is in the revocation list. The revocation list is extracted by using the [**IWMDRMSecurity::GetRevocationData**](iwmdrmsecurity-getrevocationdata.md) method.

You then use the [**IWMDRMSecurity::CheckCertForRevocation**](iwmdrmsecurity-checkcertforrevocation.md) method to verify that the certificate is not revoked.

## Related topics

<dl> <dt>

[**DRM Import**](drm-import.md)
</dt> </dl>

 

 




