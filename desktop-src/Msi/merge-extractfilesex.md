---
Description: 'The ExtractFilesEx method of the Merge object extracts the embedded .cab file from a module and then writes those files to the destination directory.'
ms.assetid: '8b063052-4f92-466a-9c52-bda26ed13d5c'
title: 'Merge.ExtractFilesEx method'
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

See [**ExtractFilesEx**](imsmmerge2-extractfilesex.md) function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 2.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




