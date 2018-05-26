---
Description: Obtains a decoder object, if one exists.
ms.assetid: b8a1c7c9-e7ac-4b0e-a342-5b923ab83df3
title: EncodedData.Decoder method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EncodedData.Decoder method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**AsnEncodedData Class**](T:System.Security.Cryptography.AsnEncodedData) in the [**System.Security.Cryptography**](frlrfSystemSecurityCryptography) namespace.\]

The **Decoder** method obtains a decoder object, if one exists.

## Syntax


```VB
EncodedData.Decoder()
```



## Parameters

This method has no parameters.

## Remarks

If the encoded data does not have a decoder object, **NULL** is returned.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




