---
title: /metadata_dir switch (MIDLRT)
description: The /metadata\_dir switch specifies one or more directories that contain platform metadata files.
ms.assetid: '578b9d3f-3ee6-4978-9d2a-0c5aee561a30'
keywords:
- /metadata_dir switch MIDL
topic_type:
- apiref
api_name:
- /metadata_dir
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /metadata_dir switch (MIDLRT)

The **/metadata\_dir** switch specifies one or more directories that contain platform metadata files.

``` syntax
midlrt /metadata_dir metadata_directory
```

## Switch Options

<dl> <dt>

*metadata\_directory* 
</dt> <dd>

Specifies one or more directories that contain platform metadata files.

</dd> </dl>

## Remarks

Use this switch to specify the location of the main metadata file for Windows, which is named windows.winmd.

## Examples

**midlrt /metadata\_dir dir1 dir2**

## Requirements



| Requirement | Value |
|-------------------|--------------------------------|
| Client<br/> | Windows 8<br/>           |
| Server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> </dl>

 

 





