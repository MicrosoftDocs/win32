---
title: MrmCreateResourceFileInMemory function (MrmResourceIndexer.h)
description: Creates a PRI file in memory, not on disk.
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

Creates PRI file in memory, not as a file on disk. This is the last stage of creating a PRI file, after creating the indexer and adding resources. 

This function can only create a single PRI file; if you want to create split PRI files
you must use the [**MrmCreateResourceFile** function](mrmcreateresourcefile.md).

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

A handle identifying the resource indexer from which to create the PRI file. This handle is returned via a call to 
[**MrmCreateResourceIndexer**](mrmcreateresourceindexer.md) or one of the related **MrmCreateResourceIndexer...*** functions.

</dd> <dt>

*packagingMode* \[in\]
</dt> <dd>

Type: **[**MrmPackagingMode**](mrmpackagingmode.md)**

Specifies what kind of PRI file the function should create. You cannot use **MrmPackagingModeAutoSplit** with this
function. See the documentation for [**MrmPackagingMode**](mrmpackagingmode.md) and the **Remarks** section of 
[**MrmCreateResourceFile**](mrmcreateresourcefile.md) for more info.

</dd> <dt>

*packagingOptions* \[in\]
</dt> <dd>

Type: **[**MrmPackagingOptions**](mrmpackagingoptions.md)**

Specifies additional options about the PRI file. Most callers should specify **MrmPackagingOptionsNone**. See the documentation for
[**MrmPackagingOptions**](mrmpackagingoptions.md) for more info.


</dd> <dt>

*outputPriData* \[out\]
</dt> <dd>

Type: **BYTE\*\***

The address of a **BYTE** pointer. On successful return, contains a pointer to the buffer allocated by
the function that contains the generated PRI file. 
You must free the memory by calling [**MrmFreeMemory**](mrmfreememory.md) when you are done with it.

</dd> <dt>

*outputPriSize* \[out\]
</dt> <dd>

Type: **ULONG\***

The address of a **ULONG**. On successful return, contains the size of the allocated memory buffer pointed to by
 *outputPriData*.

</dd> </dl>

## Return value

Type: **HRESULT**

S\_OK if the function succeeded, otherwise some other value. Use the **SUCCEEDED** or **FAILED** macros 
(defined in winerror.h) to determine success or failure.

## Remarks

If you intend to pass *outputPriData* to [**MrmCreateResourceIndexerFromPreviousPriData**](mrmcreateresourceindexerfrompreviouspridata-.md), don't free the memory until after you've finished using the 
resource indexer.

For more information about the **packagingMode** parameter, see the **Remarks** section of 
[**MrmCreateResourceFile**](mrmcreateresourcefile.md). In particular, if you intend to save the data to a file
yourself, be sure to follow the correct naming conventions.

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

[**MrmCreateResourceFile**](mrmcreateresourcefile.md)
</dt></dl>

<dl> <dt>


[Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems)
</dt> </dl>

 

