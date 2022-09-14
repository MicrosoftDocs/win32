---
title: MrmCreateResourceIndexer function (MrmResourceIndexer.h)
description: Creates a resource indexer, used to generate package resource index (PRI) files for a UWP app. For more info, and scenario-based walkthroughs of how to use these APIs, see Package resource indexing (PRI) APIs and custom build systems.
ms.assetid: 9AE3EF90-4ADC-4646-9C62-87A702333B9A
keywords:
- MrmCreateResourceIndexer function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmCreateResourceIndexer
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmCreateResourceIndexer function

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Creates a resource indexer, used to generate package resource index (PRI) files for a UWP app. For more info, and scenario-based walkthroughs of how to use these APIs, see [Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems).

## Syntax


```C++
HRESULT HRESULT MrmCreateResourceIndexer(
  _In_     PCWSTR                   packageFamilyName,
  _In_     PCWSTR                   projectRoot,
  _In_     MrmPlatformVersion       platformVersion,
  _In_opt_ PCWSTR                   defaultQualifiers,
  _Inout_  MrmResourceIndexerHandle *indexer
);
```



## Parameters

<dl> <dt>

*packageFamilyName* \[in\]
</dt> <dd>

Type: **PCWSTR**

The package family name of the UWP app for which you will be generating PRI files. This value will be used as the resource map name when you later generate a PRI file from this resource indexer.

</dd> <dt>

*projectRoot* \[in\]
</dt> <dd>

Type: **PCWSTR**

The project root of the UWP app for which you will be generating PRI files. In other words, the path to that app's resource files. You specify this so that you can then specify paths relative to that root in subsequent API calls to the same resource indexer.

</dd> <dt>

*platformVersion* \[in\]
</dt> <dd>

Type: **[**MrmPlatformVersion**](mrmplatformversion.md)**

The target platform version for the resource indexer.

</dd> <dt>

*defaultQualifiers* \[in, optional\]
</dt> <dd>

Type: **PCWSTR**

A list of default resource qualifiers. For example, L"language-en-US\_scale-100\_contrast-standard"

</dd> <dt>

*indexer* \[in, out\]
</dt> <dd>

Type: **[**MrmResourceIndexerHandle**](mrmresourceindexerhandle.md)\***

A pointer to a resource indexer handle.

</dd> </dl>

## Return value

Type: **HRESULT**

S\_OK if the function succeeded, otherwise some other value. Use the SUCCEEDED() or FAILED() macros (defined in winerror.h) to determine success or failure.

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

 

