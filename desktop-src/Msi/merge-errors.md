---
description: The read-only Errors property of the Merge object returns a collection of Error objects that is the current set of errors.
ms.assetid: 619f17cc-131a-4262-ad48-9ab1318142aa
title: Merge.Errors property (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Merge.Errors
- IMsmMerge.get_Errors
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Merge.Errors property

The read-only **Errors** property of the [**Merge**](merge-object.md) object returns a collection of [**Error**](error-object.md) objects that is the current set of errors.

This property is read-only.

## Syntax


```JScript
propVal = Merge.Errors
```



## Property value

## Remarks

The retrieval is non-destructive. Multiple instances of the error collection may be retrieved by repeatedly calling this method.

### C++

See [**get\_Errors**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-get_errors) Function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 
