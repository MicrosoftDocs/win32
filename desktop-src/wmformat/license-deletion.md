---
title: License Deletion
description: License Deletion
ms.assetid: f941efeb-145d-48a1-a3e2-d12f66b7fdcf
keywords:
- Windows Media Format SDK,licenses
- Windows Media Format SDK,deleting licenses
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- digital rights management (DRM),deleting licenses
- DRM (digital rights management),deleting licenses
- DRM Client Extended APIs,licenses
- Client Extended APIs,licenses
- DRM Client Extended APIs,deleting licenses
- Client Extended APIs,deleting licenses
- licenses,deleting
ms.topic: article
ms.date: 05/31/2018
---

# License Deletion

Any third-party licenses created locally, for example through DRM import, can be deleted by calling the [**IWMDRMLicenseManagement::ProcessLicenseDeletionMessage**](iwmdrmlicensemanagement-processlicensedeletionmessage.md) method. The string you pass to this method will be an XMR license that resembles the following:


```C++
<response type="LRB">
  <DATA>
    <LICENSEDATA>
      <DATA>
        <KID>include Key ID here to revoke certain keys</KID>
        <LID>rights ID</LID
        <META>
          <LGPUBKEY>
            <PublicKey>
              <Modulus>base64 encoded public key</Modulus>
              <Exponent>Exponent in network byte order</Exponent>
            </PublicKey>
          </LGPUBKEY>
          <UID>content-owner-specific user ID</UID>
        </META>
      </DATA>
    </LICENSEDATA>
  </DATA>
</response>
```



The owner specific user ID (UID) field is optional. Optional fields must not be included in the license response if there is not any data associated with them.

## Related topics

<dl> <dt>

[**Building an XMR License**](building-an-xmr-license.md)
</dt> <dt>

[**DRM Import**](drm-import.md)
</dt> <dt>

[**Programming Guide**](drm-programming-guide.md)
</dt> </dl>

 

 




