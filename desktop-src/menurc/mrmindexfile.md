---
title: MrmIndexFile function (MrmResourceIndexer.h)
description: Indexes a resource file belonging to a UWP app. Takes an explicit (but optional) list of resource qualifiers. For more info, and scenario-based walkthroughs of how to use these APIs, see Package resource indexing (PRI) APIs and custom build systems.
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

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Indexes a resource file belonging to a UWP app. Takes an explicit (but optional) list of resource qualifiers. For more info, and scenario-based walkthroughs of how to use these APIs, see [Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems).

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

A handle identifying the resource indexer that will index the resource file.

</dd> <dt>

*resourceUri* \[in\]
</dt> <dd>

Type: **PCWSTR**

The resource URI to assign to the resource. The path will be used as the resource map subtree name for this resource when you later generate a PRI file from this resource indexer.

</dd> <dt>

*filePath* \[in\]
</dt> <dd>

Type: **PCWSTR**

A relative path to a file containing a resource that you want to index. This path is relative to the project root of the UWP app for which you are generating PRI files. That project root is the value of *projectRoot* that you passed to [**MrmCreateResourceIndexer**](mrmcreateresourceindexer.md).

</dd> <dt>

*qualifiers* \[in, optional\]
</dt> <dd>

Type: **PCWSTR**

An optional list of resource qualifiers, for example L"language-en-US\_scale-100\_contrast-standard". An empty string or **nullptr** indicates a neutral resource. Resource qualifiers are *not* inferred from *resourceUri* nor from *containerPath*.

</dd> </dl>

## Return value

Type: **HRESULT**

S\_OK if the function succeeded, otherwise some other value. Use the SUCCEEDED() or FAILED() macros (defined in winerror.h) to determine success or failure.

## Remarks

If you want to specify any resource qualifiers, then pass them in the *qualifiers* parameter. Resource qualifiers are *not* inferred from *resourceUri* nor from *filePath*.

The file name segment of *resourceUri* (not *filePath*) is used as the resource name.

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

 

