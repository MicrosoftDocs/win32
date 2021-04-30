---
description: The read-only Patches property of the Installer object returns a StringList object that contains all the patches applied to the product.
ms.assetid: a8d46073-399b-480e-b4b0-a7a2f832e160
title: Installer.Patches property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.Patches
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.Patches property

The read-only **Patches** property of the [**Installer**](installer-object.md) object returns a [**StringList**](stringlist-object.md) object that contains all the patches applied to the product.

This property is read-only.

## Syntax


```JScript
propVal = Installer.Patches
```



## Property value

Specifies the product code.

## Remarks

To enumerate the patches, an application iterates through the [**StringList**](stringlist-object.md) object using a For Each construct. Because patches are not ordered, any new patch has an arbitrary index. This means that the function can return patches in any order.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiEnumPatches**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddmediadiska)
</dt> </dl>

 

 




