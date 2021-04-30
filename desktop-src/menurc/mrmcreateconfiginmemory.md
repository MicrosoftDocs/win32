---
title: MrmCreateConfigInMemory function (MrmResourceIndexer.h)
description: Creates new, initialized PRI configuration info (as in-memory data, not as a file) defining the qualifier defaults that you specify.
ms.assetid: D8822D6E-5F68-46A1-B99F-52575DB1D277
keywords:
- MrmCreateConfigInMemory function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmCreateConfigInMemory
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmCreateConfigInMemory function

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Creates new, initialized PRI configuration info (as in-memory data, not as a file) defining the qualifier defaults that you specify. The function allocates memory and returns a pointer to that memory in *outputXmlData*. Call [**MrmFreeMemory**](mrmfreememory.md) with the same pointer to free that memory. For more info, and scenario-based walkthroughs of how to use these APIs, see [Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems).

## Syntax


```C++
HRESULT HRESULT MrmCreateConfigInMemory(
  _In_     MrmPlatformVersion platformVersion,
  _In_opt_ PCWSTR             defaultQualifiers,
  _Out_    BYTE               **outputXmlData,
  _Out_    ULONG              *outputXmlSize
);
```



## Parameters

<dl> <dt>

*platformVersion* \[in\]
</dt> <dd>

Type: **[**MrmPlatformVersion**](mrmplatformversion.md)**

The platform version (*targetOsVersion*) to use for the generated configuration info.

</dd> <dt>

*defaultQualifiers* \[in, optional\]
</dt> <dd>

Type: **PCWSTR**

A list of default resource qualifiers. For example, L"language-en-US\_scale-100\_contrast-standard"

</dd> <dt>

*outputXmlData* \[out\]
</dt> <dd>

Type: **BYTE\*\***

The address of a pointer to BYTE. The function allocates memory and returns a pointer to that memory in *outputXmlData*. Call [**MrmFreeMemory**](mrmfreememory.md) with your pointer to BYTE to free that memory.

</dd> <dt>

*outputXmlSize* \[out\]
</dt> <dd>

Type: **ULONG\***

The address of a ULONG. In *outputXmlSize*, the function returns the size of the allocated memory pointed to by *outputXmlData*.

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

 

