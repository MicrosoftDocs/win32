---
Description: 'Adds an Attribute object to the collection.'
ms.assetid: 'dc2fe542-7168-4ffa-a10d-b2c051c4d42c'
title: 'Attributes.Add method'
---

# Attributes.Add method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**CryptographicAttributeObjectCollection Class**](T:System.Security.Cryptography.CryptographicAttributeObjectCollection) in the [**System.Security.Cryptography**](frlrfSystemSecurityCryptography) namespace.\]

The **Add** method adds an [**Attribute**](attribute.md) object to the collection.

## Syntax


```VB
Attributes.Add( _
  ByVal Attribute _
)
```



## Parameters

<dl> <dt>

*Attribute* \[in\]
</dt> <dd>

The [**Attribute**](attribute.md) object to be added at the end of the collection.

</dd> </dl>

## Return value

This method does not return a value. An application that uses this method must contain code to handle an exception raised by this method.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[Cryptography Objects](cryptography-objects.md)
</dt> <dt>

[**Attributes**](attributes.md)
</dt> </dl>

 

 




