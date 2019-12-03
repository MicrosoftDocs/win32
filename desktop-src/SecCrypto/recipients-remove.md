---
Description: Removes a Certificate object from a Recipients collection.
ms.assetid: bb75f6d0-4bab-40dd-9d0c-f0431da9c5f3
title: Recipients.Remove method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Recipients.Remove
api_type:
- COM
api_location:
- Capicom.dll
---

# Recipients.Remove method

\[The **Remove** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**CmsRecipientCollection Class**](https://msdn.microsoft.com/library/0y59h9e9(v=VS.90).aspx) in the [**System.Security.Cryptography.Pkcs**](https://msdn.microsoft.com/library/6see7k14(v=VS.100).aspx) namespace.\]

The **Remove** method removes a [**Certificate**](certificate.md) object from a [**Recipients**](recipients.md) collection.

## Syntax


```VB
Recipients.Remove( _
  ByVal Index _
)
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Index of the [**Certificate**](certificate.md) object to be removed from the collection.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> <dt>

[**Recipients**](recipients.md)
</dt> </dl>

 

 




