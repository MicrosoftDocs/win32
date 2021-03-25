---
description: The read-only ModuleTable Property returns the name of the table in the module that caused the error.
ms.assetid: 390f5889-d638-4c1c-b95c-76d38c934e7c
title: Error.ModuleTable property (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Error.ModuleTable
- IMsmError.get_ModuleTable
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Error.ModuleTable property

The read-only **ModuleTable** Property returns the name of the table in the module that caused the error.

This property is read-only.

## Syntax


```JScript
propVal = Error.ModuleTable
```



## Property value

## Remarks

The collection is empty if the values do not apply to the type of the error. You can determine the type of error by calling the [**Type**](error-type.md) property of the [**Error**](error-object.md) object.

### C++

See [**get\_ModuleTable**](/windows/win32/api/mergemod/nf-mergemod-imsmerror-get_moduletable) function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

