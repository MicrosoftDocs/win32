---
title: MrmIndexFile function (MrmResourceIndexer.h)
description: Adds a file resource to a Resource Indexer.
ms.assetid: C9F245B4-D2D3-4863-BB64-72619FC73D3C
keywords:
- MrmIndexFile function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmIndexFile
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmIndexFile function

Adds a file resource to a Resource Indexer. Note that it is the resource name that is indexed, not the file.
In other words, this function does not search the filename (or file contents) looking for things to index.

See [File resources in MRM](mrmfiles.md) for more info. 

## Syntax


```C++
HRESULT HRESULT MrmIndexFile(
  _In_     MrmResourceIndexerHandle indexer,
  _In_     PCWSTR                   resourceUri,
  _In_     PCWSTR                   filePath,
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

The URI (name) to assign to the resource. By convention, file resources are added to the `files/` path (for example, 
`ms-resource:///files/logo.png`). See [Resource names in MRM](mrmresourcenames.md) for more info.

</dd> <dt>

*filePath* \[in\]
</dt> <dd>

Type: **PCWSTR**

The file path to be added to the index. Typically, this should be a relative path to a file as it will exist
after your app is intalled.

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

The provided *filePath* is added directly to the indexer without any parsing. The file does not need to exist, 
and no checks are performed to see if it contains illegal path characters. The *resourceUri* is entirely unrelated
to the file path, for example a file may have a *resourceUri* of `/files/logo.png` but a *filePath* of 
"Assets\\Logos\\2x\\logo.png". Since the *filePath* is just a string, it can also contain absolute paths or 
parent-paths (those including "..\") although such files may not exist at runtime.

Note that files added with **MrmIndexFile** do not get qualifiers automatically added based on the filename - any
qualifiers must be explicitly added with the *qualifers* parameter. To automatically deduce qualifiers based 
on the filename (as is performed by Visual Studio and the **MakePri** tool), use 
[**MrmIndexFileAutoQualifiers**](mrmindexfileautoqualifiers.md).

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
