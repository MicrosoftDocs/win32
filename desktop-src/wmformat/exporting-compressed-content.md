---
title: Exporting Compressed Content
description: Exporting Compressed Content
ms.assetid: b312aa5e-d693-4d0a-9d74-b443713cec8c
keywords:
- Windows Media Format SDK,DRM export
- Windows Media Format SDK,export
- Windows Media Format SDK,compressed content
- digital rights management (DRM),export
- DRM (digital rights management),export
- digital rights management (DRM),compressed content
- DRM (digital rights management),compressed content
- DRM Client Extended APIs,compressed content
- Client Extended APIs,compressed content
- DRM Client Extended APIs,export
- Client Extended APIs,export
ms.topic: article
ms.date: 05/31/2018
---

# Exporting Compressed Content

This section describes exporting Windows Media DRM protected media on a Windows Media file where the application receives compressed digital media data. To do this, your application must perform inline decryption of all Windows Media DRM encrypted payloads in an ASF file.

> [!Note]  
> An ASF parsing library is supplied to you as part of the Windows Media DRM Export agreement.

 

The primary steps involved in exporting compressed content are:

1.  Perform DRM individualization, if needed.
2.  Verify that the target content protection scheme is explicitly permitted.
3.  Create a decryptor object to decrypt each ASF payload.
4.  The DRM system transcrypts each ASF payload from Windows Media DRM into RC4 before passing it to your application.

If your application changes the size of an ASF payload during transcryption, you must also remultiplex the ASF file.

Pass to the stub library a Windows Media DRM Export Application Certificate. The certificate is verified, and if it is valid, the DRM system generates an initialization vector and encrypts it using RSA OAEP.

-   An RC4 session key is created for each payload by concatenating the initialization vector and a salt value. You supply the salt value to the decryption API, and you must increment it by a positive non-zero integer value for each payload.

You will be provided a tool by Microsoft as part of the Windows Media DRM export agreement that will enable you to generate your own RSA public/private key pair. You will send the public key to Microsoft, where Microsoft will incorporate it into a signed Windows Media DRM Application Certificate, and return it.

Each payload, after it is decrypted using the RC4 decryption key, must be immediately encrypted into the output CPS. There are other restrictions on handling of unencrypted payloads that are outlined in the robustness and compliance rules, which accompany the Windows Media DRM Export agreement.

## Related topics

<dl> <dt>

[**ASF Payload Decryption and Re-encryption**](asf-payload-decryption-and-re-encryption.md)
</dt> <dt>

[**DRM Export**](drm-export.md)
</dt> <dt>

[**Performing DRM Individualization**](performing-drm-individualization.md)
</dt> <dt>

[**Verification and Initialization**](verification-and-initialization.md)
</dt> </dl>

 

 




