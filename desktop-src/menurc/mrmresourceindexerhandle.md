---
title: MrmResourceIndexerHandle structure (MrmResourceIndexer.h)
description: Represents a handle to a resource indexer object.
ms.assetid: E3ED8AB8-39B8-419C-9570-1CC6B2CFE8D0
keywords:
- MrmResourceIndexerHandle structure Menus and Other Resources
- PMrmResourceIndexerHandle structure pointer Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmResourceIndexerHandle
api_location:
- MrmResourceIndexer.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MrmResourceIndexerHandle structure

Represents a handle to a resource indexer object. Most MRM functions require an indexer handle, which can 
be obtained via one of the **MrmCreateResourceIndexer...** functions.

## Syntax


```C++
typedef struct _MrmResourceIndexerHandle {
  PVOID handle;
} MrmResourceIndexerHandle, *PMrmResourceIndexerHandle;
```



## Members

<dl> <dt>

**handle**
</dt> <dd>

Type: **PVOID**

</dd> <dd>

An opaque handle to a resource indexer object. Do not use this value directly.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1803 \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>MrmResourceIndexer.h</dt> </dl> |



## See also

<dl> <dt>

[**MrmCreateResourceIndexer**](mrmcreateresourceindexer.md)
</dt></dl>

<dl> <dt>

[**MrmCreateResourceIndexerFromPreviousPriData**](mrmcreateresourceindexerfrompreviouspridata-.md)
</dt></dl>

<dl> <dt>

[**MrmCreateResourceIndexerFromPreviousPriFile**](mrmcreateresourceindexerfrompreviousprifile.md)
</dt></dl>

<dl> <dt>

[**MrmCreateResourceIndexerFromPreviousSchemaData**](mrmcreateresourceindexerfrompreviousschemadata.md)
</dt></dl>

<dl> <dt>

[**MrmCreateResourceIndexerFromPreviousSchemaFile**](mrmcreateresourceindexerfrompreviousschemafile.md)
</dt></dl>

<dl> <dt>

[**MrmDestroyIndexerAndMessages**](mrmresourceindexermessage.md)
</dt></dl>

<dl> <dt>

[Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems)
</dt></dl>
