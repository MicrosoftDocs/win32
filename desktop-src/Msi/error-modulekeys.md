---
description: The read-only ModuleKeys property of the Error object returns a pointer to a string collection containing the primary keys of the row in the module causing the error, one key per entry in the collection.
ms.assetid: b02b609b-4682-4228-b29a-364f079e863c
title: Error.ModuleKeys property (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Error.ModuleKeys
- IMsmError.get_ModuleKeys
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Error.ModuleKeys property

The read-only **ModuleKeys** property of the [**Error**](error-object.md) object returns a pointer to a string collection containing the primary keys of the row in the module causing the error, one key per entry in the collection.

This property is read-only.

## Syntax


```JScript
propVal = Error.ModuleKeys
```



## Property value

## Remarks

The client is responsible for releasing the string collection when it is no longer needed.

The collection is empty if the values do not apply to the type of the error. You can determine the type of error by calling the [**Type**](error-type.md) property of the [**Error**](error-object.md) object.

### C++

See [**get\_ModuleKeys**](/windows/win32/api/mergemod/nf-mergemod-imsmerror-get_modulekeys) function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

