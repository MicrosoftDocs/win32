---
description: Validating the Certificate Chain
ms.assetid: e0c36f04-1694-40d8-94a1-06ee7de08777
title: Validating the Certificate Chain
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Validating the Certificate Chain

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This topic describes how to validate the driver's certificate chain when using Certified Output Protection Protocol (COPP).

The graphic driver's certificate chain is an XML document. The certificate chain contains three certificates. The first certificate is called the *leaf certificate*, and is the driver's COPP certificate. The next certificate is the signing certificate of the Independent Hardware Vendor (IHV). The last certificate is Microsoft's signing certificate. To ensure that the graphics driver is a legitimate COPP device, the application must validate all three of these certificates. A malicious program can prevent COPP from working if an application does not correctly validate the certificates in the chain.

COPP certificate chains use the UTF-8 character set. Binary data in the certificates, such as the RSA public key, are base64-encoded and stored in big-endian order. (*Big-endian* means that the most significant byte is stored in the memory location with the lowest address.)

Some elements within a certificate contain Boolean values to denote that a feature of the certificate exists. If the feature exists, the corresponding child element value is set to 1. If a feature is not present, that child element is not present in the certificate.

### XML Element Definitions

The following are definitions for elements in the certificate schema:

-   **CertificateCollection**. The root element of the XML document. It contains Certificate elements, one for each certificate in the chain.
-   **Certificate**. Contains one certificate. This element contains Data and Signature elements.
-   **Data**. Contains information about the certificate. In particular, it contains the certificate's public key and type. The Data element contains the following child elements:
    -   **PublicKey**. Contains the certificate's RSA public key. The PublicKey element contains a KeyValue element, which contains an RSAKeyValue element. The RSAKeyValue element has two child elements, Modulus and Exponent, and these define the public key. The Modulus and Exponent elements are base64-encoded and stored in big-endian order.
    -   **KeyUsage**. If the certificate is the driver's COPP certificate, this element should contain a child element called EncryptKey. If the certificate is the IHV's signing certificate or Microsoft's signing certificate, it should contain a child element called SignCertificate. Both of these child elements contain Boolean values.
    -   **SecurityLevel**. This element should be ignored.
    -   **ManufacturerData**. Specifies the manufacturer and model of the graphics device. This element is informational only.
    -   **Features**. Contains child elements that specify the usage of the certificate. The only one relevant to COPP is the COPPCertificate element. Other child elements might be present; if so, they should be ignored. If the COPPCertificate element exists, the certificate is a COPP certificate. This element must be present in the leaf node of a valid COPP certificate. This element contains a Boolean value.
-   **Signature**. Contains the signature for this certificate. It contains the following child elements:
    -   **SignedInfo**. Contains information about the signature. The important child element of this element is the DigestValue element, which contains the base64-encoded value of the SHA-1 hash over the Data element. The digest value is used when checking the certificate against the certificate revocation list (CRL).
    -   **SignatureValue**. This value is computed over the Data element and is computed according to the RSASSA-PSS digital signature scheme defined in Public-Key Cryptography Standards (PKCS) \#1 (version 2.1). For information about PKCS \#1, visit [https://www.rsa.com/](https://www.rsa.com/).
    -   **KeyInfo**. Contains the RSA public key of the next certificate in the chain. This element is used to verify that the data in the Data element has not been tampered with. This element has the same format as the PublicKey element.

### Certificate Validation

The application must perform the following steps to correctly validate the certificate chain. If any step fails, or if any element referred to in these procedures does not exist, the validation fails.

### Validate Certificate Collection Procedure

To validate the certificate chain, perform the following steps:

1.  Verify that the CertificateCollection is well-formed XML.
2.  Verify that the CertificateCollection is encoded in UTF-8 format.
3.  Check that the Version attribute in the CertificateCollection element is 2.0 or later.
4.  Verify that the certificate chain contains exactly three Certificate elements.
5.  Loop through each Certificate element in the certificate chain and perform the Validate Certificate procedure, described below, on each.

