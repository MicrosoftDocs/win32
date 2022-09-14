---
description: The VerifyDiskSpace property is a read-only property.
ms.assetid: 62f11f71-00b0-4e04-8c45-d6d670238886
title: Session.VerifyDiskSpace property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.VerifyDiskSpace
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.VerifyDiskSpace property

The **VerifyDiskSpace** property is a read-only property. It returns true if enough disk space exists and false if the disk is full. Because this property uses information gathered by the costing actions, **VerifyDiskSpace** should only be called after the [CostInitialize action](costinitialize-action.md), [FileCost action](filecost-action.md), and [CostFinalize action](costfinalize-action.md).

This property is read-only.

## Syntax


```JScript
propVal = Session.VerifyDiskSpace
```



## Property value

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



 

 




