---
Description: Retrieves a Boolean value that indicates whether the nonRepudiationEnabled bit is set.
ms.assetid: d9bcf0fc-8b2d-408c-b587-71903ef5f5f6
title: KeyUsage.IsNonRepudiationEnabled property
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- KeyUsage.IsNonRepudiationEnabled
api_type:
- COM
api_location:
- Capicom.dll
---

# KeyUsage.IsNonRepudiationEnabled property

\[The **IsNonRepudiationEnabled** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509EnhancedKeyUsageExtension Class**](https://msdn.microsoft.com/library/6f6fz8xs(v=VS.100).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

The **IsNonRepudiationEnabled** property retrieves a Boolean value that indicates whether the nonRepudiationEnabled bit is set.

## Syntax


```VB
KeyUsage.IsNonRepudiationEnabled As Boolean
```



## Property value

If **true**, the nonRepudiationEnabled bit is set.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**KeyUsage**](keyusage.md)
</dt> </dl>

 

 