### Validate Certificate Procedure

To validate a certificate in the chain, perform the following steps:

1.  Verify that none of the child elements in the Data element is duplicated. For example, there should be only one PublicKey element.
2.  Ensure that the Data/PublicKey/KeyValue/RSAKeyValue/Modulus element exists. The base64-decoded value must be 256 bytes long for all certificates except the root. In the root certificate, this element must be 128 bytes long.
3.  Ensure that the Data/PublicKey/KeyValue/RSAKeyValue/Exponent element exists. The base64-decoded value must not be larger than 4 bytes.
4.  If this certificate is the leaf certificate, verify the following:
    -   The KeyUsage element contains an EncryptKey element with the value 1.
    -   The Features element contains a COPPCertificate element with the value 1.
5.  If this certificate is not the leaf certificate, verify the following:
    -   The modulus and exponent from the Data/PublicKey element exactly match the modulus and exponent from the Signature/KeyInfo element of the previous certificate.
    -   The KeyUsage element contains a SignCertificate element, with the value 1.
6.  Use the SHA-1 hash algorithm to hash every byte in the certificate's Data element. Every byte from the first character in the &lt;Data&gt; tag to the last character in the closing &lt;/Data&gt; tag should be hashed. The hash value is used to check the certificate against the certificate revocation list (CRL), as described in [Certificate Revocation Lists](certificate-revocation-lists.md)
7.  Compare the hash value from step 6 with the base64-decoded value of the Signature/SignedInfo/Reference/DigestValue element. These values must match.
8.  Perform the Verify Signature procedure, described below.
9.  If this certificate is not the final certificate in the chain, save the Signature/KeyInfo/KeyValue/RSAKeyValue value for the next iteration of the loop.
10. If this certificate is the final certificate in the chain, ensure that the value of Signature/KeyInfo/KeyValue/RSAKeyValue matches Microsoft's public key. The Microsoft public key has the following base64-encoded values:
    -   Modulus:

        `pjoeWLSTLDonQG8She6QhkYbYott9fPZ8tHdB128ZETcghn5KHoyin7HkJEcPJ0Eg4UdSv a0KDIYDjA3EXd69R3CN2Wp/QyOo0ZPYWYp3NXpJ700tKPgIplzo5wVd/69g7j+j8M66W7V NmDwaNs9mDc1p2+VVMsDhOsV/Au6E+E=`

    -   Exponent: `AQAB`

### Verify Signature Procedure

The value of the SignatureValue element is computed over the Data element according to the RSASSA-PSS digital signature scheme defined in PKCS \#1 version 2.1 (hereinafter referred to as PKCS). To verify this signature, perform the following steps:

1.  Decode the Modulus and Exponent values in the Signature/KeyInfo/KeyValue/RSAKeyValue element. These values define the RSA public key of the signing certificate.
2.  Decode the Signature/SignatureValue element.
3.  Compute the RSASSA-PSS-Verify operation, defined in section 8.1.2 of PKCS.

For the RSASSA-PSS-Verify operation, use the following inputs:

-   (*n*,*e*) is the public key from step 1.
-   *M* is all of the bytes in the Data element, including the &lt;Data&gt; and &lt;/Data&gt; tags that enclose the element.
-   *S* is the decoded signature value from step 2.

The RSASSA-PSS-Verify operation uses the EMSA-PSS-ENCODE operation, defined in section 9.1.1. of PKCS. For this operation, COPP uses the following options:

-   Hash = SHA-1
-   *hLen* = 20
-   MGF (mask generation function) = MGF1
-   *sLen* = 0

The mask generation function MGF1 is defined in Appendix B.2 of PKCS. For this function, COPP uses the following options:

-   Hash = SHA-1
-   *hLen* = 20

The output of the RSASSA-PSS-Verify operation indicates whether the signature is valid or invalid.

## Related topics

<dl> <dt>

[Using Certified Output Protection Protocol (COPP)](using-certified-output-protection-protocol--copp.md)
</dt> </dl>

 

 



