---
Description: 'Implements the IX509PrivateKey and IX509PublicKey interfaces.'
ms.assetid: '1358053e-ed4e-4482-b160-5b9b1024c771'
title: Private and Public Key Functions
---

# Private and Public Key Functions

CertEnroll.dll implements the [**IX509PrivateKey**](ix509privatekey.md) and [**IX509PublicKey**](ix509publickey.md) interfaces. You can, for example, use the [**IX509PrivateKey**](ix509privatekey.md) interface to perform the following actions on a [*private key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-private-key-gly):

-   Create, open, close, import, export, and delete the key.
-   Specify or retrieve the [*public key algorithm*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-public-key-algorithm-gly).
-   Specify or retrieve information about the available [*cryptographic service provider*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-cryptographic-service-provider-gly) (CSP) that support the public key algorithm.
-   Specify or retrieve the [*certificate*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certificate-gly) associated with the [*private key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-private-key-gly).
-   Specify or retrieve the name of the [*key container*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-container-gly).
-   Specify or retrieve a description of and a display name for the key.
-   Specify or retrieve the export constraints places on a private key.
-   Specify or retrieve a Boolean value that indicates whether the key exists.
-   Specify or retrieve a value that indicates how the key is protected before use.
-   Specify or retrieve a value that indicates whether the key can be used for signing, encryption, or both.
-   Specify or retrieve a value that identifies the specific purpose for which the key can be used.
-   Specify or retrieve the length of the key.
-   Specify or retrieve a value that indicates whether the key is used or saved in the context of a computer or user.
-   Retrieve a Boolean value that specifies whether the key has been opened.
-   Specify a personal identification number to access a private key on a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).
-   Specify or retrieve the name of the CSP associated with the key.
-   Specify or retrieve the [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) for the key.

Each of the following sections identifies a function exported by Xenroll.dll that can be used to manage a [*cryptographic key*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-cryptographic-key-gly). Each topic also discusses how to use CertEnroll.dll to replace the function or indicates that no mapping between the two libraries exists:

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

The [**ContainerNameWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385533) function in Xenroll.dll specifies or retrieves the name of the [*key container*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-container-gly).

When using CertEnroll.dll, you can perform the following actions to retrieve the name of a key container:

