---
description: The ExtractFilesEx method of the Merge object extracts the embedded .cab file from a module and then writes those files to the destination directory.
ms.assetid: 8b063052-4f92-466a-9c52-bda26ed13d5c
title: Merge.ExtractFilesEx method (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Merge.ExtractFilesEx
- IMsmMerge.ExtractFilesEx
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Merge.ExtractFilesEx method

The **ExtractFilesEx** method of the [**Merge**](merge-object.md) object extracts the embedded .cab file from a module and then writes those files to the destination directory.

## Syntax


```JScript
Merge.ExtractFilesEx(
  Path,
  fLongFileNames,
  pFilePaths
)
```



## Parameters

<dl> <dt>

*Path* 
</dt> <dd>

The fully qualified destination directory.

</dd> <dt>

*fLongFileNames* 
</dt> <dd>

Set to specify using long file names for path segments and final file names.

</dd> <dt>

*pFilePaths* 
</dt> <dd>

This is a list of fully qualified paths for the files that were successfully extracted.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Any files in the destination directory with the same name are overwritten. The path is created if it does not already exist.

### C++

See [**ExtractFilesEx**](/windows/desktop/api/Mergemod/nf-mergemod-imsmmerge2-extractfilesex) function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 2.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




