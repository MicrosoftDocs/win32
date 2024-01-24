---
description: The ComponentCurrentState property of the Session object is a read-only property that returns the current installed state of the designated component. For state values, see the ComponentRequestState property.
ms.assetid: c8343e90-8867-462d-9844-e547341a590c
title: Session.ComponentCurrentState property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.ComponentCurrentState
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.ComponentCurrentState property

The **ComponentCurrentState** property of the [**Session**](session-object.md) object is a read-only property that returns the current installed state of the designated component. For state values, see the [**ComponentRequestState**](session-componentrequeststate.md) property.

This property is read-only.

## Syntax


```JScript
propVal = Session.ComponentCurrentState
```



## Property value

Required string name of the requested component, primary key into the Component table.

## Remarks

If the property fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



## See also

<dl> <dt>

[**Session**](session-object.md)
</dt> <dt>

[**ComponentRequestState property**](session-componentrequeststate.md)
</dt> </dl>

 

 




