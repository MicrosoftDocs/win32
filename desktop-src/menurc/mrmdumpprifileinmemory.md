---
title: MrmDumpPriFileInMemory function (MrmResourceIndexer.h)
description: Dumps a binary PRI file to its XML equivalent in memory.
ms.assetid: 04FD048F-1473-47B1-9CAB-03FEF98A9B48
keywords:
- MrmDumpPriFileInMemory function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmDumpPriFileInMemory
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmDumpPriFileInMemory function

Dumps a PRI file to its XML equivalent, storing the result in memory. PRI files are stored in an undocumented binary
format, so in order to view the contents of a file for debugging etc. it must be saved ("dumped") as XML. 

This function performs the equivalent of the `makepri dump` command, with the results being stored in memory.

COM must be initialized (e.g. by calling **[CoInitializeEx](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex)**) before using this function.

## Syntax


```C++
HRESULT HRESULT MrmDumpPriFileInMemory(
  _In_     PCWSTR      indexFileName,
  _In_opt_ PCWSTR      schemaPriFile,
  _In_     MrmDumpType dumpType,
  _Out_    BYTE        **outputXmlData,
  _Out_    ULONG       *outputXmlSize
);
```



## Parameters

<dl> <dt>

*indexFileName* \[in\]
</dt> <dd>

Type: **PCWSTR**

The path to the PRI file to dump. If this file does not have an embedded schema, then *schemaPriFile* is required.

</dd> <dt>

*schemaPriFile* \[in, optional\]
</dt> <dd>

Type: **PCWSTR**

The path to the PRI file that provides the schema for the *indexFileName* if needed, otherwise **NULL**. 
See the **Remarks** section of [**MrmDumpPriFile**](mrmdumpprifile.md) for more info.

</dd> <dt>

*dumpType* \[in\]
</dt> <dd>

Type: **[**MrmDumpType**](mrmdumptype.md)**

Specified the kind of dump to create. For most use-cases, **MrmDumpTypeBasic** is sufficient. See the 
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
as this function is essentially the same (except it dumps the XML to memory instead of to a disk file).

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

[**MrmDumpPriDataInMemory**](mrmdumppridatainmemory.md)
</dt></dl>

<dl> <dt>

[**MrmDumpPriFile**](mrmdumpprifile.md)
</dt></dl>
<dl> <dt>

[Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems)
</dt> </dl>