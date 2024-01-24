---
description: Applications that sign and verify XML digital signatures should be written according to the following best practices to avoid denial of service attacks, data loss, and compromise of private information.
ms.assetid: aa972946-9860-49c1-ae94-3f315684c291
title: XML Digital Signature Security Considerations
ms.topic: article
ms.date: 05/31/2018
---

# XML Digital Signature Security Considerations

Applications that sign and verify XML digital signatures should be written according to the following best practices to avoid denial of service attacks, data loss, and compromise of private information. The list below provides general guidance; however, developers are encouraged to perform additional security analysis specific to their applications and review the latest digital signatures best practices published by the W3C.

-   [Verify trust of the signing key](#verify-trust-of-the-signing-key)
-   [First verify the signing key and validate SignedInfo, then validate references](#first-verify-the-signing-key-and-validate-signedinfo-then-validate-references)
-   [Use the minimal set of canonicalization algorithms and transforms required](#use-the-minimal-set-of-canonicalization-algorithms-and-transforms-required)
-   [Ensure target URIs point to destinations within the expected scope](#ensure-target-uris-point-to-destinations-within-the-expected-scope)
-   [Verify the data consumed by the application is verified by the signature](#verify-the-data-consumed-by-the-application-is-verified-by-the-signature)
-   [Follow best cryptographic practices](#follow-best-cryptographic-practices)

## Verify trust of the signing key

Ensure that the signing key is trusted by verifying the corresponding [*X.509*](../secgloss/x-gly.md) certificate (and certificate chain) included in the signed message. Alternately, trust in the signing key can be established in an out-of-band fashion, such as an administrator configuring a set of trusted keys, or an application querying a trusted service over a secure channel.

## First verify the signing key and validate SignedInfo, then validate references

Verify trust in the signing key and the integrity of the **SignedInfo** element prior to validating references. Similarly, applications should validate **Manifest** elements prior to resolving references contained in the **Manifest** elements. **Reference** elements allow the specification of target URIs, transforms, and canonicalization algorithms. If not validated, these fields can potentially be used to create denial of service, data loss, or other attacks.

## Use the minimal set of canonicalization algorithms and transforms required

XSLT and XPATH should not be used within unauthenticated elements, such as **KeyInfo**. If an application requires use of XPath, constrain the set of XPATH expressions allowed to only those that use the ancestor or self axes and do not compute the string value of elements. By default, CryptXML supports a limited set of canonicalization algorithms (see supported URIs in [XML Digital Signature Cryptographic Algorithms](xml-digital-signature-cryptographic-algorithms.md)). Developers can implement additional transforms or canonicalization algorithms for use within their application. However, the use of complex algorithms creates the possibility of denial of service attacks or of breaking a signature's repudiation characteristics. In cases where transforms are required by the application, limit the number of transforms that can be specified per reference to the highest number required by the application. This practice mitigates denial of service attacks based on excessive use of transforms.

## Ensure target URIs point to destinations within the expected scope

Applications should limit target URIs to the smallest scope required by the application. For example, URIs might be expected to point to destinations within the same document, files in a specific target directory, or network locations within a specific DNS domain. URIs set by an attacker to point outside the expected domain could cause an application to retrieve malicious content, send malicious HTTP requests (possibly containing query strings), or cause applications to authenticate to malicious servers.

## Verify the data consumed by the application is verified by the signature

If the application validates the signing key and the **SignedInfo** and **Reference** elements, but the application consumes important data not referenced by the signature, the signature provides no meaningful protection. The semantic meaning of a signature may vary based on the signature's position within the document. Applications are encouraged to check the position of the signature within a document. Additionally, check the position of referenced data and element names to mitigate substitution and wrapping attacks.

## Follow best cryptographic practices

Cryptographic algorithms become weaker over time as new attacks are discovered and more computing power becomes available. Do not hard code cryptographic algorithm identifiers or key sizes into your applications. For a more complete list of best cryptographic practices, see Michael Howard and Steve Lipner, "SDL Minimum Cryptographic Standards," in *The Security Development Lifecycle* (Redmond, Washington: Microsoft Press, 2006), 251–258.

Additional best practices can be found on the W3C website: https://www.w3.org.

> [!Note]  
> These resources may not be available in some languages and countries or regions.

 

 

 
