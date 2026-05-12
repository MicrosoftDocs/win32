---
title: MrmDumpPriFile function (MrmResourceIndexer.h)
description: Dumps a binary PRI file to its XML equivalent on disk.
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

Dumps a PRI file to its XML equivalent. PRI files are stored in an undocumented binary format, so in order to view 
the contents of a file for debugging etc. it must be saved ("dumped") as an XML file.  

This function performs the equivalent of the `makepri dump` command.

COM must be initialized (e.g. by calling **[CoInitializeEx](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex)**) before using this function.

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

The path to the PRI file to dump. If this file does not have an embedded schema, then *schemaPriFile* is required.

</dd> <dt>

*schemaPriFile* \[in, optional\]
</dt> <dd>

Type: **PCWSTR**

The path to the PRI file that provides the scheme for the *indexFileName* if needed, otherwise **NULL**. 
See **Remarks** for more info.

</dd> <dt>

*dumpType* \[in\]
</dt> <dd>

Type: [**MrmDumpType**](mrmdumptype.md)

Specified the kind of dump to create. For most use-cases, **MrmDumpTypeBasic** is sufficient. See the 
[**MrmDumpType** reference](mrmdumptype.md) for more info.

</dd> <dt>

*outputXmlFile* \[in\]
</dt> <dd>

Type: **PCWSTR**

The path of the XML file to create. If the file already exists, it will be overwritten.

</dd> </dl>

## Return value

Type: **HRESULT**

S\_OK if the function succeeded, otherwise some other value. Use the **SUCCEEDED** or **FAILED** macros (defined in winerror.h) 
to determine success or failure.

## Remarks

You can create XML dumps from a PRI file, but there is no equivalent function to build a PRI file from an
XML dump - that must be done manually by using the other Resource Indexer APIs. 

### When to use a *schemaPriFile*

In a PRI file, resources are identified by both a name and an index (known as the "Schema"). When a resource-pack 
PRI file is created, the resource names can be omitted to save space. The resource-pack PRI file will contain only
the resource indexes, not the names. In order to produce the dump file (which includes resource names), the original 
base PRI file is required.

A schema-free resource pack PRI file is created by using the 
[**MrmPackagingOptionsOmitSchemaFromResourcePacks**](mrmpackagingoptions.md) option when creating a resource file via 
one of the **MrmCreateResourceFile...** functions. When dumping such a resource-pack PRI file, pass the original (main) 
PRI file as the *schemaPriFile* argument.


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

[**MrmDumpPriDataInMemory**](mrmdumppridatainmemory.md)
</dt></dl>

<dl> <dt>

[**MrmDumpPriFileInMemory**](mrmdumpprifileinmemory.md)
</dt></dl>
<dl> <dt>

[Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems)
</dt> </dl>