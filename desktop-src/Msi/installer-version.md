---
Description: The Version property of the Installer object is a read-only property that is the string representation of the current version of Windows Installer. The string is returned in the following form.
ms.assetid: 6b39bb19-4360-4d0e-a797-980912a91275
title: Installer.Version property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Installer.Version property

The **Version** property of the [**Installer**](installer-object.md) object is a read-only property that is the string representation of the current version of Windows Installer. The string is returned in the following form.

*major*.*minor*.*build*.*update*

This property is read-only.

## Syntax


```JScript
propVal = Installer.Version
```



## Property value

## Requirements



|                    |                                                                                                                                                                                                                                                         |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



 

 




