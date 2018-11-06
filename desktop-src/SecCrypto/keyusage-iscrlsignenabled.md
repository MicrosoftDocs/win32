---
Description: Retrieves a Boolean value that indicates whether the CRLSign bit is set.
ms.assetid: 76ca86e3-55f7-4720-9fa5-d465db2a7b5a
title: KeyUsage.IsCRLSignEnabled property
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- KeyUsage.IsCRLSignEnabled
api_type:
- COM
api_location:
- Capicom.dll
---

# KeyUsage.IsCRLSignEnabled property

\[The **IsCRLSignEnabled** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509EnhancedKeyUsageExtension Class**](https://msdn.microsoft.com/library/6f6fz8xs(v=VS.100).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

The **IsCRLSignEnabled** property retrieves a Boolean value that indicates whether the CRLSign bit is set.

## Syntax


```VB
KeyUsage.IsCRLSignEnabled As Boolean
```



## Property value

If **true**, the CRLSign bit is set.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**KeyUsage**](keyusage.md)
</dt> </dl>

 

 




