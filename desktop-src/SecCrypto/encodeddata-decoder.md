---
description: Obtains a decoder object, if one exists.
ms.assetid: b8a1c7c9-e7ac-4b0e-a342-5b923ab83df3
title: EncodedData.Decoder method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- EncodedData.Decoder
api_type:
- COM
api_location:
- Capicom.dll
---

# EncodedData.Decoder method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**AsnEncodedData Class**](/dotnet/api/system.security.cryptography.asnencodeddata?view=netcore-3.1) in the [**System.Security.Cryptography**](/dotnet/api/system.security.cryptography?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

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



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
