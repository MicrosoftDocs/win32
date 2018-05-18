---
Description: 'Loads a signing certificate from a specified .pfx file.'
ms.assetid: '98963354-c237-40d0-9235-8318728e2c8e'
title: 'Signer.Load method'
---

# Signer.Load method

\[The **Load** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**CmsSigner Class**](T:System.Security.Cryptography.Pkcs.CmsSigner) in the [**System.Security.Cryptography.Pkcs**](frlrfSystemSecurityCryptographyPkcs) namespace.\]

The **Load** method loads a signing certificate from a specified .pfx file.

## Syntax


```VB
Signer.Load( _
  ByVal FileName, _
  [ ByVal Password ] _
)
```



## Parameters

<dl> <dt>

*FileName* 
</dt> <dd>

Name of the .pfx file that contains the signing certificate.

</dd> <dt>

*Password* \[optional\]
</dt> <dd>

String containing the plaintext password used to open the file. Up to 32 Unicode characters, including a terminating null character, can be used for the password. The default value is an empty string (""). For information about protecting the password, see [Handling Passwords](security.handling_passwords).

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method loads the first certificate in the .pfx file that has a private key associated with it.

This method raises CAPICOM\_E\_NOT\_ALLOWED when it is scripted from a web-based application.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Signer**](signer.md)
</dt> </dl>

 

 




