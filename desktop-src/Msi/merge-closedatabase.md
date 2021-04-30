---
description: The CloseDatabase method of the Merge object closes the currently open Windows Installer database.
ms.assetid: 'a89fe77a-0099-4c49-b484-c05ee351a66a'
title: Merge.CloseDatabase method (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Merge.CloseDatabase
- IMsmMerge.CloseDatabase
api_type: 
- COM
api_location: 
- Mergemod.dll
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

See [**CloseDatabase**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-closedatabase) function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 
