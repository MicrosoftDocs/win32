---
description: The Merge method of the Merge object executes a merge of the current database and current module.
ms.assetid: '4b580b1f-5071-42f1-8022-a152817f9fdc'
title: Merge.Merge method (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Merge.Merge
- IMsmMerge.Merge
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Merge.Merge method

The **Merge** method of the [**Merge**](merge-object.md) object executes a merge of the current database and current module. The merge attaches the components in the module to the feature identified by *Feature*. The root of the module's directory tree is redirected to the location given by *RedirectDir*.

The **Merge** method can only be called once to merge a particular combination of .msi and .msm files.

## Syntax


```JScript
Merge.Merge(
  Feature,
  RedirectDir
)
```



## Parameters

<dl> <dt>

*Feature* 
</dt> <dd>

The name of a feature in the database.

</dd> <dt>

*RedirectDir* 
</dt> <dd>

The key of an entry in the [Directory table](directory-table.md) of the database. This parameter may be null or an empty string.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Once the merge is complete, components in the module are attached to the feature identified by *Feature*. This feature is not created and must be an existing feature. Note that the **Merge** method gets all the feature references in the module and substitutes the feature reference for all occurrences of the null GUID in the module database. For more information, see [Referencing Features in Merge Modules](referencing-features-in-merge-modules.md).

The module may be attached to additional features using the [**Connect**](merge-connect.md) method. Note that calling the **Connect** method only creates feature-component associations. It does not modify the rows that have already been merged in to the database.

Changes made to the database are saved if and only if the [**CloseDatabase**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-closedatabase) method is called with *bCommit* set to **TRUE**.

If any merge conflicts occur, including exclusions, they are placed in the error enumerator for later retrieval, but does not cause the merge to fail. Errors may be retrieved through the [**Errors**](error-object.md) property. Errors and informational messages are posted to the current log file.

### C++

See [**Merge**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-merge) function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 
