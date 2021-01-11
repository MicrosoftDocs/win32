---
description: PKCS \#7 is a cryptographic message syntax standard.
ms.assetid: fd4e2a13-f257-4ba9-a11d-35f49c5a6c00
title: PKCS \#7 Attributes
ms.topic: article
ms.date: 05/31/2018
---

# PKCS \#7 Attributes

PKCS \#7 is a cryptographic message syntax standard. A PKCS \#7 message does not, by itself, constitute a certificate request, but it can encapsulate a PKCS \#10 or CMC request in a **ContentInfo** ASN.1 structure by using one of the following content types. Encapsulation enables you to add extra functionality, such as multiple signatures, that is not otherwise available.

-   **Data**
-   **SignedData**
-   **EnvelopedData**
-   **SignedAndEnvelopedData**
-   **DigestedData**
-   **EncryptedData**

Attributes can be added to the **authenticatedAttributes** and **unauthenticatedAttributes** fields of the **SignedData** content type.

``` syntax
SignedData ::= SEQUENCE 
{
   version             INTEGER,
   digestAlgorithms    DigestAlgorithmIdentifiers,
   contentInfo         ContentInfo,
   certificates        [0] IMPLICIT Certificates OPTIONAL,
   crls                [1] IMPLICIT CertificateRevocationLists OPTIONAL,
   signerInfos         SignerInfos
}

SignerInfos ::= SET OF SignerInfo

SignerInfo ::= SEQUENCE 
{
    version                     INTEGER,
    sid                         CertIdentifier,
    digestAlgorithm             DigestAlgorithmIdentifier,
    authenticatedAttributes     [0] IMPLICIT Attributes OPTIONAL,
    digestEncryptionAlgorithm   DigestEncryptionAlgId,
    encryptedDigest             EncryptedDigest,
    unauthenticatedAttributes   [1] IMPLICIT Attributes
}

Attributes ::= SET OF Attribute

Attribute ::= SEQUENCE 
{
   type       EncodedObjectID,
   values     AttributeSetValue
}
```

The process required to archive a client's private key on a certification authority (CA) provides a comprehensive example of how authenticated (signed) attributes and the unauthenticated attributes can be used:

-   The client creates an [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object and adds appropriate data for the type of certificate being requested.
-   The client uses the PKCS \#10 request to initialize an [**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc) object. The PKCS \#10 request is placed into the **TaggedRequest** structure in the CMC request. For more information, see [CMC Attributes](cmc-attributes.md).
-   The client encrypts a private key and uses it to initialize an [**IX509AttributeArchiveKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributearchivekey) object. The new **ArchiveKey** attribute is encapsulated in an **EnvelopedData** structure.

    ``` syntax
    EnvelopedData ::= SEQUENCE 
    {
        version                 INTEGER,
        recipientInfos          RecipientInfos,
        encryptedContentInfo    EncryptedContentInfo
    } 

    RecipientInfos ::= SET OF RecipientInfo

    EncryptedContentInfo ::= SEQUENCE 
    {
        contentType                 ContentType,
        contentEncryptionAlgorithm  ContentEncryptionAlgId,
        encryptedContent            [0] IMPLICIT EncryptedContent OPTIONAL
    } 

    EncryptedContent ::= OCTET STRING

    RecipientInfo ::= SEQUENCE 
    {
        version                 INTEGER,
        issuerAndSerialNumber   IssuerAndSerialNumber,
        keyEncryptionAlgorithm  KeyEncryptionAlgId,
        encryptedKey            EncryptedKey
    } 
    ```

-   The client creates a SHA-1 hash of the encrypted key and uses it to initialize an [**IX509AttributeArchiveKeyHash**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributearchivekeyhash) object.
-   The client retrieves the [**CryptAttributes**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestcmc-get_cryptattributes) collection from the CMC request and adds the **ArchiveKey** and the **ArchiveKeyHash** attributes to it. The attributes are placed into the **TaggedAttributes** structure of the CMC request.
-   The client uses the CMC request to initialize an [**IX509CertificateRequestPkcs7**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs7) object. This places the CMC request into the **contentInfo** field of the PKCS \#7 **SignedData** structure.
-   The **ArchiveKeyHash** attribute is signed and placed in the **authenticatedAttributes** sequence of the **SignerInfo** structure.
-   The **ArchiveKey** attribute is placed in the **unauthenticatedAttributes** sequence of the **SignerInfo** structure associated with the primary signer of the PKCS \#7 message.

## Related topics

<dl> <dt>

[Supported Attributes](supported-attributes.md)
</dt> </dl>

 

 



