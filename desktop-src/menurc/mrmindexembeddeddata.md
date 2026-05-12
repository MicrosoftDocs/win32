---
title: MrmIndexEmbeddedData function (MrmResourceIndexer.h)
description: Adds an embeded data resource to a Resource Indexer.
ms.assetid: 4DA37CF9-43B6-44EE-8A10-DBD4510D7885
keywords:
- MrmIndexEmbeddedData function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmIndexEmbeddedData
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmIndexEmbeddedData function

Adds an embeded data resource (BLOB) to a Resource Indexer. Note that it is the resource name that is
indexed, not the data. In other words, this function does not search the data looking for things to index.

Embedded data resources are more efficient than file resources, but are less useful during app development. 
See [Files resources in MRM](mrmfiles.md) for more info. 

## Syntax


```C++
HRESULT HRESULT MrmIndexEmbeddedData(
  _In_           MrmResourceIndexerHandle indexer,
  _In_           PCWSTR                   resourceUri,
  _In_     const BYTE                     *embeddedData,
  _In_           ULONG                    embeddedDataSize,
  _In_opt_       PCWSTR                   qualifiers
);
```



## Parameters

<dl> <dt>

*indexer* \[in\]
</dt> <dd>

Type: **[**MrmResourceIndexerHandle**](mrmresourceindexerhandle.md)**

A handle identifying the resource indexer to add the resource to. This handle is returned via a call to 
[**MrmCreateResourceIndexer**](mrmcreateresourceindexer.md) or one of the related **MrmCreateResourceIndexer...*** functions.

</dd> <dt>

*resourceUri* \[in\]
</dt> <dd>

Type: **PCWSTR**

The URI (name) to assign to the resource. See [Resource names in MRM](mrmresourcenames.md) for more info.

</dd> <dt>

*embeddedData* \[in\]
</dt> <dd>

Type: **const BYTE\***

A pointer to the data you want to add to the indexer.

</dd> <dt>

*embeddedDataSize* \[in\]
</dt> <dd>

Type: **ULONG**

The size of the data pointed to by *embeddedData*.

</dd> <dt>

*qualifiers* \[in, optional\]
</dt> <dd>

Type: **PCWSTR**

An optional list of resource qualifiers for the resource, for example "language-en-US". Passing an empty 
string or **NULL** indicates a neutral resource that is applicable in any resource context. See 
[Qualifiers in MRM](mrmqualifiers.md) for more info.

</dd> </dl>

## Return value

Type: **HRESULT**

S\_OK if the function succeeded, otherwise some other value. Use the **SUCCEEDED** or **FAILED** macros 
(defined in winerror.h) to determine success or failure.

## Remarks

This function adds binary data (such as an image or audio file) directly to the indexer, so that it will
be embedded in the output PRI file. This is in contrast to file-based resources, which only adds the 
filename to the PRI file and requires the file to be installed alongside the app.

See [Files in MRM](mrmfiles.md) for more info on the pros and cons of using embedded data vs. file resources. 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1803 \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>MrmResourceIndexer.h</dt> </dl> |
| Library<br/>                  | <dl> <dt>Mrmsupport.lib</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Mrmsupport.dll</dt> </dl>       |



## See also

<dt><dt>

[**MrmIndexFile**](mrmindexfile.md)
</dt></dl>

<dt><dt>

[**MrmIndexFileAutoQualifiers**](mrmindexfileautoqualifiers.md)
</dt></dl>

<dt><dt>

[**MrmIndexResourceContainerAutoQualifiers**](mrmindexresourcecontainerautoqualifiers.md)
</dt></dl>

<dt><dt>

[**MrmIndexString**](mrmindexstring.md)
</dt></dl>

<dt><dt>

[File resources in MRM](mrmfiles.md)
</dt></dl>

<dt><dt>

[Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems)
</dt></dl>
