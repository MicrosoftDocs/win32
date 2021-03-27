---
description: The ShortcutTarget property of the Installer object examines a shortcut and returns its product, feature name, and component if available.
ms.assetid: fd7a1d34-3013-4419-af92-0a0162c93494
title: Installer.ShortcutTarget property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ShortcutTarget
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.ShortcutTarget property

The **ShortcutTarget** property of the [**Installer**](installer-object.md) object examines a shortcut and returns its product, feature name, and component if available.

This property is read-only.

## Syntax


```JScript
propVal = Installer.ShortcutTarget
```



## Property value

Full path and file name for the file.

## Remarks

ShortcutTarget returns a [**Record object**](record-object.md) that contains three fields:

-   Field 1 is a GUID for the product code of the shortcut, if available. This field can be null.
-   Field 2 is the Feature ID of the shortcut, if available. This field can be null.
-   Field 3 is a GUID for the component code, if available. This field can be null.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiGetFeatureState**](/windows/desktop/api/Msiquery/nf-msiquery-msigetfeaturestatea)
</dt> <dt>

[**MsiGetComponentState**](/windows/desktop/api/Msiquery/nf-msiquery-msigetcomponentstatea)
</dt> </dl>

 

 




