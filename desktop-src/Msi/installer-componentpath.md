---
description: The ComponentPath property is a read-only property that returns the full path to an installed component. If the key path for the component is a registry key then the registry key is returned.
ms.assetid: 6e53419d-f28a-45cd-abc8-0f451177f3fc
title: Installer.ComponentPath property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ComponentPath
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.ComponentPath property

The **ComponentPath** property is a read-only property that returns the full path to an installed component. If the key path for the component is a registry key then the registry key is returned.

This property is read-only.

## Syntax


```JScript
propVal = Installer.ComponentPath
```



## Property value

## Remarks

If the component is a registry key, the registry roots are represented numerically. For example, a registry path of "HKEY\_CURRENT\_USER\\SOFTWARE\\Microsoft" would be returned as "01:\\SOFTWARE\\Microsoft". The registry roots returned are defined as follows:



| Root                    | Returned value |
|-------------------------|----------------|
| HKEY\_CLASSES\_ROOT     | 00             |
| HKEY\_CURRENT\_USER     | 01             |
| HKEY\_LOCAL\_MACHINE    | 02             |
| HKEY\_USERS             | 03             |
| HKEY\_PERFORMANCE\_DATA | 04             |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiGetComponentPath**](/windows/desktop/api/Msi/nf-msi-msigetcomponentpatha)
</dt> </dl>

 

 




