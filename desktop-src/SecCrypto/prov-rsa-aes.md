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

The PROV\_RSA\_AES provider type supports both [digital signatures](digital-signatures.md) and data encryption. It is considered a general purpose [*cryptographic service provider*](https://www.bing.com/search?q=*cryptographic service provider*) (CSP). The RSA [*public key algorithm*](https://www.bing.com/search?q=*public key algorithm*) is used for all [*public key*](https://www.bing.com/search?q=*public key*) operations.

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                                                                                                                                                                                                       |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | [*RSA*](https://www.bing.com/search?q=*RSA*)<br/>                                                                                                                                                                                                                                     |
| Signature    | [*RSA*](https://www.bing.com/search?q=*RSA*)<br/>                                                                                                                                                                                                                                     |
| Encryption   | [*RC2*](https://www.bing.com/search?q=*RC2*)<br/> [*RC4*](https://www.bing.com/search?q=*RC4*)<br/> [*Advanced Encryption Standard*](https://www.bing.com/search?q=*Advanced Encryption Standard*) (AES) <br/>                                                       |
| Hashing      | [*MD2*](https://www.bing.com/search?q=*MD2*)<br/> [*MD4*](https://msdn.microsoft.com/windows/desktop/4c4402e9-7455-4868-978f-3899a8fd86c1)<br/> [*MD5*](https://www.bing.com/search?q=*MD5*)<br/> [*SHA-1*](https://www.bing.com/search?q=*SHA-1*)<br/> SHA-2 (SHA-256, SHA-384, and SHA-512)<br/> |



 

## Related Documentation

This provider type is defined by Microsoft and RSA Data Security. It is described in the following documents:

-   *Microsoft Cryptographic Service Provider Programmer's Guide*, Microsoft, 1996.
-   RSA Laboratories, Public Key Cryptography Standards, RSA Data Security, November 1993.

> [!Note]  
> These resources may not be available in some languages and countries or regions.

 

 

 




