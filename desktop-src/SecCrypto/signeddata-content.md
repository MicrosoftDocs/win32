---
Description: Sets or retrieves the data to be signed. This is the default property.
ms.assetid: 554ca500-403d-4c2a-868e-9e635d0b358e
title: SignedData.Content property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SignedData.Content property

\[The **Content** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**SignedCms Class**](T:System.Security.Cryptography.Pkcs.SignedCms) in the [**System.Security.Cryptography.Pkcs**](frlrfSystemSecurityCryptographyPkcs) namespace.\]

The **Content** property sets or retrieves the data to be signed. This is the default property.

## Syntax


```VB
SignedData.Content As String
```



## Property value

The data to be signed.

## Remarks

This property must be initialized before the [**Sign**](signeddata-sign.md) method is called. When the value of this property is reset, directly or indirectly, the whole [*state*](security.s_gly#-security-state-gly) of the object is reset, and any signature that was associated with the object before the property was changed is lost.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**SignedData**](signeddata.md)
</dt> </dl>

 

 




