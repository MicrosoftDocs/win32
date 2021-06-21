---
description: Authenticode time stamping is based on standard PKCS \#7 countersignatures. Signing tools from Microsoft allow developers to affix time stamps at the same time as they affix Authenticode signatures.
ms.assetid: d0bd3e2f-1eee-4f71-9467-974994f720d5
title: Time Stamping Authenticode Signatures
ms.topic: article
ms.date: 05/31/2018
---

# Time Stamping Authenticode Signatures

Microsoft Authenticode signatures provide authorship and integrity guarantees for binary data. Authenticode time stamping is based on standard PKCS \#7 countersignatures. Signing tools from Microsoft allow developers to affix time stamps at the same time as they affix Authenticode signatures. Time stamping allows Authenticode signatures to be verifiable even after the certificates used for signature have expired.

## A Brief Introduction to Authenticode

[*Authenticode*](../secgloss/a-gly.md) applies digital signature technology to guarantee the authorship and integrity of binary data such as installable software. A client web browser, or other system components, can use the Authenticode signatures to verify the integrity of the data when the software is downloaded or installed. Authenticode signatures can be used with many software formats, including .cab, .exe, .ocx, and .dll.

Microsoft maintains a list of public [*certification authorities*](/security/trusted-root/participants-list) (CAs). Issuers of Authenticode certificates currently include [SSL.com](https://www.ssl.com/), [Digicert](https://www.digicert.com/), [Sectigo(Comodo)](https://www.sectigo.com/), and [GlobalSign](https://www.globalsign.com/).

## About Cryptographic Time Stamping

In the past, a variety of cryptographic time stamping methods have been proposed. See, for example, Haber and Stornetta "How to Time-Stamp a Digital Document" in the *Journal of Cryptology* (1991) and Benaloh and de Mare "One-Way Accumulators: A Decentralized Alternative to Digital Signatures" in *Springer-Verlag Lecture Notes in Computer Science* vol. 765 (EUROCRYPT '93). An extended abstract of this article is available from [Microsoft Research](https://research.microsoft.com/research/pubs/view.aspx?id=233&type=Publication&0sr=a). (These resources may not be available in some languages and countries or regions.) Because time is a physical, rather than a mathematical, quantity, these methods generally concern how to link objects so that their order of creation can be determined or how to efficiently group objects that can all be described as having been created concurrently.

Systems that purport to authenticate time as a quantity always require some form of trust. In a strongly adversarial setting, complex protocols can be used to ensure some degree of synchrony. However, these protocols require extensive interaction between affected parties. In practice, if one only needs certification of time from a trusted source, the source can simply act as a notary by providing a signed statement (certification) that the object was presented for signature at the indicated time.

The countersignature method of time stamping implemented below allows for signatures to be verified even after the signing certificate has expired or been revoked. The time stamp allows the verifier to reliably know the time that the signature was affixed and thereby trust the signature if it was valid at that time. The time stamper should have a reliable and protected time source.

## PKCS \#7 Signed Documents and Countersignatures

PKCS \#7 is a standard format for cryptographic data, including signed data, certificates, and [*certificate revocation lists*](../secgloss/c-gly.md) (CRLs). The particular PKCS \#7 type of interest in the context of time stamping is signed data, corresponding to the PKCS \#7 defined [**SignedData**](signeddata.md) content type.

The PKCS \#7 package consists of [**SignedData**](signeddata.md) that identifies the actual content and certain information about it and SignerInfo signature blocks. A SignerInfo may itself contain a countersignature, which recursively is another SignerInfo. In principle, a sequence of such countersignatures may be present. The countersignature is an unauthenticated attribute with respect to the signature in the SignerInfo; that is, it may be affixed subsequent to the original signature. In outline form:

[**SignedData**](signeddata.md) (PKCS \#7)

-   Version (of PKCS \#7, generally version 1)
-   DigestAlgorithms (collection of all algorithms used by SignerInfo signature blocks, for optimized processing)
-   ContentInfo (contentType equals [**SignedData**](signeddata.md), plus content or reference to content)
-   OPTIONAL Certificates (collection of all certificates used)
-   OPTIONAL CRLs (collection of all CRLs)
-   SignerInfo signature blocks (the actual signature, composed of one or more SignerInfo signature blocks)

SignerInfo (the signature block)

-   Version (of PKCS \#7, generally version 1)
-   Certificate (issuer and serial number to uniquely identify of signer's certificate in [**SignedData**](signeddata.md))
-   DigestAlgorithm plus the DigestEncryptionAlgorithm plus the Digest (hash), plus the EncryptedDigest (actual signature)
-   OPTIONAL AuthenticatedAttributes (for example, signed by this signer)
-   OPTIONAL UnauthenticatedAttributes (for example, not signed by this signer)

An example of an authenticated attribute is the signing time (OID 1.2.840.113549.1.9.5) because it is part of what the time stamp service signs. An example of an unauthenticated attribute is the countersignature (OID 1.2.840.113549.1.9.6) because it can be affixed after signing. In this case, the SignerInfo itself contains a SignerInfo (the Countersignature).

> [!Note]  
> The object that is signed in the countersignature is the original signature (that is, the EncryptedDigest of the original SignerInfo).

 

## SignTool and the Authenticode Process

[SignTool](signtool.md) is available for Authenticode signing and time stamping binary data. The tool is installed in the \\Bin folder of the Microsoft Windows Software Development Kit (SDK) installation path.

Signing and time stamping binary data is relatively straightforward using [SignTool](signtool.md). The publisher must get a code signing certificate from a commercial code signing CA. For convenience, Microsoft publishes and updates a list of public CAs, including those that issue Authenticode certificates. When ready to publish, the object files are signed and time stamped using appropriate command line parameters with the SignTool tool. The result of any SignTool operation is always a PKCS \#7 format [**SignedData**](signeddata.md).

SignTool accepts as input either raw binary data to be signed and time stamped, or previously signed binary data to be time stamped. Data that has previously been signed can be time stamped by using the **signtool timestamp** command.



| Argument             | Description                                                                                                                                                                                                    |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **/t** *HTTPAddress* | Indicates that the file is to be time stamped. A URL that specifies an address of a time stamping server must be provided. **/t** can be used with both **signtool sign** and **signtool timestamp** commands. |



 

For more information about tools that may be useful in this context, see [Cryptography Tools](cryptography-tools.md) and [SignTool](signtool.md).

## Implementation Details and Wire Format

[SignTool](signtool.md) relies on the Windows Authenticode implementation to create and time stamp signatures. [*Authenticode*](../secgloss/a-gly.md) operates on binary files, for example .cab, .exe, .dll, or .ocx. Authenticode first creates the signature, producing a PKCS \#7 [**SignedData**](signeddata.md). It is this **SignedData** that must be countersigned, as described in PKCS \#9.

The countersignature process takes place in four steps:

1.  Copy the signature (that is, the encryptedDigest) from the SignerInfo of the PKCS \#7 [**SignedData**](signeddata.md).
2.  Construct a time stamp request whose content is the original signature. Send this to the time stamp server [*Abstract Syntax Notation One*](../secgloss/a-gly.md) (ASN.1) encoded as a TimeStampRequest.
3.  Receive a time stamp, formatted as a second PKCS \#7 [**SignedData**](signeddata.md), returned from the time stamp server.
4.  Copy the SignerInfo from the time stamp directly into the original PKCS \#7 [**SignedData**](signeddata.md), as a PKCS \#9 countersignature (that is, an unauthenticated attribute in the SignerInfo of the original).

## Time Stamp Request

The time stamp request is sent within an HTTP 1.1 POST message. In the HTTP header, the CacheControl directive is set to no-cache, and the Content-Type directive is set to application/octet-stream. The body of the HTTP message is a base64 encoding of [*Distinguished Encoding Rules*](../secgloss/d-gly.md) (DER) encoding of the time stamp request.

Although not currently used, the Content-Length directive should also be used in constructing the HTTP message because it helps the time stamp server locate where the request is within the HTTP POST.

Other HTTP headers may also be present and should be ignored if they are not understood by the requestor or time stamp server.

The time stamp request is an ASN.1 encoded message. The format of the request is as follows.

``` syntax
TimeStampRequest ::= SEQUENCE {
   countersignatureType OBJECT IDENTIFIER,
   attributes Attributes OPTIONAL, 
   content  ContentInfo
}
```

The countersignatureType is the [*object identifier*](../secgloss/o-gly.md) (OID) that identifies this as a time stamp countersignature and should be the exact OID 1.3.6.1.4.1.311.3.2.1.

No attributes are currently included in the time stamp request.

The content is a ContentInfo as defined by PKCS \#7. The content is the data to be signed. For signature time stamping, the ContentType should be Data, and the content should be the encryptedDigest (signature) from the SignerInfo of the PKCS \#7 content to be time stamped.

## Time Stamp Response

The time stamp response is also sent within an HTTP 1.1 message. In the HTTP header, the Content-Type directive is also set to application/octet-stream. The body of the HTTP message is a base64 encoding of DER encoding of the time stamp response.

The time stamp response is a PKCS \#7 signed message signed by the time stamper. The ContentInfo of the PKCS \#7 message is identical to the ContentInfo received in the time stamp. The PKCS \#7 content contains the signing time authenticated attribute (defined in PKCS \#99, OID 1.2.840.113549.9.5).

After Authenticode receives the time stamp from the server, Authenticode incorporates the time stamp into the original PKCS \#7 [**SignedData**](signeddata.md) as a countersignature. To accomplish this, the ContentInfo of the returned PKCS \#7 **SignedData** is discarded, and the SignerInfo of the returned time stamp is copied as a countersignature into the SignerInfo of the original PKCS \#7 **SignedData**. The certificate chain of the time stamper is also copied into Certificates in the original PKCS \#7 **SignedData** as an unauthenticated attribute of the original signer.

For more information about PKCS and other security subjects, see the [content library of the RSA website](https://www.rsa.com/content_library.aspx).

 

 
