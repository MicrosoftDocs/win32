---
description: The CloseModule method of the Merge object closes the currently open Windows Installer merge module.
ms.assetid: 'a11f72cf-4c4e-4650-95f9-549169452622'
title: Merge.CloseModule method (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Merge.CloseModule
- IMsmMerge.CloseModule
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Merge.CloseModule method

The **CloseModule** method of the [**Merge**](merge-object.md) object closes the currently open Windows Installer merge module.

## Syntax


```JScript
Merge.CloseModule()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Closing a merge module will not affect any errors that have not been retrieved.

### C++

See [**CloseModule**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-closemodule) function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 
