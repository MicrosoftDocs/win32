---
description: The read-only DatabaseTable property of the Error object returns the name of the table in the database that caused the error.
ms.assetid: 38ff45ca-4bd6-43f3-88ad-db4077daeb77
title: Error.DatabaseTable property (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Error.DatabaseTable
- IMsmError.get_DatabaseTable
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Error.DatabaseTable property

The read-only **DatabaseTable** property of the [**Error**](error-object.md) object returns the name of the table in the database that caused the error.

This property is read-only.

## Syntax


```JScript
propVal = Error.DatabaseTable
```



## Property value

## Remarks

The collection is empty if the values do not apply to the type of the error. You can determine the type of error by calling [**Type**](error-type.md) property of the [**Error**](error-object.md) object.

### C++

See [**get\_DatabaseTable**](/windows/win32/api/mergemod/nf-mergemod-imsmerror-get_databasetable) function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

