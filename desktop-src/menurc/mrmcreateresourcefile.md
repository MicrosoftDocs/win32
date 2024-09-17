---
title: MrmCreateResourceFile function (MrmResourceIndexer.h)
description: Creates one or more PRI file(s) on disk in the specified directory.
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

Creates one or more PRI files on disk in the specified directory. This is the last stage of creating a PRI file, after 
creating the indexer and adding resources.

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

A handle identifying the resource indexer from which to create the PRI file. This handle is returned via a call to 
[**MrmCreateResourceIndexer**](mrmcreateresourceindexer.md) or one of the related **MrmCreateResourceIndexer...*** functions.

</dd> <dt>

*packagingMode* \[in\]
</dt> <dd>

Type: **[**MrmPackagingMode**](mrmpackagingmode.md)**

Specifies what file(s) the function should create. To create a PRI file for an unpackaged desktop app, you *must* use
**MrmPackagingModeStandaloneFile**. See [**MrmPackagingMode**](mrmpackagingmode.md) for more info.

</dd> <dt>

*packagingOptions* \[in\]
</dt> <dd>

Type: **[**MrmPackagingOptions**](mrmpackagingoptions.md)**

Specifies additional options about the PRI file. Most callers should specify **MrmPackagingOptionsNone**. See the documentation for
[**MrmPackagingOptions**](mrmpackagingoptions.md) for more info.

</dd> <dt>

*outputDirectory* 
</dt> <dd>

Type: **PCWSTR**

The directory in which to save the PRI file(s), which may be absolute or relative. The directory must already exist.

</dd> </dl>

## Return value

Type: **HRESULT**

**S\_OK** if the function succeeded, otherwise an error value. Use the **SUCCEEDED** or **FAILED** macros (defined in winerror.h)
to determine success or failure.

Some errors you may encounter include:

* **0x80070057: E_INVALIDARG One or more arguments are invalid.** This may indicate an attempt to create a Resource Pack PRI without
specifying a main PRI. See [**MrmPackagingMode**](mrmpackagingmode.md) for more info.
* **0x80073B0F: HRESULT_FROM_WIN32(ERROR_MRM_DUPLICATE_ENTRY) : Duplicate Entry.** This indicates a resource was added twice with the
same name and qualifiers but different values. There is no way to determine which resource caused the error.
* **0x80073B08: HRESULT_FROM_WIN32(ERROR_MRM_INVALID_FILE_TYPE) : Invalid file type.** This can occur when using the packaging mode
**MrmPackagingModeResourcePack** and there are candidates that don't match the default qualifiers (e.g. the default language
is German but a resource was added for French) *or* if a resource is added that doesn't exist in the main PRI file. There is no way to
determine which resource caused the error.
* **0x80073B39: An entity was defined as both resource and scope, which is not allowed**. This indicates that a resource name inside a
resource container (e.g. a `resw` file) had embedded separators (slashes or dots) *and* the resource container was in a subdirectory such 
as `\language-en\`. There is no way to determine which resource caused the error.
* **0x8007000B HRESULT_FROM_WIN32(ERROR_BAD_FORMAT) : An attempt was made to load a program with an incorrect format.** This
indicates that a file was added via **MrmIndexFileAutoQualifiers** but it was not a relative path. There is no way to determine 
which resource caused the error.

## Remarks

If this function succeeds, it creates one or more files in the *outputDirectory* depending on the value of the *packagingMode* parameter:

* If **packagingMode** is set to **MrmPackagingModeStandaloneFile**, a single file named **resources.pri** will be created.
* If **packagingMode** is set to **MrmPackagingModeResourcePack**, a single file named **resources.pri** will be created.
* If **packagingMode** is set to **MrmPackagingModeAutoSplit**, one or more files will be created based on the different language(s) and 
/ or scale(s) used by resources added to the indexer.

See [**MrmPackagingMode**](mrmpackagingmode.md) for more info on the different *packagingMode* options, including limitations.

There is no way to specify the name of the output file(s). For packaged apps, you cannot change the names of the files or else
they will not work correctly. For unpackaged apps, you can rename **resources.pri** as long as you pass the correct filename
to the [**ResourceLoader(String, String)** constructor](/windows/windows-app-sdk/api/winrt/microsoft.windows.applicationmodel.resources.resourceloader.-ctor#microsoft-windows-applicationmodel-resources-resourceloader-ctor(system-string-system-string)).


## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1803 \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>MrmResourceIndexer.h</dt> </dl> |
| Library<br/>                  | <dl> <dt>Mrmsupport.lib</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Mrmsupport.dll</dt> </dl>       |



## See also

<dl><dt>

[**MrmCreateResourceFileInMemory**](mrmcreateresourcefileinmemory.md)
</dt></dl>

<dl> <dt>

[Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems)
</dt> </dl>

 

