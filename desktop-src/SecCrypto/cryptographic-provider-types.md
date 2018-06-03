---
Description: The field of cryptography is large and growing.
ms.assetid: ec50d6f1-999d-4ce9-85b4-816afb17550e
title: Cryptographic Provider Types
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cryptographic Provider Types

The field of [*cryptography*](https://www.bing.com/search?q=*cryptography*) is large and growing. There are many different standard data formats and protocols. These are generally organized into groups or families, each of which has its own set of data formats and way of doing things. Even if two families use the same algorithm (for example, the [*RC2*](https://www.bing.com/search?q=*RC2*) [*block cipher*](https://www.bing.com/search?q=*block cipher*)), they will often use different [*padding*](https://www.bing.com/search?q=*padding*) schemes, different [*key lengths*](https://www.bing.com/search?q=*key lengths*), and different default modes. CryptoAPI is designed so that a CSP provider type represents a particular family.

When an application connects to a CSP of a particular type, each of the CryptoAPI functions will, by default, operate in a way prescribed by the family that corresponds to that CSP type. An application's choice of provider type specifies the following items:



| Item                                                                                                                                | Description                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*Key exchange algorithm*](https://www.bing.com/search?q=*Key exchange algorithm*)                | Each provider type specifies one and only one key exchange algorithm. Every CSP of a particular type must implement this algorithm. Applications specify the key exchange algorithm to use by selecting a CSP of the appropriate provider type.                                                        |
| [*Digital signature algorithm*](https://www.bing.com/search?q=*Digital signature algorithm*) | Each provider type specifies one and only one digital signature algorithm. Every CSP of a particular type must implement this algorithm. Applications specify the digital signature algorithm to use by selecting a CSP of the appropriate provider type.                                              |
| Key BLOB formats                                                                                                                    | The provide type determines the format of the [*key BLOB*](https://www.bing.com/search?q=*key BLOB*) used to export keys from the [*CSP*](https://www.bing.com/search?q=*CSP*) and to import keys into a CSP. |
| Digital signature format                                                                                                            | The provider type determines the digital signature format. This ensures that a signature produced by a CSP of a given provider type can be verified by any CSP of the same provider type.                                                                                                              |
| Session key derivation scheme                                                                                                       | The provider type determines the method used to derived a [*session key*](https://www.bing.com/search?q=*session key*) from a [*hash*](https://www.bing.com/search?q=*hash*).                                                                                   |
| [*Key length*](https://www.bing.com/search?q=*Key length*)                                                    | Some provider types specify the length of [*public/private key pairs*](https://www.bing.com/search?q=*public/private key pairs*) and the session keys.                                                                                                               |
| Default modes                                                                                                                       | The provider type often specifies default modes for various options, such as the block encryption [*cipher mode*](https://www.bing.com/search?q=*cipher mode*) or the block encryption [*padding*](https://www.bing.com/search?q=*padding*) method.          |



 

Some advanced application might connect to more than one CSP at a time, but most application generally use only a single CSP.

There are currently a number of predefined provider types. The next sections provide information on the following provider types:

-   [PROV\_RSA\_FULL](prov-rsa-full.md)
-   [PROV\_RSA\_AES](prov-rsa-aes.md)
-   [PROV\_RSA\_SIG](prov-rsa-sig.md)
-   [PROV\_RSA\_SCHANNEL](prov-rsa-schannel.md)
-   [PROV\_DSS](prov-dss.md)
-   [PROV\_DSS\_DH](prov-dss-dh.md)
-   [PROV\_DH\_SCHANNEL](prov-dh-schannel.md)
-   [PROV\_FORTEZZA](prov-fortezza.md)
-   [PROV\_MS\_EXCHANGE](prov-ms-exchange.md)
-   [PROV\_SSL](prov-ssl.md)

Even though some CSP types might be partially compatible with others, two or more applications that need to [*exchange keys*](https://www.bing.com/search?q=*exchange keys*) and encrypted messages should use CSPs of the same type.

A custom CSP writer can define a new provider type. However, the CSP writer is then responsible for distributing the new provider type to the authors of any applications that are to use it. For information about writing custom CSPs, see [Cryptographic Service Providers](cryptographic-service-providers.md).

 

 



