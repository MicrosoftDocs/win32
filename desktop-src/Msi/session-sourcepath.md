---
description: The SourcePath property of the Session object is a read-only property that provides the full path to the designated folder on the source media or server image.
ms.assetid: ed8eea4f-e15e-4d56-ac0c-e18f9cb46d07
title: Session.SourcePath property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.SourcePath
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.SourcePath property

The **SourcePath** property of the [**Session**](session-object.md) object is a read-only property that provides the full path to the designated folder on the source media or server image.

This property is read-only.

## Syntax


```JScript
propVal = Session.SourcePath
```



## Property value

Required case-sensitive name of a folder property as specified by a primary key of the [Directory table](directory-table.md). An error is generated if the folder does not exist.

## Remarks

If the property fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



 

 




