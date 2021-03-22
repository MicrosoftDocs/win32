---
description: The ComponentRequestState property of the Session object obtains or requests a change in the Action state of a row in the Component table.
ms.assetid: d0b50c25-dca6-4bdf-8ee9-490e436fcc5b
title: Session.ComponentRequestState property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.ComponentRequestState
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.ComponentRequestState property

The **ComponentRequestState** property of the [**Session**](session-object.md) object obtains or requests a change in the Action state of a row in the [Component table](component-table.md).

This property is read-only.

## Syntax


```JScript
propVal = Session.ComponentRequestState
```



## Property value

Required string name of the component item, primary key of the Component table.

## Remarks



| Selection state        | Value | Description                                                    |
|------------------------|-------|----------------------------------------------------------------|
| Null                   | Null  | Requests that no action be taken for this item.                |
| msiInstallStateAbsent  | 2     | Item is to be removed.                                         |
| msiInstallStateLocal   | 3     | Item is to be installed locally.                               |
| msiInstallStateSource  | 4     | Item is to be installed and run from the source media.         |
| msiInstallStateDefault | 5     | If installed, the item is to be reinstalled in the same state. |



 

If the property fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



 

 




