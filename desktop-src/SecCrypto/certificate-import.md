---
Description: Imports a previously encoded certificate from a string into the Certificate object.
ms.assetid: 8515e034-08aa-4575-9b96-34cdee3ccba8
title: ICertificate2::Import method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificate.Import
- ICertificate2.Import
- ICertificate.Import
api_type:
- COM
api_location:
- Capicom.dll
---

# ICertificate2::Import method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2 Class**](https://msdn.microsoft.com/library/Hh424017(v=MSDN.10).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

The **Import** method imports a previously encoded certificate from a string into the [**Certificate**](certificate.md) object. Calling this method resets the [*state*](https://msdn.microsoft.com/library/ms721625(v=VS.85).aspx) of this object.

## Syntax


```VB
Certificate.Import( _
  ByVal EncodedCertificate _
)
```



## Parameters

<dl> <dt>

*EncodedCertificate* \[in\]
</dt> <dd>

A string that contains the encoded certificate data to be imported.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[Cryptography Objects](cryptography-objects.md)
</dt> <dt>

[**Certificate**](certificate.md)
</dt> </dl>

 

 




