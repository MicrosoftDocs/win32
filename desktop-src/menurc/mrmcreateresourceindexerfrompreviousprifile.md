---
title: MrmCreateResourceIndexerFromPreviousPriFile function (MrmResourceIndexer.h)
description: Creates a resource indexer used to create PRI files for use in resource packages.
ms.assetid: 8B3743EF-1A27-4B70-9577-8549B91DBC1E
keywords:
- MrmCreateResourceIndexerFromPreviousPriFile function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmCreateResourceIndexerFromPreviousPriFile
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmCreateResourceIndexerFromPreviousPriFile function

Creates a resource indexer used to create PRI files for use in resource packages.

This function is not needed if you created the original PRI file(s) with the **MrmPackagingModeStandaloneFile** or 
**MrmPackagingModeAutoSplit** packaging mode. If you are building resources for an unpackaged desktop app, you *cannot*
use this function since only stand-alone PRI files are supported for unpackaged apps.

COM must be initialized (e.g. by calling **[CoInitializeEx](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex)**) before using this function.

## Syntax


```C++
HRESULT HRESULT MrmCreateResourceIndexerFromPreviousPriFile(
  _In_     PCWSTR                   projectRoot,
  _In_     MrmPlatformVersion       platformVersion,
  _In_opt_ PCWSTR                   defaultQualifiers,
  _In_     PCWSTR                   priFile,
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

*priFile* \[in\]
</dt> <dd>

Type: **PCWSTR**

A fully-qualified path to an existing PRI file.

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

See general remarks about creating a resource indexer in the **Remarks** section of 
[**MrmCreateResourceIndexer**](mrmcreateresourceindexer.md).

This function is used to create language- or scale-specific PRI files that are used in addition to a primary PRI file
(the one passed as *priFile*). This is only useful if you are building a packaged MSIX app and intend to build separate
resource packages for the target language(s) / scale(s). In all other cases, this function is not needed.

For example, assume your default resources are in English and you created a PRI file for them. Now you have 
localized those resources into German and wish to create a German-language resource pack for your app. 

1. First you would create your English-language PRI file, saving it to disk.
1. Then you would call this function, passing in the path to the English-language PRI file as
the *priFile* parameter and making sure "language-de" was one of the *defaultQualifiers*.
1. Next you would add all the German-language resource candidates to the indexer. Note that you do not need to have a
German candidate for every resource; for those where the English resource is applicable (e.g. non-localized text or
images) the German candidate can be omitted.
1. Finally, you would save the German-languaeg PRI file using the **MrmPackagingModeResourcePack** packaging mode, placing it in a different directory than your English-language PRI file.

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

[**MrmCreateResourceIndexerFromPreviousPriData**](mrmcreateresourceindexerfrompreviouspridata-.md)
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
