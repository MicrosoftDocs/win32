---
title: MrmCreateResourceIndexerFromPreviousSchemaData function (MrmResourceIndexer.h)
description: Creates a resource indexer that can create PRI files that are compatible with existing PRI files.
ms.assetid: D9C90C12-CEFE-4794-9553-8BFBE9E43D99
keywords:
- MrmCreateResourceIndexerFromPreviousSchemaData function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmCreateResourceIndexerFromPreviousSchemaData
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmCreateResourceIndexerFromPreviousSchemaData function

Creates a resource indexer that can create PRI files that are compatible with existing PRI files. This function
is only needed in fairly limited scenarios; see the **Remarks** section of 
[**MrmCreateResourceIndexerFromPreviousSchemaFile**](mrmcreateresourceindexerfrompreviousschemafile.md) for more info.

COM must be initialized (e.g. by calling **[CoInitializeEx](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex)**) 
before using this function.

## Syntax


```C++
HRESULT HRESULT MrmCreateResourceIndexerFromPreviousSchemaData(
  _In_     PCWSTR                   projectRoot,
  _In_     MrmPlatformVersion       platformVersion,
  _In_opt_ PCWSTR                   defaultQualifiers,
  _In_     BYTE                     *schemaXmlData,
  _In_     ULONG                    schemaXmlSize,
  _Inout_  MrmResourceIndexerHandle *indexer
);
```



## Parameters

<dl> <dt>

*projectRoot* \[in\]
</dt> <dd>

Type: **PCWSTR**

The root directory from which some file paths will be computed. Typically this will be the root directory of your
source project, but may differ. See [File resources in MRM](mrmfiles.md) for more information.

</dd> <dt>

*platformVersion* \[in\]
</dt> <dd>

Type: **[**MrmPlatformVersion**](mrmplatformversion.md)**

The platform version (*targetOsVersion*) to use for the generated configuration file. Most callers should just 
use **MrmPlatformVersion_Windows10_0_0_5**

</dd> <dt>

*defaultQualifiers* \[in, optional\]
</dt> <dd>

Type: **PCWSTR**

A list of default resource qualifiers. For example, "language-en-US_scale-100". For more information about qualifiers, 
see [Qualifiers in MRM](mrmqualifiers.md).

</dd> <dt>

*schemaXmlData* \[in\]
</dt> <dd>

Type: **BYTE\***

A pointer to an in-memory PRI file or in-memory Schema XML dump. You can obtain an in-memory PRI file either by manually loading
an existing PRI file from disk, or by creating it in-memory with [**MrmCreateResourceFileInMemory**](mrmcreateconfig.md). You
can obtain an in-memory Schema XML dump either by manually loading an existing file from disk, or by using one of the 
**MrmDump...** functions.

</dd> <dt>

*schemaXmlSize* \[in\]
</dt> <dd>

Type: **ULONG**

The size of the data pointed to by *schemaXmlData*.

</dd> <dt>

*indexer* \[in, out\]
</dt> <dd>

Type: **[**MrmResourceIndexerHandle**](mrmresourceindexerhandle.md)\***

A pointer to a resource indexer handle. On successful return, this will contain a handle to a resource indexer.
You must free the indexer via [**MrmDestroyIndexerAndMessages**](mrmdestroyindexerandmessages.md) after using it.

</dd> </dl>

## Return value

Type: **HRESULT**

S\_OK if the function succeeded, otherwise some other value. Use the **SUCCEEDED** or **FAILED** macros (defined in winerror.h) 
to determine success or failure.

## Remarks

See the **Remarks** section
of [**MrmCreateResourceIndexerFromPreviousSchemaFile**](mrmcreateresourceindexerfrompreviousschemafile.md) for more info,
as this function is essentially the same (except it uses in-memory reference PRI rather than an on-disk file).

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

[**MrmCreateResourceIndexer**](mrmcreateresourceindexer.md)
</dt></dl>

<dl> <dt>

[**MrmCreateResourceIndexerFromPreviousPriData**](mrmcreateresourceindexerfrompreviouspridata-.md)
</dt></dl>

<dl> <dt>

[**MrmCreateResourceIndexerFromPreviousPriFile**](mrmcreateresourceindexerfrompreviousprifile.md.md)
</dt></dl>

<dl> <dt>

[**MrmCreateResourceIndexerFromPreviousSchemaFile**](mrmcreateresourceindexerfrompreviousschemafile.md)
</dt></dl>

<dl> <dt>

[Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems)
</dt></dl>
