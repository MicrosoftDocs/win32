---
title: MrmIndexFileAutoQualifiers function (MrmResourceIndexer.h)
description: Adds a file resource to a Resource Indexer, inferring the resource name and qualifiers from the file path.
ms.assetid: CEA4D845-987C-48D6-B80E-9F055363FFE0
keywords:
- MrmIndexFileAutoQualifiers function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmIndexFileAutoQualifiers
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmIndexFileAutoQualifiers function

Adds a file resource to a Resource Indexer, inferring the resource name and qualifiers from the file path.
Note that it is the resource name that is indexed, not the file. In other words, this function does not search 
the filename (or file contents) looking for things to index.

See [File resources in MRM](mrmfiles.md) for more info. 

## Syntax


```C++
HRESULT HRESULT MrmIndexFileAutoQualifiers(
  _In_ MrmResourceIndexerHandle indexer,
  _In_ PCWSTR                   filePath
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

*filePath* \[in\]
</dt> <dd>

Type: **PCWSTR**

The file path to be added to the index, and from which to infer both the resource name and the qualifiers. 
See the **Remarks** section below for more info.

</dd> </dl>

## Return value

Type: **HRESULT**

S\_OK if the function succeeded, otherwise some other value. Use the **SUCCEEDED** or **FAILED** macros (defined in winerror.h) 
to determine success or failure.

Note that this function may succeed even if you pass an invalid value for the *filePath* parameter. The error will be reported 
as **0x8007000B (HRESULT_FROM_WIN32(ERROR_BAD_FORMAT))** when you try to 
create the PRI file via [**MrmCreateResourceFile**](mrmcreateresourcefile.md) or one of the related functions. See **Remarks**
for more info.

## Remarks

This function is equivalent to [**MrmIndexFile**](mrmindexfile.md) except the *resourceUri* and *qualifiers*
parameters are inferred from the *filePath* argument. Given a *filePath* of the form `path1\path2\pathn\filename`, the 
following basic algorithm is used:

1. Let `resourceName` be the string `ms-resource:///Files/`.
1. Let `qualifiers` be an empty string.
1. For each `path` segment in *filePath*, check if it consists of a valid qualifier list string
(see [Qualifiers in MRM](mrmqualifiers.md) for more info). If so, append those qualifiers to `qualifiers`, otherwise append it 
to `resourceName`.
1. For `filename`, split it up into segments separated by dots (`.`). 
1. For each segment, if it is a valid qualifier list then add it to `qualifiers`, otherwise append it to
`resourceName`.
1. Call the equivalent of **MrmIndexFile(indexer, resourceName, filePath, qualifiers)**

For example:

| filePath | resourecName | qualifiers |
|-|-|-|
| Assets\\**language-en**\\**scale-200**\logo.png | ms-resource:///files/Assets/logo.png | language-en_scale-200 |
| Images\icon.**scale-100**.**contrast-high**.jpg | ms-resource:///files/Images/icon.jpg | scale-100_contrast-high |
| Data\menu.txt | ms-resource:///files/Data/menu.txt | \<N/A> |
| Images\\**scale-200**\HomePage\\**language-de**\welcome.**contrast-high**.png | ms-resource:///files/Images/HomePage/welcome.png | scale-200_language-de_contrast-high |

Note that there is no way to determine what the inferred `resourceName` and `qualifiers` are
for a given string; they are simply added to the indexer. The only way to determine the values
that were inferred is to create the PRI file and then dump it using one of the **MrmDump...** functions.

### Valid file paths

Unlike **MrmIndexFile**, the *filePath* argument should be a legal file path, although the file does not 
need to exist. It should be a relative path, not including a parent directory escape (`..\`). The *projectRoot* 
specified during indexer creation can be used to generate relative file paths. For example, if the indexer was created 
with a *projectRoot* of `C:\Projects\MyApp` and you index the file `C:\Projects\MyApp\Assets\file.scale-200.jpg`, 
the function will automatically convert that to the relative filename `Assets\file.scale-200.jpg` (of course you could
just add the relative name `Assets\file.scale-200.jpg` directly).

There are two important caveats with the validation of the *filePath* parameter:

1. Using forward slashes (`/`) instead of backslashes (`\`) bypasses the checking performed by
this function, and can result in illegal filenames in the PRI file. 
1. Invalid file paths are **not** detected when this function is called, but only when the resource file 
is created on. 

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
