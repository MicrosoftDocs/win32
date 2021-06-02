---
description: Determines whether the signatures on signed data in the SignedData object are valid.
ms.assetid: 920ac235-0c1a-4b15-9cdd-c7e0c3ea6107
title: SignedData.Verify method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- SignedData.Verify
api_type:
- COM
api_location:
- Capicom.dll
---

# SignedData.Verify method

\[The **Verify** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**SignedCms Class**](/dotnet/api/system.security.cryptography.pkcs.signedcms?view=dotnet-plat-ext-3.1&preserve-view=true) in the [**System.Security.Cryptography.Pkcs**](/dotnet/api/system.security.cryptography.pkcs?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

The **Verify** method determines whether the [*signatures*](../secgloss/d-gly.md) on signed data in the [**SignedData**](signeddata.md) object are valid. To verify a signature, the encrypted [*hash*](../secgloss/h-gly.md) of the contents is decrypted by using the signer's public key from the signer's certificate. The decrypted hash is compared to a new hash of the data content. A signature is valid if the hashes match. In addition, this method also builds a certificate chain to determine the validity of the certificate that provides the [*public key*](../secgloss/p-gly.md) used to decrypt the hash.

## Syntax


```VB
SignedData.Verify( _
  ByVal SignedMessage, _
  [ ByVal bDetached ], _
  [ ByVal VerifyFlag ] _
)
```



## Parameters

<dl> <dt>

*SignedMessage* \[in\]
</dt> <dd>

A string that contains the signed message to be verified.

</dd> <dt>

*bDetached* \[in, optional\]
</dt> <dd>

If **True**, the data to be signed is detached; that is, the content that is signed is not included as part of the signed object. To verify the signature on detached content, an application must have a copy of the original content. Detached content is often used to decrease the size of a signed object to be sent across the web, if the recipient of the signed message has an original copy of the signed data. The default value is **False**.

</dd> <dt>

*VerifyFlag* \[in, optional\]
</dt> <dd>

A value of the [CAPICOM\_SIGNED\_DATA\_VERIFY\_FLAG](capicom-signed-data-verify-flag.md) enumeration that indicates the verification policy. The default value is CAPICOM\_VERIFY\_SIGNATURE\_AND\_CERTIFICATE. Using this value, both the validity of the certificate and the validity of the signature are checked. This parameter may be set to verify the signature and not the certificate. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                             | Meaning                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| <span id="CAPICOM_VERIFY_SIGNATURE_ONLY"></span><span id="capicom_verify_signature_only"></span><dl> <dt>**CAPICOM\_VERIFY\_SIGNATURE\_ONLY**</dt> </dl>                                   | Only the signature is checked.<br/>                                                                   |
| <span id="CAPICOM_VERIFY_SIGNATURE_AND_CERTIFICATE"></span><span id="capicom_verify_signature_and_certificate"></span><dl> <dt>**CAPICOM\_VERIFY\_SIGNATURE\_AND\_CERTIFICATE**</dt> </dl> | Both the signature and the validity of the certificate used to create the signature are checked.<br/> |



 

</dd> </dl>

## Return value

This method returns a string that contains the encoded, signed data.

If this method fails, an error will be thrown. The **Err** object will contain additional information about the error.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> <dt>

[**SignedData**](signeddata.md)
</dt> </dl>

 

 
