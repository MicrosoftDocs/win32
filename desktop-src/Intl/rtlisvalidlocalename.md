---
description: Determines if a locale specified by name is installed or supported on the operating system.
ms.assetid: 6df92e4d-d78e-48b5-9515-18f0497de95b
title: RtlIsValidLocaleName function (Ntrtl.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlIsValidLocaleName
api_type: 
- DllExport
api_location: 
- Kernel32.dll
---

# RtlIsValidLocaleName function

Determines if a locale specified by name is installed or supported on the operating system.

> [!Note]  
> This function is available for use in Windows Vista only. It might be altered or unavailable in subsequent versions. Applications should use [**IsValidLocaleName**](/windows/desktop/api/Winnls/nf-winnls-isvalidlocalename).

 

## Syntax


```C++
BOOL RtlIsValidLocaleName(
  _In_ LPCWSTR LocaleName,
  _In_ ULONG   Flags
);
```



## Parameters

<dl> <dt>

*LocaleName* \[in\]
</dt> <dd>

[Locale name](locale-names.md) to validate. This parameter can specify the name of a [custom locale](custom-locales.md).

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Flags indicating if neutral locales are considered valid. Currently the only defined flag is [LOCALE\_ALLOW\_NEUTRAL](locale-allow-neutral.md). The default value is that they are not.

</dd> </dl>

## Return value

Returns a nonzero value if successful, or 0 otherwise.

## Remarks

This function is similar to [**IsValidLocaleName**](/windows/desktop/api/Winnls/nf-winnls-isvalidlocalename). The only difference is that if LOCALE\_ALLOW\_NEUTRAL is set, **RtlIsValidLocaleName** returns **TRUE** for a name that corresponds to a neutral locale (such as "en"), while [**IsValidLocaleName**](/windows/desktop/api/Winnls/nf-winnls-isvalidlocalename) returns **TRUE** only for a specific locale (such as "en-US"). Neutral locales are used as part of the resource loading strategy in Windows Vista and later. Only a small class of highly specialized applications use **RtlIsValidLocaleName** and set LOCALE\_ALLOW\_NEUTRAL, because neutral locales are of very limited use. None of the functions described in [Calling the "Locale Name" Functions](calling-the--locale-name--functions.md) accept neutral locales as inputs.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Ntrtl.h</dt> </dl>      |
| Library<br/>                  | <dl> <dt>Kernel32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Kernel32.dll</dt> </dl> |



## See also

<dl> <dt>

[National Language Support](national-language-support.md)
</dt> <dt>

[National Language Support Functions](national-language-support-functions.md)
</dt> <dt>

[**IsValidLocaleName**](/windows/desktop/api/Winnls/nf-winnls-isvalidlocalename)
</dt> </dl>

 

 




