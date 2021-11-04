---
description: The CreateRecord method of the Installer object returns a new Record object with the requested number of fields.
ms.assetid: 7f9adb28-87da-48dd-ab5c-e138b356b133
title: Installer.CreateRecord method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.CreateRecord
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.CreateRecord method

The **CreateRecord** method of the [**Installer**](installer-object.md) object returns a new [**Record**](record-object.md) object with the requested number of fields.

## Syntax


```JScript
Installer.CreateRecord(
  count
)
```



## Parameters

<dl> <dt>

*count* 
</dt> <dd>

Required number of fields, which may be 0. The maximum number of fields in a record is limited to 65535.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Field 0, not one of the fields in *count*, is normally used for record-oriented items such as format strings or execution op-codes.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



 

 




