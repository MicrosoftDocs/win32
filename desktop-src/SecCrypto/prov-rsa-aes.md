---
Description: Supports both digital signatures and data encryption. It is considered a general purpose cryptographic service provider (CSP).
ms.assetid: da0b50ec-25a6-40dd-af83-73500b4a4c08
title: PROV\_RSA\_AES
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PROV\_RSA\_AES

The PROV\_RSA\_AES provider type supports both [digital signatures](digital-signatures.md) and data encryption. It is considered a general purpose [*cryptographic service provider*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (CSP). The RSA [*public key algorithm*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) is used for all [*public key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) operations.

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                                                                                                                                                                                                       |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | [*RSA*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd)<br/>                                                                                                                                                                                                                                     |
| Signature    | [*RSA*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd)<br/>                                                                                                                                                                                                                                     |
| Encryption   | [*RC2*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd)<br/> [*RC4*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd)<br/> [*Advanced Encryption Standard*](https://msdn.microsoft.com/0baaa937-f635-4500-8dcd-9dbbd6f4cd02) (AES) <br/>                                                       |
| Hashing      | [*MD2*](https://msdn.microsoft.com/4c4402e9-7455-4868-978f-3899a8fd86c1)<br/> [*MD4*](https://msdn.microsoft.com/4c4402e9-7455-4868-978f-3899a8fd86c1)<br/> [*MD5*](https://msdn.microsoft.com/4c4402e9-7455-4868-978f-3899a8fd86c1)<br/> [*SHA-1*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50)<br/> SHA-2 (SHA-256, SHA-384, and SHA-512)<br/> |



 

## Related Documentation

This provider type is defined by Microsoft and RSA Data Security. It is described in the following documents:

-   *Microsoft Cryptographic Service Provider Programmer's Guide*, Microsoft, 1996.
-   RSA Laboratories, Public Key Cryptography Standards, RSA Data Security, November 1993.

> [!Note]  
> These resources may not be available in some languages and countries or regions.

 

 

 




