---
Description: Adds a Certificate object to a Recipients collection.
ms.assetid: 2a1b9e0f-ccbf-4042-871b-397de6b6fc35
title: Recipients.Add method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Recipients.Add
api_type:
- COM
api_location:
- Capicom.dll
---

# Recipients.Add method

\[The **Add** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**CmsRecipientCollection Class**](https://msdn.microsoft.com/library/0y59h9e9(v=VS.90).aspx) in the [**System.Security.Cryptography.Pkcs**](https://msdn.microsoft.com/library/6see7k14(v=VS.100).aspx) namespace.\]

The **Add** method adds a [**Certificate**](certificate.md) object to a [**Recipients**](recipients.md) collection.

## Syntax


```VB
Recipients.Add( _
  ByVal Certificate _
)
```



## Parameters

<dl> <dt>

*Certificate* \[in\]
</dt> <dd>

Expression that resolves to the [**Certificate**](certificate.md) object to be added to the collection.

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

 

 




