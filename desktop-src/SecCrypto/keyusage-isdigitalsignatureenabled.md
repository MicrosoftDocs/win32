---
Description: Retrieves a Boolean value that indicates whether the digitalSignature bit is set.
ms.assetid: 561eea86-ff23-4a26-adf2-b43009566eaa
title: KeyUsage.IsDigitalSignatureEnabled property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- KeyUsage.IsDigitalSignatureEnabled
api_type:
- COM
api_location:
- Capicom.dll
---

# KeyUsage.IsDigitalSignatureEnabled property

\[The **IsDigitalSignatureEnabled** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509EnhancedKeyUsageExtension Class**](https://msdn.microsoft.com/library/6f6fz8xs(v=VS.100).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

The **IsDigitalSignatureEnabled** property retrieves a Boolean value that indicates whether the digitalSignature bit is set.

## Syntax


```VB
KeyUsage.IsDigitalSignatureEnabled As Boolean
```



## Property value

If **true**, the digitalSignature bit is set.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**KeyUsage**](keyusage.md)
</dt> </dl>

 

 




