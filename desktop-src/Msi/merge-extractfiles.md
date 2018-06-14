---
Description: The ExtractFiles method of the Merge object extracts the embedded .cab file from a module and then writes those files to the destination directory.
ms.assetid: e5bafd2d-0750-4aa6-87e8-22ef3cfdd5ff
title: Merge.ExtractFiles method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Merge.ExtractFiles method

The **ExtractFiles** method of the [**Merge**](merge-object.md) object extracts the embedded .cab file from a module and then writes those files to the destination directory.

## Syntax


```JScript
Merge.ExtractFiles(
  Path
)
```



## Parameters

<dl> <dt>

*Path* 
</dt> <dd>

The fully qualified destination directory.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Any files in the destination directory with the same name are overwritten. The path is created if it does not already exist.

**ExtractFiles** always extracts files using short file names for the path. To use long file names for the path, use the [**ExtractFilesEx method**](merge-extractfilesex.md).

### C++

See [**ExtractFiles**](https://msdn.microsoft.com/en-us/library/Aa369270(v=VS.85).aspx) function.

## Requirements



|                    |                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                                     |
| Header<br/>  | <dl> <dt>Advpub.h (include Mergemod.h)</dt> </dl> |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl>                  |



 

 




