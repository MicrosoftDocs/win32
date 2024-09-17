---
title: MrmCreateConfig function (MrmResourceIndexer.h)
description: Creates a new, initialized PRI config file for use with the makepri tool.
ms.assetid: F8FB4E9C-1C04-460A-BFA1-FB663653DA3C
keywords:
- MrmCreateConfig function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmCreateConfig
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmCreateConfig function

Creates a new, initialized PRI config file for use with the Windows SDK **MakePri** tool. None of the other MRM functions work with config files.

This function performs the equivalent of the `makepri createconfig` command.

COM must be initialized (e.g. by calling **[CoInitializeEx](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex)**) before using this function.

## Syntax


```C++
HRESULT HRESULT MrmCreateConfig(
  _In_     MrmPlatformVersion platformVersion,
  _In_opt_ PCWSTR             defaultQualifiers,
  _In_     PCWSTR             outputXmlFile
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

*outputXmlFile* \[in\]
</dt> <dd>

Type: **PCWSTR**

The path of the configuration file to create. The file will be overwritten if it already exists.
The directory must already exist.

</dd> </dl>

## Return value

Type: **HRESULT**

**S\_OK** if the function succeeded, otherwise an error value. Use the **SUCCEEDED** or **FAILED** macros (defined in winerror.h) to determine success or failure.

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

 

