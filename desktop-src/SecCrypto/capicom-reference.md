---
description: Provides services that enable application developers to add security based on cryptography to applications.
ms.assetid: 9a2add82-53f9-49ed-b20c-019f95e7d260
title: CAPICOM Reference
ms.topic: article
ms.date: 05/31/2018
---

# CAPICOM Reference

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista and Windows XP. Instead, use the .NET Framework to implement security features. For more information, see [Alternatives to Using CAPICOM](alternatives-to-using-capicom.md).\]

The CAPICOM COM client provides services that enable application developers to add security based on [*cryptography*](../secgloss/c-gly.md) to applications. CryptoAPI includes functionality for authentication using [*digital signatures*](../secgloss/d-gly.md), for enveloping messages, and for encrypting and decrypting data.



| Category                    | Description                                                                                                                |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Certificate Store Objects   | Objects available for using certificate stores and the certificates in those stores.                                       |
| Digital Signature Objects   | Objects used to digitally sign data and to verify digital signatures.                                                      |
| Enveloped Data Objects      | Objects used to create enveloped data messages for privacy and to decrypt data in enveloped messages.                      |
| Data Encryption Objects     | Objects used to encrypt data and to decrypt encrypted data.                                                                |
| Auxiliary Objects           | Objects used to change default behaviors and to manage certificates, certificate stores, and user interface (UI) messages. |
| Interoperability Interfaces | Interfaces that allow derivations of CryptoAPI to work together with CAPICOM 2.0.                                          |
| Enumeration Types           | Enumeration types used with CAPICOM.                                                                                       |



 

## Certificate Store Objects

The following objects work with [*certificate stores*](../secgloss/c-gly.md) and the certificates in those stores. CAPICOM supports the use of Current User, Local Machine, Memory, and Active Directory certificate stores.



| Object                                             | Description                                                                                                             |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [**Certificate**](certificate.md)                 | A single digital certificate.                                                                                           |
| [**CertificatePolicies**](certificatepolicies.md) | A collection of [**PolicyInformation**](policyinformation.md) objects.                                                 |
| [**Certificates**](certificates.md)               | Collection of [**Certificate**](certificate.md) objects.                                                               |
| [**CertificateStatus**](certificatestatus.md)     | Provides status information on a certificate.                                                                           |
| [**Chain**](chain.md)                             | Creates and checks a certificate validation chain based on a digital certificate.                                       |
| [**ExtendedProperties**](extendedproperties.md)   | Represents a collection of [**ExtendedProperty**](extendedproperty.md) objects.                                        |
| [**ExtendedProperty**](extendedproperty.md)       | Represents a Microsoft-extended property.                                                                               |
| [**Extension**](extension.md)                     | Represents a single certificate extension.                                                                              |
| [**Extensions**](extensions.md)                   | Represents a collection of [**Extension**](extension.md) objects.                                                      |
| [**PrivateKey**](privatekey.md)                   | Represents a private key.                                                                                               |
| [**PublicKey**](publickey.md)                     | Represents a public key in a [**Certificate**](certificate.md) object.                                                 |
| [**Store**](store.md)                             | Provides the properties and methods to choose, manage, and use certificate stores and the certificates in those stores. |
| [**Template**](template.md)                       | Represents the certificate extension template of the certificate.                                                       |



 

## Digital Signature Objects

The following objects are exported to digitally sign data and to verify digital signatures.



| Object                           | Description                                                                        |
|----------------------------------|------------------------------------------------------------------------------------|
| [**SignedCode**](signedcode.md) | Provides functionality for signing content with an Authenticode digital signature. |
| [**SignedData**](signeddata.md) | Object used to sign data and to verify the signature on signed data.               |
| [**Signer**](signer.md)         | Information on a single data signer, including the signer's certificate.           |
| [**Signers**](signers.md)       | Collection of [**Signer**](signer.md) objects.                                    |



 

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
| [**OID**](oid.md)                             | Represents an object identifier that is used by several CAPICOM properties.                                                                     |
| [**OIDs**](oids.md)                           | Represents a collection of [**OID**](oid.md) objects.                                                                                          |
| [**PolicyInformation**](policyinformation.md) | Provides access to the policy OIDs of an extension.                                                                                             |
| [**Qualifier**](qualifier.md)                 | Represents a Certification Practice Statement (CPS) pointer or user notice qualifier.                                                           |
| [**Qualifiers**](qualifiers.md)               | Represents a collection of qualifiers.                                                                                                          |
| [**Settings**](settings.md)                   | Enables or disables dialog boxes to prompt for signer or sender identity if that identity is not specified.                                     |
| [**Utilities**](utilities.md)                 | Provides functionality for common tasks.                                                                                                        |



 

