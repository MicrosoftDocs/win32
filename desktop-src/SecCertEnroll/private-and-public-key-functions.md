---
description: Implements the IX509PrivateKey and IX509PublicKey interfaces.
ms.assetid: 1358053e-ed4e-4482-b160-5b9b1024c771
title: Private and Public Key Functions
ms.topic: article
ms.date: 05/31/2018
---

# Private and Public Key Functions

CertEnroll.dll implements the [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) and [**IX509PublicKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509publickey) interfaces. You can, for example, use the [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) interface to perform the following actions on a [*private key*](/windows/desktop/SecGloss/p-gly):

-   Create, open, close, import, export, and delete the key.
-   Specify or retrieve the [*public key algorithm*](/windows/desktop/SecGloss/p-gly).
-   Specify or retrieve information about the available [*cryptographic service provider*](/windows/desktop/SecGloss/c-gly) (CSP) that support the public key algorithm.
-   Specify or retrieve the [*certificate*](/windows/desktop/SecGloss/c-gly) associated with the [*private key*](/windows/desktop/SecGloss/p-gly).
-   Specify or retrieve the name of the [*key container*](/windows/desktop/SecGloss/k-gly).
-   Specify or retrieve a description of and a display name for the key.
-   Specify or retrieve the export constraints places on a private key.
-   Specify or retrieve a Boolean value that indicates whether the key exists.
-   Specify or retrieve a value that indicates how the key is protected before use.
-   Specify or retrieve a value that indicates whether the key can be used for signing, encryption, or both.
-   Specify or retrieve a value that identifies the specific purpose for which the key can be used.
-   Specify or retrieve the length of the key.
-   Specify or retrieve a value that indicates whether the key is used or saved in the context of a computer or user.
-   Retrieve a Boolean value that specifies whether the key has been opened.
-   Specify a personal identification number to access a private key on a [*smart card*](/windows/desktop/SecGloss/s-gly).
-   Specify or retrieve the name of the CSP associated with the key.
-   Specify or retrieve the [*security descriptor*](/windows/desktop/SecGloss/s-gly) for the key.

Each of the following sections identifies a function exported by Xenroll.dll that can be used to manage a [*cryptographic key*](/windows/desktop/SecGloss/c-gly). Each topic also discusses how to use CertEnroll.dll to replace the function or indicates that no mapping between the two libraries exists:

