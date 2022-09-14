---
description: The MergeEx method of the Merge object is equivalent to the Merge function, except that it takes an extra argument.
ms.assetid: 83b6d62b-d176-42ac-b513-d1c2e562965c
title: Merge.MergeEx method (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Merge.MergeEx
- IMsmMerge.MergeEx
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Merge.MergeEx method

The **MergeEx** method of the [**Merge**](merge-object.md) object is equivalent to the [**Merge**](/windows/win32/api/mergemod/nf-mergemod-imsmmerge-merge) function, except that it takes an extra argument. The *pConfiguration* argument is an interface implemented by the client. The argument may be null. The presence of this argument indicates that the client is capable of supporting the configuration functionality, but does not obligate the client to provide configuration data for any specific configurable item.

The [**Merge**](merge-merge.md) method executes a merge of the current database and current module. The merge attaches the components in the module to the feature identified by *Feature*. The root of the module's directory tree is redirected to the location given by *RedirectDir*.

## Syntax


```JScript
Merge.MergeEx(
  Feature,
  RedirectDir,
  pConfiguration
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

</dd> <dt>

*pConfiguration* 
</dt> <dd>

The *pConfiguration* argument is an interface implemented by the client. The argument may be null. The presence of this argument indicates that the client is capable of supporting the configuration functionality, but does not obligate the client to provide configuration data for any specific configurable item.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Once the merge is complete, components in the module are attached to the feature identified by *Feature*. This feature is not created and must be an existing feature. The module may be attached to additional features using the [**Connect**](merge-connect.md) method.

Changes made to the database are saved if and only if the [**CloseDatabase**](merge-closedatabase.md) method is called with *bCommit* set to **TRUE**.

If any merge conflicts occur, including exclusions, they are placed in the error enumerator for later retrieval, but does not cause the merge to fail. Errors may be retrieved through the [**Errors**](merge-errors.md) property. Errors and informational messages are posted to the current log file.

When the merge fails because of an incorrect module configuration the [**MergeEx**](/windows/desktop/api/Mergemod/nf-mergemod-imsmmerge2-mergeex) function returns E\_FAIL. This includes these msmErrorType errors: **msmErrorBadNullSubstitution**, **msmErrorBadSubstitutionType**, **msmErrorBadNullResponse**, **msmErrorMissingConfigItem**, and **msmErrorDataRequestFailed**. These errors cause the merge to stop immediately when the error is encountered. The error object is still added to the enumerator when **MergeEx** returns E\_FAIL. For more information about msmErrorType errors, see [**get\_Type Function (Error Object)**](/windows/win32/api/mergemod/nf-mergemod-imsmerror-get_type). All other errors cause **MergeEx** to return S\_FALSE and cause the merge to continue.

### C++

See [**MergeEx**](/windows/desktop/api/Mergemod/nf-mergemod-imsmmerge2-mergeex) function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 2.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 
