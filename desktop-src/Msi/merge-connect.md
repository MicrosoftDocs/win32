---
Description: The Connect method of the Merge object connects a module to an additional feature. The module must have already been merged into the database or will be merged into the database. The feature must exist before calling this function.
ms.assetid: f491beb8-90f7-4e41-891d-ef674306339d
title: Merge.Connect method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Merge.Connect method

The **Connect** method of the [**Merge**](merge-object.md) object connects a module to an additional feature. The module must have already been merged into the database or will be merged into the database. The feature must exist before calling this function.

Changes made to the database are not saved to disk unless the [**CloseDatabase**](merge-closedatabase.md) method is called with *bCommit* set to **TRUE**.

## Syntax


```JScript
Merge.Connect(
  Feature
)
```



## Parameters

<dl> <dt>

*Feature* 
</dt> <dd>

The name of a feature already existing in the database.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Errors may be retrieved through the [**Errors**](merge-errors.md) property. Errors and informational messages are posted to the current log file.

### C++

See [**Connect**](https://msdn.microsoft.com/en-us/library/Aa369268(v=VS.85).aspx) function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




