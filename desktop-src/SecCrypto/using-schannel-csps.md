---
Description: The SSL protocol engine (Schannel) uses a cryptographic service provider (CSP) when performing cryptographic operations. Cryptographic applications can call CryptAcquireContext using the PROV\_RSA\_SCHANNEL and PROV\_DH\_SCHANNEL providers.
ms.assetid: ad1eabf1-23bc-4d23-8f8b-13f0bda95120
title: Using Schannel CSPs
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Schannel CSPs

The SSL protocol engine ([*Schannel*](security.s_gly#-security-schannel-gly)) uses a [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP) when performing cryptographic operations. Cryptographic applications can call [**CryptAcquireContext**](/windows/win32/Wincrypt/nf-wincrypt-cryptacquirecontexta?branch=master) using the PROV\_RSA\_SCHANNEL and PROV\_DH\_SCHANNEL providers.

This section defines the RSA and Diffie-Hellman Schannel [*CSP types*](security.c_gly#-security-csp-type-gly) and describes the functionality that a CSP must support to be compatible with Schannel.dll, the cryptographic protocol engine. A protocol engine is a program that establishes a secure communications channel between a client and server application.

Applications should not attempt to use information in this documentation to use PROV\_RSA\_SCHANNEL or PROV\_DH\_SCHANNEL directly. Rather, this documentation explains how CSP developers and vendors must write Schannel CSPs that are compatible with Microsoft Schannel providers.

This documentation is intended to help CSP developers implement compatible RSA or Diffie-Hellman Schannel CSPs. Developers are assumed to be familiar with the [*Secure Socket Layer*](security.s_gly#-security-secure-sockets-layer-protocol-gly) (SSL) protocol version 3.0, [*public key*](security.p_gly#-security-public-key-gly) cryptography, [*digital certificates*](security.d_gly#-security-digital-certificate-gly), and the CryptoAPI function set. Developers new to these topics are advised to read the SSL Protocol 3.0 specification and the [Cryptography Essentials](cryptography-essentials.md) documentation in this SDK. In addition, RSA and Diffie-Hellman CSP developers must know [*Transport Layer Security*](security.t_gly#-security-transport-layer-security-protocol-gly) (TLS) protocol specifications along with the relevant RSA and [*Diffie-Hellman algorithms*](security.d_gly#-security-diffie-hellman-algorithm-gly).

For an example used by a Microsoft protocol engine, see [Creating the Master Key](creating-the-master-key.md). The calls to cryptography functions in this example result in calls to CP functions that a CSP must implement. To write a compatible CSP, a developer must understand the SSL 3.0 specification and combine that knowledge with an understanding of the protocol engine code similar to that used in this example.

Because use of the Private Communications Technology protocol is expected to be minimal in the future, developers of new CSPs need not support this protocol. The Schannel protocol engine supports it strictly for backward compatibility.

 

 



