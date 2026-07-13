---
title: MrmDumpPriDataInMemory function (MrmResourceIndexer.h)
description: Dumps an in-memory binary PRI file to its XML equivalent in memory.
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

Dumps an in-memory PRI file to its XML equivalent, storing the result in memory. PRI files are stored in an
undocumented binary format, so in order to view the contents of a file for debugging etc. it must be saved
("dumped") XML. 

This function performs the equivalent of the `makepri dump` command, but entirely in memory.

COM must be initialized (e.g. by calling **[CoInitializeEx](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex)**) before using this function.

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

A pointer to an in-memory PRI file. If this in-memory file does not have an embedded schema, then *schemaPriData* 
is required.

</dd> <dt>

*inputPriSize* \[in\]
</dt> <dd>

Type: **ULONG**

The size of the data pointed to by *inputPriData*.

</dd> <dt>

*schemaPriData* \[in, optional\]
</dt> <dd>

Type: **BYTE\***

A pointer to an in-memory PRI file that provides the schema for *inputPriData* if needed, otherwise **NULL**. 
See the **Remarks** section of [**MrmDumpPriFile**](mrmdumpprifile.md) for more info.

</dd> <dt>

*schemaPriSize* \[in\]
</dt> <dd>

Type: **ULONG**

The size of the data pointed to by *schemaPriData*.

</dd> <dt>

*dumpType* \[in\]
</dt> <dd>

Type: **[**MrmDumpType**](mrmdumptype.md)**

Specified the kind of dump to create. For most debugging use-cases, **MrmDumpTypeBasic** is sufficient. See the 
[**MrmDumpType** reference](mrmdumptype.md) for more info.

</dd> <dt>

*outputXmlData* \[out\]
</dt> <dd>

Type: **BYTE\*\***

The address of a **BYTE** pointer. On successful return, contains a pointer to the buffer allocated by
the function that contains the generated XML content. You must free the memory by calling 
[**MrmFreeMemory**](mrmfreememory.md) when you are done with it.

</dd> <dt>

*outputXmlSize* \[out\]
</dt> <dd>

Type: **ULONG\***

The address of a **ULONG**. On successful return, contains the size of the allocated memory buffer pointed to by
 *outputXmlData*.

</dd> </dl>

## Return value

Type: **HRESULT**

S\_OK if the function succeeded, otherwise some other value. Use the **SUCCEEDED** or **FAILED** macros (defined in winerror.h) 
to determine success or failure.

## Remarks

See the **Remarks** section of [**MrmDumpPriFile**](mrmdumpprifile.md) for more info,
as this function is essentially the same (except it works with in-memory data instead of files).

You can obtain an in-memory PRI file either by manually loading an existing PRI file from disk, or by creating it 
in-memory with [**MrmCreateResourceFileInMemory**](mrmcreateconfig.md).

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

[**MrmDumpPriFile**](mrmdumpprifile.md)
</dt></dl>

<dl> <dt>

[**MrmDumpPriFileInMemory**](mrmdumpprifileinmemory.md)
</dt></dl>
<dl> <dt>

[Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems)
</dt> </dl>

 

