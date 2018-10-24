---
Description: Loads a signing certificate from a specified .pfx file.
ms.assetid: 98963354-c237-40d0-9235-8318728e2c8e
title: Signer.Load method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Signer.Load
api_type:
- COM
api_location:
- Capicom.dll
---

# Signer.Load method

\[The **Load** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**CmsSigner Class**](https://msdn.microsoft.com/library/5x3db70t(v=VS.90).aspx) in the [**System.Security.Cryptography.Pkcs**](https://msdn.microsoft.com/library/6see7k14(v=VS.100).aspx) namespace.\]

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

String containing the plaintext password used to open the file. Up to 32 Unicode characters, including a terminating null character, can be used for the password. The default value is an empty string (""). For information about protecting the password, see [Handling Passwords](https://msdn.microsoft.com/en-us/library/ms717799(v=VS.85).aspx).

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

 

 




