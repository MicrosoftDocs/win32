---
Description: Retrieves a Boolean value that indicates whether the KeyUsage extension is marked critical.
ms.assetid: 'f7d53570-2b89-40a9-ab56-fcae4e4cb70c'
title: KeyUsage.IsCritical property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- KeyUsage.IsCritical
api_type:
- COM
api_location:
- Capicom.dll
---

# KeyUsage.IsCritical property

\[The **IsCritical** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509EnhancedKeyUsageExtension Class**](https://msdn.microsoft.com/library/6f6fz8xs(v=VS.100).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

The **IsCritical** property retrieves a Boolean value that indicates whether the KeyUsage extension is marked critical.

## Syntax


```VB
KeyUsage.IsCritical As Boolean
```



## Property value

If **true**, the KeyUsage extension is marked critical.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**KeyUsage**](keyusage.md)
</dt> </dl>

 

 




