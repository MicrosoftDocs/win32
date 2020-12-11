---
title: MrmDumpPriDataInMemory function (MrmResourceIndexer.h)
description: Dumps PRI info (as a blob in memory, created by a previous call to MrmCreateResourceFileInMemory) to its XML equivalent (as in-memory data), in order to make it more easily readable.
ms.assetid: 6E563B43-4E0A-465D-A8EA-7DE61738DE06
keywords:
- MrmDumpPriDataInMemory function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmDumpPriDataInMemory
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmDumpPriDataInMemory function

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Dumps PRI info (as a blob in memory, created by a previous call to [**MrmCreateResourceFileInMemory**](mrmcreateresourcefileinmemory.md)) to its XML equivalent (as in-memory data), in order to make it more easily readable. The function allocates memory and returns a pointer to that memory in *outputXmlData*. Call [**MrmFreeMemory**](mrmfreememory.md) with the same pointer to free that memory. For more info, and scenario-based walkthroughs of how to use these APIs, see [Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems).

## Syntax


```C++
HRESULT HRESULT MrmDumpPriDataInMemory(
  _In_     BYTE        *inputPriData,
  _In_     ULONG       inputPriSize,
  _In_opt_ BYTE        *schemaPriData,
  _In_     ULONG       schemaPriSize,
  _In_     MrmDumpType dumpType,
  _Out_    BYTE        **outputXmlData,
  _Out_    ULONG       *outputXmlSize
);
```



## Parameters

<dl> <dt>

*inputPriData* \[in\]
</dt> <dd>

Type: **BYTE\***

A pointer to PRI data created by a previous call to [**MrmCreateResourceFileInMemory**](mrmcreateresourcefileinmemory.md).

</dd> <dt>

*inputPriSize* \[in\]
</dt> <dd>

Type: **ULONG**

The size of the data pointed to by *inputPriData*.

</dd> <dt>

*schemaPriData* \[in, optional\]
</dt> <dd>

Type: **BYTE\***

An optional pointer to PRI info (as a blob in memory) representing schema data created by a previous call to [**MrmCreateResourceFileInMemory**](mrmcreateresourcefileinmemory.md). Don't free *schemaPriData* until after you've finished using the resource indexer. Also see Remarks.

</dd> <dt>

*schemaPriSize* \[in\]
</dt> <dd>

Type: **ULONG**

The size of the data pointed to by *schemaPriData*.

</dd> <dt>

*dumpType* \[in\]
</dt> <dd>

Type: **[**MrmDumpType**](mrmdumptype.md)**

Specifies how detailed the XML dump should be, or whether a schema should be dumped.

</dd> <dt>

*outputXmlData* \[out\]
</dt> <dd>

Type: **BYTE\*\***

The address of a pointer to BYTE. The function allocates memory and returns a pointer to that memory in *outputXmlData*. Call [**MrmFreeMemory**](mrmfreememory.md) with your pointer to BYTE to free that memory.

</dd> <dt>

*outputXmlSize* \[out\]
</dt> <dd>

Type: **ULONG\***

The address of a ULONG. In *outputXmlSize*, the function returns the size of the allocated memory pointed to by *outputXmlData*.

</dd> </dl>

## Return value

Type: **HRESULT**

S\_OK if the function succeeded, otherwise some other value. Use the SUCCEEDED() or FAILED() macros (defined in winerror.h) to determine success or failure.

## Remarks

A schema-free resource pack is one that was created with the [**MrmPackagingOptionsOmitSchemaFromResourcePacks**](mrmpackagingoptions.md) argument passed to [**MrmCreateResourceFile**](mrmcreateresourcefile.md) or [**MrmCreateResourceFileInMemory**](mrmcreateresourcefileinmemory.md) (or with the *omitSchemaFromResourcePacks* switch in the PRI config file). To dump a schema-free resource pack, pass the path to your main package PRI data as the argument for the *schemaPriData* parameter.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1803 \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>MrmResourceIndexer.h</dt> </dl> |
| Library<br/>                  | <dl> <dt>Mrmsupport.lib</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Mrmsupport.dll</dt> </dl>       |



## See also

<dl> <dt>

[Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems)
</dt> </dl>

 

