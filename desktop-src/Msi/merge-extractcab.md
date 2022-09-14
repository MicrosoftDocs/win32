---
description: The ExtractCAB method of the Merge object extracts the embedded .cab file from a module and saves it as the specified file. The installer creates this file if it does not already exist and overwritten if it does exist.
ms.assetid: 'a6fe8b69-8f4a-45f7-b7e6-7620a00500bb'
title: Merge.ExtractCAB method (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Merge.ExtractCAB
- IMsmMerge.ExtractCAB
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Merge.ExtractCAB method

The **ExtractCAB** method of the [**Merge**](merge-object.md) object extracts the embedded .cab file from a module and saves it as the specified file. The installer creates this file if it does not already exist and overwritten if it does exist.

## Syntax


```JScript
Merge.ExtractCAB(
  FileName
)
```



## Parameters

<dl> <dt>

*FileName* 
</dt> <dd>

The fully qualified destination file.

</dd> </dl>

## Return value

This method does not return a value.

## C++

See [**ExtractCAB**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-extractcab) function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 
