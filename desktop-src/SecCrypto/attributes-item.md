---
Description: Retrieves the Attribute object that represents the indexed attribute.
ms.assetid: 35c54c5f-f83f-40eb-b341-129c1aac6181
title: Attributes.Item property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Attributes.Item
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Attributes.Item property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**CryptographicAttributeObjectCollection Class**](https://www.bing.com/search?q=**CryptographicAttributeObjectCollection+Class**) in the [**System.Security.Cryptography**](https://www.bing.com/search?q=**System.Security.Cryptography**) namespace.\]

The **Item** property retrieves the [**Attribute**](attribute.md) object that represents the indexed attribute. This is the default property.

This property is read-only.

## Syntax


```VB
Attributes.Item( _
  ByVal Index _
) As Variant
```



## Property value

An [**Attribute**](attribute.md) object that represents the indexed attribute.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




