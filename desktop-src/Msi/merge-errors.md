---
Description: The read-only Errors property of the Merge object returns a collection of Error objects that is the current set of errors.
ms.assetid: 619f17cc-131a-4262-ad48-9ab1318142aa
title: Merge.Errors property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

See [**get\_Errors**](https://msdn.microsoft.com/en-us/library/Aa369272(v=VS.85).aspx) Function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




