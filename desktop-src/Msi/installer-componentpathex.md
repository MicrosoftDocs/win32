---
description: Returns a RecordList object that gives the full path of a specified installed component.
ms.assetid: 0f4f9d21-f1cc-44fd-a22f-1b6f055fef9e
title: Installer.ComponentPathEx property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ComponentPathEx
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.ComponentPathEx property

This property returns a [**RecordList**](recordlist-object.md) object that gives the full path of a specified installed component. This property calls [**MsiGetComponentPathEx**](/windows/desktop/api/Msi/nf-msi-msigetcomponentpathexa).

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This property is available beginning with Windows Installer 5.0.

This property is read-only.

## Syntax


```JScript
propVal = Installer.ComponentPathEx
```



## Property value

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                           |



## See also

<dl> <dt>

[**MsiGetComponentPathEx**](/windows/desktop/api/Msi/nf-msi-msigetcomponentpathexa)
</dt> </dl>

 

 