1.  Call the [**Request**](ix509enrollment-request-property.md) property on an existing [**IX509Enrollment**](ix509enrollment.md) object.
2.  Call the [**GetInnerRequest**](ix509certificaterequest-getinnerrequest-method.md) method on the request returned from step 1 to retrieve the innermost request.
3.  Call **QueryInterface** on the [**IX509CertificateRequest**](ix509certificaterequest.md) object returned from step 2 to cast to an [**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md) object.
4.  Call the [**PrivateKey**](https://msdn.microsoft.com/library/windows/desktop/aa387352) property on the PKCS \#10 request.
5.  Call the [**ContainerName**](ix509privatekey-containername-property.md) property on the [**IX509PrivateKey**](ix509privatekey.md) object retrieved from step 4.

## GenKeyFlags

The [**GenKeyFlags**](https://msdn.microsoft.com/library/windows/desktop/aa385573) function defined in Xenroll.dll specifies or retrieves flags used to generate a private key or [*public/private key pair*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-public-private-key-pair-gly).

When using CertEnroll.dll, you can specify a number of different properties that will determine how a private key is created. For more information, see [**Create**](ix509privatekey-create-method.md).

## GetKeyLen

The [**GetKeyLen**](https://msdn.microsoft.com/library/windows/desktop/aa385593) function defined in Xenroll.dll retrieves the maximum or minimum key size of an encryption key.

When using CertEnroll.dll, you can call the [**Length**](ix509privatekey-length-property.md) property on an [**IX509PrivateKey**](ix509privatekey.md) or [**IX509PublicKey**](ix509publickey.md) object to retrieve the key size, in bits.

## GetKeyLenEx

The [**GetKeyLenEx**](https://msdn.microsoft.com/library/windows/desktop/aa385595) function defined in Xenroll.dll retrieves the maximum or minimum key size or the increment length of an encryption key.

When using CertEnroll.dll, you can call the [**Length**](ix509privatekey-length-property.md) property on an [**IX509PrivateKey**](ix509privatekey.md) or [**IX509PublicKey**](ix509publickey.md) object to retrieve the key size, in bits. If an algorithm supports incremental key lengths, you can call the [**IncrementLength**](icspalgorithm-incrementlength-property.md) property on the [**ICspAlgorithm**](icspalgorithm.md) object to retrieve the increment value. You can also call the [**MinLength**](icspalgorithm-minlength-property.md) and [**MaxLength**](icspalgorithm-maxlength-property.md) properties to retrieve the minimum and maximum key sizes.

## GetSupportedKeySpec

The [**GetSupportedKeySpec**](https://msdn.microsoft.com/library/windows/desktop/aa385615) function defined in Xenroll.dll retrieves a value that indicates whether a CSP supports exchange keys, signing keys, or both.

When using CertEnroll.dll, you can call the [**KeySpec**](ix509privatekey-keyspec-property.md) property on the [**IX509PrivateKey**](ix509privatekey.md) or [**ICspInformation**](icspinformation.md) objects to retrieve the operations supported by the key.

## KeySpec

The [**KeySpec**](https://msdn.microsoft.com/library/windows/desktop/aa385639) function defined in Xenroll.dll specifies or retrieves the key type.

When using CertEnroll.dll, you can call the [**KeySpec**](ix509privatekey-keyspec-property.md) property on an [**IX509PrivateKey**](ix509privatekey.md) object to retrieve the operations supported by the key.

## LimitExchangeKeyToEncipherment

The [**LimitExchangeKeyToEncipherment**](https://msdn.microsoft.com/library/windows/desktop/aa385642) function defined in Xenroll.dll specifies or retrieves a Boolean value that indicates whether an encryption key can be used only for data or key encipherment.

CertEnroll.dll does not contain a direct equivalent for this function. You can, however, achieve a nearly equivalent result by specifying an [**IX509ExtensionKeyUsage**](ix509extensionkeyusage.md) object and adding it to the certificate request.

## PVKFileNameWStr

The [**PVKFileNameWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385664) function defined in Xenroll.dll specifies or retrieves the name of a file that contains exported keys.

When using CertEnroll.dll, you can call the [**Export**](ix509privatekey-export-method.md) method on an [**IX509PrivateKey**](ix509privatekey.md) object to export a key to a **BSTR**. You can call the [**ExportPublicKey**](ix509privatekey-exportpublickey-method.md) method to export the [*public key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-public-key-gly) portion of an asymmetric key pair.

## ReuseHardwareKeyIfUnableToGenNew

The [**ReuseHardwareKeyIfUnableToGenNew**](https://msdn.microsoft.com/library/windows/desktop/aa385698) function defined in Xenroll.dll specifies or retrieves a Boolean value that indicates whether an existing key is reused when an error is encountered when generating a new key.

When using CertEnroll.dll, you can call the [**InitializeFromCertificate**](ix509certificaterequestpkcs10-initializefromcertificate-method.md) method on an [**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md) object and specify a value of the [**X509RequestInheritOptions**](x509requestinheritoptions-enum.md) enumeration type to reuse an existing private key.

## UseExistingKeySet

The [**UseExistingKeySet**](https://msdn.microsoft.com/library/windows/desktop/aa386150) function defined in Xenroll.dll specifies or retrieves a Boolean value that indicates whether to use existing keys.

When using CertEnroll.dll, you can call the [**InitializeFromCertificate**](ix509certificaterequestpkcs10-initializefromcertificate-method.md) method on an [**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md) object and specify a value of the [**X509RequestInheritOptions**](x509requestinheritoptions-enum.md) enumeration type to reuse existing private and public keys.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> </dl>

 

 



