---
title: IDWriteFontFallbackBuilder AddMapping method
description: Appends a single mapping to the list. Call this once for each additional mapping.
ms.assetid: FCA3CD9C-9FB3-49BD-B4D1-53AEAAAAEE8A
keywords:
- AddMapping method Direct Write
- AddMapping method Direct Write , IDWriteFontFallbackBuilder interface
- IDWriteFontFallbackBuilder interface Direct Write , AddMapping method
topic_type:
- apiref
api_name:
- IDWriteFontFallbackBuilder.AddMapping
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteFontFallbackBuilder::AddMapping method

Appends a single mapping to the list. Call this once for each additional mapping.

## Syntax


```C++
HRESULT AddMapping(
                       DWRITE_UNICODE_RANGE  *ranges,
                       UINT32                rangesCount,
  [in]           const WCHAR                 **targetFamilyNames,
                       UINT32                targetFamilyNamesCount,
  [in, optional]       IDWriteFontCollection fontCollection = nullptr,
  [in, optional] const WCHAR                 *localeName = nullptr,
  [in, optional] const WCHAR                 *baseFamilyName = nullptr,
                       FLOAT                 scale = 1
);
```



## Parameters

<dl> <dt>

*ranges* 
</dt> <dd>

Type: **[**DWRITE\_UNICODE\_RANGE**](/windows/win32/api/Dwrite_1/ns-dwrite_1-dwrite_unicode_range)\***

Unicode ranges that apply to this mapping.

</dd> <dt>

*rangesCount* 
</dt> <dd>

Type: **UINT32**

Number of Unicode ranges.

</dd> <dt>

*targetFamilyNames* \[in\]
</dt> <dd>

Type: **const WCHAR\*\***

List of target family name strings.

</dd> <dt>

*targetFamilyNamesCount* 
</dt> <dd>

Type: **UINT32**

Number of target family names.

</dd> <dt>

*fontCollection* \[in, optional\]
</dt> <dd>

Type: **[**IDWriteFontCollection**](/windows/win32/api/dwrite/nn-dwrite-idwritefontcollection)**

Optional explicit font collection for this mapping.

</dd> <dt>

*localeName* \[in, optional\]
</dt> <dd>

Type: **const WCHAR\***

Locale of the context.

</dd> <dt>

*baseFamilyName* \[in, optional\]
</dt> <dd>

Type: **const WCHAR\***

Base family name to match against, if applicable.

</dd> <dt>

*scale* 
</dt> <dd>

Type: **FLOAT**

Scale factor to multiply the result target font by.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/> |
| Library<br/>                  | <dl> <dt>Dwrite.lib</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Dwrite.dll</dt> </dl>   |



## See also

<dl> <dt>

[**IDWriteFontFallbackBuilder**](idwritefontfallbackbuilder.md)
</dt> </dl>

 

