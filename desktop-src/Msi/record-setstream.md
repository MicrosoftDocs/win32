---
description: The SetStream method of the Record object copies the content of the specified file into the designated record field as stream data. Stream data cannot be inserted into temporary fields.
ms.assetid: feb79371-d0c4-4bb0-b539-2f431ee1051b
title: Record.SetStream method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Record.SetStream
api_type: 
- COM
api_location: 
- Msi.dll
---

# Record.SetStream method

The **SetStream** method of the [**Record**](record-object.md) object copies the content of the specified file into the designated record field as stream data. Stream data cannot be inserted into temporary fields.

## Syntax


```JScript
Record.SetStream(
  field,
  filePath
)
```



## Parameters

<dl> <dt>

*field* 
</dt> <dd>

Required field number of the value within the record, 1-based.

</dd> <dt>

*filePath* 
</dt> <dd>

The location of the file to copy. No translation of any type is performed.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

If the method fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IRecord is defined as 000C1093-0000-0000-C000-000000000046<br/>                                                                                                                                                                              |



 

 