## Interoperability Interfaces

The following interfaces allow derivations of CryptoAPI to work together with CAPICOM 2.0.



| Interface                              | Description                                                                                                                                                                              |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICertContext**](icertcontext.md)   | Provides access to the context of a CAPICOM X.509v3 [**Certificate**](certificate.md) object. This context allows the CAPICOM certificate to be used in other derivations of CryptoAPI. |
| [**ICertStore**](icertstore.md)       | Provides access to the context of a CAPICOM [**Store**](store.md) object. This context allows the CAPICOM certificate store to be used in other derivations of CryptoAPI.               |
| [**IChainContext**](ichaincontext.md) | Provides access to the context of a CAPICOM [**Chain**](chain.md) object. This context allows the CAPICOM certificate trust chain to be used in other derivations of CryptoAPI.         |



 

## Enumeration Types

CAPICOM defines the following enumeration types:

-   [**CAPICOM\_ACTIVE\_DIRECTORY\_SEARCH\_LOCATION**](capicom-active-directory-search-location.md)
-   [**CAPICOM\_ATTRIBUTE**](capicom-attribute.md)
-   [**CAPICOM\_CERT\_INFO\_TYPE**](capicom-cert-info-type.md)
-   [**CAPICOM\_CERTIFICATE\_FIND\_TYPE**](capicom-certificate-find-type.md)
-   [**CAPICOM\_CERTIFICATE\_INCLUDE\_OPTION**](capicom-certificate-include-option.md)
-   [**CAPICOM\_CERTIFICATE\_SAVE\_AS\_TYPE**](capicom-certificate-save-as-type.md)
-   [**CAPICOM\_CERTIFICATES\_SAVE\_AS\_TYPE**](capicom-certificates-save-as-type.md)
-   [**CAPICOM\_CHECK\_FLAG**](capicom-check-flag.md)
-   [**CAPICOM\_EKU**](capicom-eku.md)
-   [**CAPICOM\_ENCODING\_TYPE**](capicom-encoding-type.md)
-   [**CAPICOM\_ENCRYPTION\_ALGORITHM**](capicom-encryption-algorithm.md)
-   [**CAPICOM\_ENCRYPTION\_KEY\_LENGTH**](capicom-encryption-key-length.md)
-   [**CAPICOM\_ERROR\_CODE**](capicom-error-code.md)
-   [**CAPICOM\_EXPORT\_FLAG**](capicom-export-flag.md)
-   [**CAPICOM\_HASH\_ALGORITHM**](capicom-hash-algorithm.md)
-   [**CAPICOM\_KEY\_LOCATION**](capicom-key-location.md)
-   [**CAPICOM\_KEY\_SPEC**](capicom-key-spec.md)
-   [**CAPICOM\_KEY\_STORAGE\_FLAG**](capicom-key-storage-flag.md)
-   [**CAPICOM\_OID**](capicom-oid.md)
-   [**CAPICOM\_PROPID**](capicom-propid.md)
-   [**CAPICOM\_PROV\_TYPE**](capicom-prov-type.md)
-   [**CAPICOM\_SECRET\_TYPE**](capicom-secret-type.md)
-   [**CAPICOM\_SIGNED\_DATA\_VERIFY\_FLAG**](capicom-signed-data-verify-flag.md)
-   [**CAPICOM\_STORE\_LOCATION**](capicom-store-location.md)
-   [**CAPICOM\_STORE\_OPEN\_MODE**](capicom-store-open-mode.md)
-   [**CAPICOM\_STORE\_SAVE\_AS\_TYPE**](capicom-store-save-as-type.md)

 

 
