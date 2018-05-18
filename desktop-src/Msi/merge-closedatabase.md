---
Description: 'The CloseDatabase method of the Merge object closes the currently open Windows Installer database.'
ms.assetid: 'efbb6238-e9e3-4603-896a-75fcff2bb362'
title: 'Merge.CloseDatabase method'
---

# Merge.CloseDatabase method

The **CloseDatabase** method of the [**Merge**](merge-object.md) object closes the currently open Windows Installer database.

## Syntax


```JScript
Merge.CloseDatabase(
  bCommit
)
```



## Parameters

<dl> <dt>

*bCommit* 
</dt> <dd>

**TRUE** if changes should be saved, **FALSE** otherwise.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Closing a database clears all dependency information but does not affect any errors that have not been retrieved.

### C++

See [**CloseDatabase**](imsmmerge-closedatabase.md) function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




