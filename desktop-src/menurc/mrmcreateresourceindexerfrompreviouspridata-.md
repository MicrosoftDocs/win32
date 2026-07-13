---
title: MrmCreateResourceIndexerFromPreviousPriData function (MrmResourceIndexer.h)
description: Creates a resource indexer used to create PRI files for use in resource packages.
ms.assetid: 945ED98C-8D73-404F-ACE3-7DD314FB405A
keywords:
- MrmCreateResourceIndexerFromPreviousPriData function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmCreateResourceIndexerFromPreviousPriData
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmCreateResourceIndexerFromPreviousPriData function

Creates a resource indexer used to create PRI files for use in resource packages. 

This function is not needed if you created the original PRI file(s) with the **MrmPackagingModeStandaloneFile** or 
**MrmPackagingModeAutoSplit** packaging mode. If you are building resources for an unpackaged desktop app, you *cannot*
use this function since only stand-alone PRI files are supported for unpackaged apps.

COM must be initialized (e.g. by calling **[CoInitializeEx](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex)**) before using this function.

## Syntax

```C++
HRESULT HRESULT MrmCreateResourceIndexerFromPreviousPriData (
  _In_     PCWSTR                   projectRoot,
  _In_     MrmPlatformVersion       platformVersion,
  _In_opt_ PCWSTR                   defaultQualifiers,
  _In_     BYTE                     *priData,
  _In_     ULONG                    priSize,
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

The platform version (*targetOsVersion*) to use for the generated configuration file. Most callers should just use **MrmPlatformVersion_Windows10_0_0_5**

</dd> <dt>

*defaultQualifiers* \[in, optional\]
</dt> <dd>

Type: **PCWSTR**

A list of default resource qualifiers. For example, "language-en-US_scale-100". For more information about qualifiers, see [Qualifiers in MRM](mrmqualifiers.md).

</dd> <dt>

*priData* \[in\]
</dt> <dd>

Type: **BYTE\***

A pointer to an in-memory PRI file. You can obtain an in-memory PRI file either by manually loading an existing PRI
file from disk, or by creating it in-memory with [**MrmCreateResourceFileInMemory**](mrmcreateconfig.md).

</dd> <dt>

*priSize* \[in\]
</dt> <dd>

Type: **ULONG**

The size of the data pointed to by *priData*.

</dd> <dt>

*indexer* \[in, out\]
</dt> <dd>

Type: **[**MrmResourceIndexerHandle**](mrmresourceindexerhandle.md)\***

A pointer to a resource indexer handle. On successful return, this will contain a handle to a resource indexer.
You must free the indexer via [**MrmDestroyIndexerAndMessages**](mrmdestroyindexerandmessages.md) after using it.

</dd> </dl>

## Return value

Type: **HRESULT**

S\_OK if the function succeeded, otherwise some other value. Use the **SUCCEEDED** or **FAILED** macros (defined in winerror.h) to determine success or failure.

## Remarks

See the **Remarks** section
of [**MrmCreateResourceIndexerFromPreviousPriFile**](mrmcreateresourceindexerfrompreviousprifile.md) for more info,
as this function is essentially the same (except it uses in-memory PRI rather than an on-disk file).

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

[**MrmCreateResourceIndexerFromPreviousPriFile**](mrmcreateresourceindexerfrompreviousprifile.md)
</dt></dl>

<dl> <dt>

[**MrmCreateResourceIndexerFromPreviousSchemaData**](mrmcreateresourceindexerfrompreviousschemadata.md)
</dt></dl>

<dl> <dt>

[**MrmCreateResourceIndexerFromPreviousSchemaFile**](mrmcreateresourceindexerfrompreviousschemafile.md)
</dt></dl>

<dl> <dt>

[Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems)
</dt></dl>
