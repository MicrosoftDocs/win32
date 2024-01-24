---
title: MrmDumpPriFile function (MrmResourceIndexer.h)
description: Dumps a PRI file (which is binary) to its XML equivalent (as a file on disk), in order to make it more easily readable.
ms.assetid: FE1982AB-881C-4F07-8B9E-E3770E5B5099
keywords:
- MrmDumpPriFile function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmDumpPriFile
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmDumpPriFile function

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Dumps a PRI file (which is binary) to its XML equivalent (as a file on disk), in order to make it more easily readable. For more info, and scenario-based walkthroughs of how to use these APIs, see [Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems).

## Syntax


```C++
HRESULT HRESULT MrmDumpPriFile(
  _In_     PCWSTR      indexFileName,
  _In_opt_ PCWSTR      schemaPriFile,
  _In_     MrmDumpType dumpType,
  _In_     PCWSTR      outputXmlFile
);
```



## Parameters

<dl> <dt>

*indexFileName* \[in\]
</dt> <dd>

Type: **PCWSTR**

A full file path to a PRI file. This is the PRI file that will be dumped to XML.

</dd> <dt>

*schemaPriFile* \[in, optional\]
</dt> <dd>

Type: **PCWSTR**

An optional full file path to a schema file (or to a PRI file representing a schema; see Remarks).

</dd> <dt>

*dumpType* \[in\]
</dt> <dd>

Type: **[**MrmDumpType**](mrmdumptype.md)**

Specifies how detailed the XML dump should be, or whether a schema should be dumped.

</dd> <dt>

*outputXmlFile* \[in\]
</dt> <dd>

Type: **PCWSTR**

The path of an XML file to create.

</dd> </dl>

## Return value

Type: **HRESULT**

S\_OK if the function succeeded, otherwise some other value. Use the SUCCEEDED() or FAILED() macros (defined in winerror.h) to determine success or failure.

## Remarks

A schema-free resource pack is one that was created with the [**MrmPackagingOptionsOmitSchemaFromResourcePacks**](mrmpackagingoptions.md) argument passed to [**MrmCreateResourceFile**](mrmcreateresourcefile.md) or [**MrmCreateResourceFileInMemory**](mrmcreateresourcefileinmemory.md) (or with the *omitSchemaFromResourcePacks* switch in the PRI config file). To dump a schema-free resource pack, pass the path to your main package PRI data as the argument for the *schemaPriFile* parameter.

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

 

