---
description: In Windows Installer versions 1.0 and 1.1 the Path property is always the empty string. Future versions may use this value to return the path to the file or directory that could not be created.
ms.assetid: b79dd347-acda-47d7-aa3b-c0f9a6ca1d3b
title: Error.Path property (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Error.Path
- IMsmError.get_Path
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Error.Path property

In Windows Installer versions 1.0 and 1.1 the Path property is always the empty string. Future versions may use this value to return the path to the file or directory that could not be created.

This property is read-only.

## Syntax


```JScript
propVal = Error.Path
```



## Property value

## Remarks

This value is only valid for errors of type msmErrorFileCreate or msmErrorDirCreate. You can determine the type of error by calling [**Type**](error-type.md) property of the [**Error**](error-object.md) object.

### C++

See [**get\_Path**](/windows/win32/api/mergemod/nf-mergemod-imsmerror-get_path) function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

