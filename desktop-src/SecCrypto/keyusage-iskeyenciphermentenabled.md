---
Description: Retrieves a Boolean value that indicates whether the keyEncipherment bit is set.
ms.assetid: 2bdce181-3de7-4dc1-8059-1e1ca96c0d2d
title: KeyUsage.IsKeyEnciphermentEnabled property
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- KeyUsage.IsKeyEnciphermentEnabled
api_type:
- COM
api_location:
- Capicom.dll
---

# KeyUsage.IsKeyEnciphermentEnabled property

\[The **IsKeyEnciphermentEnabled** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509EnhancedKeyUsageExtension Class**](https://msdn.microsoft.com/library/6f6fz8xs(v=VS.100).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

The **IsKeyEnciphermentEnabled** property retrieves a Boolean value that indicates whether the keyEncipherment bit is set.

## Syntax


```VB
KeyUsage.IsKeyEnciphermentEnabled As Boolean
```



## Property value

If **true**, the keyEncipherment bit is set.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**KeyUsage**](keyusage.md)
</dt> </dl>

 

 




