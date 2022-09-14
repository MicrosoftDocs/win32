---
description: The read-only Module property of the Dependency Object returns the ModuleID of the module that is required by the current string in the form of a BSTR. The ModuleID is the same form that is used in the ModuleSignature Table.
ms.assetid: 22aae1b6-59b6-4842-9523-d1e064511380
title: Dependency.Module property (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Dependency.Module
- IMsmDependency.get_Module
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Dependency.Module property

The read-only **Module** property of the [**Dependency Object**](dependency-object.md) returns the ModuleID of the module that is required by the current string in the form of a **BSTR**. The ModuleID is the same form that is used in the [ModuleSignature Table](modulesignature-table.md).

This property is read-only.

## Syntax


```JScript
propVal = Dependency.Module
```



## Property value

## C++

See the [**IMsmDependency\_get\_Module**](/windows/win32/api/mergemod/nf-mergemod-imsmdependency-get_module) method.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

