---
title: Importing License and Key Material
description: Importing License and Key Material
ms.assetid: 72ce5901-3e5b-4339-b695-592895ac6bfe
keywords:
- Windows Media Format SDK,DRM import
- Windows Media Format SDK,import
- Windows Media Format SDK,licenses
- digital rights management (DRM),import
- DRM (digital rights management),import
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- digital rights management (DRM),key material
- DRM (digital rights management),key material
- DRM Client Extended APIs,import
- Client Extended APIs,import
- DRM Client Extended APIs,licenses
- Client Extended APIs,licenses
- DRM Client Extended APIs,key material
- Client Extended APIs,key material
- licenses,importing
ms.topic: article
ms.date: 05/31/2018
---

# Importing License and Key Material

If you have media content that was encrypted using a third-party content protection system and you want to import the license and key material into Windows Media DRM, follow these steps:

1.  Retrieve the Windows Media DRM machine certificate collection by calling the [**IWMDRMSecurity::GetMachineCertificate**](iwmdrmsecurity-getmachinecertificate.md) method.
2.  Parse the certificate collection, ensuring that it is signed correctly and is validated to a known Microsoft root public key. The certificate collection conforms to the XMR schema. For more information, see [Building an XMR License](building-an-xmr-license.md).
3.  Optional: Extract the revocation list by calling the [**IWMDRMSecurity::GetRevocationData**](iwmdrmsecurity-getrevocationdata.md) method.
4.  Optional: Insure that no certificate in the collection is revoked. For more information, see [Checking Certificate Revocation](checking-certificate-revocation.md).
5.  Generate a license in the XMR format that represents the policy requirements for the import content and contains the appropriate Windows Media DRM key material. For more information, see the topic [Building an XMR License](building-an-xmr-license.md).
6.  Pass the XMR license to the Windows Media DRM system for processing, by using the [**IWMDRMLicenseManagement::StoreLicense**](iwmdrmlicensemanagement-storelicense.md) method.

> [!Note]  
> Details about the XMR schema will be provided to you when you license Windows Media DRM.

 

## Related topics

<dl> <dt>

[**Checking Certificate Revocation**](checking-certificate-revocation.md)
</dt> <dt>

[**Building an XMR License**](building-an-xmr-license.md)
</dt> <dt>

[**DRM Import**](drm-import.md)
</dt> </dl>

 

 




