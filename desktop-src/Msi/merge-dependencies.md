---
description: The read-only Dependencies property of the Merge object returns a collection of Dependency objects that enumerates a set of unsatisfied dependencies for the current database.
ms.assetid: d7081ffe-3d9e-486e-84b6-b45e92fff5f0
title: Merge.Dependencies property (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Merge.Dependencies
- IMsmMerge.get_Dependencies
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Merge.Dependencies property

The read-only **Dependencies** property of the [**Merge**](merge-object.md) object returns a collection of [**Dependency**](dependency-object.md) objects that enumerates a set of unsatisfied dependencies for the current database.

This property is read-only.

## Syntax


```JScript
propVal = Merge.Dependencies
```



## Property value

## Remarks

A module does not need to be open to retrieve dependency information.

### C++

See [**get\_Dependencies**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-get_dependencies) Function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 
