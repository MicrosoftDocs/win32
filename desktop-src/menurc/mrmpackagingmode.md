---
title: MrmPackagingMode enumeration (MrmResourceIndexer.h)
description: Defines constants that specify what kind of PRI file(s) should be created by MrmCreateResourceFile and MrmCreateResourceFileInMemory.
ms.assetid: 5695B67E-5446-4538-83D2-F8FF91A5080E
keywords:
- MrmPackagingMode enumeration Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmPackagingMode
api_location:
- MrmResourceIndexer.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MrmPackagingMode enumeration

Defines constants that specify what kind of PRI file(s) should be created by [**MrmCreateResourceFile**](mrmcreateresourcefile.md) and 
[**MrmCreateResourceFileInMemory**](mrmcreateresourcefileinmemory.md). 

## Syntax


```C++
typedef enum _MrmPackagingMode { 
  MrmPackagingModeStandaloneFile  = 0,
  MrmPackagingModeAutoSplit       = 1,
  MrmPackagingModeResourcePack    = 2
} MrmPackagingMode;
```



## Constants

<dl> <dt>

<span id="MrmPackagingModeStandaloneFile"></span><span id="mrmpackagingmodestandalonefile"></span><span id="MRMPACKAGINGMODESTANDALONEFILE"></span>**MrmPackagingModeStandaloneFile**
</dt> <dd>

A single PRI file should be created containing all resources. This is the most common usage, and the only supported mode
for unpackaged desktop apps.

</dd> <dt>

<span id="MrmPackagingModeAutoSplit"></span><span id="mrmpackagingmodeautosplit"></span><span id="MRMPACKAGINGMODEAUTOSPLIT"></span>**MrmPackagingModeAutoSplit**
</dt> <dd>

One or more PRI files should be created, determined by language or scale. See **Remarks** for more info.

</dd> <dt>

<span id="MrmPackagingModeResourcePack"></span><span id="mrmpackagingmoderesourcepack"></span><span id="MRMPACKAGINGMODERESOURCEPACK"></span>**MrmPackagingModeResourcePack**
</dt> <dd>

A single resource-pack PRI file should be created. See **Remarks** for more info.

</dd> </dl>

## Remarks

PRI files created for unpackaged apps must use **MrmPackagingModeStandaloneFile** as MRT Core only supports a single PRI file. 
For packaged apps, you should also use **MrmPackagingModeStandaloneFile** unless you plan on building Resource Packs to minimize 
download / install size. A single stand-alone PRI file contains all resources in all languages / scales, and so is usable in all 
target markets. If you are building a packaged app and want to create Resource Packs, you can use one of the other two values.

**MrmPackagingModeAutoSplit** creates a PRI file for each of the following kinds of resources:

1. A main PRI, including all resources with the default language qualifier and all neutral resources.
1. One language-specific PRI for each set of resources using a non-default language qualifier.
1. One scale-specific PRI for each scale factor that is not a default qualifier and did not also have a language specifier.

For example, assume the indexer was created with English as the default qualifer, and it contains resources with all the 
following qualifiers:

1. \<none>
1. language-en
1. language-en_scale-100
1. language-de
1. language-de_scale-200
1. scale-400

In this case, 3 PRI files will be created:

* The file `resources.pri` will contain resources #1 (neutral) and #2 & #3 (default language).
* The file `resources.language-de.pri` will contain resources #4 & #5 (non-default language).
* The file `resources.scale-400.pri` will contain resource #6 (scale but no language).

Note that if the option **MrmPackagingOptionsSplitLanguageVariants** is specified when creating the PRI files,
a PRI file will be created for each language variant (eg, en-US, en-AU, and en-GB) instead of just one for each
language.

**MrmPackagingModeResourcePack** produces a single PRI file that contains resources in a single language. All
resources must have the same language as the default qualifier language. The resource indexer *must* have been created using 
[**MrmCreateResourceIndexerFromPreviousPriFile**](mrmcreateresourceindexerfrompreviousprifile.md) or
[**MrmCreateResourceIndexerFromPreviousPriData**](mrmcreateresourceindexerfrompreviouspridata-.md) and passing
the main PRI file as the *priFile* or *priData* parameters, respectively. Unlike the **AutoSplit** mode, there is no
mechanism to create individual scale-based resource packs.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1803 \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>MrmResourceIndexer.h</dt> </dl> |



## See also

<dl> <dt>

[**MrmCreateResourceFile**](mrmcreateresourcefile.md)
</dt> </dl>
<dl> <dt>

[**MrmCreateResourceFileInMemory**](mrmcreateresourcefileinmemory.md)
</dt> </dl>
<dl> <dt>

[Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems)
</dt> </dl>