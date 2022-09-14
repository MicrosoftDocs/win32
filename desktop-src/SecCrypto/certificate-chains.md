---
description: To use certificates for security, the authenticity and validity of each certificate received must be verified. This verification depends upon the concept of trust and the delegation of trust \[Platform Software Development Kit (SDK)\].
ms.assetid: e6cb0280-f531-40dc-bbb1-d8115d026e03
title: Certificate Chains
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Chains

To use [*certificates*](../secgloss/c-gly.md) for security, the authenticity and validity of each certificate received must be verified. This verification depends upon the concept of trust and the delegation of trust; for more information, see [Hierarchy of Trust](hierarchy-of-trust.md).

Every certificate contains a subject field that identifies the individual or group to which the certificate was issued. Every certificate also contains an issuer field that identifies the [*certification authority*](../secgloss/c-gly.md) (CA) empowered to certify the identity of the subject.

A certificate chain consists of all the certificates needed to certify the subject identified by the end certificate. In practice this includes the end certificate, the certificates of intermediate CAs, and the certificate of a root CA trusted by all parties in the chain. Every intermediate CA in the chain holds a certificate issued by the CA one level above it in the trust hierarchy. The root CA issues a certificate for itself.

The process of verifying the authenticity and validity of a newly received certificate involves checking all of the certificates in the chain of certificates from the original, universally trusted CA, through any intermediate CAs, down to the certificate just received which is called the end certificate. A new certificate can only be trusted if each certificate in that certificate's chain is properly issued and valid.

Tracking all of the certificates that back a new end certificate can become cumbersome. Therefore, [*CryptoAPI*](../secgloss/c-gly.md) 2.0 technology provides functions that automate creating the chain of certificates that back any given end certificate. These functions also check and report on the validity of each certificate in a chain.

The chain-building and checking functions of [*CryptoAPI*](../secgloss/c-gly.md) 2.0 use a chain engine to create and verify chains of certificates. A chain engine defines a store namespace and cache partitioning for the Certificate Chaining Infrastructure. CryptoAPI 2.0 provides a default chain engine for any application process that only uses default system stores (for example, MY, Root, CA, and Trust) for chain building and caching. An application can define its own store namespace or have its own partitioned cache by creating its own chain engine. To achieve optimal caching behavior, we recommend you create a single chain engine at application startup and use that chain engine throughout the lifetime of the application.

For a list of functions, see [Certificate Chain Verification Functions](cryptography-functions.md). For a program that builds certificate chains and verifies certificates, see [Example C Program: Creating a Certificate Chain](example-c-program-creating-a-certificate-chain.md).

 

 
