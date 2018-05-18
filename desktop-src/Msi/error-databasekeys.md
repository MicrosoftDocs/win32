---
Description: 'The read-only DatabaseKeys property of the Error object returns a string collection that contains the primary keys of the database row causing the error. There is one key per entry in the collection.'
ms.assetid: '416a6cef-4c70-4c06-a8d2-801c9440e25a'
title: 'Error.DatabaseKeys property'
---

# Error.DatabaseKeys property

The read-only **DatabaseKeys** property of the [**Error**](error-object.md) object returns a string collection that contains the primary keys of the database row causing the error. There is one key per entry in the collection.

This property is read-only.

## Syntax


```JScript
propVal = Error.DatabaseKeys
```



## Property value

## Remarks

The client is responsible for releasing the string collection when it is no longer needed.

The collection is empty if the values do not apply to the type of the error. You can determine the type of error by calling the [**Type**](error-type.md) property of the [**Error**](error-object.md) object.

### C++

See [**get\_DatabaseKeys**](imsmerror-get-databasekeys.md) function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




