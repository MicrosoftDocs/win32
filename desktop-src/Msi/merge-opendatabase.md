---
description: The OpenDatabase method of the Merge object opens a Windows Installer installation database, located at a specified path, that is to be merged with a module.
ms.assetid: '86f168e5-bc76-476d-9757-9b2a21bb9c4b'
title: Merge.OpenDatabase method (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Merge.OpenDatabase
- IMsmMerge.OpenDatabase
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Merge.OpenDatabase method

The **OpenDatabase** method of the [**Merge**](merge-object.md) object opens a Windows Installer installation database, located at a specified path, that is to be merged with a module.

## Syntax


```JScript
Merge.OpenDatabase(
  Path
)
```



## Parameters

<dl> <dt>

*Path* 
</dt> <dd>

Path to the database being opened.

</dd> </dl>

## Return value

This method does not return a value.

## C++

See [**OpenDatabase**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-opendatabase) function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 
