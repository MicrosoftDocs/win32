---
description: Lists the objects provided by CryptoAPI.
ms.assetid: 4ab16355-1341-4c7a-b570-bd33f11dde00
title: Cryptography Objects
ms.topic: article
ms.date: 05/31/2018
---

# Cryptography Objects

Cryptography objects are categorized according to usage as follows:

-   [Certificate Store Objects](#certificate-store-objects)
-   [Digital Signature Objects](#digital-signature-objects)
-   [Enveloped Data Objects](#enveloped-data-objects)
-   [Data Encryption Objects](#data-encryption-objects)
-   [Auxiliary Objects](#auxiliary-objects)
-   [Certificate Enrollment Objects](#certificate-enrollment-objects)

## Certificate Store Objects

The following objects work with [*certificate stores*](../secgloss/c-gly.md) and the certificates in those stores. CAPICOM supports the use of Current User, Local Machine, memory, and Active Directory certificate stores.



| Object                                             | Description                                                                                                             |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [**Certificate**](certificate.md)                 | A single digital certificate.                                                                                           |
| [**CertificatePolicies**](certificatepolicies.md) | A collection of [**PolicyInformation**](policyinformation.md) objects.                                                 |
| [**Certificates**](certificates.md)               | Collection of [**Certificate**](certificate.md) objects.                                                               |
| [**CertificateStatus**](certificatestatus.md)     | Provides status information on a certificate.                                                                           |
| [**Chain**](chain.md)                             | Creates and checks a certificate validation chain based on a digital certificate.                                       |
| [**ExtendedProperties**](extendedproperties.md)   | Represents a collection of [**ExtendedProperty**](extendedproperty.md) objects.                                        |
| [**ExtendedProperty**](extendedproperties.md)     | Represents a Microsoft-extended property.                                                                               |
| [**Extension**](extension.md)                     | Represents a single certificate extension.                                                                              |
| [**Extensions**](extensions.md)                   | Represents a collection of [**Extension**](extension.md) objects.                                                      |
| [**PrivateKey**](privatekey.md)                   | Represents a private key.                                                                                               |
| [**PublicKey**](publickey.md)                     | Represents a public key in a [**Certificate**](certificate.md) object.                                                 |
| [**Store**](store.md)                             | Provides the properties and methods to choose, manage, and use certificate stores and the certificates in those stores. |
| [**Template**](template.md)                       | Represents the certificate extension template of the certificate.                                                       |



 

## Digital Signature Objects

The following objects are exported to digitally sign data and to verify digital signatures.



| Object                           | Description                                                                                                 |
|----------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**SignedCode**](signedcode.md) | Object used to sign code with an Authenticode digital signature and to verify the signature on signed code. |
| [**SignedData**](signeddata.md) | Object used to sign data and to verify the signature on signed data.                                        |
| [**Signer**](signer.md)         | Information on a single data signer, including the signer's certificate.                                    |
| [**Signers**](signers.md)       | Collection of [**Signer**](signer.md) objects.                                                             |



 

## Enveloped Data Objects

The following objects are exported to create enveloped data messages for privacy and to decrypt data in enveloped messages.



| Object                                 | Description                                                                                                                                |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnvelopedData**](envelopeddata.md) | Objects used to create, send, and receive enveloped data. Enveloped data is encrypted so that only the intended recipients can decrypt it. |
| [**Recipients**](recipients.md)       | Collection of the [**Certificate**](certificate.md) objects of the intended recipients of an enveloped message.                           |



 

## Data Encryption Objects

The following object is exported to encrypt arbitrary data for privacy and to decrypt encrypted data.



| Object                                 | Description                                                                                                        |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [**EncryptedData**](encrypteddata.md) | Objects used to encrypt data. Encrypted data in an [**EncryptedData**](encrypteddata.md) object can be decrypted. |



 

## Auxiliary Objects

The following objects are exported to change default behaviors of other objects and to manage certificates, certificate stores, and messages.



| Object                                         | Description                                                                                                                                     |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Algorithm**](algorithm.md)                 | Sets the algorithm and [*key length*](../secgloss/k-gly.md) to be used in cryptographic operations. |
| [**Attribute**](attribute.md)                 | Provides a single piece of added information about a signature, such as the time of signing.                                                    |
| [**Attributes**](attributes.md)               | Collection of [**Attribute**](attribute.md) objects.                                                                                           |
| [**BasicConstraints**](basicconstraints.md)   | Provides read-only access to basic constraints on the uses of a certificate.                                                                    |
| [**EKU**](eku.md)                             | Provides access to EKU properties of certificates.                                                                                              |
| [**EKUs**](ekus.md)                           | Collection of [**EKU**](eku.md) objects.                                                                                                       |
| [**EncodedData**](encodeddata.md)             | Represents a block of encoded data.                                                                                                             |
| [**ExtendedKeyUsage**](extendedkeyusage.md)   | Provides read-only access to the extended key usage properties of certificates.                                                                 |
| [**HashedData**](hasheddata.md)               | Provides functionality for applying a hash algorithm to a string.                                                                               |
| [**KeyUsage**](keyusage.md)                   | Provides read-only access to key usage properties of certificates.                                                                              |
| [**NoticeNumbers**](noticenumbers.md)         | Represents a collection of [**Extension**](extension.md) objects.                                                                              |
| [**OID**](oid.md)                             | Represents an object identifier that is used by several CAPICOM properties.                                                                     |
| [**OIDs**](oids.md)                           | Represents a collection of [**OID**](oid.md) objects.                                                                                          |
| [**PolicyInformation**](policyinformation.md) | Provides access to the policy OIDs of an extension.                                                                                             |
| [**Qualifier**](qualifier.md)                 | Represents a Certification Practice Statement (CPS) pointer or user notice qualifier.                                                           |
| [**Qualifiers**](qualifiers.md)               | Represents a collection of qualifiers.                                                                                                          |
| [**Settings**](settings.md)                   | Enables or disables dialog boxes to prompt for signer or sender identity if that identity is not specified.                                     |
| [**Utilities**](utilities.md)                 | Provides functionality for common tasks.                                                                                                        |



 

## Certificate Enrollment Objects

The following object is used for certificate enrollment.



| Object                     | Description                                                                                                                                      |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CEnroll**](/previous-versions/windows/desktop/legacy/aa376007(v=vs.85)) | Object that represents the Certificate Enrollment Control. It is primarily used when programming in Visual Basic or another Automation language. |



 

 

 
