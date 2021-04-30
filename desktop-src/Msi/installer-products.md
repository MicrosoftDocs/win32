---
description: The Products property is a read-only property that returns a StringList object enumerating the set of all products installed or advertised for the current user and machine.
ms.assetid: 5c210827-a7cc-4358-bfe6-4d8e9767bd8c
title: Installer.Products property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.Products
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.Products property

The **Products** property is a read-only property that returns a [**StringList**](stringlist-object.md) object enumerating the set of all products installed or advertised for the current user and machine.

This property is read-only.

## Syntax


```JScript
propVal = Installer.Products
```



## Property value

## Remarks

To enumerate the products, an application iterates through the [**StringList**](stringlist-object.md) object using a For Each construct. Because products are not ordered, any new product has an arbitrary index. This means that the function can return products in any order.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiEnumProducts**](/windows/desktop/api/Msi/nf-msi-msienumproductsa)
</dt> </dl>

 

 




