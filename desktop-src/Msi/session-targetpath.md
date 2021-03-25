---
description: The TargetPath property of the Session object is a read-write property that provides the full path to the designated folder on the installation target drive.
ms.assetid: 563b874e-c669-4f5b-b3fa-eeb6b6e578f2
title: Session.TargetPath property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.TargetPath
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.TargetPath property

The **TargetPath** property of the [**Session**](session-object.md) object is a read-write property that provides the full path to the designated folder on the installation target drive.

This property is read/write.

## Syntax


```JScript
propVal = Session.TargetPath
Session.TargetPath = propVal 
```



## Property value

Required case-sensitive name of a folder property as specified by a primary key of the [Directory table](directory-table.md). An error is generated if the folder does not exist.

## Remarks

Do not attempt to configure the target path if the components using those paths are already installed for the current user or for a different user. Check the [**ProductState**](productstate.md) property to determine if the product that contains the component is installed.

If the property fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



 

 




