---
Description: 'The OpenModule method of the Merge object opens a Windows Installer merge module in read-only mode. A module must be opened before it can be merged with an installation database.'
ms.assetid: '37225e61-c24f-4a44-8fdf-673590a6e09d'
title: 'Merge.OpenModule method'
---

# Merge.OpenModule method

The **OpenModule** method of the [**Merge**](merge-object.md) object opens a Windows Installer merge module in read-only mode. A module must be opened before it can be merged with an installation database.

## Syntax


```JScript
Merge.OpenModule(
  FileName,
  Language
)
```



## Parameters

<dl> <dt>

*FileName* 
</dt> <dd>

Fully qualified file name pointing to a merge module.

</dd> <dt>

*Language* 
</dt> <dd>

A valid language identifier (LANGID).

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This function opens the merge module in read-only mode and excludes other programs from writing to the merge module until the [**CloseModule**](merge-closemodule.md) method is called.

The installer attempts to open the module in the language specified by *Language*, or a more general language. For example, if *Language* is specified as 1033, a module with a default language of 1033, 9, or 0 can be opened in its default language. A *Language* value of 9 opens modules with a default language of 9 or 0. If the default language of the module does not meet the specified requirements, an attempt is made to transform the module to the requested language. If that fails, the module is transformed to increasingly general languages, all the way to language neutral. If none of the transforms succeed, the module fails to open. In this case, an error is added to the error list of type msmErrorLanguageUnsupported. If there is an error transforming the module to the desired language, an error is added to the error list of type msmErrorLanguageFailed. For details, see the [**Type**](error-type.md) property of the [**Error**](error-object.md) object. Opening a merge module clears any errors that have not already been retrieved.

### C++

See [**OpenModule**](imsmmerge-openmodule.md) function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




