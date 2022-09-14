---
title: MrmCreateResourceFileInMemory function (MrmResourceIndexer.h)
description: Creates PRI info as a blob in memory, not as a file on disk.
ms.assetid: 68BDAD27-545A-4DC6-B909-4242A0863690
keywords:
- MrmCreateResourceFileInMemory function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmCreateResourceFileInMemory
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmCreateResourceFileInMemory function

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Creates PRI info as a blob in memory, not as a file on disk. The function allocates memory and returns a pointer to that memory in *outputPriData*. Call [**MrmFreeMemory**](mrmfreememory.md) with the same pointer to free that memory. For more info, and scenario-based walkthroughs of how to use these APIs, see [Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems).

## Syntax


```C++
HRESULT HRESULT MrmCreateResourceFileInMemory(
  _In_  MrmResourceIndexerHandle indexer,
  _In_  MrmPackagingMode         packagingMode,
  _In_  MrmPackagingOptions      packagingOptions,
  _Out_ BYTE                     **outputPriData,
  _Out_ ULONG                    *outputPriSize
);
```



## Parameters

<dl> <dt>

*indexer* \[in\]
</dt> <dd>

Type: **[**MrmResourceIndexerHandle**](mrmresourceindexerhandle.md)**

A handle identifying the resource indexer from which to create the PRI info.

</dd> <dt>

*packagingMode* \[in\]
</dt> <dd>

Type: **[**MrmPackagingMode**](mrmpackagingmode.md)**

Specifies whether the PRI info should be standalone, or be a resource pack. **MrmPackagingModeAutoSplit** is not supported.

</dd> <dt>

*packagingOptions* \[in\]
</dt> <dd>

Type: **[**MrmPackagingOptions**](mrmpackagingoptions.md)**

Specifies additional options about the PRI info.

</dd> <dt>

*outputPriData* \[out\]
</dt> <dd>

Type: **BYTE\*\***

The address of a pointer to BYTE. The function allocates memory and returns a pointer to that memory in *outputPriData*. Call [**MrmFreeMemory**](mrmfreememory.md) with your pointer to BYTE to free that memory.

</dd> <dt>

*outputPriSize* \[out\]
</dt> <dd>

Type: **ULONG\***

The address of a ULONG. In *outputPriSize*, the function returns the size of the allocated memory pointed to by *outputPriData*.

</dd> </dl>

## Return value

Type: **HRESULT**

S\_OK if the function succeeded, otherwise some other value. Use the SUCCEEDED() or FAILED() macros (defined in winerror.h) to determine success or failure.

## Remarks

If you pass *outputPriData* to [**MrmCreateResourceIndexerFromPreviousPriData**](mrmcreateresourceindexerfrompreviouspridata-.md), then don't free the memory until after you've finished using the resource indexer.

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

 

