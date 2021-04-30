---
title: MrmCreateResourceFile function (MrmResourceIndexer.h)
description: Creates a PRI file (named \ 0034;resources.pri \ 0034;), or files, on disk in the specified folder. For more info, and scenario-based walkthroughs of how to use these APIs, see Package resource indexing (PRI) APIs and custom build systems.
ms.assetid: B9CE0638-4650-4E1A-BE5E-4CC7C6614030
keywords:
- MrmCreateResourceFile function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmCreateResourceFile
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmCreateResourceFile function

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Creates a PRI file (named "resources.pri"), or files, on disk in the specified folder. For more info, and scenario-based walkthroughs of how to use these APIs, see [Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems).

## Syntax


```C++
HRESULT HRESULT MrmCreateResourceFile(
  _In_ MrmResourceIndexerHandle indexer,
  _In_ MrmPackagingMode         packagingMode,
  _In_ MrmPackagingOptions      packagingOptions,
       PCWSTR                   outputDirectory
);
```



## Parameters

<dl> <dt>

*indexer* \[in\]
</dt> <dd>

Type: **[**MrmResourceIndexerHandle**](mrmresourceindexerhandle.md)**

A handle identifying the resource indexer from which to create the PRI file.

</dd> <dt>

*packagingMode* \[in\]
</dt> <dd>

Type: **[**MrmPackagingMode**](mrmpackagingmode.md)**

Specifies whether the PRI file should be standalone, be automatically split by resource qualifier, or be a resource pack.

</dd> <dt>

*packagingOptions* \[in\]
</dt> <dd>

Type: **[**MrmPackagingOptions**](mrmpackagingoptions.md)**

Specifies additional options about the PRI file.

</dd> <dt>

*outputDirectory* 
</dt> <dd>

Type: **PCWSTR**

A path to a folder in which to save the PRI file.

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

 

