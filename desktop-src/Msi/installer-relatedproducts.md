---
description: The read-only RelatedProducts property returns a StringList object enumerating the set of all products installed or advertised for the current user and machine with a specified UpgradeCode property in their Property table.
ms.assetid: 0316e536-ccd4-4d7a-9c49-66e6c4a07f1c
title: Installer.RelatedProducts property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.RelatedProducts
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.RelatedProducts property

The read-only **RelatedProducts** property returns a [**StringList**](stringlist-object.md) object enumerating the set of all products installed or advertised for the current user and machine with a specified [**UpgradeCode**](upgradecode.md) property in their [Property table](property-table.md).

This property is read-only.

## Syntax


```JScript
propVal = Installer.RelatedProducts
```



## Property value

The upgrade code of related products that the installer enumerates.

## Remarks

To enumerate the related products, an application iterates through the [**StringList**](stringlist-object.md) using a For Each construct. Because related products are not ordered, any new related product has an arbitrary index. This means that the function can return related products in any order.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiEnumRelatedProducts**](/windows/desktop/api/Msi/nf-msi-msienumrelatedproductsa)
</dt> </dl>

 

 




