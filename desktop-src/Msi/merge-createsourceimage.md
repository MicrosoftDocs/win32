---
description: The CreateSourceImage method of the Merge object allows the client to extract the files from a module to a source image on disk after a merge, taking into account changes to the module that might have been made during module configuration.
ms.assetid: c3e3465a-d5a7-4fcc-b26a-5a8c763c23d9
title: Merge.CreateSourceImage method (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Merge.CreateSourceImage
- IMsmMerge.CreateSourceImage
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Merge.CreateSourceImage method

The **CreateSourceImage** method of the [**Merge**](merge-object.md) object allows the client to extract the files from a module to a source image on disk after a merge, taking into account changes to the module that might have been made during module configuration. The list of files to be extracted is taken from the file table of the module during the merge process. The list of files consists of every file successfully copied from the file table of the module to the target database. File table entries that were not copied due to primary key conflicts with existing rows in the database are not a part of this list. At image creation time, the directory for each of these files comes from the open (post-merge) database. The path specified in the *Path* parameter is the root of the source image for the install. *fLongFileNames* determines whether or not long file names are used for both path segments and final file names. The function fails if no database is open, no module is open, or no merge has been performed.

## Syntax


```JScript
Merge.CreateSourceImage(
  Path,
  fLongFileNames,
  pFilePaths
)
```



## Parameters

<dl> <dt>

*Path* 
</dt> <dd>

The path of the root of the source image for the install.

</dd> <dt>

*fLongFileNames* 
</dt> <dd>

*fLongFileNames* determines whether or not long file names are used for both path segments and final file names.

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

See [**CreateSourceImage**](/windows/desktop/api/Mergemod/nf-mergemod-imsmmerge2-createsourceimage) function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 2.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