-   [ContainerNameWStr](#containernamewstr)
-   [GenKeyFlags](#genkeyflags)
-   [GetKeyLen](#getkeylenex)
-   [GetKeyLenEx](#getkeylenex)
-   [GetSupportedKeySpec](#getsupportedkeyspec)
-   [KeySpec](#getsupportedkeyspec)
-   [LimitExchangeKeyToEncipherment](#limitexchangekeytoencipherment)
-   [PVKFileNameWStr](#pvkfilenamewstr)
-   [ReuseHardwareKeyIfUnableToGenNew](#reusehardwarekeyifunabletogennew)
-   [UseExistingKeySet](#useexistingkeyset)
-   [Related topics](#related-topics)

## ContainerNameWStr

The [**ContainerNameWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_containernamewstr) function in Xenroll.dll specifies or retrieves the name of the [*key container*](/windows/desktop/SecGloss/k-gly).

When using CertEnroll.dll, you can perform the following actions to retrieve the name of a key container:

1.  Call the [**Request**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509enrollment-get_request) property on an existing [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object.
2.  Call the [**GetInnerRequest**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequest-getinnerrequest) method on the request returned from step 1 to retrieve the innermost request.
3.  Call **QueryInterface** on the [**IX509CertificateRequest**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequest) object returned from step 2 to cast to an [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object.
4.  Call the [**PrivateKey**](/windows/desktop/SecCrypto/privatekey) property on the PKCS \#10 request.
5.  Call the [**ContainerName**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_containername) property on the [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) object retrieved from step 4.

## GenKeyFlags

The [**GenKeyFlags**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_genkeyflags) function defined in Xenroll.dll specifies or retrieves flags used to generate a private key or [*public/private key pair*](/windows/desktop/SecGloss/p-gly).

When using CertEnroll.dll, you can specify a number of different properties that will determine how a private key is created. For more information, see [**Create**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-create).

## GetKeyLen

The [**GetKeyLen**](/windows/desktop/api/xenroll/nf-xenroll-ienroll2-getkeylen) function defined in Xenroll.dll retrieves the maximum or minimum key size of an encryption key.

When using CertEnroll.dll, you can call the [**Length**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_length) property on an [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) or [**IX509PublicKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509publickey) object to retrieve the key size, in bits.

## GetKeyLenEx

The [**GetKeyLenEx**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-getkeylenex) function defined in Xenroll.dll retrieves the maximum or minimum key size or the increment length of an encryption key.

When using CertEnroll.dll, you can call the [**Length**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_length) property on an [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) or [**IX509PublicKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509publickey) object to retrieve the key size, in bits. If an algorithm supports incremental key lengths, you can call the [**IncrementLength**](/windows/desktop/api/CertEnroll/nf-certenroll-icspalgorithm-get_incrementlength) property on the [**ICspAlgorithm**](/windows/desktop/api/CertEnroll/nn-certenroll-icspalgorithm) object to retrieve the increment value. You can also call the [**MinLength**](/windows/desktop/api/CertEnroll/nf-certenroll-icspalgorithm-get_minlength) and [**MaxLength**](/windows/desktop/api/CertEnroll/nf-certenroll-icspalgorithm-get_maxlength) properties to retrieve the minimum and maximum key sizes.

## GetSupportedKeySpec

The [**GetSupportedKeySpec**](/windows/desktop/api/xenroll/nf-xenroll-ienroll2-getsupportedkeyspec) function defined in Xenroll.dll retrieves a value that indicates whether a CSP supports exchange keys, signing keys, or both.

When using CertEnroll.dll, you can call the [**KeySpec**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_keyspec) property on the [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) or [**ICspInformation**](/windows/desktop/api/CertEnroll/nn-certenroll-icspinformation) objects to retrieve the operations supported by the key.

## KeySpec

The [**KeySpec**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_keyspec) function defined in Xenroll.dll specifies or retrieves the key type.

When using CertEnroll.dll, you can call the [**KeySpec**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_keyspec) property on an [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) object to retrieve the operations supported by the key.

## LimitExchangeKeyToEncipherment

The [**LimitExchangeKeyToEncipherment**](/windows/desktop/api/xenroll/nf-xenroll-ienroll2-get_limitexchangekeytoencipherment) function defined in Xenroll.dll specifies or retrieves a Boolean value that indicates whether an encryption key can be used only for data or key encipherment.

CertEnroll.dll does not contain a direct equivalent for this function. You can, however, achieve a nearly equivalent result by specifying an [**IX509ExtensionKeyUsage**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionkeyusage) object and adding it to the certificate request.

## PVKFileNameWStr

The [**PVKFileNameWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_pvkfilenamewstr) function defined in Xenroll.dll specifies or retrieves the name of a file that contains exported keys.

When using CertEnroll.dll, you can call the [**Export**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-export) method on an [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) object to export a key to a **BSTR**. You can call the [**ExportPublicKey**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-exportpublickey) method to export the [*public key*](/windows/desktop/SecGloss/p-gly) portion of an asymmetric key pair.

## ReuseHardwareKeyIfUnableToGenNew

The [**ReuseHardwareKeyIfUnableToGenNew**](/windows/desktop/api/xenroll/nf-xenroll-ienroll2-get_reusehardwarekeyifunabletogennew) function defined in Xenroll.dll specifies or retrieves a Boolean value that indicates whether an existing key is reused when an error is encountered when generating a new key.

When using CertEnroll.dll, you can call the [**InitializeFromCertificate**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-initializefromcertificate) method on an [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object and specify a value of the [**X509RequestInheritOptions**](/windows/desktop/api/CertEnroll/ne-certenroll-x509requestinheritoptions) enumeration type to reuse an existing private key.

## UseExistingKeySet

The [**UseExistingKeySet**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_useexistingkeyset) function defined in Xenroll.dll specifies or retrieves a Boolean value that indicates whether to use existing keys.

When using CertEnroll.dll, you can call the [**InitializeFromCertificate**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-initializefromcertificate) method on an [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object and specify a value of the [**X509RequestInheritOptions**](/windows/desktop/api/CertEnroll/ne-certenroll-x509requestinheritoptions) enumeration type to reuse existing private and public keys.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> </dl>

 

 
