---
Description: Retrieves the collection of user notice numbers.
ms.assetid: 5db38a53-e71b-4e80-9374-69b0c044fbc5
title: Qualifier.NoticeNumbers property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Qualifier.NoticeNumbers property

\[The **NoticeNumbers** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Extension Class**](T:System.Security.Cryptography.X509Certificates.X509Extension) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Policies to process qualifiers that are part of the policy information in the Certificate Policies extension.\]

The **NoticeNumbers** property retrieves the collection of user notice numbers. This property may be empty.

## Syntax


```VB
Qualifier.NoticeNumbers As NoticeNumbers
```



## Property value

The collection of user notice numbers.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Qualifier**](qualifier.md)
</dt> </dl>

 

 




