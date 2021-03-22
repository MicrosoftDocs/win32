---
description: The UILevel property of the Installer object is a read-write property that indicates the type of user interface to be used when opening and processing subsequent packages within the current process space.
ms.assetid: c89545b5-aeb7-4b05-94b0-d6e2a237152e
title: Installer.UILevel property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.UILevel
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.UILevel property

The **UILevel** property of the [**Installer**](installer-object.md) object is a read-write property that indicates the type of user interface to be used when opening and processing subsequent packages within the current process space.

This property is read/write.

## Syntax


```JScript
propVal = Installer.UILevel
Installer.UILevel = propVal 
```



## Property value

## Remarks



| User interface level   | Value | Description                                                                                                                                                                                        |
|------------------------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| msiUILevelNoChange     | 0     | Does not change UI level.                                                                                                                                                                          |
| msiUILevelDefault      | 1     | Uses default UI level.                                                                                                                                                                             |
| msiUILevelNone         | 2     | Silent installation.                                                                                                                                                                               |
| msiUILevelBasic        | 3     | Simple progress and error handling.                                                                                                                                                                |
| msiUILevelReduced      | 4     | Authored UI and wizard dialog boxes suppressed.                                                                                                                                                    |
| msiUILevelFull         | 5     | Authored UI with wizards, progress, and errors.                                                                                                                                                    |
| msiUILevelHideCancel   | 32    | If combined with the msiUILevelBasic value, the installer shows progress dialog boxes but does not display a **Cancel** button on the dialog box to prevent users from canceling the installation. |
| msiUILevelProgressOnly | 64    | If combined with the msiUILevelBasic value, the installer displays progress dialog boxes but does not display any modal dialog boxes or error dialog boxes.                                        |
| msiUILevelEndDialog    | 128   | If combined with any above value, the installer displays a modal dialog box at the end of a successful installation or if there has been an error. No dialog box is displayed if the user cancels. |



 

See also, [Determining UI Level from a Custom Action](determining-ui-level-from-a-custom-action.md).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



 

 




