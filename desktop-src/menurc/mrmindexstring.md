---
title: MrmIndexString function (MrmResourceIndexer.h)
description: Adds a string resource to a Resource Indexer.
ms.assetid: 098F47E7-4BEC-452F-A33C-111F3F524E67
keywords:
- MrmIndexString function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmIndexString
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmIndexString function

Adds a string resource to a Resource Indexer. Note that it is the resource name that is indexed, not the string.
In other words, this function does not search the string looking for things to index.

## Syntax


```C++
HRESULT HRESULT MrmIndexString(
  _In_     MrmResourceIndexerHandle indexer,
  _In_     PCWSTR                   resourceUri,
  _In_     PCWSTR                   resourceString,
  _In_opt_ PCWSTR                   qualifiers
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

The URI (name) to assign to the resource. By convention, string resources are added to the `strings/` path (for example, 
`ms-resource:///strings/appName`). See [Resource names in MRM](mrmresourcenames.md) for more info.

</dd> <dt>

*resourceString* \[in\]
</dt> <dd>

Type: **PCWSTR**

The string to add to the index.

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

S\_OK if the function succeeded, otherwise some other value. Use the **SUCCEEDED** or **FAILED** macros (defined in winerror.h) 
to determine success or failure.

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

[**MrmIndexEmbeddedData**](mrmindexembeddeddata.md)
</dt></dl>

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

[File resources in MRM](mrmfiles.md)
</dt></dl>

<dt><dt>

[Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems)
</dt></dl>
