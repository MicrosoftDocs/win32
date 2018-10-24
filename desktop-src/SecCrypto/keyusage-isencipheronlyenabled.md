---
Description: Retrieves a Boolean value that indicates whether the encipherOnly bit is set.
ms.assetid: 60d79ea4-4968-49e0-8d16-873fbcbd951c
title: KeyUsage.IsEncipherOnlyEnabled property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- KeyUsage.IsEncipherOnlyEnabled
api_type:
- COM
api_location:
- Capicom.dll
---

# KeyUsage.IsEncipherOnlyEnabled property

\[The **IsEncipherOnlyEnabled** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509EnhancedKeyUsageExtension Class**](https://msdn.microsoft.com/library/6f6fz8xs(v=VS.100).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

The **IsEncipherOnlyEnabled** property retrieves a Boolean value that indicates whether the encipherOnly bit is set.

## Syntax


```VB
KeyUsage.IsEncipherOnlyEnabled As Boolean
```



## Property value

If **true**, the encipherOnly bit is set.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**KeyUsage**](keyusage.md)
</dt> </dl>

 

 




