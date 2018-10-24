---
Description: Retrieves the number of EKU objects in the collection.
ms.assetid: a38ac480-4f9b-4d69-a7e6-fae4993fe2cf
title: EKUs.Count property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- EKUs.Count
api_type:
- COM
api_location:
- Capicom.dll
---

# EKUs.Count property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509ExtensionCollection Class**](https://msdn.microsoft.com/library/bs5ba18k(v=VS.90).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

The **Count** property retrieves the number of [**EKU**](eku.md) objects in the collection.

This property is read-only.

## Syntax


```VB
EKUs.Count As Long
```



## Property value

The number of [**EKU**](eku.md) objects in the collection. Each **EKU** object represents a single extended key usage (EKU) property of a certificate.

## Remarks

The **Count** property can be used to specify the last [**EKU**](eku.md) object in a collection when retrieving a specific **EKU** object using the [**EKUs.Item**](ekus-item.md) property.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




