---
title: MrmCreateConfigInMemory function (MrmResourceIndexer.h)
description: Creates a new, initialized PRI config file in-memory for use with the makepri tool.
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

Creates a new, initialized PRI config file in memory (i.e. not on disk) for use with the Windows SDK **MakePri** tool. 
None of the other MRM functions work with config files.

This function performs the equivalent of the `makepri createconfig` command, but in memory.

COM must be initialized (e.g. by calling **[CoInitializeEx](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex)**) 
before using this function.

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

The platform version (*targetOsVersion*) to use for the generated configuration file. Most callers should just use **MrmPlatformVersion_Windows10_0_0_5**

</dd> <dt>

*defaultQualifiers* \[in, optional\]
</dt> <dd>

Type: **PCWSTR**

A list of default resource qualifiers. For example, "language-en-US_scale-100". For more information about qualifiers, see [Qualifiers in MRM](mrmqualifiers.md).

</dd> <dt>

*outputXmlData* \[out\]
</dt> <dd>

Type: **BYTE\*\***

The address of a **BYTE** pointer. On successful return, contains a pointer to the buffer allocated by
the function that contains the generated config file. 
You must free the memory by calling [**MrmFreeMemory**](mrmfreememory.md) when you are done with it.

</dd> <dt>

*outputXmlSize* \[out\]
</dt> <dd>

Type: **ULONG\***

The address of a **ULONG**. On successful return, contains the size of the allocated memory buffer pointed to by
 *outputXmlData*.

</dd> </dl>

## Return value

Type: **HRESULT**

**S\_OK** if the function succeeded, otherwise an error value. Use the **SUCCEEDED** or **FAILED** macros (defined in winerror.h) to determine 
success or failure.

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

 

