---
title: MrmIndexString function (MrmResourceIndexer.h)
description: Indexes a single string resource belonging to a UWP app.
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

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Indexes a single string resource belonging to a UWP app. Takes an explicit (but optional) list of resource qualifiers. For more info, and scenario-based walkthroughs of how to use these APIs, see [Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems).

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

A handle identifying the resource indexer that will index the string resources.

</dd> <dt>

*resourceUri* \[in\]
</dt> <dd>

Type: **PCWSTR**

The resource URI to assign to the resource. The path will be used as the resource map subtree name for this resource when you later generate a PRI file from this resource indexer.

</dd> <dt>

*resourceString* \[in\]
</dt> <dd>

Type: **PCWSTR**

The value of the string resource.

</dd> <dt>

*qualifiers* \[in, optional\]
</dt> <dd>

Type: **PCWSTR**

An optional list of resource qualifiers, for example L"language-en-US\_scale-100\_contrast-standard". An empty string or **nullptr** indicates a neutral resource. Resource qualifiers are *not* inferred from *resourceUri*.

</dd> </dl>

## Return value

Type: **HRESULT**

S\_OK if the function succeeded, otherwise some other value. Use the SUCCEEDED() or FAILED() macros (defined in winerror.h) to determine success or failure.

## Remarks

If you want to specify any resource qualifiers, then pass them in the *qualifiers* parameter. Resource qualifiers are *not* inferred from *resourceUri*.

The file name segment of *resourceUri* is used as the resource name.

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

 

