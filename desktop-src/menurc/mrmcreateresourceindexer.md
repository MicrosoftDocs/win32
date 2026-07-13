---
title: MrmCreateResourceIndexer function (MrmResourceIndexer.h)
description: Creates a resource indexer, used to generate package resource index (PRI) files.
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

Creates a resource indexer, used to generate package resource index (PRI) files for both packaged and unpackaged
desktop apps. 

COM must be initialized (e.g. by calling **[CoInitializeEx](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex)**) 
before using this function.

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

The package family name (PFN) of the app for which you will be generating PRI files. If you are building a PRI file
for a packaged app, this *must* match the PFN of the app (as listed in the AppxManifest). If you are building
a PRI file for an unpackaged app, this *must* be the string **"Application"**.

</dd> <dt>

*projectRoot* \[in\]
</dt> <dd>

Type: **PCWSTR**

The root directory from which some file paths will be computed. Typically this will be the root directory of your
source project, but may differ. See [File resources in MRM](mrmfiles.md) for more information.

</dd> <dt>

*platformVersion* \[in\]
</dt> <dd>

Type: **[**MrmPlatformVersion**](mrmplatformversion.md)**

The platform version (*targetOsVersion*) to use for the generated configuration file. Most callers should just 
use **MrmPlatformVersion_Windows10_0_0_5**

</dd> <dt>

*defaultQualifiers* \[in, optional\]
</dt> <dd>

Type: **PCWSTR**

A list of default resource qualifiers. For example, "language-en-US_scale-100". For more information about qualifiers, 
see [Qualifiers in MRM](mrmqualifiers.md).

</dd> <dt>

*indexer* \[in, out\]
</dt> <dd>

Type: **[**MrmResourceIndexerHandle**](mrmresourceindexerhandle.md)\***

A pointer to a resource indexer handle. On successful return, this will contain a handle to a resource indexer.
You must free the indexer via [**MrmDestroyIndexerAndMessages**](mrmdestroyindexerandmessages.md) after using it.

</dd> </dl>

## Return value

Type: **HRESULT**

S\_OK if the function succeeded, otherwise some other value. Use the **SUCCEEDED** or **FAILED** macros (defined in winerror.h) 
to determine success or failure.

## Remarks

Most of the MRM APIs require an indexer handle to operate. The handle is created by this function or one of the related
functions listed below under **See Also**. 

Use [**MrmDestroyIndexerAndMessages**](mrmdestroyindexerandmessages.md) to
release the resources associated with the indexer after using it.

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

[**MrmCreateResourceIndexerFromPreviousPriData**](mrmcreateresourceindexerfrompreviouspridata-.md)
</dt></dl>

<dl> <dt>

[**MrmCreateResourceIndexerFromPreviousPriFile**](mrmcreateresourceindexerfrompreviousprifile.md)
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
