---
Description: The Item property retrieves an extension, by index, from the collection. This is the default property.
ms.assetid: 0242dc14-abf2-49df-b75a-9005b2376cfc
title: Extensions.Item property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Extensions.Item
api_type:
- COM
api_location:
- Capicom.dll
---

# Extensions.Item property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509ExtensionCollection Class**](https://msdn.microsoft.com/library/bs5ba18k(v=VS.90).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

The **Item** property retrieves an extension, by index, from the collection. This is the default property.

## Syntax


```VB
Extensions.Item( _
  ByVal Index _
) As Variant
```



## Property value

An [**Extension**](extension.md) object that represents the indexed certificate extension of the collection.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Extensions**](extensions.md)
</dt> </dl>

 

 




