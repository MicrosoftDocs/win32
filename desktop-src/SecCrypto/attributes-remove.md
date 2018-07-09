---
Description: Removes an indexed Attribute object from the collection.
ms.assetid: 6d9423e3-ab24-4973-b0aa-32e38abd607a
title: Attributes.Remove method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Attributes.Remove
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Attributes.Remove method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**CryptographicAttributeObjectCollection Class**](https://www.bing.com/search?q=**CryptographicAttributeObjectCollection+Class**) in the [**System.Security.Cryptography**](https://www.bing.com/search?q=**System.Security.Cryptography**) namespace.\]

The **Remove** method removes an indexed [**Attribute**](attribute.md) object from the collection.

## Syntax


```VB
Attributes.Remove( _
  ByVal Index _
)
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Index of the [**Attribute**](attribute.md) object to be removed.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Applications that use this method must contain code to handle an exception raised by this method.

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

 

 




