---
title: MrmPackagingOptions enumeration (MrmResourceIndexer.h)
description: Defines constants that specify options for the PRI file created by MrmCreateResourceFile and MrmCreateResourceFileInMemory.
ms.assetid: 11FADCB2-CE6F-449E-8A85-DA50B52B26D0
keywords:
- MrmPackagingOptions enumeration Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmPackagingOptions
api_location:
- MrmResourceIndexer.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MrmPackagingOptions enumeration

Defines constants that specify options for the PRI file created by [**MrmCreateResourceFile**](mrmcreateresourcefile.md) and 
[**MrmCreateResourceFileInMemory**](mrmcreateresourcefileinmemory.md).

## Syntax


```C++
typedef enum _MrmPackagingOptions { 
  MrmPackagingOptionsNone                         = 0x00,
  MrmPackagingOptionsOmitSchemaFromResourcePacks  = 0x01,
  MrmPackagingOptionsSplitLanguageVariants        = 0x02
} MrmPackagingOptions;
```



## Constants

<dl> <dt>

<span id="MrmPackagingOptionsNone"></span><span id="mrmpackagingoptionsnone"></span><span id="MRMPACKAGINGOPTIONSNONE"></span>**MrmPackagingOptionsNone**
</dt> <dd>

No options. Most callers should use this value.

</dd> <dt>

<span id="MrmPackagingOptionsOmitSchemaFromResourcePacks"></span><span id="mrmpackagingoptionsomitschemafromresourcepacks"></span><span id="MRMPACKAGINGOPTIONSOMITSCHEMAFROMRESOURCEPACKS"></span>**MrmPackagingOptionsOmitSchemaFromResourcePacks**
</dt> <dd>

Resource Pack PRIs should be created without an embedded schema. See **Remarks** for more info.

</dd> <dt>

<span id="MrmPackagingOptionsSplitLanguageVariants"></span><span id="mrmpackagingoptionssplitlanguagevariants"></span><span id="MRMPACKAGINGOPTIONSSPLITLANGUAGEVARIANTS"></span>**MrmPackagingOptionsSplitLanguageVariants**
</dt> <dd>

Auto-split PRIs should be created based on language variants. See **Remarks** for more info.

</dd> </dl>

## Remarks

PRI files created for unpackaged desktop apps should specify **MrmPackagingOptionsNone** as resource packs are
not supported. Most packaged apps should also specify **MrmPackagingOptionsNone** as it eases development.

**MrmPackagingOptionsOmitSchemaFromResourcePacks** is used when creating a resource pack PRIs, either 
with the **AutoSplit** or **ResourcePack** packaging modes. The resource pack PRIs will not contain the
resource names (only the indexes) which reduces the file size but makes certain debugging operations 
(such as dumping to XML) harder. See the **Remarks** section of 
[**MrmCreateResourceIndexerFromPreviousSchemaFile**](mrmcreateresourceindexerfrompreviousschemafile.md)
for additional info about schemas.

**MrmPackagingOptionsSplitLanguageVariants** is used when creating resource pack PRIs with the **AutoSplit**
mode. In this case, rather than creating a single PRI per language, each language variant (eg en-US, en-AU, 
and en-GB) will have their own PRI files generated.

See [**MrmPackagingMode**](mrmpackagingmode.md) for more info.

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