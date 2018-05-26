---
title: /metadata\_dir switch
description: The /metadata\_dir switch specifies one or more directories that contain platform metadata files.
ms.assetid: E95D410B-D384-4337-B0A0-6D5DDA3BE699
keywords:
- /metadata_dir switch MIDL
topic_type:
- apiref
api_name:
- /metadata_dir
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# /metadata\_dir switch

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



|                   |                                |
|-------------------|--------------------------------|
| Client<br/> | Windows 8<br/>           |
| Server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> </dl>

 

 





