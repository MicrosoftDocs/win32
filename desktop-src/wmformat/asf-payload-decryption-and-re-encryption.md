---
title: ASF Payload Decryption and Re-encryption
description: ASF Payload Decryption and Re-encryption
ms.assetid: 0a8c996d-2167-483a-93af-6fe22f0efaf1
keywords:
- Windows Media Format SDK,ASF payload decryption and re-encryption
- Windows Media Format SDK,payload decryption and re-encryption
- Windows Media Format SDK,decryption
- Windows Media Format SDK,re-encryption
- digital rights management (DRM),ASF payload decryption and re-encryption
- DRM (digital rights management),ASF payload decryption and re-encryption
- digital rights management (DRM),payload decryption and re-encryption
- DRM (digital rights management),payload decryption and re-encryption
- digital rights management (DRM),decryption
- DRM (digital rights management),decryption
- digital rights management (DRM),re-encryption
- DRM (digital rights management),re-encryption
- DRM Client Extended APIs,ASF payload decryption and re-encryption
- Client Extended APIs,ASF payload decryption and re-encryption
- DRM Client Extended APIs,payload decryption and re-encryption
- Client Extended APIs,payload decryption and re-encryption
- DRM Client Extended APIs,decryption
- Client Extended APIs,decryption
- DRM Client Extended APIs,re-encryption
- Client Extended APIs,re-encryption
- Advanced Systems Format (ASF),re-encryption
- ASF (Advanced Systems Format),re-encryption
- Advanced Systems Format (ASF),decryption
- ASF (Advanced Systems Format),decryption
- Advanced Systems Format (ASF),payload decryption and re-encryption
- ASF (Advanced Systems Format),payload decryption and re-encryption
ms.topic: article
ms.date: 05/31/2018
---

# ASF Payload Decryption and Re-encryption

The steps below describe the actions that an application must complete to decrypt and re-encrypt each payload:

1.  Increment the salt value.
2.  Pass the payload (encrypted with Windows Media DRM) and the salt value to the decryption function, [**IWMDRMDecrypt::Decrypt**](iwmdrmdecrypt-decrypt.md), which will return the payload, encrypted using the RC4 public key.
3.  Derive a transitory RC4 key by applying an SHA-1 hash of the initialization vector concatenated with the salt value.
4.  Use your transitory key to decrypt the payload.
5.  Immediately re-encrypt the payload with the authorized content protection scheme according to the Windows Media DRM export compliance and robustness rules.
6.  Locate the next payload.

## Related topics

<dl> <dt>

[**Exporting Compressed Content**](exporting-compressed-content.md)
</dt> </dl>

 

 




