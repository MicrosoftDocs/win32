---
description: The Features property is a read-only property that returns a StringList object enumerating the set of published features for the specified product.
ms.assetid: feb8f09a-fa97-4fee-9082-8f04288af22f
title: Installer.Features property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.Features
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.Features property

The **Features** property is a read-only property that returns a [**StringList**](stringlist-object.md) object enumerating the set of published features for the specified product.

This property is read-only.

## Syntax


```JScript
propVal = Installer.Features
```



## Property value

Specifies the product code of the product.

## Remarks

To enumerate the features, an application iterates through the [**StringList**](stringlist-object.md) object using a For Each construct. Because features are not ordered, any new feature has an arbitrary index, meaning the function can return features in any order.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiEnumFeatures**](/windows/desktop/api/Msi/nf-msi-msienumfeaturesa)
</dt> <dt>

[System Status Functions](installer-function-reference.md)
</dt> </dl>

 

 




