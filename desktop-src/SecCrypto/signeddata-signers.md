---
Description: Retrieves the signature creators of the data.
ms.assetid: 3e28f08a-c4d8-4dd7-953a-e1500eb5bee0
title: SignedData.Signers property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- SignedData.Signers
api_type:
- COM
api_location:
- Capicom.dll
---

# SignedData.Signers property

\[The **Signers** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**SignedCms Class**](https://msdn.microsoft.com/library/kz82bs5e(v=VS.90).aspx) in the [**System.Security.Cryptography.Pkcs**](https://msdn.microsoft.com/library/6see7k14(v=VS.100).aspx) namespace.\]

The **Signers** property retrieves the signature creators of the data.

## Syntax


```VB
SignedData.Signers As Signers
```



## Property value

The [**Signers**](signers.md) collection that represents the signature creators of the data.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**SignedData**](signeddata.md)
</dt> </dl>

 

 




