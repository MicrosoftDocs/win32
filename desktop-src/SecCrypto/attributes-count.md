---
description: Retrieves the number of Attribute objects in the collection.
ms.assetid: d5f9db7d-52a2-4feb-8d35-902caf536510
title: Attributes.Count property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Attributes.Count
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Attributes.Count property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**CryptographicAttributeObjectCollection Class**](/dotnet/api/system.security.cryptography.cryptographicattributeobjectcollection?view=dotnet-plat-ext-3.1&preserve-view=true) in the [**System.Security.Cryptography**](/previous-versions/windows/) namespace.\]

The **Count** property retrieves the number of [**Attribute**](attribute.md) objects in the collection.

This property is read-only.

## Syntax


```VB
Attributes.Count As Long
```



## Property value

The number of [**Attribute**](attribute.md) objects in the collection. Each **Attribute** object represents a single attribute in the collection.

## Remarks

The **Count** property can be used to specify the last [**Attribute**](attribute.md) object in the collection when retrieving a specific **Attribute** object by using the [**Attributes.Item**](attributes-item.md) property.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Attributes**](attributes.md)
</dt> </dl>

 

 
