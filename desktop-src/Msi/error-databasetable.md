---
Description: 'The read-only DatabaseTable property of the Error object returns the name of the table in the database that caused the error.'
ms.assetid: '38ff45ca-4bd6-43f3-88ad-db4077daeb77'
title: 'Error.DatabaseTable property'
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

See [**get\_DatabaseTable**](imsmerror-get-databasetable.md) function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




